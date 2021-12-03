x = "global"
def fun1():
  x = "local" # initialised local variable 
  print(x,"variable is x")
fun1()
def fun2():
    print(x,"variable is x") # calling global variable
fun2()
  