#-------------->DSA(Data Structure)----------------->
#------------->Linked List------------------------->
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

#insertion of the linkd List
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

#Display the Linked List
def displayList(head):
	temp=head
	if temp==None:
		print("Linked list Underflow")
		return
	while temp!=None:
		print(temp.data,end="==>")
		temp=temp.next
	print("None")
displayList(head)



