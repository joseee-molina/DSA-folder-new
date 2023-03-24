
class DisjointSet_QF:
    """ Quick Find Disjoint Set implementation 
    The structure is an array containing the parent of the
    current element in itself, making it easy to Find the parent
    but O(N) time to union elements
    """

    def __init__(self, size=1):
        self.size=size
        self.arr=[]
        self.fillSet()
    
    def fillSet(self):
        self.arr=[]
        for i in range(self.size):
            self.arr.append(i)
    
    def printSet(self):
        set_string= ""
        for i in range(self.size):
            set_string += str(self.arr[i])+ " "
        print(set_string)

    def find(self, element):
        return self.arr[element]
    
    def union(self, el1, el2):
        
        el2_parent = self.arr[el2]
        el1_parent = self.arr[el1]
        for i in range(self.size):
            if self.arr[i]==el2_parent:
                self.arr[i] = el1_parent
                
        

class DisjointSet_QU:
    """
    Disjoint Set Quick Union
    Array with -Size at the array[element] if top node
    or parent at array[element] if element is not top node
    Easy to Union but can be up to O(N) to Find
    """
    
    def __init__(self,size = 1):
        self.arr =[]
        self.size = size
        self.fillSet()

    def fillSet(self):
        self.arr=[]
        for i in range(self.size):
            self.arr.append(-1)
    
    def printSet(self):
        set_string= ""
        for i in range(self.size):
            set_string += str(self.arr[i])+ " "
        print(set_string)

    def sizeOf(self, element):
        #Give me an element, give you the size of the tree
        if arr[element]<0:
            return -1*arr[element]
        else:
            return sizeOf(arr[element])

    def parent(self, element):
        return self.arr[element]

    def root(self, element):
        if self.arr[element]<0:
            return element
        else:
            return self.root(self.arr[element])

    def union(self, el1, el2):
        
        rootNodeEl1 = self.root( el1)
        
        rootNodeEl2 = self.root(el2)
        
        if(-1*self.arr[rootNodeEl1] > -1*self.arr[rootNodeEl2]):
            #Stick el2 to el1
            self.arr[rootNodeEl1]+=self.arr[rootNodeEl2]
            self.arr[rootNodeEl2] = rootNodeEl1
        else:
            self.arr[rootNodeEl2]+=self.arr[rootNodeEl1]
            self.arr[rootNodeEl1] = rootNodeEl2


def testing():
    qf_example = DisjointSet_QF(5)
    qf_example.union(3, 0)
    qf_example.printSet()
    #print(qf_example.find(3))

    #############################
    
    qu_example = DisjointSet_QU(5)
    qu_example.union(1,3)
    qu_example.union(0,1)
    qu_example.union(2,4)
    qu_example.union(4,0)
    qu_example.printSet()

if __name__ == "__main__":
    testing()