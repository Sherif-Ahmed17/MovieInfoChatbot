import mysql.connector as mysql
import datetime
import requests
import constants
import time



mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="hangout_chatbot"
)


def doesUserExist(user):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `UserName`= '{}'".format(user)
    cur.execute(qry)
    result = cur.fetchone()
    return False if result is None else True


def registerUser(user, Password):
    cur = mydb.cursor()
    sql = "INSERT INTO user (UserName, Password) VALUES (%s, %s)"
    val = (user, Password)
    cur.execute(sql, val)
    mydb.commit()
    print(cur.rowcount, "record inserted.")
    return True


def authenticateUser(user, Password):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `UserName`= '{}' AND `Password`= {}".format(user, Password)
    cur.execute(qry)
    user = cur.fetchone()
    print(user)
    return False if user is None else True


def ShowMovieInfo(movie):

    api = "https://api.themoviedb.org/3/search/movie?api_key=faab06148028317bf23fe119c533b8dc&query="+movie
    json_data = requests.get(api).json()
    
    original_title = str(json_data['results'][0]['original_title'])
    overview = json_data['results'][0]['overview']
    release_date = str(json_data['results'][0]['release_date'])
    vote_average = str(json_data['results'][0]['vote_average'])
    original_language = json_data['results'][0]['original_language']
    adult = str(json_data['results'][0]['adult'])

    return original_title, overview, release_date, vote_average, original_language, adult

