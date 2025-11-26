x=input("Enter the number 1:")
y=input(" Enter the number 2: ")

d=0

try:
    d=int(x)/int(y)
    a='baby yoda'+56
except  ZeroDivisionError as ze:
    print("Exception occured:", ze)
    d=-1
print("Division is :",d)
