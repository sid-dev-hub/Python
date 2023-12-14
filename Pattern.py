def Triangle(n):
    for i in range (n):    
        for j in range (i):
            print(end="* ")
        print()
    
def Square(n):
    
    for i in range (n):    
        for j in range (n):
            print(end="* ")
        print()

def RevTriangle(n):
    
    k=(2*n)-2
    for i in range (n):
        
        for j in range (k):
            print(end=" ")
        k-=2
        
        for j in range (i+1):
            print("* ", end="")
        print()

def Pyramid(n):
    
    k=(2*n)-2
    for i in range (n):
        
        for j in range (k):
            print(end=" ")
        k-=1
        
        for j in range (i+1):
            print("* ", end="")
        print()
        
def RevPyramid(n):
    
    k=(2*n)-2
    for i in range (n,0,-1):
            
        for j in range (k,0,-1):
            print(end=" ")
        k+=1
        
        for j in range (i,0,-1):
            print("* ", end="")        
        print()

#n = int(input("Enter a number "))
#print("What pattern do you wish to print")
#choice=int(input("1.Triangle 2.Opp.Traingle 3.Sqaure 4.Pyramid 5. Reverse "))
n = 7
#if choice ==1:
Triangle(n)
#elif choice==2:
RevTriangle(n)
#elif choice==3:
Square(n)
#elif choice ==4:
Pyramid(n)
#elif choice==5:
RevPyramid(n)
#else:
#print("Invalid choice")
