import random

"""
This program should put all the people in the list of names into random groups. 
Each group should have no fewer than 2 and not more than 4 people. 

The number of groups will be determined by the size of the input file.
"""

def make_groups(min_size, max_size, names):
    #make a copy of the original list 
    listOfNames = names.copy()
    #initialize an empty list to store the list of groups of people
    groups = []

    while len(listOfNames) > max_size: #loop runs until the number of remaining names is less than the maximum size of a group
        newgroup=[]
        for i in range(random.randint(min_size,max_size)): #randomly choose the size of the group
            newgroup.append(listOfNames.pop())     #remove a name from the list and append it to the new group
        groups.append(newgroup)     #add the new group to the list of groups

    if len(listOfNames) < min_size:  #if the number of remaining names is less than the minimum size of a group
        #initialize the index of the starting group
        start = 0   
        for i in listOfNames:
            #if the current group is already at maximum capacity, move to the next group
            while len(groups[start]) == max_size:
                start+=1
            groups[start].append(i) #add the name to the current group
    elif (len(listOfNames) != 0):   #if the number of remaining names is between min size and max size
        groups.append(listOfNames)  #add the group to the list of groups

    #Return the list of groups
    return groups