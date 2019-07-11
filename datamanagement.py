import random

class MenuItem:
    def road(self):
        print("Rolling the dice...")
    def dais(self,daisA,daisB):
        print("Die:"+str(daisA))
        print("Die:"+str(daisB))
    def hello(self):
        print("Hello,"+self.name+"!")
    def win(self,times,resu,win,lost):
        print("After "+str(times)+" experiments, "+self.name+" won "+str(win)+" times, lost "+str(lost)+" times. And the probability of winning was "+str(resu)+"%.")


win=0
lost=0
i=0

menu_item1 = MenuItem()
print("What is your name?")
menu_item1.name = input(">")
menu_item1.hello()
times = int(input("How many times do you experiment? "))
menu_item1.road()

while i < times :
    daisA = random.randint(1,6)
    daisB = random.randint(1,6)
    result = daisA + daisB
    if result > 7:
        win+=1
    else:
        lost+=1
    i+=1

resu = win + lost
resu = float(win / resu)
menu_item1.win(times,resu*100,win,lost)
