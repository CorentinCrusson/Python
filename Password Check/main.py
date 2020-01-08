# Import
import os
import sqlite3

from colorama import init, Fore
from passwordVerification import checkingPass
from databaseMethods import *


def colorFromLevel(level):
    if(level == "VERY BAD"):
        return Fore.RED
    elif(level == "BAD"):
        return Fore.LIGHTRED_EX
    elif(level == "MEDIUM"):
        return Fore.YELLOW
    elif(level == "GOOD"):
        return Fore.LIGHTGREEN_EX
    else:
        return Fore.GREEN


def resultInFile(listUsers):
    f = open("password.txt", "w+")
    for user in listUsers:
        f.write("["+user[1]+"] => "+user[0]+" : "+user[2]+"\n")

        print(colorFromLevel(user[1])+"["+user[1]+"] => "+Fore.WHITE +
              user[0]+" : "+user[2]+"\n")
    f.close()


    # Just the main path
if __name__ == "__main__":

    # If the database not exists
    if (os.path.isfile('house.db') is False):
        con, curs = connectDatabase()
        createDatabase(con, curs)
    else:
        con, curs = connectDatabase()

    # Init Colorama
    init()

    # The user list
    users = userList(curs)

    # Checking each password
    lstUsers = []
    while users:
        lvl, comm = checkingPass(users[1])
        lstUsers.append((users[0], lvl, comm, users[1]))

        users = curs.fetchone()

    # The resultat in a file named "password.txt"
    resultInFile(lstUsers)

    con.close()
