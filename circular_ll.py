class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Cllist:
    def __init__(self):
        self.head = None
        self.ctr = 0

    def insertbeg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            self.head = node
        self.ctr += 1
        return

    def insertend(self, data):
        node = Node(data)
        if self.head == Node:
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
        self.ctr += 1
        return

    def insertinter(self, pos, data):
        node = Node(data)
        if pos < 1 or pos > self.ctr:
            print("Invalid")
        else:
            temp = self.head
            i = 1
            while i < pos:
                temp = temp.next
                i += 1
            node.next = temp.next
            temp.next = node
            self.ctr += 1
        return

    def deletebeg(self):
        if self.head is None:
            print("No Nodes Exists")
        elif self.ctr == 1:
            print("Nodes Deleted")
            self.head = None
            self.ctr -= 1
        else:
            print("Node Deleted")
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
            self.ctr -= 1
        return

    def deleteend(self):
        if self.head is None:
            print("No Nodes Exist")
        elif self.ctr == 1:
            print("Node deleted")
            self.head = None
            self.ctr -= 1
        else:
            temp = self.head
            prev = temp
            while temp.next is not self.head:
                prev = temp
                temp = temp.next
            print("node deleted")
            prev.next = temp.next
            self.ctr -= 1
        return

    def deleteinter(self, pos):
        if self.head is None:
            print("No Nodes Exist")
        elif pos > 1 or pos > self.ctr:
            print("Invalid")
        elif self.ctr == 1:
            print("node deleteD")
            self.head = None
            self.ctr -= 1
        else:
            temp = self.head
            prev = temp
            i = 0
            while i < pos:
                prev = temp
                temp = temp.next
                i += 1
            prev.next = temp.next
            print("Node DeLeted")
            self.ctr -= 1
        return

    def traverse(self):
        temp = self.head
        i = 0
        while i < self.ctr:
            print(temp.data)
            temp = temp.next
            i += 1
        return


def menu():
    print("Insert at Begin = 1")
    print("Insert at middle = 2")
    print("Insert at end = 3")
    print("Delete begin = 4")
    print("Delete middle = 5")
    print("Delete end = 6")
    print("Traverse = 7")
    print("No Nodes = 8")
    print("quit = 9")
    return


c = Cllist()
menu()
while True:
    ch = int(input("Enter Choice"))
    if ch == 1:
        data = input("Enter Data:")
        c.insertbeg(data)
    elif ch == 2:
        data = input("Enter Data:")
        pos = input("Enter Position:")
        c.insertinter(pos,data)
    elif ch ==3:
        data = input("Enter Data:")
        c.insertend(data)
    elif ch == 4:
        c.deletebeg()
    elif ch == 5:
        pos = input("Enter Position:")
        c.deleteinter(pos)
    elif ch == 6:
        c.deleteend()
    elif ch == 7:
        c.traverse()
    elif ch == 8:
        print("No Of Nodes:",c.ctr)
    else:
        print("Exitted")
        break
