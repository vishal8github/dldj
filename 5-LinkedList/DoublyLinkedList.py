class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    #--------------------------------------------------------------------------------------
    #To INSERT node at the Start of the D-linked list
    def push(self, data):
        newNode = Node(data)

        if self.head.next == None:
            self.head.next = newNode
            return

        temp1 = self.head.next
        temp2 = self.head.next.prev

        self.head.next = newNode
        newNode.next = temp1
        temp2 = newNode

    #to INSERT node at end of the D-linked list
    def append(self, data):
        newNode = Node(data)

        if self.head.next == None:
            self.head.next = newNode
            return
        
        curnt_node = self.head

        while curnt_node.next != None:
            curnt_node = curnt_node.next
        curnt_node.next = newNode
        newNode.prev = curnt_node

    #to INSERT node at specific INDEX of the D-linked list
    def insertDataAtIndex(self, index, data):
        if index >= self.length() or index <= -1:
            print("\n<ERROR: 'Insert': Index out of range !!! >")
            return
        
        newNode = Node(data)
        curnt_index = 0
        curnt_node = self.head
        while True:
            temp = curnt_node
            curnt_node = curnt_node.next
            if curnt_index == index:
                temp.next = newNode
                newNode.next = curnt_node
                newNode.prev = temp
                break
            curnt_index += 1



    #--------------------------------------------------------------------------------------
    #TRAVERSE and GET the data from SPECIFIC INDEX
    def getDataFromIndex(self, index):
        if index >= self.length() or index <= -1:
            return "<ERROR: 'Get': Index out of range !!! >"

        curnt_index = 0
        curnt_node = self.head
        while True:
            curnt_node = curnt_node.next
            if curnt_index == index:
                return curnt_node.data
            curnt_index += 1        

    #TRAVERSE and SET the data to SPECIFIC INDEX
    def setDataToIndex(self, index, data):
        if index >= self.length() or index <= -1:
            return "<ERROR: 'Get': Index out of range !!! >"

        curnt_index = 0
        curnt_node = self.head
        while True:
            curnt_node = curnt_node.next
            if curnt_index == index:
                curnt_node.data = data
                break
            curnt_index += 1
    
    
    
    #------------------------------------------------------------
    #TRAVERSE and DELETE the data from perticular INDEX of the D-linked list
    def delDataFromIndex(self, index):
        if index >= self.length() or index <= -1:
            print("\n<ERROR: 'Delete': Index out of range !!! >")
            return
        
        curnt_index = 0
        curnt_node = self.head
        while True:
            last_node = curnt_node
            curnt_node = curnt_node.next
            if curnt_index == index:
                if index == self.length()-1:
                    last_node.next = None
                    break
                last_node.next = curnt_node.next
                curnt_node.next.prev = last_node
                break
            curnt_index += 1
    
    #TRAVERSE and DELETE the data from the FIRST of the D-linked list
    def delDataFromFirst(self):
        if self.head == None:
            print("Already Empty Linked-list !!!")
        else:
            self.head = self.head.next
            self.head.next.prev = self.head

    #TRAVERSE and DELETE the data from the END of the D-linked list
    def delDataFromEnd(self):
        if self.head == None:
            print("Already Empty Linked-list !!!")
            return
        last_node = self.head
        curnt_node = self.head.next
        while curnt_node.next != None:
            last_node = curnt_node
            curnt_node = curnt_node.next
        last_node.next = None
        curnt_node.prev = None



    #--------------------------------------------------------------------------------------
    #To print the list of the D-linked list   
    def display(self):
        elems = []

        curnt_node = self.head
        
        while curnt_node.next != None:
            curnt_node = curnt_node.next
            elems.append(curnt_node.data)
        print(f"Linked list: {elems}")


    #--------------------------------------------------------------------------------------
    #To print the list of the D-linked list   
    def length(self):
        curnt_node = self.head.next
        count = 0
        while curnt_node != None:
            count += 1
            curnt_node = curnt_node.next
        return count




#Execution starts from here
mylist = DoublyLinkedList() 
mylist.display()
print(f"Length of list: {mylist.length()}")

print("\nINSERTING nodes at the START of the D-linked list")
mylist.push(10)
mylist.push(20)
mylist.push(30)
mylist.display()
print(f"Length of list: {mylist.length()}")

print("\nINSERTING nodes at the END of the D-linked list")
mylist.append(99)
mylist.append(87)
mylist.display()
print(f"Length of list: {mylist.length()}")

print("\nINSERTING nodes at the SPECIFIC INDEX of the D-linked list")
print("Inserting data at index 2: 55")
mylist.insertDataAtIndex(2, 55)
mylist.display()
print(f"Length of list: {mylist.length()}")

print("\nSETTING nodes to the SPECIFIC INDEX of the D-linked list")
print("Setting data to index 3: 67")
mylist.setDataToIndex(3, 67)
mylist.display()
print(f"Length of list: {mylist.length()}")

print(f"\nGetting data from index 2: {mylist.getDataFromIndex(2)}")

print("\nDELETING node from the SPECIFIC INDEX of the D-linked list")
print("Deleting data from index: 2")
mylist.delDataFromIndex(2)
mylist.display()
print(f"Length of list: {mylist.length()}")

print("\nDELETING node from FIRST INDEX of the D-linked list")
mylist.delDataFromFirst()
mylist.display()
print(f"Length of list: {mylist.length()}")

print("\nDELETING node from END INDEX of the D-linked list")
mylist.delDataFromEnd()
mylist.display()
print(f"Length of list: {mylist.length()}")