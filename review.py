import pymysql
from baseObject import baseObject
from customer import customerList
from event import eventList
class reviewList(baseObject):
    #this is the assignment
    def __init__(self):
        self.setupObject('conlontj_attends')
        
    def verifyNew(self,n=0):
        self.errorList = []
        event_id = self.data[n]['event_id']
        customer_id = self.data[n]['customer_id']
        e = eventList()
        e.getById(event_id)
        event_name = e.data[0]['name']
        
        c = customerList()
        c.getById(customer_id )
        customer_name = c.data[0]['fname']
        prefix_text = customer_name + '\'s review of "' + event_name + '": '
        
        if len(self.data[n]['review']) == 0:
            self.errorList.append("Review body cannot be blank.")
        else:
            self.data[n]['review'] = prefix_text + self.data[n]['review']
        
        #self.data[n]['review_date'] = now
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
        #print('tokens:',str(tokens))
        self.log(sql,tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)