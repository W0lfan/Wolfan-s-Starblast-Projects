import os
import sqlite3
from random import randrange

class DatabaseHandler():
    def __init__(self, database_name:str):
        self.connexion = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.connexion.row_factory = sqlite3.Row
    def createStatus(self,userID:int,link):
        cursor = self.connexion.cursor()
        query = f"INSERT INTO user_levels (user_id,level,xp,first_message,has_custom_role) VALUES ({userID},0,0,'{link}',False);"
        cursor.execute(query)
        cursor.close()
        self.connexion.commit()
    def returnValue(self,type:str,userID:str):
        cursor = self.connexion.cursor()
        query = f"SELECT {type} FROM user_levels WHERE user_id = {userID};"
        cursor.execute(query)
        typeResult = cursor.fetchall()
        cursor.close()
        if not typeResult:
            return False
        a = dict(typeResult[0])[type]
        return a
    def modify(self,userID:int,type,value):
        cursor = self.connexion.cursor()
        query = f"UPDATE user_levels SET {type} = ? WHERE user_id = ?;"
        cursor.execute(query,(value,str(userID)))
        cursor.close()
        self.connexion.commit()