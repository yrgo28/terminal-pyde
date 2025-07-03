import os
import termcolor
from termcolor import colored

import pyderc #THIS IS CONFIG FILE

has_wd: bool
FIRST_TIME_OPTIONS = pyderc.FIRST_TIME_OPTIONS
show_wd_main = pyderc.show_wd_main
pdir = pyderc.program_directory

separator = pyderc.char_separators
editor_work_dir = pyderc.workspace

pydeascii = colored(""" ____   __ __   ___    ___ 
| |  | |  V  | |   \  |   |
|  _/   \   /  |  | | | | |
| |      | |   |  | | | __|  _
|_|      |_|   |___/  |___| |_| v1.2
by: yrgo28 (2025)""", "yellow")

def inter(multiplier: int):

    multiplier += 1

    while True:
        if(multiplier > 0):
            multiplier -= 1
            print(' ')
        else:
            break;

def clear():
    os.system('clear')

def _exec(arg: str):
    os.system(arg)

def choose_main():
    global editor_work_dir

    op = input('Type your option: ')
    while True:
        if(op == "X" or op == "x"):
            clear()
            exit()

        if(op == "E" or op == "e"):
            if(editor_work_dir == None):
                print((separator * 36))
                editor_work_dir = input('Type working address: ')

            _exec('sudo vim ' + editor_work_dir)

        if(op == "O" or op == "o"):
            options_menu()

        if(op == "T" or op == "t"):
            _credits()

        main_menu()        

def main_menu():
    clear()
    while True:
        print(pydeascii)
        print((separator * 36))

        if(editor_work_dir != None):
            has_wd = True
        else: 
            has_wd = False

        if(show_wd_main == True and has_wd):
            print('Working Directory: ' + editor_work_dir)
        print("[E]dit")
        print("[O]ptions")
        print("Credi[T]s")
        print("E[x]it")
        print((separator * 36))
        choose_main()

def options_choose():
    global editor_work_dir
    global has_wd
    global show_wd_main

    cons_subcommand: str

    while True:
        command = input('Command: ')

        if(command == "W" or command == "w"):
            cons_subcommand = input('Type working directory (you can cancel changes typing "cancel"): ')
            if(cons_subcommand == "cancel"):
                options_menu()
            else:
                editor_work_dir = cons_subcommand

            options_menu()
            
        if(command == "L" or command == "l" and editor_work_dir != None):
            print('=' * 36)
            _exec('ls ' + editor_work_dir + '/*.py')
            cons = input('Press [Enter] to continue...')
            options_menu()

        if(command == "R" or command == "r"):
            if(show_wd_main == True):
                show_wd_main = False
            elif(show_wd_main == False):
                show_wd_main = True
            options_menu()

        if(command == "I" or command == "i"):
            _exec('sudo vim ' + pdir + '/pyderc.py')

        if(command == 'done'):
            main_menu()

        options_menu()

def options_menu():
    global FIRST_TIME_OPTIONS

    while True:
        clear()
        if(FIRST_TIME_OPTIONS == True):
            print(colored('NOTE: type "done" for back to main menu.', "yellow"))
            print(colored('NOTE: all configs are in "pyderc.py".', "blue"))
            inter(0)
            FIRST_TIME_OPTIONS = False
        print('Options')
        print(separator * 36)
        print("Set [W]orking Directory")
        if(editor_work_dir == None):
            inter(0)
            print(colored("NOTE: Working directory is not loaded yet!", "red"))
            inter(0)
        elif(editor_work_dir != None):
            print("[L]ist files")
            print("""Toggle: show/hide working
di[R]ectory in main menu.""")

        print("Ed[i]t pyrc.py (Restart required)")
        print(separator * 36)
        options_choose()

def _credits():
    clear()
    print("""PYDE, a minimal way to manage your python's projects.

*Programming and design: yrgo28         
*Base and "engine": vim, vim-jedi
You're a modder? Put your name here!
    
LICENSE: GPL-3.0

THANKS FOR USE <3
/yrgo28""")
    inter(0)
    cos = input('press [enter] to continue...')


main_menu()
