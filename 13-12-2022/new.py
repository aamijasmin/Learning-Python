# greet = "Welcome "
#
# n = "Ripon"
#
# # concanet
# print(greet + n)

# variable
# first_name = "steve"
# last_name = "jobs"
#
# f_name = first_name.upper()
# l_name = last_name.upper()

# f_name = first_name.title()
# l_name = last_name.title()
# methods
# .title()

# print(f_name + " " + l_name)
import time 

f_name = input("First Name : ")
l_name = input("Last Name : ")

f_name = f_name.strip()
l_name = l_name.strip()

message = "Welcome ! "
m_morning = "Good Morning "
m_noon = "Good afternoon "
m_eve = "Good Evening "

if (time.localtime().tm_hour<12):
    print(m_morning + f_name.title() + " " + l_name.title())
elif (time.localtime().tm_hour<18):
    print(m_noon + f_name.title() + " " + l_name.title())
else:
    print(m_eve + f_name.title() + " " + l_name.title())


# Python strip method
# strip() removes whitesapce
# from both end
#
# lstrip() removes whitespaces 
# from preceedings ( beginning)
#
# rstrip() removes space
# from succeding spce (end)
