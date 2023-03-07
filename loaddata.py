import pymysql
def load_owners(cursor):

        owners_data=open("owners.txt")
        for rowline in owners_data:
                row=rowline.split(",")
                sql="INSERT INTO owners(name,gender,phone) VALUES('{}','{}', '{}');".format(row[0], row[1], row[2])

                cursor.execute(sql)
        cursor.execute("SELECT * from owners;")
        print(cursor.fetchall())

def load_pets(cursor):
    pets_data = open("pets.txt")
    for rowline in pets_data:
        row=rowline.split(",")
        cursor.execute("INSERT INTO pets(owner_id,name,gender,species,color,age) VALUES( (SELECT id FROM owners WHERE name='{0}'), '{1}', '{2}', '{3}', '{4}', '{5}');".format(*row))

if __name__=="__main__":
    db=pymysql.connect(host='localhost', user="root", passwd='', db="python_practice")
    cursor=db.cursor()
    load_owners(cursor)
    load_pets(cursor)
    db.commit()
    db.close()