import PriorityQueueList

pq = PriorityQueueList.PriorityQueueList() #create an empty queue

pq.enqueue(20)
pq.enqueue(9)
pq.enqueue(10)
pq.enqueue(8)

print(pq)
print(pq.size())

pq_item = pq.dequeue()
print(pq_item)

print(pq.size())
print(pq.is_empty())