# class Person:  # class names have a capital leading letter
#     # creating an object
#     uniqueID = 0
#
#     def __init__(self, name, age):  # self is what we choose to enter
#         self._name = name  # _ means its a private variable. private attribute
#         self._age = age
#         Person.uniqueID += 1
#
#     def __str__(self):  # module within the object made
#         return f"{self._name} Age: {self._age} ID: {self.uniqueID}"
#
# # class Vehicle:
# #     def __init__(self, wheels, make):
# #         self._wheels = wheels
# #         self._make = make
#
# per1 = Person("Andy",41)
# print(per1)
# # person2 = Person("bob")
# # print(person2)
#
# # veh1 = Vehicle(4,"Ford")
# # print(veh1)
# # print(veh1._wheels)

class Account:

    accountID = 0
    def __init__(self, initial):
        self._balance = initial
        Account.accountID += 1

    def getbalance(self):  #  getter
        return f" Your balance is: £{self._balance}"

    def deposit(self, amt):  # setters
        self._balance += amt
        return f"You added £{amt}. Your new Balance £{self._balance}"
    def withdraw(self, amt):
        self._balance -= amt
        return f"You Withdrew £{amt}. Your new Balance £{self._balance}"

jill = Account(4690)
print(jill.deposit(6534))
print(jill.withdraw(560))

dave = Account(100)
print(dave.accountID)



