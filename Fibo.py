

def fibo(n):
        print("Inside Fibo", __name__)
        p1 = 0
        p2 = 1
        sum = 0
        rs = [0,1]
        while sum < n:
                   
            sum = p1 + p2
            if sum > n:
                break
            rs.append(sum)
            
            p1 = p2
            p2 = sum
        return rs 
            


