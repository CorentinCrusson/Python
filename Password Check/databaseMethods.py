import sqlite3

# Connection to the database "house.db"


def connectDatabase():
    connexion = sqlite3.connect("house.db")
    cursor = connexion.cursor()
    return connexion, cursor

# Create the database with creation of the user table and the insert of users


def createDatabase(connexion, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        username TEXT,
        mail TEXT,
        password TEXT,
        levelPassword TEXT DEFAULT NULL
    )''')

    users = [
        ("Antoine", "antoinePeson@gmail.com", "mbappe"),
        ("Jordan", "jordy67232@outlook.com", "Henri5"),
        ("Isabella", "isaberlPes@live.fr", "chipou2"),
        ("Albert", "albertoDuCanape0@albertpesson.fr", "Pe!SNo1b3r7"),
        ("Suzie", "suzielaNosa@gmail.com", "R1jolieSuz"),
    ]

    cursor.executemany(
        "INSERT INTO user(username, mail, password) VALUES(?, ?, ?) ", users)

    connexion.commit()

def insertDatabase(connexion,cursor,users):
    cursor.executemany(
        "INSERT INTO user(username, mail, password) VALUES(?, ?, ?) ", users)
    
    try:
        connexion.commit()
    except:
        return False
    
    return True

def updateLevelPass(connexion,cursor,users):
    cursor.executemany("UPDATE user SET levelPassword = (?) WHERE username = (?)", users)

    connexion.commit()

def userList(cursor):
    cursor.execute('''SELECT username,password,mail,levelPassword FROM user''')
    return cursor.fetchone()

def userInfo(cursor,username='',level=''):

    cursor.execute('''SELECT username,password,mail,levelPassword FROM user WHERE username LIKE ? and levelPassword LIKE ? ''', (username+'%',level+'%'))
    return cursor.fetchone()

#A Corriger
def requeteur(cursor,requete):
    cursor.execute(requete)
    return cursor.fetchall()
