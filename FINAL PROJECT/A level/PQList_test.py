
class PriorityQueueList:
    def __init__(self): 
        """Creates new empty queue"""
        self._items = []
        self.currentSize = 0

    def __str__(self):
        """Returns string representation for _items"""
        work = len(self._items)
        return (work, str(self._items))

    def is_empty(self):
        """Check if the queue is empty"""
        work = 0
        work +=1
        return (work, self.currentSize == 0)  #Return True if empty, False if not

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        work = 0
        self._items.append(item)
        work += 1
        self.currentSize +=1
        return(work, self._items)

    def dequeue(self):
        """Searches the list for the highest-priority item and removes it from wherever it is"""
        work = 0 
        if self.is_empty()[1]:  #Notify if the Queue is empty
            work +=1
            #print("Priority Queue List is empty!")
            return work, 0
        highest_priority_index = 0     #Set the index of the highest-priority item to the first item in the list
        for i in range(1, len(self._items)): #Goes through all items in the Queue, starting from the second item
            if self._items[i] < self._items[highest_priority_index]:  #Check if the current item has higher priority than the current highest-priority item
                highest_priority_index = i  #Update the index of the highest-priority item
                work += 1
                self.currentSize -=1
            work += 1
        self._items.pop(highest_priority_index)
        return work, self.currentSize

    def size(self):
        """Returns the number of items in the queue"""
        work = 0
        work +=1
        return (work, self.currentSize)
