"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    rate = 0
    def __init__(self, rate):
        self.rate = rate
    
    def get_rate(self):
        return self.rate

class Monthly_Contract(Contract):
    def __init__(self, rate):
        super().__init__(rate)
    
    def get_pay(self):
        return super().get_rate()
    
    def get_desc(self):
        return " works on a monthly salary of " + str(super().get_rate())

class Hourly_Contract(Contract):
    def __init__(self, rate, hours):
        self.hours = hours
        super().__init__(rate)

    def get_pay(self):
        return super().get_rate() * self.hours
    
    def get_desc(self):
        return " works on a contract of " + str(self.hours) + " hours at " + str(super().get_rate()) + "/hour"


class Commission:
    rate = 0
    def __init__(self, rate):
        self.rate = rate
    
    def get_rate(self):
        return self.rate
    
class Bonus_Commission(Commission):
    def __init__(self, rate):
        super().__init__(rate)
    
    def get_pay(self):
        return super().get_rate()
    
    def get_desc(self):
        return " and receives a bonus commission of " + str(super().get_rate())
    
class Contract_Commission(Commission):
    def __init__(self, rate, contracts):
        self.contracts = contracts
        super().__init__(rate)

    def get_pay(self):
        return super().get_rate() * self.contracts
    
    def get_desc(self):
        return " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(super().get_rate()) + "/contract"
    
class No_Commission(Commission):
    def __init__(self):
        pass
    
    def get_pay(self):
        return super().get_rate()
    
    def get_desc(self):
        return ""


class Employee:
    contract = None
    commission = None

    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_pay()

    def __str__(self):
        return self.name + self.contract.get_desc() + self.commission.get_desc() + ". Their total pay is " + str(self.get_pay()) + "."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
contract = Monthly_Contract(4000)
commission = No_Commission()
billie = Employee('Billie', contract, commission)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
contract = Hourly_Contract(25, 100)
commission = No_Commission()
charlie = Employee('Charlie', contract, commission)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
contract = Monthly_Contract(3000)
commission = Contract_Commission(200, 4)
renee = Employee('Renee', contract, commission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
contract = Hourly_Contract(25, 150)
commission = Contract_Commission(220, 3)
jan = Employee('Jan', contract, commission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
contract = Monthly_Contract(2000)
commission = Bonus_Commission(1500)
robbie = Employee('Robbie', contract, commission)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
contract = Hourly_Contract(30, 120)
commission = Bonus_Commission(600)
ariel = Employee('Ariel', contract, commission)
