class Node:

    def __init__(self, d=None):
        """Create an empty Node"""
        self._data = d
        self._next = None
    def get_data(self):
        """Returns the value of the instance variable _data"""
        return self._data
    def set_data(self,d):
        """Set the new value for _data"""
        self._data = d
    def get_next(self):
        """Returns the value of the instance variable _next"""
        return(self._next)
    def set_next(self,n):   
        """Set the new value for the instance variable _next"""
        self._next = n
    def __str__(self):
        """Return the string represent for _data"""
        return(str(self._data))
    def check_next(self):
        """Check if there is any next node"""
        if self._next == None:
            return True         #returns True if there's no next node
        return False




