from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'lrngsql', passwd = 'rdg935', db = 'mysql')
cur = conn.cursor()
cur.execute('USE League')

def insertChampion(character_name, date_added):
  cur.execute('SELECT * FROM Champion WHERE character_name = %s AND date_added = %s',(character_name, date_added))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Champion (character_name, date_added) VALUES (%s, %s)', (character_name, date_added))
    conn.commit()

def main():
  html = urlopen('http://leagueoflegends.wikia.com/wiki/List_of_champions')
  soup = BeautifulSoup(html)
  dateList = soup.findAll('td')
  i = 0
  for date in dateList:
    if (i >= 10) and ((i % 10 == 0) or (i % 10 == 7)):
      if (i % 10 == 0):
        character_name = date.text[:]
        character_name = character_name.strip()
      if (i % 10 == 7):
        date_added = date.text[:]
        insertChampion(character_name, date_added)
    i = i + 1

  print(date.text[:])


main()