
# importing abstractmethod
from abc import ABC, abstractmethod
# parent class
class creditCard(ABC):
    # creating a method
    def monthlyPayment(self, amount):
        print("Your monthly payment: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass

class creditBalance(creditCard):
    def payment(self, amount):
        print("Your new credit card balance is {}".format(amount))

obj = creditBalance()
obj.monthlyPayment("$200")
obj.payment("$1,200")
