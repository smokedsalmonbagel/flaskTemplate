import pymysql
from baseObject import baseObject
class eventList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('conlontj_events')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['name']) == 0:
            self.errorList.append("Name cannot be blank.")
        
        #Add if statements for validation of other fields
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
    def verifyChange(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['name']) == 0:
            self.errorList.append("Name cannot be blank.")
        
        #Add if statements for validation of other fields
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
    
    
    
    
    
    
    
    
    
    
        