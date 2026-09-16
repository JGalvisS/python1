"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
#User register
USERS=[{'user': 'programación', 'password': 'programación'}]
class User:
    #Constructor
    def __init__(self, user, password):
        self.user=user
        self.password=password
        
    #Create an new user checking if there isn't one equal 
    def create_user(self, user, password):
        found_user=False
        for i in USERS:
            if i["user"] == user:
                found_user=True
                print("This user is already registered")
                return False
        if found_user ==False: 
            USERS.append({"user":user,"password":password})
            print(f"The user {user} was created successful.")
            return True
    #Validate user and password
    def validate_user(self,user, password):
        for i in USERS:
            if i["user"]== user and i["password"]== password:
                print("User validation was done successful")
                return True
        return False


"""                       
user1=User("user1",123456)
user1.create_user(user1.user,user1.password)
#user2=User.create_user("user2",123)


#User.validate_user("user1",123456)
#User.validate_user("user1",123)
"""