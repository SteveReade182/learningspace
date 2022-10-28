# mynum = [45, 55, 34, 56, 3, 14, 5, 7]
#
# print(mynum)

# print(f"min: {min(mynum)}"
#       f"max: {max(mynum)}"
#       f"sum: {sum(mynum)}"
#       f"ave: {sum(mynum/len(mynum))}")

# mydict = {
#     'fred' : 3,
#     'jim' : 8,
#     'dave' : 42
# }
# print(f"Min of myDict {min(mydict.keys())}")

# a = 4
# b = 6
# a, b = b, a
# print(a,b)

# one, two, three = range(3)
# print(one, two, three)


# greetings = 'hello',
# print(type(greetings))

# mytup = ('a', 'b', 'c')
# # mylist = list(mytup)
# # print(mylist)
# another = mytup * 4
# print(another)

# del mynum[2:5]

# t1 = ('cats', 'dogs', 'snakes', 'mice', 'camels')
# t2 = ('kelp', 'crab', 'lobster', 'fish')
#
# for a, *b, c in t1, t2: # wilcared middle one
#     print(a, b, c)

# myList = ["Liverpool", "Man City", "Arsenal", "Stevenage"]
# #
# # myList[:0] = ["Newcatle", "Palace"]  # adding list into list at a specific location
# # myList.append("Leeds")  # drops something on end of list
# # myList.extend(["Everton"])  # creates a list of Everton and adds to the end of list.
# # myList += ["Man U"]  # increment of a variable. adds to the end of list
# #
# # mystr = "Dave"
# # mystr += "Smith"  # mystr __add__ (" Smith")
#
# # myList.insert(2, "Tottenham") # goes into position 2 in the list
# # myList[2:2] = ["Burnley", "Leicester"]  # bumps the element accros to fit this into element 2
# # # myList[3] = "Aston Villa"  # would delete leicester and replace with villa
# # print(myList)
#
# # print(myList.pop(3)) # takes the value out from identifier 3
# # print(myList.pop())  # right most value removed
# # try:  # checks if it is in the list
# #     myList.remove("Man")
# # except ValueError:  # cant remove so prints below, exception handling, means system doesnt crash
# #     print("That was not in the list")
# #  error handling
# print(myList)

# mynum = [45, 55, 34, 56, 3, 14, 5, 55]
#
# print(mynum.count(55))  # checks how many of the same value
# print(mynum.index(34))  # finds index number of value
# print(mynum.index(55))  # doesn't matter there are 2 it will find the 1st
#

# -------------------------------------------------------------------------------

# sets
# represents an induvidual circle in a ven diagram, mutable so can be changed
# every item in a set are unique
# even when they are joined together
# sets are unequivically unordered

# mySet = {2,4,5,7,8,3,2}
# print(mySet) # doesnt matter how many 2's will only print 1
#
# mynewset = set([2,5,7,8,9])
# print(mynewset)
# we like to join blocks of data together and see how much data is the same
# s4 = {23, 42, 66, 123}
# s5 = {56, 27, 42}
# print(f"{s4}{s5}")
# s4.remove(123)
# s5.add(123)
# print(f"{s4}{s5}")
# # once a list is turned to a set, it removes duplicates, we can then make it a list again.
# print( s4 & s5)  # each item in both
# print(s4 | s5)  # all items in both
# print(s4 - s5)  #
# print(s4 ^ s5)  #
# dictionaries are sets but with key value pairs

# files

f = open("new.txt" "w")
print(f)
f.close()

