#Lab #12
#Due Date: 03/22/2019, 11:59PM
########################################
#                                      
# Name: Ryan Herman
# Collaboration Statement: I worked on this lab by myself using information from the lectures
#  
########################################



class MaxHeapPriorityQueue:
    '''
        >>> h = MaxHeapPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
    '''

    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        #write your code here
    #Returns the length which is the length -1
        return len(self.heap) - 1


    def parent(self,index):
        # write your code here
    #Checks if root has parent
        if index == 1:
            return self.heap[index]
    #Returns parent
        elif (index > 1 and index < self.size):
            return int(index/2)

    def leftChild(self,index):
        # write your code here
        #Returns left child
        return index*2


    def rightChild(self,index):
        #write your code here
        #Returns Right Child
        return index*2 + 1

    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]

        

    def insert(self,x):
        #write your code here
        self.heap.append(x)
        x = int(x)
        self.size = self.size + 1
        i = self.size
    #Checks if parent is less than inserted number
        while (i > 1 and self.parent(i) is not None and self.parent(i) < x):
    #Moves up child
            self.swap(i,x)
    #Moves up towards root
            i = i / 2
    #Recursively runs again
            self.heap.insert(i ,x)

    def deleteMax(self):

        if self.size<=0:
            return None
        elif self.size==1:
            self.size=0
            return self.heap[0]

        #write your code here
        else:
            self.heap.append(0)
            max = self.heap[0]
        #Puts last element as root (from lecture)
            self.heap[0] = self.heap[len(self.heap)-1]
            self.size = self.size - 1
