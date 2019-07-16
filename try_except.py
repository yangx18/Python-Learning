## use the try/except 
## 02/06/2019

a = input('Enter a number')
try:
    print('the number is')
    b = int(a)
    print(a)
except:
    b = -1
if b == -1 :
    print('bad')