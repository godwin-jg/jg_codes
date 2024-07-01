class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Policy(User):
    def __init__(self, id, name, policyId, policyName):
        super().__init__(id, name)
        self.customerId = id
        self.customerName = name
        self.policyId = policyId
        self.policyName = policyName # type, duration,benefits,amount
    def display(self):
        print(f'User ID: {self.id}')
        print(f'User Name: {self.name}')
        print(f'Policy ID: {self.policyId}')
        print(f'Policy Name: {self.policyName}')
class Users:
    def __init__(self):
        self.users = []
    def addUser(self, user):
        self.users.append(user)
    def displayUsers(self):
        for user in self.users:
            print(user.name)
            # user.display()
class Policies:
    def __init__(self):
        self.policies = []
    def addPolicy(self, policy):
        self.policies.append(policy)
    def displayPolicies(self):
        for policy in self.policies:
            print(policy.policyName)
    def policyDetails(self):
        print("Customer and Policy Details: ")
        for policy in self.policies:
            print("Customer: ",policy.customerId,policy.customerName)
            print("Policy: ",policy.policyId,policy.policyName)
            print()
        
def displayPolicies():
    policies = {1:'Health', 2:'Life', 3:'Motor', 4:'Travel'}
    for k,v in policies.items():
        print(f'{k}. {v}')
    choice = int(input('Enter your choice: '))
    if choice == 1: return (1,'Health')
    elif choice == 2: return (2,'Life')
    elif choice == 3: return (3,'Motor')
    elif choice == 4: return (4,'Travel')
    
def ViewpolicyDetails():
    policies = {1:'Health', 2:'Life', 3:'Motor', 4:'Travel'}
    policyDetails = {1:'Name: Health, type: Monthly, duration: 5-10 years, benefits:Covers everything from head to toe,amount:Rs.10000',
                     2:'Name: Life, type: Yearly, duration: 1-60 years, benefits: Covers your life and your loved ones,amount:Rs.50000',
                     3:'Name: Motor, type: quarterly, duration: 5-15 years,benefits: Cover fourwheelers and twowheelers,amount:Rs.15000',
                     4:'Name: Travel, type: Monthly, duration: 6 months ,benefits: all places,amount:Rs.20000'}
    for k,v in policies.items():
        print(f'{k}. {v}')
    choice = int(input('Enter your choice: '))
    print(policyDetails[choice])
    
def showPolicies():
    policies = {1:'Health', 2:'Life', 3:'Motor', 4:'Travel'}
    for k,v in policies.items():
        print(f'{k}. {v}')
    print()
    
def chooseUser():
    users = {1:'John', 2:'Alice'}
    for k,v in users.items():
        print(f'{k}. {v}')
    choice = int(input('Enter your choice: '))
    if choice == 1: return (1,'John')
    elif choice == 2: return (2,"Alice")

        
# user1 = User(1,'John')
# user2 = User(2,'Alice')
# user1Policy = Policy(user1.id, user1.name, 101, 'Health')
allUsers = Users() 
allPolicies = Policies()   
while True:
    # print("press any other key to continue")
    print("press 0 to exit")
    print("press 1 to display users and their policies")
    print("press 2 to display all available policies")
    print("press 3 to purchase a policy")
    print("press 4 to view policy details")
    choice = input()
    if choice == '0':
        break
    elif choice == "1":
        allPolicies.policyDetails()
    elif choice == '2':
        showPolicies()
    elif choice == '3':
        print('Choose User')
        id,name = chooseUser()
        user  = User(id,name)
        # print(user.name)
        allUsers.addUser(user)
        # print(allUsers.displayUsers())
        print('Choose Policy to Purchase')
        policyId,policyName = displayPolicies()
        Policy1 = Policy(user.id, user.name, policyId, policyName)
        allPolicies.addPolicy(Policy1)
        # print("All Policies")
    elif choice == "4":
        print("View Policy Details")
        ViewpolicyDetails()
    print()
    # Policy()
    # print('2. Choose Policy')
    # displaypolicies()
    # intChoice = int(input('Enter your choice: '))