from customer import customerList
from event import eventList
from review import reviewList

r = reviewList()
r.getByCustomer(3)
print(r.data)