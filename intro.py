from curses import def_prog_mode
from dataclasses import asdict
from email.errors import FirstHeaderLineIsContinuationDefect
from sre_constants import SRE_FLAG_DEBUG


print("Hello World from Python!")

#variablee declarations
name="Victoria"
last_name = "Warren"
age = 99
total = 23.784
found = False

print(name)
print(last_name)
print(age)
print(total)
print(found)

if (age < 100):
    print("Don't worry you are still young!!")
    print("inside the if")
    print("inside the if")
    print("inside the if")
elif (age ==100):
    print("Congrats on the centruy!!!")
else:
    print("Sorry, but you are getting old")
    print("Inside the if")

 # functions

def say_hello():
    print("Hello there!!")
    print("I'm inside the fn")

say_hello()
say_hello()