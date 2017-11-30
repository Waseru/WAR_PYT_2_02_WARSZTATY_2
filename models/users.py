"""CREATE TABLE User (
id INT AUTO_INCREMENT,
email VARCHAR(255) UNIQUE,
username VARCHAR(255),
hashed_password VARCHAR(80),
PRIMARY KEY(id)
);"""
from models.clcrypto import generate_salt, password_hash, check_password

class User:
    __id = None
    username = None
    __hashed_password = None
    email = None

    def __init__(self):
        print('stworzony')
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        self.__hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        if self.__id == -1:
            #	saving	new	instance	using	prepared	statements
            sql = "INSERT INTO User(username, email, hashed_password) VALUES(%s, %s, %s)"
            values = (self.username, self.email, self.hashed_password)
            cursor.execute(sql, values)
            self.__id = cursor.lastrowid
            return True

        return False

    @staticmethod
    def load_user_by_id(cursor, id):
        sql = "SELECT * FROM User WHERE id=%s"
        cursor.execute(sql, (id,))
        print('co jest', cursor.lastrowid)
        data = cursor.fetchone()
        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[2]
            loaded_user.email = data[1]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT *	FROM User"
        ret = []
        result = cursor.execute(sql).fetchall()
        for row in result:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[2]
            loaded_user.email = row[1]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        return ret
