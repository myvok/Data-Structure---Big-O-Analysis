import PQList_test
import time
import random

random.seed(2007)

#re-initialize the data collection file
file1 = open("PQListDataTest_enqueue.csv","w")
file1.write("operation, n, work\n")
file1.close()

file2 = open("PQListDataTest_dequeue.csv","w")
file2.write("operation, n, work\n")
file2.close()

file3 = open("PQListDataTest_size.csv","w")
file3.write("operation, n, work\n")
file3.close()

file4 = open("PQListDataTest_isEmpty.csv","w")
file4.write("operation, n, work\n")
file4.close()

file5 = open("PQListDataTest_str_.csv","w")
file5.write("operation, n, work\n")
file5.close()

file1 = open("PQListDataTest_enqueue.csv","a") #open in append mode so the data isn't overwritten
file2 = open("PQListDataTest_dequeue.csv","a")
file3 = open("PQListDataTest_size.csv","a")
file4 = open("PQListDataTest_isEmpty.csv","a")
file5 = open("PQListDataTest_str_.csv","a")

for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    pql = PQList_test.PriorityQueueList()
    for i in range(random.randint(100000,1000000)):
        #fill the list with random integers
        pql.enqueue(random.randint(11,100000))
    
    #now that the heap is big, set up the tests and check how long it takes to add a new item of high priority
    work,_ = pql.enqueue(8)
    _, n = pql.size()
    file1.write("add, "+str(n)+", "+str(work)+"\n")
    print("added 8 into a queue with size "+str(n))

    #now that the heap is big, set up the tests and check how long it takes to add a new item of high priority
    work,_ = pql.dequeue()
    _, n = pql.size()
    file2.write("remove, "+str(n)+", "+str(work)+"\n")
    print("removed an item from a queue with size "+str(n))

    #now that the heap is big, set up the tests and check how long it takes to the return the size of the queue
    work, n = pql.size()
    file3.write("size, "+str(n)+", "+str(work)+"\n")
    print("The queue with size "+str(n))

    #now that the heap is big, set up the tests and check how long it takes to check if the LinkedQueue is empty
    work,_ = pql.is_empty()
    _, n = pql.size()
    file4.write("size, "+str(n)+", "+str(work)+"\n")
    print("Check if the LinkedQueue is empty with size "+str(n))

    #now that the heap is big, set up the tests and check how long it takes to return a string represents the contents of the queue
    work,_ = pql.__str__()
    _, n = pql.size()
    file5.write("size, "+str(n)+", "+str(work)+"\n")
    print("Returns a string represents the contents of the queue with size "+str(n))

print("End priority queue list add\n")
print("End priority queue list remove\n")
print("End priority queue list size\n")
print("End priority queue list isEmpty\n")
print("End priority queue list __tr__\n")

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()

print("Done. check the file for your test results")