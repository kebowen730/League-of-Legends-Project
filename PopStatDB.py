import LeagueScraper as ls
import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'lrngsql', passwd = 'rdg935', db = 'mysql')
cur = conn.cursor()
cur.execute('USE League')

def insertPatch(patch_id, patch_date):
  cur.execute('SELECT * FROM Patch WHERE patch_id = %s AND patch_date = %s',(patch_id, patch_date))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Patch (patch_id, patch_date) VALUES (%s, %s)', (patch_id, patch_date))
    conn.commit()

def insertStatistic(stat_id, patch_id, stat, character_name, previous_stat):
  cur.execute('SELECT * FROM Statistic WHERE stat_id = %s AND patch_id = %s AND stat = %s AND character_name = %s AND previous_stat = %s',(stat_id, patch_id, stat, character_name, previous_stat))
  if (cur.rowcount == 0):
    cur.execute('INSERT INTO Statistic (stat_id, patch_id, stat, character_name, previous_stat) VALUES (%s, %s, %s, %s, %s)', (stat_id, patch_id, stat, character_name, previous_stat))
    conn.commit()


def populate():
    patches=[]
    stats=ls.scrape()
    for i in stats:
        data=i
        if data['patch_id'] not in patches:
            patches.append([data['patch_id'],data['patch_date']])       
   # for j in patches:
    #    insertPatch(j[0],j[1])
    for k in stats:
        print(k)
        insertStatistic(k['stat_id'],k['patch_id'],k['stat'],k['champ_id'],k['previous'])
def main():
    populate()
main()
