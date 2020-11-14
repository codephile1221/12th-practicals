def filewrite(x):

      f1= open('class9.txt', 'w+' )

      for i in range (x):
            y=input('enter student name : ')
            z=float(input('enter student aggregate marks : '))
            f1.write(f"{y}:{z}")
            f1.write('\n')
            print(y + ' : ' + str(z))

      f1.close()

def write1():

      f1= open('class9.txt', 'r' )
      f2= open('class10A.txt', 'w' )
      f3= open('class10B.txt', 'w' )
      f4= open('class10C.txt', 'w' )

      global x
      s=f1.readlines()
      v=x%3
      
      for j in (f2,f3,f4):
            for k in range(3):
                  j.write(s[0])
                  x=s.pop(0)
      while v!=0:
            for i in (f2,f3):
                  i.write(s[0])
                  x=s.pop(0)
                  v-=1
                  if v == 0:
                        break
            break      

      
      f1.close()
      f2.close()
      f3.close()
      f4.close()

def fileread():

      f1= open('class9.txt', 'r' )
      f2= open('class10A.txt', 'r' )
      f3= open('class10B.txt', 'r' )
      f4= open('class10C.txt', 'r' )


      for f in (f1,f2,f3,f4):
            print(f.name)
            print('\n')
            n=f.readlines()
            print(n)
            print('\n')

      f1.close()
      f2.close()
      f3.close()
      f4.close()

x=int(input('Enter the number of students : '))

filewrite(x)
write1()
fileread()
