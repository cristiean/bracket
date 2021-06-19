import bracket.bracket as br
import sys,sqlite3,copy,os

def newBracket():
    clrScreen()
    print("Enter name of bracket: ", end='')
    name = input()
    if name.endswith(".db"):
        name = name[:-3]
    print("Enter relative path of where the bracket will be saved:", end='')
    path = input()
    if path.endswith("/") or path.endswith("\\"):
        path = path[:-1]
    fullPath = path+"/"+name+".db"
    try:
        open(fullPath,"w+").close()
    except:
        print("Cannot create file")
        return
    try:
        conn = sqlite3.connect(fullPath)
    except:
        print("Unable to open database file")
        return
    c = conn.cursor()
    c.execute("CREATE TABLE bracket (round INT)")
    bracket = begin()
    createDB(bracket,conn)
    update(bracket,2)
    closeBracket(bracket,conn)

def createDB(bracket,conn):
    cursor = conn.cursor()
    for i in range(1,bracket.totalNumTeams+1):
        cursor.execute("ALTER TABLE bracket ADD COLUMN team"+str(i)+" TEXT")
    for i in range(0,bracket.numRounds):
        columns = "('round',"
        for j in range(1,len(bracket.rounds[i])+1):
            columns += "'team"+str(j)+"',"
        columns = columns[:-1]+")"
        cursor.execute("INSERT INTO bracket "+columns+" VALUES ("+str(i+1)+",'"+"','".join(bracket.rounds[i])+"')")
    conn.commit()

def openBracket():
    clrScreen()
    print("Enter full path of file:", end='')
    path = input()
    if path.endswith(".db"):
        path = path[:-3]
    path += ".db"
    try:
        open(path).close()
    except:
        print("File not found")
        return
    conn = sqlite3.connect(path)
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM bracket")
    except:
        print("Bracket not found")
        return
    rows = c.fetchall()
    teams = [x for x in list(rows[0])[1:] if x[0]!="-"]
    temp = []
    for row in rows:
        temp.append([str(x) for x in row if isinstance(x,unicode)])
    bracket = br.Bracket(teams)
    bracket.rounds = copy.deepcopy(temp)
    Round = bracket.numRounds
    for i in range(1,bracket.numRounds+1):
        if "-"*bracket.max in bracket.rounds[i]:
            Round = i+1
            break
    update(bracket,Round)
    closeBracket(bracket,conn)

def begin():
    clrScreen()
    numTeams = br.getNumTeams()
    teams = br.getTeamNames(numTeams)
    bracket = br.Bracket(teams)
    print("Shuffle the teams?", end='')
    if input() in ["Yes","Y","yes","y","Yeah","yeah","1"]:
        bracket.shuffle()
    return bracket
  
def update(bracket,Round):
    updated = False
    while not updated:
        clrScreen()
        bracket.show()
        print("")
        print("Type Q to quit and save.")
        print("Update round "+str(Round)+": ", end='')
        teams = input().replace(", ",",").split(",")
        if teams[0] in ["Q","q","Quit","quit"]:
            return
        updated = bracket.update(Round, teams)
    if Round==bracket.numRounds:
        clrScreen()
        bracket.show()
        print("")
        print(bracket.rounds[-1][0]+" won!")
        print("")
        print("Press enter to go to main menu.")
        input()
    else:
        update(bracket,Round+1)

def saveBracket(bracket,conn):
    cursor = conn.cursor()
    for i in range(0,bracket.numRounds):
        keys = []
        for j in range(1,len(bracket.rounds[i])+1):
            keys.append("team"+str(j))
        sql = ('UPDATE bracket SET '+','.join(key+' = ?' for key in keys)+' WHERE round = ?')
        args = bracket.rounds[i]+[i+1]
        cursor.execute(sql,args)
    conn.commit()

def closeBracket(bracket,conn):
    saveBracket(bracket,conn)
    conn.close()

def mainMenu():
    clrScreen()
    print("1. New bracket")
    print("2. Open bracket")
    print("3. Quit")
    print("")
    print("Enter number: ", end='')
    try:
        ans = int(input())
    except:
        mainMenu()
        return
    if ans==1:
        newBracket()
    elif ans==2:
        openBracket()
    else:
        clrScreen()
        sys.exit()
    mainMenu()

if "-f" in sys.argv:
    def clrScreen():
        pass
else:
    def clrScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    mainMenu()