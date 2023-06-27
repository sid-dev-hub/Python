

class A:
    @staticmethod
    def init():
        print("in init")
    def display(self):
        print("Inside A")
class B:
    def display():
        print("Inside B")
        
    def met():
           A.display() 
        

class mod(A):
    
    def chek(alpa):
        if alpa == "A":
            return A()
        elif alpa=="B":
            return B()
      
#ch = input("Enter A or B: ")
#a = mod.chek(ch)

a = A()
B.met()




    