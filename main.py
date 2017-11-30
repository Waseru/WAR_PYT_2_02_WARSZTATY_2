from mysql.connector import connect
from models.users import User
from models.messages import Messages

cnx = connect(user="root", password="coderslab", host="127.0.0.1", database="war2_db")
cursor = cnx.cursor()



#user1 = User()
# user1.username = "Janko"
# user1.email = "janeczko@gmail.com"
# user1.set_password('ktorytakismieszek', 'cdbcd')
# user1.save_to_db(cursor)
# cnx.commit()
# cursor.close()
# cnx.close()

# user2 = User()
# user2.username = "Szczawik"
# user2.email = "szczawik@gmail.com"
# user2.set_password('kolejnydzientosamo', 'MOJASOL')
# user2.save_to_db(cursor)
# cnx.commit()
# cursor.close()
# cnx.close()

#metoda statyczna ale w siedzi w klasie i przez nia sie odwolujemy
new_user = User.load_user_by_id(cursor, 8)
print(new_user.username)

show_users = User.load_all_users(cursor)

# wykonać zadania ze slajdów. Przesłać Oldze link do repo w mailu. ogarnac mysql dump. zmiany commitowac
# tworzymy tabele message od tego mozna zaczac. rozwinac poszczegolne metoy klasy message wykorzystać moduł argparse
# chyba w zadaniu 6
