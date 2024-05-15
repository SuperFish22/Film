
import sqlite3
from config import BaseConfig

# устанавливаем соединение с базой данных
conn = sqlite3.connect(BaseConfig.bd_name, check_same_thread=False)

def chk_conn(conn):
    try:
        # создаем курсор для выполнения операций с базой данных
        cursor = conn.cursor()
        return True
    except sqlite3.Error as error:
        print(error)
        return False


def pouisc_Film(id_film):
    if (chk_conn(conn) == True):
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Film WHERE id = (?)",(id_film))
        cursor = cursor.fetchall()
        return cursor    

def FilmGo():
    if (chk_conn(conn) == True):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Film ")
        cursor = cursor.fetchall()
        return cursor    
    
 
