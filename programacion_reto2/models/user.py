"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
#User register
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
        if found_user==True:
            return False
    #Validate user and password
    def validate_user(self,user, password):
        credential_validates=False
        for i in USERS:
            if i["user"]== user and i["password"]== password:
                print("User validation was done successful")
                credential_validates=True
                return credential_validates
            else:
                print("Check your user and password data")
                return credential_validates
                        
"""
user1=User.create_user("user1",123456)
user2=User.create_user("user1",123)
print(f"{USERS}")
User.validate_user("user1",123456)
User.validate_user("user1",123)
"""