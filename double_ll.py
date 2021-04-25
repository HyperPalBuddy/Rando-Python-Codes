class Node:
    def __init__(self,data):
        self.data = data
        self.prev = self.next = None
class Dllist:
    def __init__(self):
        self.start = None
    def create(self):
        n = int(input("Enter Size:"))
        for i in range(n):
            data = input("Enter Data:")
            newnode = Node(data)
            if self.start == None:
                self.start = newnode
            else:
                temp = self.start
                while temp.next != None:
                    temp = temp.next
                temp.next = newnode
                newnode.prev = temp
    def insertbeg(self):
        data = input("Enter Data:")
        newnode = Node(data)
        if self.start == None:
            self.start = newnode
        else:
            newnode.next = self.start
            self.start.prev = newnode
            self.start = newnode
    def insertend(self):
        data = input("Enter Data:")
        newnode = Node(data)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
    def insertinter(self):
        data = input("Enter Data:")
        newnode = Node(data)
        pos = int(input("Enter Position:"))
        if self.start == None:
            self.start = newnode
        else:
            i = 1
            if pos>1:
                temp = self.start
                while i<pos-1 and temp.next!= None:
                    temp = temp.next
                    i+=1
                if i == [pos-1]:
                    newnode.next = temp.next
