#puts the date into an sql format
def formatDate(date):
    date=date.split()
    months=['January','February','March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month=str(months.index(date[0])+1)+'-'
    year=date[2]+'-'
    day=''
    for i in date[1]:
        if i.isnumeric():
            day+=i
    if len(month)==2:
        month='0'+month
    if len(day)==1:
        day='0'+day
    return year+month+day
    
#stores all the relevant data about a stat change    
class ChampStat(object):    
    def __init__(self,champ,text,version,date):
        
        self.date=formatDate(date)
        self.type=''
        lttr=''
        
        tag=False
       # for i in text:
        #    if i in ('<','>'):
         #       tag=not tag
#                continue
 #           if tag==True:
  #              continue
   #         change+=i
        self.champ=champ 
        
        stop_idx=0
        change=text.strip('.\n')
       #gets the stat name
        for i in range(len(change)):
            if change[i:i+4] not in (' inc',' red',' dec'):
               self.type+=change[i]
               
            else:
                stop_idx=i
                break
        change=change[stop_idx:]
        print(change)
        jump=0
        if 'reduced' in change:
            change=change[9:]
        else:
            change=change[11:]
        if change[0]=='f':
            change=change[5:]
        else:
            change=change[3:]
        self.previous=''
        self.val=''
        #gets the new value of the stat
        for i in range(len(change)):
            lttr=change[i]
            if lttr==' ':
                change=change[i+6:]
                break
            else:
                self.val+=lttr
        
        
        self.vers=[]
        #splits the patch number into a list for comparison
        for i in version.split('.'):
            if not i.isnumeric():
                end=''
               # print(i)
                
                for j in i:
                    if j in ('(',')'):
                        continue
                    #print(j,end) 
                    if j.isalpha():
                        self.vers.append(int(end))
                      
                        end=''
                        
                    
                    end+=j 
                #print(end+'a')    
                self.vers.append(end)    
            else:
                self.vers.append(int(i))
        if (self.val)=='':
            print('broken')
        #self.val=int(self.val)
        #self.previous=int(self.previous)
   #comparisons
   
    def __eq__(self,other):
        
        return self.vers==other.vers
    
    def __ne__ (self, other):
        
        return (self.vers != other.vers)

    def __lt__ (self, other):
        ov=other.vers
        sv=self.vers
        ovl=len(ov)
        svl=len(sv)
        for j in range(min(svl,ovl)):
            if ov[j]==sv[j]:
                continue
            return ov[j]>sv[j]
            
        return svl<ovl

    def __le__ (self, other):
        
        ov=other.vers
        sv=self.vers
        ovl=len(ov)
        svl=len(sv)
        for j in range(min(svl,ovl)):
            if ov[j]==sv[j]:
                continue
            return ov[j]>sv[j]
            
        return svl<=ovl

    def __gt__ (self, other):
        ov=other.vers
        sv=self.vers
        ovl=len(ov)
        svl=len(sv)
        for j in range(min(svl,ovl)):
            if ov[j]==sv[j]:
                continue
            return ov[j]<sv[j]
            
        return svl>ovl
            

    def __ge__ (self, other):
        ov=other.vers
        sv=self.vers
        ovl=len(ov)
        svl=len(sv)
        for j in range(min(svl,ovl)):
            if ov[j]==sv[j]:
                continue
            return ov[j]>sv[j]
            
        return svl>=ovl
   #returns string version of the version list 
    def __str__(self):
        return str(self.vers)
    #returns dictionary of all the attributes and their values
    def getData(self):
        data={}
        data['stat_id']=self.type
        data['champ_id']=self.champ
        data['stat']=self.val
        
        vers=self.vers
        patch_id='V'+str(vers[0])
        for i in range(1,len(vers)):
            x=vers[i]
            if isinstance(vers[i],int):
                patch_id+='.'+str(vers[i])
            else:
                patch_id+=vers[i]
                
        data['patch_id']=patch_id
        data['date']=self.date
        
        return data
        
        
