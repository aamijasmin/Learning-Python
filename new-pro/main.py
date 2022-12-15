import math
a = 100
b = 1000
jasmin = {
        "phone": 8918310327,
        "address": 'cob',
        "married": False

        }
jasmin["phone"]=45663782267
jasmin["address"]= 'cob'
jasmin["married"]= True

mobiles = ['iphone',
           'vivo',
           'oppo',
           'realme',
           'sumsung',
           'tab'
           ]
for i in mobiles:
    print(i.upper())
name = input("Enter name please : ")
print("Hello " + name)
j = int(input("Enter length : "))
k = int (input("Enter breadth : "))
l = 2*(j+k)
area = j*k 
print("perimaster : ", l, "Area :", area )
n = int(input("Enter a number : "))
print(math.pow(n, 0.5))

