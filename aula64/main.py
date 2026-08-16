import pymysql
import dotenv
import os

TABLE_NAME = 'costumers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute( 
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (' 
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'  
        )
        connection.commit()
        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME}'
                '(nome, idade)'
                'VALUES (%s, %s)'
            )
            cursor.execute(sql,('Matheus', 21))
            connection.commit()

    with connection.cursor() as cursor:
        sql2 = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = (
            {"age": 17,"name": "Felipe",},
            {"age": 44,"name": "Jonatan",},
            {"age": 67,"name": "Lucas",},
        )
        cursor.executemany(sql2, data2)  
        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql) 
        data5 = cursor.fetchall()  

        for row in data5:
            print(row)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        print(cursor.executemany(sql, (4, 5, 6, 7)))  
        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Maria', 102, 4))  
        connection.commit()

