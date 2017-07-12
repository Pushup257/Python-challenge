class Taco:
   def __init__(self, meat, topping):
       self.meat = meat
       self.topping = topping

   def toString(self):
       tacoString = "Taco with "

       if(self.meat != None):
           tacoString += self.meat + ", "

       if (self.topping != None):
           tacoString += self.topping

       return tacoString

print("Welcome to the Taco Shop!\n")

meatIn = input("What kind of meat would you like?: ")
topIn = input("What kind of topping  would you like?: ")

user_taco = Taco(meatIn, topIn)

print("\n" + user_taco.toString())



