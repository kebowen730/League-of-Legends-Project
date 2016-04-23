class ChampStat(object):
    def __init__(self,champ,text,version):
        self.type=''
        lttr=''
        change=''
        tag=False
       # for i in text:
        #    if i in ('<','>'):
         #       tag=not tag
#                continue
 #           if tag==True:
  #              continue
   #         change+=i
           
        for i in range(len(change)):
            if change[i:i+4] not in (' inc',' red'):
               self.type+=change[i]
            else:
                change=change[i+1:]
                break
        if 'reduced' in change:
            change=change[11:]
        else:
            change=change[13:]
        self.previous=''
        self.val=''
        
        for i in range(len(change)):
            lttr=change[i]
            if lttr==' ':
                change=change[i+6:]
                break
            else:
                self.val+=lttr
        self.previous=change.strip('.')
        
        self.vers=[int(i) for i in version.split('.')]
        
        
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
        
        
        
        
        
        
        
        
        
        