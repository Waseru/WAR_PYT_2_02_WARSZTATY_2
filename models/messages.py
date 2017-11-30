"""

CREATE TABLE Messages (
id INT AUTO INCREMENT,
sender_id INT NOT NULL,
recipient_id INT NOT NULL,
text VARCHAR(256),
creation_date DATE,
PRIMARY KEY(id),
FOREIGN KEY(sender_id) REFERENCES User(id)
);

"""

class Messages:
    __id = None
    sender_id = None
    recipient_id = None
    text = None
    creation_date = None

    def __init__(self):
        self.__id = -1
        self.sender_id = 0
        self.recipient_id = 0
        self.text = ""
        self.creation_date = ""

    @property
    def id(self):
        return self.__id

    @staticmethod
    def load_message_by_id(cursor, id):
        sql = "SELECT * FROM Messages WHERE id=%s"
        cursor.execute(sql, (id,))
        print('co jest', cursor.lastrowid)
        data = cursor.fetchone()
        if data is not None:
            loaded_message = Messages()
            loaded_message.__id = data[0]
            loaded_message.sender_id = data[1]
            loaded_message.recipient_id = data[2]
            loaded_message.text = data[3]
            loaded_message.creation_date = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_messages_for_user():
        sql = "SELECT * FROM WHERE reci"


