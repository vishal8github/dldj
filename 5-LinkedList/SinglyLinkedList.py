#create singly linked list node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        #initialize HEAD node
        self.head = Node()

    #------------------------------------------------------------
    #INSERT node AT the START of the linked list
    def push(self, data):
        newNode = Node(data)

        if self.head.next == None:
            self.head.next = newNode
            return
        temp = self.head.next
        self.head.next = newNode
        newNode.next = temp

    #INSERT node AT the END of the linked list
    def append(self, data):
        newNode = Node(data)
        curnt_node = self.head

        while curnt_node.next != None:
            curnt_node = curnt_node.next
        curnt_node.next = newNode

    #INSERT node AT perticular INDEX
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
                break
            curnt_index += 1
                

    #------------------------------------------------------------
    #TRAVERSE through the linked list and find the length
    def length(self):
        curnt_node = self.head.next
        count = 0
        while curnt_node != None:
            count += 1
            curnt_node = curnt_node.next
        return count

    #------------------------------------------------------------
    #TRAVERSE through the linked list and display the data of nodes
    def display(self):
        elems = []

        curnt_node = self.head
        
        while curnt_node.next != None:
            curnt_node = curnt_node.next
            elems.append(curnt_node.data)
        print(f"Linked list: {elems}")

    #------------------------------------------------------------
    #TRAVERSE and get the data from perticular INDEX
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
    
    #------------------------------------------------------------
    #TRAVERSE and set the data to perticular INDEX
    def setDataToIndex(self, index, data):
        if index >= self.length() or index <= -1:
            print("<ERROR: 'Set': Index out of range !!! >")
        
        curnt_index = 0
        curnt_node = self.head
        while True:
            curnt_node = curnt_node.next
            if curnt_index == index:
                curnt_node.data = data
                break
            curnt_index += 1

    #------------------------------------------------------------
    #TRAVERSE and DELETE the data from perticular INDEX
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
                return
            curnt_index += 1
    
    #TRAVERSE and DELETE the data from the FIRST index of the linked list
    def delDataFromFirst(self):
        if self.head == None:
            print("Already Empty Linked-list !!!")
        else:
            self.head = self.head.next

    #TRAVERSE and DELETE the data from the END index of the linked list
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
        



#Execution starts from here ***
my_list = SinglyLinkedList()

my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nINSERTING data...")
my_list.append(11)
my_list.append(22)
my_list.append(33)
my_list.append(44)
my_list.append(55)
my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nINSERTING data at the start of the list...")
my_list.push(99)
my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nGETTING data from the specified index of the list...")
my_list.display()
print(f"Get data from index 2: {my_list.getDataFromIndex(2)}")

print("\nSETTING data to the specified index of the list...")
my_list.setDataToIndex(2, 70)
print(f"Set data to index 2: {my_list.getDataFromIndex(2)}")
my_list.display()

print("\nDELETING data from the specified index of the list...")
print(f"DELETE data from index 2: {my_list.getDataFromIndex(2)}")
my_list.delDataFromIndex(2)
my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nINSERTING data at the specified index of the list...")
print("INSERT data at index 3: 888")
my_list.insertDataAtIndex(3, 888)
my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nDELETING data from the end of the list...")
my_list.delDataFromEnd()
my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nDELETING data from the first of the list...")
my_list.delDataFromFirst()
my_list.display()
print(f"Lenght of list: {my_list.length()}")

print("\nINSERTING data at the start of the list...")
my_list.push(120)
my_list.display()
print(f"Lenght of list: {my_list.length()}")