# polyporism ka mean ha ke same funtion ho per working different ho
# aik kam ke many forms ho sekta ha like

class TV:
    def power(self):
        print("TV is turned ON")

class AC:
    def power(self):
        print("AC is turned ON")

class Fan:
    def power(self):
        print("Fan is turned ON")

# same function works for different objects
def press_power(device):
    device.power()

press_power(TV())
press_power(AC())
press_power(Fan())

'''Same method name, different behavior → Polymorphism'''


# example 2
class Cash:
    def pay(self):
        print("this method pay the cash money")

class Creditcard():
     def pay(self):
        print("this method pay the creditcard money")

class Online():
     def pay(self):
        print("this method pay the online money")

def make_money(wow):
    wow.pay()

make_money(Cash())
make_money(Creditcard())
make_money(Online())

# wow is a argument ha hum jo bhi de sekta ha 