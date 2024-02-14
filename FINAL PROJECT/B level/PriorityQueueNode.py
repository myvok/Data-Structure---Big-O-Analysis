
import Node
class PriorityQueueNode():
    
    def __init__(self):
        """Create an empty LinkedQueue"""
        self._front = None
        self._rear = None
        self._length = 0

    def size(self):
        """Returns the size of the LinkedQueue"""
        return self._length
    
    def is_empty(self):
        """Check if the LinkedQueue is empty"""
        return(self._length==0) #Returns True if emtpy, False if not
    
    def enqueue(self,item): 
        """Adds a node containing an item to the end of the LinkedQueue"""
        node = Node.Node(item)            #Create a node containing an item
        if not self.is_empty():           #If the LinkedQueue is not empty
            self._rear.set_next(node)     #Add the node to the position after the rear
            self._rear = self._rear.get_next()

        else:                             #If empty: 
            self._front = node            #set the front point to the new Node
            self._rear = node             #set the rear to point to the new Node
        
        self._length +=1                  #Length increase by 1 when adding 1 item

    def dequeue(self):    
        """Searches the list for the highest-priority item and removes it from wherever it is"""

        if self.is_empty():
            return None

        highest_priority_node = self._front     #Set the highest-priority node to the front of the queue
        prev_node = None                        #Set previous node to None
        current_node = self._front              #Set current node to the front of the queue
        while current_node is not None:     #Loop runs until the queue is empty
            #If the item in current node has higher priority than that of the highest-priority node
            if current_node.get_data() < highest_priority_node.get_data():
                #Update the highest-priority node
                highest_priority_node = current_node    
                prev_highest_priority_node = prev_node

            #Moves to the next node
            prev_node = current_node
            current_node = current_node.get_next()
        
        if highest_priority_node == self._front:    #If the highest-priority node is the front node
            self._front = highest_priority_node.get_next()  #Set the front node to the next node
            highest_priority_node._next = None   #Remove the link between 2 nodes
            
        else:
            #Set the next node of the previous highest-priority node next to the next node of the highest-priority node
            prev_highest_priority_node.set_next(highest_priority_node.get_next())
            if highest_priority_node == self._rear:      #If the highest-priority node is the rear node
                self._rear = prev_highest_priority_node     #Set the rear node to the previous highest-priority node
            
        self._length -= 1   #Length decrease by 1 when removing 1 item
        return highest_priority_node.get_data()  #return the item of the highest-priority node
             
    def __str__(self):   
        """Returns a string represents the contents of the queue"""   
        current = self._front       #saves a reference to the front node in a temporary variable
        queue = ""                  #create a new empty string
        while current != None:              #Let the temporary variable run until it reaches the rear
            queue += str(current) + " "     
            current = current.get_next()    #Make the new top
        return str(queue)