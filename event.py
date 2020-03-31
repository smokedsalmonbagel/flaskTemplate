import pymysql
from baseObject import baseObject
class eventList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('conlontj_events')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        
        #Add if statements for validation of other fields
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
    def getUpcoming(self):    
        #SELECT * FROM `conlontj_events` WHERE EventStartDate > NOW() AND EventStartDate < NOW() + 5days
        sql = 'SELECT * FROM `conlontj_events` WHERE EventStartDate > NOW() AND EventStartDate < NOW() + 5days;'
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        n=0
        for row in cur:
            self.data.append(row)
            n+=1

    
    
    
    
    
    
    
    
    
    
        