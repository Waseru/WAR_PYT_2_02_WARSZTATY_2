CREATE TABLE User (
id INT AUTO_INCREMENT,
email VARCHAR(255) UNIQUE,
username VARCHAR(255),
hashed_password VARCHAR(80),
PRIMARY KEY(id)
);

"wyrzuca błąd. wydaje mi się, ze nie moze byc dwóch pozycji z int not null?"
CREATE TABLE Messages (
id INT AUTO INCREMENT,
sender_id INT NOT NULL,
recipient_id INT NOT NULL,
text VARCHAR(256),
creation_date DATE,
PRIMARY KEY(id),
FOREIGN KEY(sender_id) REFERENCES User(id)
);


mysql> show tables;
+-------------------+
| Tables_in_war2_db |
+-------------------+
| User              |
+-------------------+

mysql> explain User;
+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| id              | int(11)      | NO   | PRI | NULL    | auto_increment |
| email           | varchar(255) | YES  | UNI | NULL    |                |
| username        | varchar(255) | YES  |     | NULL    |                |
| hashed_password | varchar(80)  | YES  |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+

