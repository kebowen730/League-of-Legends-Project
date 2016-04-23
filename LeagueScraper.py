from urllib.request import urlopen
from bs4 import BeautifulSoup
from ChampStat import ChampStat
from LinkedList import LinkedList
#def getFromTable(site,table,tag,attr)
def getStats(link):
    soup=BeautifulSoup(link)
    stats=[]
    champ=0
    stats=soup.findAll('li')
    
def main():
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
    stats=LinkedList()
    for url in links:
        html=urlopen(site+url)
        patch=BeautifulSoup(html,'lxml')
        stat_tags=[]
        li_tags=patch.findAll('li')
        vers='6'
        for tag in li_tags:
            if 'Stats' in tag.text and tag.span==None and tag.ul!=None and tag.children!=None :
                for i in tag.ul.children:
                   
                    content=i.text[1:]
                    if content[0] not in '0123456789':
                        vers=''
                        for i in range(len(url)-1,-1,-1):
                            if url[i]=='V':
                                break
                            
                            vers=url[i]+vers
                      
                        stat=ChampStat('Rusty',content,vers)
                        stats.addInOrder(stat)
                        #print(content)
                
                print(site+url)
                stat_tags.append(tag)
        if int(vers[0])<4:
            break

                 
        #break
main()