import random
n=int(random.random()*1000000000%100+1)
a=int(input("Guess a number"))
while a!=n:
      if a>n:
          print("Too big")
      else:
        print("Too small")
      a=int(input("Guess a number"))
print("You Won!")
    
      
