class Pod:
    # Class variable
    member = {}
    # Class Constructor method is called when an object is instantiated
    def __init__(self,leader,cell):
        Pod.member[leader] = cell
    # Method to add member and to member dictionary
    def add_member(self,member_to_add,cell_number):
        Pod.member[member_to_add] = cell_number
    # Class method to print the Pod_leader and cell numbers
    def display_members(self):
        print('\n')
        for Pod.member, number in Pod.member.items():
            print(Pod.member, number)

# Prompt for the Pod leader name and number
leader = input('Who is the leader? ')
cell = input('What is the leaders cell number? ')

# Initialize the Pod Dictionary with the leader's name and number
pod = Pod(leader,cell)
pod.add_member(leader,cell)
amount = input("How many members would you like to add")

for i in (0,amount):
    member = input('What is your name')
    cell = input('What is your phone number')
    pod.add_member(member,cell)

