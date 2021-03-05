#Lab #10
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name: Ryan Herman
# Collaboration Statement: None
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
        self.length = 0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        #write your code here
        #Checks if the stack is empty
        if self.top == None:
            return True
        return False

    def __len__(self):
        #write your code here
        #Traverses through the stack adding one until the next Node is None
        current = self.top
        #While there is a Node add one
        while current:
            self.length += 1
            current = current.next
        #Returns the length
        return self.length

    def peek(self):
        #write your code here
        #Returns the top layer of the stack
        return self.top.value

    def push(self,value):
        #write your code here
        #Checks if empty then makes the top Node equal to new node
        if self.top == None:
            self.top = Node(value)
        #If the stack is not empty adjusts the next Node and top Node accordingly
        else:
            newNode = Node(value)
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        #write your code here
        #Checks if stack is empty, because can't remove anything from an empty list
        if self.top == None:
            return 'Stack is empty'
        #If the stack is not empty adjusts the next Node and top Node accordingly
        else:
            popValue = self.top.value
            self.top = self.top.next
            return popValue