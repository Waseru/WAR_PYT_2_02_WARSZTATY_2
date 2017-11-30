"""
baza danych -> war2_db

CREATE TABLE User (
id INT AUTO_INCREMENT,
email VARCHAR(255) UNIQUE,
username VARCHAR(255),
hashed_password VARCHAR(60),
PRIMARY KEY(id)
);
"""