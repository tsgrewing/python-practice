import pymysql

server = pymysql.connect(host='localhost', user="root", passwd='')

cursor = server.cursor()

sql = "CREATE DATABASE IF NOT EXISTS python_practice;"
cursor.execute(sql)

sql = "USE python_practice;"
cursor.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS owners(id integer NOT NULL AUTO_INCREMENT,
                                            name varchar(30) NOT NULL, 
                                            gender varchar(7), 
                                            phone varchar(10), 
                                            PRIMARY KEY (id));'''

cursor.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS pets(pet_id integer NOT NULL AUTO_INCREMENT,
                                            owner_id integer,
                                            name varchar(30), 
                                            gender varchar(7), 
                                            species varchar(20),
                                            color varchar(15),
                                            age integer,
                                            PRIMARY KEY (pet_id),
                                            FOREIGN KEY (owner_id) REFERENCES owners(id));'''                       

cursor.execute(sql)

sql="SHOW tables;"

cursor.execute(sql)
print(cursor.fetchall())