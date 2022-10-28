class Person:  # class names have a capital leading letter
    # creating an object
    uniqueID = 0

    def __init__(self, name):  # self is what we choose to enter
        self._name = name  # _ means its a private variable. private attribute
        Person.uniqueID += 1

    def __str__(self):  # module within the object made
        return f"ID: {self.uniqueID}"

class Employee(Person):
    def __init__(self, name, dep):
        super().__init__(name)
        self._dep = dep

    def __str__(self):
        return f"{self._name} ID: {self.uniqueID} DEP: {self._dep}"

class InsufficientFundError(Exception):
    pass


class Cust(Person):

    def __init__(self, name,initial):
        super().__init__(name)
        self._balance = initial

    def getbalance(self):  #  getter
        return f" Your balance is: £{self._balance}"

    def deposit(self, amt):  # setters
        self._balance += amt
        return f"You added £{amt}. Your new Balance £{self._balance:5.2f}"
    def withdraw(self, amt):
        try:
            new = self._balance - amt < 0 # if this calculation puts balance below 0 TRUE
            if new: # same as if new == TRUE:
                raise InsufficientFundError("You Do Not Have Enough Money")
        except InsufficientFundError as err:
            print("ooops", err)
        else:
            self._balance -= amt
        return f"Balance: {self._balance}"

        # self._balance -= amt
        # return f"You Withdrew £{amt}. Your new Balance £{self._balance}"

jill = Cust('Jill', 6700)
print(jill.getbalance())
print(jill.withdraw(8000))
# emp1 = Employee("Bill", "IT")
#
# print(emp1)