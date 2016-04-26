import LeagueScraper as ls
import lolquery as lq
def populate():
    patches=[]
    for i in ls.scrape():
        data=i.getData()
        if data['patch_id'] not in patches:
            patches.append([data['patch_id'],data['patch_date']])
        lq.insertStatistic(data['stat_id'],data['patch_id'],data['stat'],data['character_name'],'0')
    for j in patches:
        lq.insertPatch(j[0],j[1])
def main():
    populate()
main()