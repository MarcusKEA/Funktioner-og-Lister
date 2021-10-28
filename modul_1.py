def add_together(*args):
    result = 0
    for i in args:
        result += i
    return result

def say_str(a: str):
    print(a)

def say_int(a):
    print(a)

def say_float(a:float):
    print(a)

def reverse_message():
    message = input("Write message:\n")
    translated = ""

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i -= 1

    print (translated)
