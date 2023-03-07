import pymysql

#initialize empty HTML string
htmlString=""

#create an HTML HEAD
def headhtml(htmlString):
    htmlString+="<DOCTYPE html>\n<html lang='eng'>\n<head><title>Owners of Pets</title>\n</head>\n<body>"
    return(htmlString)

# create an HTML footer
def foothtml(htmlString):
    htmlString+="</body>\n</html>"
    return(htmlString)

# query the db
def ownerquery():
    print("start")
    db = pymysql.connect(host='localhost', user="root", passwd='', db="python_practice")
    cursor = db.cursor()
    sql="SELECT * FROM owners;"
    cursor.execute(sql)
    owners = cursor.fetchall()
    sql = "SELECT column_name from information_schema.COLUMNS where TABLE_NAME='owners';"
    cursor.execute(sql)
    columns = cursor.fetchall()
    print(columns)
    return(owners,columns)

def ownersTable(owners_list, column_names, html):
    html+="<table border='1'>"
    html+="<tr>"
    i=0
    for name in column_names:
        html+="<th>"+name[0]+"</th>"
        i+=1
    html+="</tr>"
    for owner in owners_list:
        html+="<tr>"
        r=0
        while r<i:
            html+="<td>{0}</td>".format(owner[r])
            r+=1
        html+="</tr>"
    html+="</table>"
    return(html)

def petquery():
    db = pymysql.connect(host='localhost', user="root", passwd='', db="python_practice")
    cursor = db.cursor()
    sql="SELECT * FROM pets;"
    cursor.execute(sql)
    pets = cursor.fetchall()
    sql = "SELECT column_name from information_schema.COLUMNS where TABLE_NAME='pets';"
    cursor.execute(sql)
    columns = cursor.fetchall()
    return(pets,columns)

def petsTable(pets_list, column_names, html):
    html+="<table border='1'>"
    html+="<tr>"
    i=0
    for name in column_names:
        html+="<th>"+name[0]+"</th>"
        i+=1
    html+="</tr>"
    for pet in pets_list:
        html+="<tr>"
        r=0
        while r<i:
            html+="<td>{0}</td>".format(pet[r])
            r+=1
        html+="</tr>"
    html+="</table>"
    return(html)
if __name__=="__main__":
    htmlString=headhtml(htmlString)
    (owners, headers)=ownerquery()
    htmlString=ownersTable(owners, headers, htmlString)
    (pets, headers) = petquery()
    htmlString=petsTable(pets, headers, htmlString)
    htmlString=foothtml(htmlString) 
    #write to file
    outf = open ("rendering.html", "w")
    outf.write(htmlString)
    outf.close() 
