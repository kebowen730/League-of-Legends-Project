from urllib.request import urlopen
from bs4 import BeautifulSoup
from ChampStat import ChampStat


def is_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
def scrape():
    html=urlopen('http://leagueoflegends.wikia.com/wiki/Patch')
    soup=BeautifulSoup(html)
    site='http://leagueoflegends.wikia.com/wiki/'
    table=soup.find('table',{'class':'navbox hlist'})
    info=table.findAll('a')
    title=''
    links=[]
    versions=['1','2','3','4','5','6']
    for link in info:  #adds relevant patch urls to list
        
        title=link.get('title')
        if title==None:
            continue
        if title[0]=='V' and title[1] in versions:
            links.append(title)
    #stat_names==['armor','health','health_regeneration','attack_damage']
    stats=[]
    count=0
    for url in links:
        html=urlopen(site+url)
        patch=BeautifulSoup(html')
        
        li_tags=patch.findAll('li') 
        vers='6'
        
        
        release_table=patch.find('table')
        
        tr=release_table.findAll('tr')
        
        try:
            date=tr[2].td.next_sibling.text.strip()
        except AttributeError:
            try:
                date=tr[1].td.next_sibling.text.strip()
            except AttributeError:
                date=tr[3].td.next_sibling.text.strip()
       
        
        for tag in li_tags:
            
            
            if 'Stats' == tag.text[1:6] and tag.span==None and tag.ul!=None and tag.children!=None :
                name =tag.parent.previous.previous.previous
                
               
                for i in tag.ul.children:
                    
                    content=i.text[1:]
                    if 'autoattack' in content:
                        continue
                    
                    if content[0] not in '0123456789':
                        vers=''
                        for i in range(len(url)-1,-1,-1):#works backwards from end of url to get the version
                            if url[i]=='V':
                                break
                            
                            vers=url[i]+vers
                        
                        
                        if vers=='4.01':
                            break
                        if  'growth' not in content and 'Growth' not in content and 'per level' not in content:
                            count+=1
                            try:    
                                stat=ChampStat(str(name),str(content),str(vers),str(date))
                                stats.append(stat)
                            except IndexError:
                                #print(name,content,vers,date)
                                continue
                            
    champ_dates={}
    list_html = urlopen('http://leagueoflegends.wikia.com/wiki/List_of_champions')
    soup = BeautifulSoup(list_html)
    date_list = soup.findAll('td')
    
    i = 0
    for date in date_list:
        if (i >= 10) and ((i % 10 == 0) or (i % 10 == 7)):
            if (i % 10 == 0):
                character_name = date.text[:]
                character_name = character_name.strip()
                

            if (i % 10 == 7):
                date_added = date.text[:]
                champ_dates[character_name]=date_added
        
        
        i +=1
    
    stat_html=('http://leagueoflegends.wikia.com/wiki/Base_champion_statistics')
    soup=BeautifulSoup(stat_html)
    stat_list=soup.findAll('td')
     
    
    
    
    #for stat in stat_list:
        
    
    stats.sort()  
    stat_data=[i.getData()  for i in stats if is_number(i.val)]
    add_stats=[]
    checklist=[]
    for i in stat_data:
        ch_id=i['champ_id']
        st_id=i['stat_id']
        if ch_id=='Leblanc':
            ch_id='LeBlanc'
        if (i['champ_id'],i['stat_id']) not in checklist:
            
            add_stats.append({'champ_id':ch_id, 'patch_id':'0','patch_date':champ_dates[ch_id],'previous':None,'stat':i['previous'], 'stat_id':st_id})
            checklist.append((i['champ_id'],i['stat_id']))
    i=0
    var_tup=()
    for stat in stat_list:
        if i%19==0:
            name=i.text[:]
            if name=='Leblanc':
                name='LeBlanc'
        if i%19==1:
            var_tup=(name,'Health')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Health'})
        if i%19==3:
            var_tup=(name,'Health Regeneration')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Health Regeneration'})
        if i%19==5:
            var_tup=(name,'Mana')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Mana'})
        if i%19==7:
            var_tup=(name,'Health')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Mana regeneration'})
        if i%19==9:
            var_tup=(name,'Attack damage')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Attack damage'})
        if i%19==11:
            var_tup=(name,'Attack speed')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Attack speed'})
        if i%19==13:
            var_tup=(name,'Armor')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Armor'})
        if i%19==15:
            var_tup=(name,'Magic resistance')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Magic resistance'})
        if i%19==17:
            var_tup=(name,'Movement speed')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Movement speed'})
        if i%19==18:
            var_tup=(name,'Range')
            if var_tup not in checklist:
                checklist.append(var_tup)
                add_stats.append({'champ_id':name, 'patch_id':'0','patch_date':champ_dates[name],'previous':None,'stat':stat.text[:], 'stat_id':'Range'})
        i+=1
    stat_data=stat_data+add_stats
  #      statdata[i]['previous']=None
   #     sdict=statdata[i]
    #    for j in range(i-1,-1,-1):
     #       if sdict['stat_id']==statdata[j]['stat_id'] and sdict['champ_id']==statdata[j]['champ_id']:
      #          statdata[i]['previous']=statdata[j]['stat']
       #        
        #        break
        #if statdata[i]['previous']==None:
         #   statdata[i]['previous']=statdata[i]['stat']
            
    return stat_data
