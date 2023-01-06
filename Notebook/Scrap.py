import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

import mysql.connector
from mysql.connector import Error

connection_config = {
    "host" : "localhost",
    "user" :"py",
    "password":"python",
    "auth_plugin" : "mysql_native_password",
    "database" : "Allocine",
    "port" : "3308"        
}

id_film = '130738' # mettre l'id du film, trouvable dans l'URL

def note_sql(User, Note, Commentaire):
    
    try :
        mydb = mysql.connector.connect(**connection_config)
        mycursor = mydb.cursor()
        sql = f"""INSERT INTO notes (`ID`, `User`, `Note`,`Commentaire`) VALUES ('4',"{User}",'{Note}',"{Commentaire}");"""  
        print(sql)    
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, f"record inserted.")
        return True

    except Error as e:
        print(f"ça marche pas, parce que : {e}")
        # sys.exit()
        return False

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")


def url_set():
    
    i=1

    global soup

    for i in range(1,117):
        
        try:
            url = f"""https://www.allocine.fr/film/fichefilm-{id_film}/critiques/spectateurs/?page={i}"""
            req = requests.get(url)
            soup = BeautifulSoup(req.content, features="html.parser")
            # print(scrap())
            list_note = scrap()
            for x in list_note:
                if not note_sql(x, list_note[x][0], list_note[x][1])==False:
                    pass
                else:
                    break    
            
            i=i+1

        except:
            print("NOK")
            return False


def scrap():
    
    n_n = {}

    for link in soup.find_all('div', {"class": "hred review-card cf"}):
        str_link = BeautifulSoup(str(link), features="html.parser")
        # print(str_link)
        
        try:
            name = (str_link.select_one("figure", class_='thumbnail', ).select_one("span").attrs["title"])
            note = (str_link.find("span", class_="stareval-note").text).replace(",",".")
            commentaire = (str_link.find("div", class_="content-txt review-card-content").text).replace("\n"," ").replace('"',"''").replace('[',"(").replace(']',")")
            n_n[name]=note,commentaire

        except:
            pass

    return n_n

url_set()