USERS=[]
class User:
    #Constructor
    def __init__(self, user, password):
        self.user=user
        self.password=password
    #Create an new user checking if there isn't one equal 
    def create_user(user, password):
        found_user=False
        for i in USERS:
            if i["user"] == user:
                found_user=True 
        if found_user ==False:    
            new_user=User(user,password)
            USERS.append({"user":user,"password":password})
            print(f"User {new_user.user} created successful ")
        else:
            print("This user is registered")
    #Validate user and password
    def validate_user(user, password):
        for i in USERS:
            if i["user"]== user and i["password"]== password:
                print("User validation done successful")
                return True
            else:
                print("Check your user and password data")
                return False
                
        

user1=User.create_user("user1",123456)
user2=User.create_user("user1",123)
print(f"{USERS}")
User.validate_user("user1",123456)
User.validate_user("user1",123)
