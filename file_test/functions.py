# def my_funct(file, dir, user='root'):
#     print(f"file: {file}, dir: {dir}, to:{user}")
#
# my_funct(file='one', dir='two')
#
# def myFunct(a,b,c):
#     print(a,b,c)
#
# mytup = 23,45,88
#
# myFunct(*mytup)
# # wildcard *
# def myfun(dir, *files):  # *args  arguments
#     print('Dir', dir, 'Files', files)
#
# myfun('C:/myFiles','f1.txt','f2.txt','f3.pdf')

  # • has made the group of files into a tuple. returns a tuple

#   **kwargs keyword arguments

# def print_vat(**kwargs): # give me as many arguments as you want
#     print(kwargs)
#
# # print_vat(vatpc=17.5, gross=9.54, message='sum:')
# # returns a dictionary
# argsdict = dict(vatpc=17.5, gross=9.54, message='sum:')
# print_vat(**argsdict)

# we are passing a tuple and changing it to a dictionary

# variables and scope

# myvar = 7  # because its made at root of code, Global Variable
#
# def scope_test():
#     global myvar  # when you call a global variable into subroutine, you change the variable itself
#     myvar = 42  #variable in subs, stay in subroutine, local variable, doesnt exist outside
#
# print(myvar)
# scope_test()
# print(myvar)  # after subroutine


# score = 46

# def score_change(points):
#     global score
#     score += points
#     return f"Your new Credit Score is {score}"
#
# print(score_change(8))
# print(score)

