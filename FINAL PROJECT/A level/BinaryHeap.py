
class BinaryHeap:
    
    def __init__(self):
        self.heapList = [None]
        self.currentSize = 0
        
    def insert(self,k):
       # initialize a counter to keep track of the number of operations performed
       work = 0
       self.heapList.append(k)  # Add the new element to the end of the heap list
       work += 1
       self.currentSize += 1    # Increase the size of the heap
       work += self.perc_up(self.currentSize)   # Move the new element to its correct position
       return work
       
    def perc_up(self,i):
        # initialize a counter to keep track of the number of operations performed
        work = 0
        while i//2>0:   # While the current element has a parent and is smaller than its parent
            work += 1
             # Swap if the current element is smaller than its parent
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
                work += 3
            
            # Move up to the parent of the current element
            i = i//2
            work += 1
        return(work)

    def get_root(self):
        # initialize a counter to keep track of the number of operations performed
        work = 0
        if self.is_empty()[1]:   # If the heap is empty, return None
            return None #I added this; it wasn't in the book
        
        # Get the root node 
        retval = self.heapList[1]
        # Replace the root node with the last node in the heap
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1   # Decrement the current size of the heap by 1
        self.heapList.pop()     # Remove the last node
        work +=4
        work += self.percDown(1)
        # print("a")

        return retval, work
    
    def percDown(self,i):
        # initialize a counter to keep track of the number of operations performed
        work = 0
        while(i*2) <= self.currentSize:
            # print(i)
            work +=1
            w, mc = self.minChild(i)
            work += w
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp 
                work +=3
            i = mc
            # print(mc)
            work +=1
        return (work)

    def minChild(self,i):
        # initialize a counter to keep track of the number of operations performed
        work = 0
        if i*2 +1 > self.currentSize:
            work +=1
            return (work, i*2)
        else:
            work +=1
            if self.heapList[i*2] < self.heapList[i*2+1]:
                work +=2
                return (work, i*2)
            else:
                work +=2
                return (work, i*2+1)

    
    def size(self):
        work = 0
        work +=1
        return work, self.currentSize
    
    def is_empty(self):
        work = 0
        work +=1
        return work, self.currentSize == 0
            
    def __str__(self):
        work = 0
        work = len(self.heapList)
        return work, (str(self.heapList))