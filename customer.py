import pymysql
from baseObject import baseObject
class customerList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('conlontj_customers')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First name cannot be blank.")
        #Add if statements for validation of other fields
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
    
    
    
    
    
    
    
    
    
    
        