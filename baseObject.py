import pymysql

class baseObject:
    
    def setupObject(self,tn):
        self.data = []
        self.tempdata = {}
        self.tn = tn
        self.fnl = []
        self.pk = ''
        self.conn = None
        self.errorList = []
        self.getFields()
    
    def connect(self):
        import config
        self.conn = pymysql.connect(host=config.DB['host'], port=config.DB['port'], 
        user=config.DB['user'],passwd=config.DB['passwd'], db=config.DB['db'], 
        autocommit=True)
    def getFields(self):
        sql = 'DESCRIBE `' + self.tn + '`;'
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)
        self.fnl = []
        for row in cur:
            self.fnl.append(row['Field'])
            if row['Extra'] == 'auto_increment' and row['Key'] == 'PRI':
                self.pk = row['Field']
        #print(self.fnl)
    def add(self):
        self.data.append(self.tempdata)
    def set(self,fn,val):
        if fn in self.fnl:
            self.tempdata[fn] = val
        else:
            print('Invalid field: ' + str(fn))
    def update(self,n,fn,val):
        if len(self.data) >= (n + 1) and fn in self.fnl:
            self.data[n][fn] = val
        else:
            print('could not set value at row ' + str(n) + ' col ' + str(fn) )
    def insert(self,n=0):
        cols = ''
        vals = ''
        tokens = []
        for fieldname in self.fnl:
            if fieldname in self.data[n].keys():
                tokens.append(self.data[n][fieldname])
                vals += '%s,'
                cols += '`'+fieldname+'`,'
        vals = vals[:-1]
        cols = cols[:-1]
        sql = 'INSERT INTO `' + self.tn +'` (' +cols + ') VALUES (' + vals+');'
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data[n][self.pk] = cur.lastrowid
    def delete(self,n=0):
        item = self.data.pop(n)
        self.deleteById(item[self.pk])
        
    def deleteById(self,id):
        sql = 'DELETE FROM `' + self.tn + '` WHERE `'+self.pk+'` = %s;'
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
    
        
    def getById(self,id):
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `'+self.pk+'` = %s;'
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)
    def getAll(self,order = None):
        sql = 'SELECT * FROM `' + self.tn + '` '
        if order != None:
            sql += ' ORDER BY `'+order+'`'
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql)
        self.data = []
        for row in cur:
            self.data.append(row)   
            
    def update(self,n=0):
        tokens = []
        setstring = ''
        for fieldname in self.data[n].keys():
            if fieldname != self.pk:
                setstring += ' `'+fieldname+'` = %s,'
                tokens.append(self.data[n][fieldname])
            
        setstring = setstring[:-1]
        sql = 'UPDATE `' + self.tn + '` SET ' + setstring + ' WHERE `' + self.pk + '` = %s' 
        tokens.append(self.data[n][self.pk])
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
    
    def getByField(self,field,value):
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `'+field+'` = %s;'
        tokens = (value)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)
    def getLikeField(self,field,value):
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `'+field+'` LIKE %s;'
        tokens = ('%'+value+'%')
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)
