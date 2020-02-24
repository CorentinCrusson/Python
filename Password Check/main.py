# Import
import os
import sys
import sqlite3
import argparse
import time

# Import function from package or other files
from colorama import init, Fore
from passwordVerification import checkingPass
from databaseMethods import *
from genUser import generateUser, lengthOfFile


# Return a color from the level
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
    # Open the file password.txt
    f = open("password.txt", "w+")

    # Display
    for user in listUsers:
        lvl = user[1]  # Level of the Complexity

        f.write("["+lvl+"] => "+user[0]+user[2]+"\n")

        print(colorFromLevel(lvl)+"["+lvl+"] => "+Fore.WHITE +
              user[0]+user[2]+"\n")

    f.close()


    # Just the main path
if __name__ == "__main__":

    # Init Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--password", help="Input your password",
                        type=str)
    parser.add_argument('-g', '--generate', help='Generate users',
                        type=int)
    parser.add_argument("-ck", "--check", help="Turn on the checking of the complexify",
                        action="store_true")
    parser.add_argument("-s", "--select", help="Display users presents in the table",
                        action="store_true")
    parser.add_argument('-u', '--username', help='Give Informations with a username on the user',
                        type=str)
    parser.add_argument('-l', '--level', help='Give Informations on users with have the input level',
                        type=str)
    parser.add_argument('-r', '--requete', help='Execute my request',
                        type=str)
    args = parser.parse_args()

    # Init Colorama
    init()

    # If the database not exists
    if (os.path.isfile('house.db') is False):
        con, curs = connectDatabase()
        createDatabase(con, curs)
    else:
        con, curs = connectDatabase()

    # Number of Arguments > 1
    if len(sys.argv) > 1:
        os.system('cls')

    # If the argument check is here
    if args.password is None:

        # Checking of Complexity of all Users
        if args.check:

            # The user list
            users = userList(curs)

            # Checking each password
            lstUsers = []
            lstUpdate = []  # List to update levelPassword
            while users:
                lvl, comm = checkingPass(users[1])
                lstUpdate.append((lvl, users[0]))
                lstUsers.append((users[0], lvl, comm, users[1]))

                users = curs.fetchone()

            # Save New State levelPassword
            updateLevelPass(con, curs, lstUpdate)

            # The resultat in a file named "password.txt"
            resultInFile(lstUsers)

            con.close()

    else:

        lvl, comm = checkingPass(args.password)

        user = [('', lvl, comm, args.password)]

        # The result in a file named "password.txt"
        resultInFile(user)

    # Génération des users
    lstUsers = []
    if args.generate is not None:

        # Time
        myTime = time.time()

        # Init Filepath Generation
        fp = ['name.txt', 'mailList.txt', 'dictionnary.txt']
        files = []
        for f in fp:
            files.append((f, lengthOfFile(f)))

        for i in range(0, args.generate):
            lstUsers.append(generateUser(files))

        print('Génération des utilisateurs Fini en {0}'.format(time.strftime('%M min et %S secondes', time.localtime(
            time.time()-myTime))) if insertDatabase(con, curs, lstUsers) else 'Génération des utilisateurs interrompu')

    # Select Users
    if args.select is True:

        print('-----------------------\nListes des Utilisateurs\n-----------------------\n')
        users = userList(curs)

        while users:
            print(
                "{0} - {1} - {2} [PASSWORD : {3}]".format(users[0], users[1], users[2], users[3]))

            users = curs.fetchone()

    # Select One User
    if args.username is not None:

        users = userInfo(curs, args.username)

        while users:
            print(
                "{0} - {1} - {2} [PASSWORD : {3}]".format(users[0], users[1], users[2], users[3]))

            users = curs.fetchone()

    if args.level is not None:
        lvl = args.level
        lstLvl = []
        if (',') in lvl:
            for lv in lvl.split(','):
                lstLvl.append(lv)
        else:
            lstLvl.append(lvl)

        for level in lstLvl:
            users = userInfo(curs, level=level)

            while users:
                print("{0} - {1} - {2}".format(users[0], users[1], users[2]))

                users = curs.fetchone()
    """
    if args.requete is not None:
        print(requeteur(curs,args.requete))
    """
