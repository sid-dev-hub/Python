from datetime import datetime

def log_main(func):
    def wrapper():
        func()
        print(f'{"-"*30}')
        print(f"Function:{func.__name__}\nRun on: {datetime.today().strftime('%d-%m-%Y %H:%M:%S')}")
        print(f'{"-"*15}')
        
    return wrapper

@log_main
def Logs():
    print("Logs done")
    
Logs()