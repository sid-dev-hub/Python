
class Facto: 
           
    def fact(self,n):
        
        print("Inside Fact")
        sum = 1
        for i in range (1, n+1):
            sum = sum * i 
        print(sum) 

Facto.fact(self=None,n=4)
print()

