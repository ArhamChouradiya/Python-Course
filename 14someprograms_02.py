"""
def display(name):
    def message():
        return "Hello"
    result=message()+" "+name
    return result

print(display("arham"))

#print(message) will show erroe because it is enclosed in display function
"""

def display():
    def message():
        return "HELLO"
    return message
    
fun=display()
print(fun())