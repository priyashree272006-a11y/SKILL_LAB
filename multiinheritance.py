def decorator(func):
    def wrapper():
        func()
        print("the function has ended")
    return wrapper
def hello():
    print("this are the line being executed")

hello_var=decorator(hello)
hello_var()