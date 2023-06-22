
def search(list,n):
    k=0
    for i in list:
        k+=1    
        if i == n:
            return k
                    
list = [3,7,2,9,4,6,1,8]
print(list)
n = int(input("Enter the number to search"))
p = search(list,n)
if  p != 0:
    print("Number found at ",p)
else:
    print("Not found")
    