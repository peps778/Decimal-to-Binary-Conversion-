# Binary to decimal converter 
# Paul Jhon Magbanua™
print("Enter Decimal Number:")
try:
  num=float(input())
  print('Your Decimal number is:'+str(num))
  def dec_binary(z):
     x,y=int(z),z-int(z)
     c=y
     a,b=[],[]
     while y!=0:
       if y*2>=1: b.append(1)
       else:b.append(0)
       y=(y*2)-int(y*2)
     while x>0:
       if x%2==0:
          a.append(0)
       else:
          a.append(1)
       x=x//2
     a=a[::-1]
     for i in a:
       print(i,end ='') 
     print('.',end='')
     if c==0:
        print('0',end='')
     for i in b:
        print(i,end='')
  print('Your Binary number is:',end='')  
  dec_binary(num)
except:
  print ('Sorry you did not enter Decimal number')
  print(' OR ' + 'Unexpected error Occured')

#convertion made easy HAHA linte