"""
PART 1: Discussion Questions

Runtime:

1.) What determines the workload (i.e. # of tasks) it takes to figure out whether
my animal cracker box contains an elephant? It depends on
which data structure I use. If I put all the animal crackers in a set, the
workload will be small, and thus creating a constant runtime: O(1). If I use
a different data structure, for example if I put all of my animal crackers in a
list, then my workload will be greater, since I will have to check every item in
the list to see if the elephant is in there, thus creating a linear runtime: O(n).


2.) Ordering following runtimes from fastest (first) to slowest (last):
    a.) O(1)
    b.) O(log n)
    c.) O(n)
    d.) O(n log n)
    e.) O(n2)
    f.) O(2n)


Stacks and Queues:

1. In the following cases, would a stack or queue be a more appropriate data structure?
    1.) The process of loading and unloading pallets onto a flatbed truck: STACK 
    2.) Putting bottle caps on bottles of beer as they roll down an assembly line: QUEUE 
    3.) Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2): STACK 

2.) Describe two more situations where a queue would be an appropriate data structure.
    1.) Patients coming to a pharmacy, waiting to pick up their medicine.
    2.) A deli line 
3.) Describe two more situations where a stack would be an appropriate data structure.
    1.) Putting Pringles chips into a pringles tin, and then taking them out to eat them :)
    2.) Folding and stacking all the towels at the gym, then members taking them one by one 
    for their workout and shower.


Linked List:

1.) The 3 nodes are Apple, Berry, and Cherry. The data (which is one attribute of the node) 
for each node is: "Apple", "Berry", and "Cherry" respectively. The head is pointing to 
the Apple node. There is no tail in this diagram. Each node has a second attibute of 'next' 
which is referencing the next node in the sequence.

2.) Nodes in singly linked lists only have an attribute of 'next' so the node 
only has knowledge of the following node in the sequence, whereas nodes in doubly linked lists
have an attribute of 'next' and also an attribute of 'prev', which means each node
not only has knowledge of the next node in the sequence, but also the prior node in the sequence. 

3.) It is faster to append to a linked list if we keep track of the tail as an attribute,
because then we can go directly to the end of the list when appending, which means
we would have a runtime of O(1), whereas we would have to traverse the whole sequence
to find the end of the list if we are not keeping track of the tail, which means we would
have an O(n) runtime.  















"""