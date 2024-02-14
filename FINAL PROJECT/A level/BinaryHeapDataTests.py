import BinaryHeap
import time
import random

random.seed(2007)

#re-initialize the data collection file
file1 = open("BinaryHeapData_insert.csv","w")
file1.write("operation, n, work\n")
file1.close()

file2 = open("BinaryHeapData_percUp.csv","w")
file2.write("operation, n, work\n")
file2.close()

file3 = open("BinaryHeapData_getRoot.csv", "w")
file3.write("operation, n, work\n")
file3.close()

file4 = open("BinaryHeapData_percDown.csv", "w")
file4.write("operation, n, work\n")
file4.close()

file5 = open("BinaryHeapData_minChild.csv", "w")
file5.write("operation, n, work\n")
file5.close()

file6 = open("BinaryHeapData_size.csv", "w")
file6.write("operation, n, work\n")
file6.close()

file7 = open("BinaryHeapData_isEmpty.csv", "w")
file7.write("operation, n, work\n")
file7.close()

file8 = open("BinaryHeapData_str.csv", "w")
file8.write("operation, n, work\n")
file8.close()

file1 = open("BinaryHeapData_insert.csv","a") #open in append mode so the data isn't overwritten
file2 = open("BinaryHeapData_percUp.csv","a")
file3 = open("BinaryHeapData_getRoot.csv", "a")
file4 = open("BinaryHeapData_percDown.csv", "a")
file5 = open("BinaryHeapData_minChild.csv", "a")
file6 = open("BinaryHeapData_size.csv", "a")
file7 = open("BinaryHeapData_isEmpty.csv", "a")
file8 = open("BinaryHeapData_str.csv", "a")

for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100000,1000000)):
        #fill the list with random integers
        bh.insert(random.randint(11,100000))

    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    work = bh.insert(8)
    _, n = bh.size()
    file1.write("insert, "+str(n)+", "+str(work)+"\n")
    print("inserted 8 into a heap with size "+str(n))

    #now that the heap is big, set up the tests and check how long it takes to perc up item
    _, n = bh.size()
    work = bh.perc_up(n)
    file2.write("perc_up, "+str(n)+", "+str(work)+"\n")
    print("heap of size "+str(n) + " perc_up")

    #now that the heap is big, set up the tests and check how long it takes to get the root of the heap
    _, work = bh.get_root()
    _, n = bh.size()
    file3.write("get_root, "+str(n)+", "+str(work)+"\n")
    print("got the root in heap with size "+str(n))

    #set up the tests and check how long it takes to perc down item
    _, n = bh.size()
    work = bh.percDown(1)
    file4.write("perc_down, "+str(n)+", "+str(work)+"\n")
    print("heap of size "+str(n)+" perc_down")

    # test minChild()
    _, n = bh.size()
    work, _ = bh.minChild(1)
    file5.write("minChild, " + str(n) + ", " + str(work) + "\n")
    print("found minChild for heap with size " + str(n))

    # test size()
    work, n = bh.size()
    file6.write("size, " + str(n) + ", " + str(work) + "\n")
    print("returned size for heap with size " + str(n))

    # test is_empty()
    work,_ = bh.is_empty()
    _, n = bh.size()
    file7.write("is_empty, " + str(n) + ", " + str(work) + "\n")
    print("returned is_empty for heap with size " + str(n))

    # test __str__()
    work,_ = bh.__str__()
    _, n = bh.size()
    file8.write("__str__, " + str(n) + ", " + str(work) + "\n")
    print("returned a string representation for heap with size " + str(n))

print("End binary heap insert\n")
print("End binary heap perc_up\n")
print("End binary heap get_root\n")
print("End binary heap perc_down\n")
print("End binary heap minChild\n")
print("End binary heap size\n")
print("End binary heap is_empty\n")
print("End binary heap __str__\n")


file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()



print("Done. check the file for your test results")

