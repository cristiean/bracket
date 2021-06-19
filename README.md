# BracketMaker
Create brackets of any size and neatly print them to the screen.

Useful for visually representing tournaments and updating them on the fly.

## Included Files
- `bin/main.py`
    - store and update brackets (uses bracket.bracket)
- `bracket/bracket.py`
    - Python module used for creating and displaying brackets

## Installation
[](TODO)In the terminal type “cd path/to/this/directory” and then “python setup.py install”. This will add the bracket module to your site-packages.

## How to Run
[](TODO)You can either choose to run a finished python program that uses the bracket module or create your own script with the module.

[](TODO)If you want to just run the finished version, the file will be found in the “bin” directory. Double click on the file or type “python main.py” in the terminal to run.

[](TODO)To use the bracket module in your own program the include it at the top of the file with `from bracket import bracket`. There is only one module in the `bracket/` directory.

## How to Use `main.py`
In the main menu, your options are to create a new bracket or open an existing one. 

### New Bracket
You will be asked to enter a name and location to save the bracket. The location must be the full path excluding the name of the bracket.

Then you must enter the number of teams that will participate in the tournament and their names.

You will also be asked to shuffle the teams. Enter `yes` if you want to give the teams random seeds. Enter `no` to use the way you enter the teams as the rankings.

### Open Bracket
Enter the full path of where the bracket was saved including the name of the bracket.

### Updating the Bracket
Type the name of a team that should go on to the next round. You can type multiple teams at once by separating the names with a comma.

You can also edit incorrect updates by typing the other team that should have won instead.

### Quit and Save
In the update screen type `quit` to quit and save. This will return you to the main menu as well.

### Command Line Arguments
There is only one additional argument for main.py. It is `-f` to show the full output of the program and never clear the screen.

To use this feature open the terminal and run `$ python path/to/directory/main.py -f`.
