import random

class MenuItem:
    def road(self):
        print("Rolling the dice...")
    def dais(self,daisA,daisB):
        print("Die: "+str(daisA))
        print("Die: "+str(daisB))
    def hello(self):
        print("Hello,"+self.name+"!")
    def win(self):
        print(self.name+" won!")
    def lost(self):
        print(self.name+" lost.")



menu_item1 = MenuItem()
daisA = random.randint(1,6)
daisB = random.randint(1,6)

result = daisA + daisB
print("What is your name?")
menu_item1.name = input("> ")
menu_item1.hello()
menu_item1.road()
menu_item1.dais(daisA,daisB)
print("Total value: "+str(result))

if result > 7:
    menu_item1.win()
else:
    menu_item1.lost()
