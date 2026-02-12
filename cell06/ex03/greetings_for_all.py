#!/usr/bin/env python3

def greetings(greetings=None):
    if isinstance(greetings, str):
        return print("Hello, " + greetings + ".")
    elif greetings == None:
        return print("Hello, noble stranger.")
    else:
        return print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
