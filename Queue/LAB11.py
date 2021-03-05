#Lab #11
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name: Ryan Herman
# Collaboration Statement: I completed this lab by myself using information from the course
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> print(x)
        Head:Node(1)
        Tail:Node(3)
        Queue:1 2 3
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self): 
        self.head=None
        self.tail=None
        self.length = 0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        #write your code here
        #Checks to see if head node is empty
        if self.head == None:
            return True
        return False

    def __len__(self):
        #write your code here
        #If empty returns zero
        if self.head == None:
            return 0
        #If queue is not empty traverses and counts number of nodes in queue
        current = self.head
        while current:
            self.length += 1
            current = current.next
        #Returns the length
        return self.length

    def enqueue(self, value):
        #write your code here
        node = Node(value)
        #Checks if empty assigns nodes
        if self.head == None:
            self.head = node
            self.tail = node
        #If not empty, assigns nodes
        else:
            self.tail.next = node
            self.tail = node


    def dequeue(self):
        #write your code here
        #Checks if queue is empty because cannot remove Node from an empty queue
        if self.head == None:
            return 'Queue is empty'
        #If not empty, assigns the nodes to their values
        else:
            deqValue = self.head.value
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            #Returns the value being dequeued
            return deqValue
