import hashing_algo
import mysql.connector
from mysql.connector import Error
import datetime

def dbconnect():
    message = str(input("Enter your msg: "))
    nowt = str(datetime.datetime.now())
    i = 0
    ts = ""
    while len(ts)<14:
        if(nowt[i]>="0" and nowt[i]<="9"):
            ts=ts+nowt[i];
        i=i+1
    n = int(ts)
    print(ts)
    hashkey = hashing_algo.idToHash(n)
    
    try:
        cnx = mysql.connector.connect(host='localhost', database='soundcomm', user='root', password='mysql')
        if cnx.is_connected():
            query = "insert into msgdb values(%s,%s,%s)"
            args = (ts,message,hashkey)
            cursor = cnx.cursor()
            cursor.execute(query,args)
            cnx.commit()
    except Error as e:
        print(e)
    finally:
        cnx.close()
        cursor.close()


if __name__ == '__main__':
    dbconnect()
