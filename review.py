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
    def getByCustomer(self,id):
        '''
        SELECT * FROM `conlontj_attends` 
        LEFT JOIN `conlontj_events` ON `conlontj_events`.`eid` = `conlontj_attends`.`event_id`
        WHERE  `conlontj_attends`.`customer_id` = 3
        
        '''
        sql = '''SELECT * FROM `conlontj_attends` 
        LEFT JOIN `conlontj_events` ON `conlontj_events`.`eid` = `conlontj_attends`.`event_id`
        WHERE  `conlontj_attends`.`customer_id` = %s'''
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)