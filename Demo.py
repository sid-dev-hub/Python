def decorate(function):
    
        function()
        print("Inside wrapper")
    
def funct():
    print("Inside A fucntion")

decorate(funct)