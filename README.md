# CLISU
CLI Syncing Utility

# What is it and why does it exist?
CLISU is a solution to the problem of synchronizing between computer and external media.

After venturing into the world of cloud-based streaming, having forsaken the old way, the bugs and limitations of the new way drove me to return to having a locally-owned collection. File management was one of the pain points that drove me to try the new way, so in returning to the old I am taking it upon myself to create an alternative that works best for me.

After spending a couple of months trying to do everything at once (and failing), I scaled the code way back. Now that it functions usefully I will slowly add the bells and whistles that I envisioned for it. For this first release, all the program does is basically clone a directory (including subdirectories) from one location to another. The program will ignore files and subdirectories that begin with '.' (Ex. '/sys/path/.file.mp3')

Currently, the program requires no external dependencies, but that will change in future versions.

The program will change dramatically, in both form and function, in the future, so as updates are applied, make sure to check back. Or don't, it's your life.

# Using CLISU
Using CLISU is easy.

There are two ways to launch the program: directly or with terminal prompts. Both ways involve the command-line. If this is your first time, quickly look at the CLI section below before continuing.

Using the '-h' or '--help' flags will launch the help.

## Running Directly
If you just want to point the program to the desired locations and let it work, use the '-r' or '--run' flag, including the FROM directory, then the TO directory.
Example: './clisu.py -r /FROM/ /TO/'
Note: Keep in mind that the directories are case-sensitive and if there are any sub/directories with a space in the name, include the whole directory in quotes. '/from/path/of directory'

## Running With Prompts
If you want the program to guide you, simply use the '-t' or '--terminal' flag.
Example: './clisu.py -t'

# CLI

To use a command-line interface program (for the most part and including here), you need to load up your terminal or command prompt. The user will type the name of the program file (in this case './clisu.py'), the 'flag' of the function (something like '-x' or '--xyz', typically), and any necessary/optional information after.

An example is: './clisu.py --help'
'./clisu.py' is the program file and '--help' is the flag.

# Limitations
Currently the code only does the one thing.

I wasted a few days of my life trying to get the program to interact with the protocol known as MTP and gotten nowhere, so for the time being the program will not sync with an MTP-connected device. I hope to fix this eventually.

This program is being developed on and for Linux, so cross-platform capability isn't guaranteed at this time.
