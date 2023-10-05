from re import X


def suma (a,b):
  x = a + b
 return x

def resta(a,b):
  x = a- b 
return x

print("dame el primer numero")
a =int(imput())

print ("dame el sugundo numero:")
b = int(input())
print("la suma da",suma(a,b),"y la resta da ",resta(a,b))


def multiplication(a,b):
  x = a*b
  return X

def division(a,b)
x = a/b
  return x

print("give me the first number:")
a = int(input())
print("give me the second number:")
b = int(input())
print("the multiplication is", multiplication(a,b), "and the division is", division(a,b))


def conversion(kilometers):
  kilometers = int(input("give me the amount kilometers"))
  return kilometers/1000
  print("you will have driven", conversion(kilometers), "in meters")


def triangle_area(): 
  height = int(input("give me the height of the triangle"))
  base = int(input("give me the base of the triangle"))
  return (base*height)/2
print("the area of your triangle will be", triangle_area())
