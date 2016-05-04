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
 # character_name VARCHAR(40) NOT NULL,
 # stat FLOAT(6, 3),
 # previous_stat FLOAT(6, 3),
 # CONSTRAINT pk_statistic PRIMARY KEY (stat_id, patch_id, character_name),
 # CONSTRAINT fk_patch FOREIGN KEY (patch_id)
 #   REFERENCES Patch (patch_id),
 # CONSTRAINT fk_character FOREIGN KEY (character_name)
 #   REFERENCES Champion (character_name)
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
    
def insertChampion(character_name, date_added):
  cur.execute('SELECT * FROM Statistic WHERE stat_id = %s AND type = %s AND description = %s',(stat_id, type, description))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Statistic (stat_id, type, description) VALUES (%s, %s, %s)', (stat_id, type, description))
    conn.commit()

def insertStatChampPatch(stat_id, patch_id, character_name, stat, previous_stat)
  cur.execute('SELECT * FROM StatChampPatch WHERE stat_id = %s AND patch_id = %s AND character_name = %s AND stat = %s AND previous_stat = %s',(stat_id, patch_id, character_name, stat, previous_stat))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO StatChampPatch (stat_id, patch_id, character_name, stat, previous_stat) VALUES (%s, %s, %s, %s, %s)', (stat_id, patch_id, character_name, stat, previous_stat))
    conn.commit()
'''




def stat_hist(name):

  cur.execute('SELECT patch_id, stat FROM Statistic WHERE character_name = %s ORDER BY patch_id', (name))
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())
  if (cur.rowcount == 0):
    print('None')

def patch_date(lower, upper):

  cur.execute('SELECT patch_id, patch_date FROM Patch WHERE patch_date >= %s AND patch_date <= %s ORDER BY patch_date', (lower, upper))
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())
  if (cur.rowcount == 0):
    print('None')

def char_date(lower, upper):
  cur.execute('SELECT character_name FROM Champion WHERE date_added >= %s AND date_added <= %s ORDER BY date_added', (lower, upper))
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())
  if (cur.rowcount == 0):
    print('None')

def stat_patch(p_id):
  cur.execute('SELECT character_name, stat FROM Statistic WHERE patch_id = %s', (p_id))
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())
  if (cur.rowcount == 0):
    print('None')

def find_charchange(name, change):
  cur.execute('SELECT patch_id FROM Statistic WHERE character_name = %s AND stat = %s', (name, change))
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())
  if (cur.rowcount == 0):
    print('None')

def find_change(change):
  cur.execute('SELECT character_name, patch_id FROM Statistic wHERE stat = %s ORDER BY patch_id', (change))
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())
  if (cur.rowcount == 0):
    print('None')

def show_patch():
  cur.execute('SELECT * FROM Patch ORDER BY patch_date')
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())

def show_champion():
  cur.execute('SELECT * FROM Champion ORDER BY character_name')
  for i in range(0, (cur.rowcount)):
    print(cur.fetchone())

def main():

  print("Enter 1 to view an individual champion's history of changes over all patches\n")
  print('Enter 2 to look up a range of patch ids in a given time interval\n')
  print('Enter 3 to look up a range of the characters that were added to the game in a given time interval\n')
  print('Enter 4 to view all statistic changes from a specific patch\n')
  print('Enter 5 to find a patch where a given change to a certain champion occurred\n')
  print('Enter 6 to for a given stat change, find all champions that received the change and the patch in which it occurred\n')
  print('Enter 7 to show the Patch Table\n')
  print('Enter 8 to show the Champion Table\n')
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
      
    if (prompt == 7):
      show_patch()

    if (prompt == 8):
      show_champion()
      
    prompt = eval(input('Enter desired query: '))



main()





