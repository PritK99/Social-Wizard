class User:
    def __init__(self):
        self.username = None 
        self.user_id = None 
        self.description = ""
        self.location = None 
        self.expected_age = None 

    def set_location(self,location):
        self.location = location
    
    def set_name(self,name):
        self.username = name
    def set_description(self,description):
        self.description = description
    def print_user(self):
        print("-----------------------------")
        print("User ID: ",self.user_id)
        print("Username: ",self.username)
        print("Description: ",self.description)
        print("-----------------------------")
        print("\n")

    def set_id(self,id):
        self.user_id = id
    
    def set_age(self,age):
        self.expected_age = age
