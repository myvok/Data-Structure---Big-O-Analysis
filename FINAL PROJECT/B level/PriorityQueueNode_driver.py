import PriorityQueueNode
import sys

pq = PriorityQueueNode.PriorityQueueNode()

# Add items to the queue with different priorities
# pq.enqueue(2023)
# pq.enqueue(8)
# pq.enqueue(111)
# pq.enqueue(5)
pq.enqueue(1)
pq.enqueue(2)
pq.enqueue(3)
pq.enqueue(4)

print(pq)
# print(pq.size())
# print(pq.is_empty())

# #Dequeue items 
print(sys.getsizeof(pq._front))

print(pq.dequeue())
print(sys.getsizeof(pq._front))
print(pq)

# print(pq.dequeue())
# print(pq)

# print(pq.size())
# print(pq.is_empty())

# print("----------------")
# print(pq.dequeue())
# print(pq.dequeue())

# print(pq.size())
# print(pq.is_empty())