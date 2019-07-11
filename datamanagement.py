import random

class MenuItem:
    def road(self):
        print("Rolling the dice...")
    def dais(self,daisA,daisB):
        print("Die:"+str(daisA))
        print("Die:"+str(daisB))



menu_item1 = MenuItem()
menu_item1.road()
daisA = random.randint(1,6)
daisB = random.randint(1,6)

result = daisA + daisB
menu_item1.dais(daisA,daisB)
print("Total value:"+str(result))
