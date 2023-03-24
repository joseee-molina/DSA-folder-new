from _2_linked_list import *
import hashlib

class Entry:
    def __init__(self, key,value):
        self.key = key
        self.value=value

class HashTable:


    def __init__(self, initialCapacity=10, OCCUPATION_RATIO = 0.75):
        self.size= 0
        self.initialCapacity = initialCapacity
        self.arr = []
        self.fillArr(self.initialCapacity)
        self.OCCUPATION_RATIO = OCCUPATION_RATIO

    def fillArr(self,initialCapacity):
        for i in range(initialCapacity):
            self.arr.append( LinkedList())

    def containsKey(self, key):
        position = hash(key)%self.initialCapacity
        ptr = self.arr[position].sentinel.next
        while ptr!=self.arr[position].sentinel:
            if ptr.item.key == key:
                return True
            ptr = ptr.next
        return False
        

    def put(self,key,value):
        
        position = hash(key) % self.initialCapacity
        self.arr[position].addLast(Entry(key,value))
        self.size+=1
        if(float(self.size)/float(self.initialCapacity)>self.OCCUPATION_RATIO):
            self.resize()

    def remove(self,key):
        position = hash(key) % self.initialCapacity
        ptr = self.arr[position].sentinel.next
        while ptr!=self.arr[position].sentinel:
            if ptr.item.key == key:
                ptr.prev.next=ptr.next
                ptr.next.prev=ptr.prev
                break
            ptr = ptr.next
        
    
    def resize(self):
        newArr = []
        newLength = self.initialCapacity*2
        for i in range(newLength):
            newArr.append(LinkedList())

        for i in range(self.initialCapacity):
            currPtr = self.arr[i].sentinel.next
            while currPtr != self.arr[i].sentinel:
                entry = currPtr.item
                position = hash(entry.key) % newLength
                newArr[position].addLast(Entry(entry.key,entry.value))
                currPtr = currPtr.next
        
        self.arr = newArr
        self.initialCapacity=newLength     

    def print(self):
        for i in range(len(self.arr)):
            printThis = "Bucket "+str(i)
            print(printThis)
            printThis = ""
            ptr = self.arr[i].sentinel.next
            while ptr!=self.arr[i].sentinel:
                printThis+= (str(ptr.item.key) + " -> "+str(ptr.item.value)+" , ")
                ptr = ptr.next
            print(printThis)

def testing():
    hashTable = HashTable(4)
    hashTable.put(2,3)
    hashTable.put(5,6)
    hashTable.put(10,11)
    hashTable.put(7,8)
    #hashTable.put("apple")
    #hashTable.put("banana")
    #hashTable.put("cherry")
    hashTable.print()
    hashTable.remove(10)
    hashTable.print()
    #print(hashTable.containsKey(17))


if __name__ == "__main__":
    testing()