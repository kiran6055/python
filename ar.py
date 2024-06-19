x=input("enter x value: ")
y=input("enter y value: ")

result=x + y
print(f"the addition of {x} and {y} is: {result}")
print(type(result))
# we have to give data types to perform the function if not it will take numbers as string and append it

a=int(input("enter a value: "))
b=int(input("enter b value: "))

results=a-b
print(f"the result of {a} minus {b} is : {results}")
print(type(results))

# we have eval function it will automatically deciade ifit is int or float or string if we are giving string we need to give inside quotes "" then only it will take or it will throw syntax error

k=eval(input("enter a value: "))
p=eval(input("enter a value: "))

result= k+p

print(f"the result of {k} and {p} is : {result}")
print(type(result))
