class ChampStat(object):
    def __init__(self,champ,text,version,date):
        
        self.date=self.formatDate(date)
        self.type=''
        lttr=''
        
        tag=False

        if 'Thresh' in champ:
            self.champ='Thresh'
        elif champ=='Leblanc':
            self.champ='LeBlanc'
        elif 'Volibear' in champ:
            self.champ='Volibear'
        elif 'upgrade' in champ and version=='5.15' :
            self.champ='Fiora'
        elif 'rework' in champ and version=='5.9':
            self.champ='Ashe'
        elif champ=='.' and version=='3.10':
            self.champ='Master Yi'
        elif 'Xerath' in champ:
            self.champ='Xerath'
        elif 'soldiers' in champ or 'Voidspawn' in champ or 'Gromp' in champ or 'uto' in self.type:
            x=champ[len(champ)]
          
        else:
            self.champ=champ 
        
        stop_idx=0
        change=text.strip('.\n')
        for i in range(len(change)):
            if change[i:i+4] not in (' inc',' red',' dec',' cha',' nor',' low'):
               self.type+=change[i]
               
            else:
                stop_idx=i
                break
        
        self.type=self.formatID(self.type)       

        change=change[stop_idx:]
        
        change=change[1:]
        i=0
        while change[0]!=' ':
            change=change[1:]
        
        change=change[1:] 
        while change[0:3]=='to ':
            change=change[3:]
        self.previous=''
        self.val=''
        #print(change)
        chars_left=len(change)
        for i in range(chars_left):
            lttr=change[i]
            if change[i:i+2]==' f':
                change=change[i+6:]
                j=i
                #print(change)
                chars_left-=6
                self.previous=change
                if change[0]=='.':
                    self.previous='0'+self.previous
                if '0.625' in self.previous:
                    self.previous='0.625'
                
              
                break
            else:
                self.val+=lttr
        
        if 'per' in self.val:
            self.val=self.val[:len(self.val)-14]
        if self.val[0]=='.':
            self.val='0'+self.val
        self.vers=[]
        for i in version.split('.'):
            if not i.isnumeric():
                end=''
              
                
                for j in i:
                    if j in ('(',')'):
                        continue
                   
                    if j.isalpha():
                        self.vers.append(int(end))
                      
                        end=''
                        
                    
                    end+=j 
 
                self.vers.append(end)    
            else:
                self.vers.append(int(i))

        floatable=False
        while floatable==False:
            try:
                float(self.val)
                floatable=True
            except ValueError:
                self.val=self.val[:len(self.val)-1]
            if self.val=='':
                x=version[len(version)]
        floatable=False
        while floatable==False:
            try:
                float(self.previous)
                floatable=True
            except ValueError:
                self.previous=self.previous[:len(self.previous)-1]
            if self.previous=='':
                x=version[len(version)]
 
    def formatID(self,stat_id):
        if 'ana regen' in stat_id:
            return 'Mana regeneration'
        if 'th regen' in stat_id:
            return 'Health regeneration'
        if 'agic resist' in stat_id:
            return 'Magic resistance'
        if 'amage' in stat_id or 'AD' in stat_id:
            return 'Attack damage'
        if 'ealth' in stat_id:
            return 'Health'
        if 'rmor' in stat_id:
            return 'Armor'
        if 'ove' in stat_id and 'peed' in stat_id:
            return 'Movement speed'
        if 'tack' in stat_id and 'peed' in stat_id:
            return 'Attack Speed'
        if 'ange' in stat_id:
            return 'Attack range'
        if 'ase man' in stat_id:
            return 'Mana'

        return stat_id
    def formatDate(self,date):
        date=date.split()
        months=['January','February','March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month=str(months.index(date[0])+1)+'-'
        if date[2]==',':
            del date[2] 
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
    def __str__(self):
        return str(self.vers)

    def getData(self):
        data={}
        data['stat_id']=self.type
        data['champ_id']=self.champ
        data['stat']=float(self.val)
        
        vers=self.vers
        patch_id='V'+str(vers[0])
        for i in range(1,len(vers)):
            x=vers[i]
            if isinstance(vers[i],int):
                patch_id+='.'+str(vers[i])
            else:
                patch_id+=vers[i]
                
        data['patch_id']=patch_id
        data['patch_date']=self.date
        data['previous']=float(self.previous)
        return data
