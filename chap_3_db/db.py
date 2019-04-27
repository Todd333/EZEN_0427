import sqlite3

class Database:

    def __init__(self):
        self._conn = sqlite3.connect('sqlite.db')

    def create(self):
        sql = """
            CREATE TABLE  IF NOT EXISTS Persons (
                    user_id varchar(10) primary key,
                    password varchar(10),
                    name varchar(10),
                    phone varchar(15),
                    address varchar(10),
                    regdate date default current_timestamp 
            );
        """
        print('쿼리 체크:{}'.format(sql))
        self._conn.execute(sql)
        self._conn.commit()

    def insert_one(self, user_id, password, name, phone, address):
        sql = """
                INSERT INTO Persons (
                user_id, password, name, phone, address)
                VALUES (
                ?, ?, ?, ?, ?);
                """
        self._conn.execute(sql, user_id, password, name, phone, address)
        self._conn.commit()

    def insert_many(self):
        data = [('lee','1','이순신','010-1234-1234','사당'),
                ('hong','1','홍길동','010-1234-2345','강남'),
                ('kang','1','강감찬','010-1234-2345','부산')]
        sql = """
        INSERT INTO Persons (
        user_id, password, name, phone, address)
        VALUES (
        ?, ?, ?, ?, ?);
        """
        self._conn.executemany(sql,data)
        self._conn.commit()


    def fecth_one(self, user_id) -> object:
        sql = """
           SELECT * FROM Persons WHERE userid LIKE ?;
        """
        cursor = self._conn.execute(sql, user_id)
        row = cursor.fetchone()
        return row

    def fecth_all(self) -> object:
        sql = """
           SELECT * FROM Persons;
        """
        cursor = self._conn.execute(sql)
        rows=cursor.fetchall()
        return rows

    def count_all(self) -> object:
        sql = """
           SELECT count(*) FROM Persons;
        """
        cursor = self._conn.execute(sql)
        row = cursor.fetchone()
        return row

    def update(self, user_id, password):
        sql = """
        UPDATE Persons
        SET password = ?
        WHERE user_id = ?;
        """
        self._conn.execute(sql, password, user_id)
        self._conn.commit()

    def remove(self, user_id):
        sql = """
        DELETE FROM Persons WHERE user_id=?;
        """
        self._conn.execute(sql, user_id)
        self._conn.commit()