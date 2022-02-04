#https://leetcode.com/problems/reverse-linked-list/
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"-->",end=" ")
            temp=temp.next
    def reverse_linked_list(self):
        if self.head is None:
                return None
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head= prev
    def reverse2(self):
        node_stack=[]
        node=self.head
        while node:
            node_stack.append(node)
            node=node.next
        self.head=node_stack.pop()
        node=self.head
        while len(node_stack)>0:
            next_node=node_stack.pop()
            node.next=next_node
            node=next_node
        node.next=None
list=LinkedList()
list.add(2)
list.add(3)
list.add(4)
list.add(5)
list.add(6)
list.printList()
list.reverse2()
print("\n")
list.printList()