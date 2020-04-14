from customer import customerList
import time

cl = customerList()

c = customerList()
c.set('fname','Testguy')
c.set('lname','Test')
c.set('email','a@a.com')
c.set('subscribed','True')
c.set('password','12345')
c.add()
# A - show the mysql table

c.verifyNew()

print(c.errorList)
print(c.data)




















