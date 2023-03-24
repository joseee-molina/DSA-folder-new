class Node:
    """ item, previous and next nodes """
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class LinkedList:
    """ Circular implementation, sentinel Node to dennote beginning and end"""
    def __init__(self):
        self.sentinel = Node(-1)
        self.sentinel.prev = self.sentinel
        self.sentinel.next=self.sentinel
        
        self.size=0
    
    def addLast(self,item):
        node = Node(item,self.sentinel.prev, self.sentinel)
        self.sentinel.prev = node
        node.prev.next = node
        self.size+=1

    def print_list(self):
        ptr = self.sentinel.next
        nodes = ""
        while (ptr!=self.sentinel):
            nodes = nodes + str(ptr.item) + " "
            ptr = ptr.next
        print(nodes)


#Testing Method
def testing():
    list1 = LinkedList()
    list1.addLast(11)
    list1.addLast(12)
    list1.addLast(13)

    list1.print_list()

#if __name__ =="__main__":
#    testing()
