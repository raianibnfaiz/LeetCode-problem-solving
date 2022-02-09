#https://leetcode.com/problems/reverse-linked-list-ii/
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def add(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    
        
    def reverse(self,left,right):
        if self.head is None or self.head.next is None:
            return self.head
        if left == right:
            return self.head
        node=self.head
        current_position = 1
        previous_node=None
        while current_position < left :
            previous_node=node
            node=node.next
            current_position+=1
        start=node
        node_before_start=previous_node
        current_position=1
        node=self.head
        while current_position < right :
            node=node.next
            current_position+=1
        end=node
        node_after_end=node.next
        node_stack=[]
        node=start
        while node != end:
            node_stack.append(node)
            node=node.next
        if node_before_start:
            node_before_start.next=node
        else:
            self.head=end
        while len(node_stack)>0:
            top=node_stack.pop()
            node.next=top
            node=top
        node.next=node_after_end
        return self.head       
    def printList(self):
        n=self.head
        while n is not None:
            print("",n.data,end="-->")
            n=n.next
            
a=LinkedList()
a.add(3)
a.add(5)


a.reverse(1,2)
a.printList()

            