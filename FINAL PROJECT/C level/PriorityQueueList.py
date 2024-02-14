
class PriorityQueueList:
    def __init__(self): 
        """Creates new empty queue"""
        self._items = []

    def __str__(self):
        """Returns string representation for _items"""
        return str(self._items)

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)  #Return True if empty, False if not

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self._items.append(item)

    def dequeue(self):
        """Searches the list for the highest-priority item and removes it from wherever it is"""
        if self.is_empty():  #Notify if the Queue is empty
            print("Priority Queue List is empty!")
        highest_priority_index = 0     #Set the index of the highest-priority item to the first item in the list
        for i in range(1, len(self._items)): #Goes through all items in the Queue, starting from the second item
            if self._items[i] < self._items[highest_priority_index]:  #Check if the current item has higher priority than the current highest-priority item
                highest_priority_index = i  #Update the index of the highest-priority item
        return self._items.pop(highest_priority_index)   #Removes and returns the highest-priority item


    def size(self):
        """Returns the number of items in the queue"""
        return len(self._items)
