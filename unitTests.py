from customer import customerList
import time

cl = customerList()

print(cl.fnl)
print(cl.pk)

c = customerList()
c.set('fname','Testguy')
c.set('lname','Test')
c.set('email','a@a.com')
c.set('subscribed','True')
c.set('password','12345')
c.add()
# A - show the mysql table

c.insert()

c = customerList()
c.getAll()
print(c.data)




















