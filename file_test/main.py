# # # files
# #
# # f = open("new.txt","a")
# # name = input("Enter your name")
# # f.write(name)
# # f.write(",")
# # last = input("Enter your Last name")
# # f.write(last)
# # f.write(",")
# # age = int(input("Enter your age"))
# # agestr = str(age)
# # f.write(agestr + "\n")
# #
# # lines = ["This is one line,\n","This is another,\n"]
# # f.writelines(lines)
# # f.close() #explicit better than implicit
# # print(f)
#
# f = open("dvla.txt","r")
# lines = f.readlines() #builds list of data
# print(lines)
# target = input("Enter Reg: ").upper() #enter reg and convert to upper case
# for line in lines:
#     car = line.strip("\n") # takes format away
#     car = car.split(",") # makes it into data lists
#     reg = car[0]
#     name = car[1]
#     address = car[2:5]
#     # city = car[3]
#     # postcode = car[4]
#     if reg == target:
#         print("File Found")
#         print(f"The registered owner of: {reg} is "
#               f"{name}")
#         print(f"There address is: {address}")
#         # print(f"There address is: {address}, {city}, {postcode}")

with open("dvla.txt", "r") as f: # with closes the file automatically
    for line in f:  # f means file
        print(line)  # if you add print(type(line)) would write string
        pass
