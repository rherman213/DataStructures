#Lab #9
#Due Date: 03/01/2019, 11:59PM
########################################
#                                      
# Name: Ryan Herman
# Collaboration Statement: I worked on this lab by myself using information from the course
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.isEmpty()
        True
        >>> x.pop()
        'List is empty'
        >>> x.add(8)
        >>> x.add(7)
        >>> x.add(3)
        >>> x.add(-6)
        >>> x.add(58)
        >>> x.add(33)
        >>> x.add(1)
        >>> x.add(-88)
        >>> print(x)
        Head:Node(58)
        Tail:Node(-88)
        List:58 33 8 7 3 1 -6 -88
        >>> x.isEmpty()
        False
        >>> len(x)
        8
        >>> x.pop()
        -88
        >>> print(x)
        Head:Node(58)
        Tail:Node(-6)
        List:58 33 8 7 3 1 -6
        >>> x.pop()
        -6
        >>> x.pop()
        1
        >>> x.pop()
        3
        >>> print(x)
        Head:Node(58)
        Tail:Node(7)
        List:58 33 8 7
        >>> len(x)
        4
        >>> x.add(-4)
        >>> print(x)
        Head:Node(58)
        Tail:Node(-4)
        List:58 33 8 7 -4
        >>> x.add(7.5)
        >>> x.pop()
        -4
        >>> print(x)
        Head:Node(58)
        Tail:Node(7)
        List:58 33 8 7.5 7
    '''
    def __init__(self):
    	#You can add a count attribute for len
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        # write your code here
        newNode = Node(value)
        self.count += 1
        # Checks if Linked List is empty, places in new Node
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        # Checks if new value can go at beginning of Linked List
        elif self.head.value < value:
            node = Node(value)
            node.next = self.head
            self.head = node
        else:
            # Will sort in descending order
            temp = self.head
            while (temp.next):
                if temp.next.value < value:
                    newNode.next = temp.next
                    temp.next = newNode
                    return
                temp = temp.next

            # Sets the newNodes in the list
            temp.next = newNode
            self.tail = newNode

    def pop(self):
        # write your code here
        # Checks if LinkedList is empty because it wouldn't be able to call pop method
        if self.isEmpty():
            return 'List is empty'
        else:
            currentValue = self.tail.value
            # Checks if only one Node in Linked List
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.count -= 1
            # Traverses to the end of the Linked List then sets it to None and stores the value that was removed
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = None
                self.tail = temp
            # Decreases the count so that the length is updated
                self.count -= 1
            return currentValue

    def isEmpty(self):
        # write your code here
        if self.head == None:
            return True
        return False

    def __len__(self):
        # write your code here
        return self.count


