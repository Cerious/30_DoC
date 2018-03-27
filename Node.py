class Node(object):
    def __init__(self, data=None, up_next=None):
        self.data = data
        self.up_next = up_next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.up_next

    def set_next(self, new_value):
        self.up_next = new_value


class LinkedList(object):

    #def __init__(self, head=None):
    #    self.head = None

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    #def get_head(self):
    #    return self.head

    def insert(self,head,data):
            new_node = Node(data)
            head = Node(head)
            if head == None:
                head = new_node
            else:
                current = head
                while current.get_next() != None:
                    current = current.get_next()

                current.set_next(new_node)

lyst = [5,2,7,9]
lync = LinkedList()

for item in lyst:
    head =  lyst[0]
    lync.insert(head,item)

current = lync.get_head()
while current:
    print(current.get_data())
    current = current.get_next()

#print('Current: ' + str(current))
nex = lync.head.get_next()
print("Head: " + str(lync.head.data))
print('Head Next: ' + str(nex.get_data()))
#mylist= Solution()
#T=int(input())
#head=None
#for i in range(T):
#    data=int(input())
#    head=mylist.insert(head,data)
#mylist.display(head);
