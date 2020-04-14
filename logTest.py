from customer import customerList
from event import eventList
from review import reviewList

r = reviewList()
r.getById(2)
print(r.data)