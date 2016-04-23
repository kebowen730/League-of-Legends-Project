class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  def swap(self):
    next_data=self.data
    self.data=self.next.data
    self.next.data=next_data
class LinkedList (object):
  def __init__ (self):
    self.first = None
  def extendLinks(self,link):
    current=self.first
    while current.next!=None:
      current=current.next
    current.next=link
  def insertFirst (self, data):
    newLink = Link (data)

    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    
    current = self.first
    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink (self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next
 
    return current

  def deleteLink (self, data):
    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

      if (current == self.first):
        self.first = self.first.next
      else:
         previous.next = current.next

    return current

  def sortList(self,sorted=None):
    
    if sorted==None:
      sorted=self.copyList()
    current=sorted.first
    swapped=False
    while current.next!=None :
      if current.data>current.next.data:
        current.swap()
        swapped=True
      current=current.next
    if swapped:
      return self.sortList(sorted)
    return sorted
  def getNumLinks(self):
    ln=0
    current=self.first
    while current!=None:
      ln+=1
      current=current.next
    return ln
  def addInOrder(self,data):
    self.insertFirst(data)
    current=self.first
    while current.next!=None and current.data>current.next.data:
      current.swap()
      current=current.next
    
     
  def isSorted(self):
    current=self.first
    while current.next!=None:
      if current.data>current.next.data:
        return False
      current=current.next
    return True
  def isEmpty(self):
    return self.first==None
  def isEqual(self,b):
    if self.getNumLinks!=b.getNumLinks:
      return False
    current=self.first
    currentb=b.first
    while current.next!=None:
      if current.data!=currentb.data:
        return False
      current=current.next
      currentb=currentb.next
    return True
  def removeDuplicates(self):
    current=self.first
    used=[current.data]
    while current.next!=None:
      if current.next.data in used:
        current.next=current.next.next
      else: 
        used.append(current.next.data)
        current=current.next
        
  def findUnordered(self,data):
    current=self.first
    while current!=None and current.data!=data:
      current=current.next
    return current
  def findOrdered(self,data):
    current=self.first
    while current!=None and current.data!=data:
      current=current.next
    return current
  def mergeList(self,b):
    current=self.first
    currentb=b.first
    merged=LinkedList()
    while current!=None or currentb!=None:
      if current==None:
        merged.extendLinks(currentb)
        break
      elif currentb==None:
        merged.extendLinks(current)
        break
      elif current.data>currentb.data:
        merged.insertLast(currentb.data)
        currentb=currentb.next
      else:
        merged.insertLast(current.data)
        current=current.next
    return merged
      
         
    
  def __str__(self):
    out=""
    current=self.first
    i=0
    while current!=None:
      if i%10==0 and i!=0:
        out+="\n"
      out+=str(current.data)+" "
      current=current.next
      
        
      i+=1
    return out
      
    return out
  def copyList(self):
    return copy.deepcopy(self)
  def reverseList(self):
    reverse=LinkedList()
    current=self.first
    while current!=None:
      reverse.insertFirst(current.data)
      current=current.next
    return reverse
  def addLinks(self,lst):
    self.first=None
    for i in lst:
      self.insertLast(i)
