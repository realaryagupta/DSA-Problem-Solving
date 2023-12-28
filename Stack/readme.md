## What is Stack?
1. Stack is a linear data structure that follows a particular order in which the operations are performed.
2. The order may be LIFO(Last In First Out) or FILO(First In Last Out).
3. LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.
_______________
![image](https://github.com/realaryagupta/DSA-Notes/assets/119800001/e4e531bb-a294-49b7-9b75-ea89de8700bc)
______________

## Basic Operations on Stack
1. push() To Insert an Element Into the Stack
2. pop() To Remove an Element from The Stack
3. top() Returns The Top Element of The Stack.
4. isEmpty() Returns True if Stack Is Empty Else False.
5. size() Returns the Size of Stack.
___________________

## Algorithm for Each Operation
#### Push - Adds an item to the stack. If the stack is full, then it is said to be an Overflow condition.
**Algorithm for Push:**
  1. Begin
  2. If the stack is full, return (exit the procedure)
  3. Else
     - Increment the top of the stack
     - Assign a value to `stack[top]`
  4. End Else
  5. End Procedure


#### Pop - Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
**Algorithm for Pop:**
  1. Begin
  2. If the stack is empty, return (exit the procedure)
  3. Else
     - Store the value of `stack[top]`
     - Decrement the top of the stack
     - Return the stored value
  4. End Else
  5. End Procedure

#### Top - Returns the top element of the stack.
**Algorithm for Top:**
  1. Begin
  2. Return `stack[top]`
  3. End Procedure

#### isEmpty - Returns true if the stack is empty, else false.
**Algorithm for isEmpty:**
  1. Begin
  2. If `top` is less than 1
     - Return true
  3. Else
     - Return false
  4. End Procedure

## Time Complexity
|Operation|Complexity|
|---------|----------|
|push()|O(1)|
|pop()|O(1)|
|isEmpty()|O(1)|
|size()|O(1)|

## Types of Stack
1. Fixed Size Stack - As the name suggests, a fixed size stack has a fixed size and cannot grow or shrink dynamically.
2. Dynamic Size Stack - A dynamic size stack can grow or shrink dynamically. When the stack is full, it automatically increases its size to accommodate the new element, and when the stack is empty, it decreases its size.\

In addition to these two main types, there are several other variations of Stacks, including:

1. Infix to Postfix Stack: This type of stack is used to convert infix expressions to postfix expressions.
2. Expression Evaluation Stack: This type of stack is used to evaluate postfix expressions.
3. Recursion Stack: This type of stack is used to keep track of function calls in a computer program and to return control to the correct function when a function returns.
4. Memory Management Stack: This type of stack is used to store the values of the program counter and the values of the registers in a computer program, allowing the program to return to the previous state when a function returns.
5. Balanced Parenthesis Stack: This type of stack is used to check the balance of parentheses in an expression.
6. Undo-Redo Stack: This type of stack is used in computer programs to allow users to undo and redo actions.




















