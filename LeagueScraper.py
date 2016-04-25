from urllib.request import urlopen
from bs4 import BeautifulSoup
from ChampStat import ChampStat


    
def scrape():
    html=urlopen('http://leagueoflegends.wikia.com/wiki/Patch')
    soup=BeautifulSoup(html,'lxml')
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
    stats=[]
    for url in links:
        html=urlopen(site+url)
        patch=BeautifulSoup(html,'lxml')
        stat_tags=[]
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
                    if ('autoattack' or 'reduction') in content:
                        continue
                    
                    if content[0] not in '0123456789':
                        vers=''
                        for i in range(len(url)-1,-1,-1):#works backwards from end of url to get the version
                            if url[i]=='V':
                                break
                            
                            vers=url[i]+vers
                        
                        
                        if vers=='4.01':
                            break
                        
                        try:    
                            stat=ChampStat(name,content,vers,date)
                        except IndexError:
                            continue
                        stats.append(stat)
                        
                
                print(site+url)
                stat_tags.append(tag)
                

    return stats
