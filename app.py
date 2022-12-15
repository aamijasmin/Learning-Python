import time
f_name = input("First name")
l_name = input("last name")
massege = "welcome !"
m_morning = "good morning"
m_noon = "good afternoon"
m_eve = "good evening"

# indent - verb
# indentation - nount

if (time.localtime().tm_hour<12):
    print (m_morning + f_name.title() + " " + l_name.title ())
elif (time.localtime().tm_hour<18):
    print(m_noon + f_name.title() + " " + l_name.title())
else : 
     print (m_eve + f_name.title() + " " + l_name.title())

a = 5
b = 3


if (a>b):
    print(a)
print(b)






















