import pymysql
from baseObject import baseObject
class reviewList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('conlontj_attends')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['review']) == 0:
            self.errorList.append("Review body cannot be blank.")
        
        #Add if statements for validation of other fields
  
        if len(self.errorList) > 0:
            return False
        else:
            return True