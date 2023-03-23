from _7_graphs import Graph
from _2_linked_list import LinkedList
from _5_hash_table import HashTable
from _3_disjoint_sets import DisjointSet_QU
from _3_disjoint_sets import DisjointSet_QF


def generalTesting():
    g = Graph()
    g.addUndirectedEdge(0, 1)
    g.addUndirectedEdge(0, 3)
    g.addUndirectedEdge(0, 2)
    g.addUndirectedEdge(1,3)
    g.addUndirectedEdge(2, 3)
    g.addUndirectedEdge(3, 4)
    g.addUndirectedEdge(2, 5)
    g.addUndirectedEdge(5, 6)
    #g.addUndirectedEdge(5, 6)
    #g.print()
    #print(g.isAdjacent(5 , 6))
    #print(g.neighbors(7))
    #print(g.inDegree(3))
    #print(g.allVertices())
    print(g.DFS_pre(0))
    print(g.DFS_pre_rec(0))
    print(g.DFS_post(0))
    print(g.topologicalSort(0))
    print(g.BFS(0))

    list1 = LinkedList()
    list1.addLast(11)
    list1.addLast(12)
    list1.addLast(13)

    list1.print_list()

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
    generalTesting()