import pymysql
from baseObject import baseObject
class customerList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('conlontj_customers')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        c = customerList()
        c.getByField('email',self.data[n]['email'])
        if len(c.data) > 0:
            self.errorList.append("Email address is already registered.")
        
        
        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First name cannot be blank.")
        if len(self.data[n]['lname']) == 0:
            self.errorList.append("Last name cannot be blank.")
        #Add if statements for validation of other fields
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
    def verifyChange(self,n=0):
        self.errorList = []
        
        c = customerList()
        c.getByField('email',self.data[n]['email'])
        #print(c.data)
        if len(c.data) > 0:
            print(self.data[n])
            print(c.data[0])
            if str(self.data[n]['id']) != str(c.data[0]['id']):
                self.errorList.append("Email address is already registered.")
        
        
        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First name cannot be blank.")
        if len(self.data[n]['lname']) == 0:
            self.errorList.append("Last name cannot be blank.")
        
        if len(self.errorList) > 0:
            return False
        else:
            return True
    def tryLogin(self,email,pw):    
        #SELECT * FROM `conlontj_customers` WHERE `email` = 'b@a.com' AND `password` = '123'
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `email` = %s AND `password` = %s;'
        tokens = (email,pw)
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
        if n > 0:
            return True
        else:
            return False
    
    
    
    
    
    
    
    
    
    
        