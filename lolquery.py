#DATABASE


#CREATE DATABASE League;


#TABLES


#CREATE TABLE Patch
#( patch_id VARCHAR(20) NOT NULL,
 # patch_date DATE NOT NULL,
 # CONSTRAINT pk_patch PRIMARY KEY (patch_id)
#);


#CREATE TABLE Champion
#( character_name VARCHAR(40) NOT NULL,
 # date_added DATE NOT NULL,
 # CONSTRAINT pk_character PRIMARY KEY (character_name)
#);


#CREATE TABLE Statistic
#( stat_id VARCHAR(40) NOT NULL,
 # patch_id VARCHAR(20) NOT NULL,
 # stat VARCHAR(50),
 # character_name VARCHAR(40) NOT NULL,
 # difference VARCHAR(50),
 # previous_stat VARCHAR(40),
 # CONSTRAINT pk_stat PRIMARY KEY (stat_id),
 # CONSTRAINT fk_patch FOREIGN KEY (patch_id)
 #   REFERENCES Patch (patch_id),
 # CONSTRAINT fk_character FOREIGN KEY (character_name)
 #   REFERENCES Champion (character_name),
 # CONSTRAINT fk_previous FOREIGN KEY (previous_stat)
 #   REFERENCES Statistic (stat_id)
#);










import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'lrngsql', passwd = 'rdg935', db = 'mysql')
cur = conn.cursor()
cur.execute('USE League')

'''
def insertPatch(patch_id, patch_date):
  cur.execute('SELECT * FROM Patch WHERE patch_id = %s AND patch_date = %s',(patch_id, patch_date))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Patch (patch_id, patch_date) VALUES (%s, %s)', (patch_id, patch_date))
    conn.commit()

def insertChampion(character_name, date_added):
  cur.execute('SELECT * FROM Champion WHERE character_name = %s AND date_added = %s',(character_name, date_added))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Champion (character_name, date_added) VALUES (%s, %s)', (character_name, date_added))
    conn.commit()

def insertStatistic(stat_id, patch_id, stat, character_name, difference, previous_stat)
  cur.execute('SELECT * FROM Statistic WHERE stat_id = %s AND patch_id = %s AND stat = %s AND character_name = %s AND difference = %s AND previous_stat = %s',(stat_id, patch_id, stat, character_name, difference, previous_stat))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Statistic (stat_id, patch_id, stat, character_name, difference, previous_stat) VALUES (%s, %s, %s, %s, %s, %s)', (stat_id, patch_id, stat, character_name, difference, previous_stat))
    conn.commit()
'''




def stat_hist(name):

  cur.execute('SELECT patch_id, stat FROM Statistic WHERE character_name = %s ORDER BY patch_id', (name))
  print(cur.fetchall())

def patch_date(lower, upper):

  cur.execute('SELECT patch_id, patch_date FROM Patch WHERE patch_date >= %s AND patch_date <= %s ORDER BY patch_date', (lower, upper))
  print(cur.fetchall())

def char_date(lower, upper):
  cur.execute('SELECT character_name FROM Champion WHERE date_added >= %s AND date_added <= %s ORDER BY date_added', (lower, upper))
  print(cur.fetchall())

def stat_patch(p_id):
  cur.execute('SELECT character_name, stat FROM Statistic WHERE patch_id = %s', (p_id))
  print(cur.fetchall())

def find_charchange(name, change):
  cur.execute('SELECT patch_id FROM Statistic WHERE character_name = %s AND stat = %s', (name, change))
  print(cur.fetchall())

def find_change(change):
  cur.execute('SELECT character_name, patch_id FROM Statistic wHERE stat = %s ORDER BY patch_id', (change))
  print(cur.fetchall())

def main():

  print("Enter 1 to view an individual champion's history of changes over all patches\n")
  print('Enter 2 to look up a range of patch ids in a given time interval\n')
  print('Enter 3 to look up a range of the characters that were added to the game in a given time interval\n')
  print('Enter 4 to view all statistic changes from a specific patch\n')
  print('Enter 5 to find a patch where a given change to a certain champion occurred\n')
  print('Enter 6 to for a given stat change, find all champions that received the change and the patch in which it occurred\n')
  print('Enter 0 to quit\n')

  prompt = eval(input('Enter desired query: '))
  while (prompt != 0):
    if (prompt == 1):
      name = input('Enter name of champion: ')
      stat_hist(name)

    if (prompt == 2):
      lower = input('Enter first date: ')
      upper = input('Enter last date: ')
      patch_date(lower, upper)

    if (prompt == 3):
      lower = input('Enter first date: ')
      upper = input('Enter last date: ')
      char_date(lower, upper)

    if (prompt == 4):
      p_id = input('Enter patch number: ')
      stat_patch(p_id)

    if (prompt == 5):
      name = input('Enter name of champion: ')
      change = input('Enter desired change: ')
      find_charchange(name, change)

    if (prompt == 6):
      change = input('Enter desired change: ')
      find_change(change)

    prompt = eval(input('Enter desired query: '))



main()





