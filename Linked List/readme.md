## What is Linked List
- A Linked List Is a Linear Data Structure, in Which the Elements Are Not Stored at Contiguous Memory Locations. the Elements in A Linked List Are Linked Using Pointers
- Linked List Contain of Nodes Where Each Node Consist of Data Field and Reference Field.
___
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/e8cb4245-2d35-481b-9995-46780ab95718)
___
### Key Terms in Linked List 
**Node Structure:** A node in a linked list typically consists of two components:\
**Data:** It holds the actual value or data associated with the node.\
**Next Pointer:** It stores the memory address (reference) of the next node in the sequence.\
**Head and Tail:** The linked list is accessed through the head node, which points to the first node in the list. The last node in the list points to NULL or nullptr, indicating the end of the list. This node is known as the tail node.
_____________
### Advantage of Linked List
1. Dynamic Data structure
2. Ease of Insertion/Deletion
3. Efficient Memory Utilization
4. Implementation: Various advanced data structures can be implemented using a linked list like a stack, queue, graph, hash maps, etc.
________________________________
## Types of Linked List
1. Single-linked list
- In a singly linked list, each node contains a reference to the next node in the sequence.
- Traversing a singly linked list is done in a forward direction.
__________________
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/3215824d-7641-423b-aceb-b4b0e766d8c6)


2. Double linked list
- In a doubly linked list, each node contains references to both the next and previous nodes.
- This allows for traversal in both forward and backward directions, but it requires additional memory for the backward reference.
______________________
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/d5f5978e-c002-41eb-b031-62bf08b8d617)


3. Circular linked list
-  In a circular linked list, the last node points back to the head node, creating a circular structure.
-  It can be either singly or doubly linked.
  ___________________________
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/2fcd3874-6049-4c1c-8bcc-f3b886e04269)

________________

## Operation on Linked List
1. Insertion
2. Deletion
3. Searching
4. Displaying a Value

## Disadvantages of Linked Lists
1. Random Access: Unlike arrays, linked lists do not allow direct access to elements by index. Traversal is required to reach a specific node.
2. Extra Memory: Linked lists require additional memory for storing the pointers, compared to arrays.
3. Memory usage: The use of pointers is more in linked lists hence, complex and requires more memory.
4. Search Operation Costly: Searching for An Element Is Costly and Requires O(n) Time Complexity.

## Linked List vs. Array
________________________________
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/55087c45-5b5e-46a4-8c22-f6965e8de3bd)

## Linked List vs. Array in Time Complexity
________________________
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/ac545121-15d4-470f-a13b-84ceec6107bf)

## What is the difference between a singly and doubly linked list?

| Singly Linked List | Doubly Linked List|
|--------------------|-------------------|
|SLL nodes contains 2 field data field and next link field.| DLL nodes contains 3 fields data field, a previous link field and a next link field.|
|In SLL, the traversal can be done using the next node link only. Thus traversal is possible in one direction only.|In DLL, the traversal can be done using the previous node link or the next node link. Thus traversal is possible in both directions (forward and backward).
|The SLL occupies less memory than DLL as it has only 2 fields.|The DLL occupies more memory than SLL as it has 3 fields.
|The Complexity of insertion and deletion at a given position is O(n). |The Complexity of insertion and deletion at a given position is O(n / 2) = O(n) because traversal can be made from start or from the end.
|Complexity of deletion with a given node is O(n), because the previous node needs to be known, and traversal takes O(n)|Complexity of deletion with a given node is O(1) because the previous node can be accessed easily 
|A singly linked list consumes less memory as compared to the doubly linked list.|The doubly linked list consumes more memory as compared to the singly linked list.












