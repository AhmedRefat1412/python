# print(2-7) 
# print(10-5)
# a =100+5j

# print("The type of variable having value", a, " is ", type(a))

# name='ahmed refat'
# print('n'in name)
# print(f'your name is :- {name}')




# if statment


""""
print ('plesse enter your name ')
name =input()

print ('plesse enter your passwod  ')
password =input()

password =123

if (name =='ahmed refat'and password==123) :
    print('welcome')
    print ('enter your age ')     
    age=input()
    

    if(age==20):
      print('you are accept')
    else :
     print ('you are not accept')

else:
  print( 'there is something not correct')
  """""

# while #

""""
repeat=0
while repeat<5 :
    print('repeat')
    repeat= repeat+1
  """""

 

 # for loop with range and dectionary 
""""
my_range =range(1,10,2)
for i in my_range:
    print(i)

degrees  ={
    " ahmed" : "10" ,
    "ali" :"11",
    "samy" :"12",
    "morad" :"13"
}
for degree in degrees:
    #print(degrees[degree])
    print(f"the student {degree}  has a degree = {degrees.get((degree))}")
"""""


 #function
"""""
def nm (name):
    return f"your name is {name}"


print(nm("ahmed"))

"""""


# a = [1, 2, 3]
# b = ['cat', 'dog', 'rat', 'snake']
# c = ['hello', 3.1415926, ['a','b','c'], None, 23]
# # print(a[0])
# # print(a[1:2])
# # print(b[3])
# # print(c[2])
# # print(c[2][2])

# print([1, 2, 3] + ['A', 'B', 'C'])
# print('zzzzzzzzzzzzzzzzzzzzzzzzzzz')

# c[0]='donkey'
# print(c)


# for loop inside dictionary 

"""""
meals = {'protein': 'egg', 'drink': 'milk', 'fruit': 'orange'}


for v in meals.items():
    print(v)
"""

# class 
"""""
class member :

    count=0

    # class method
    @classmethod
    def  class_method (cls):
        print("i am class method")


    # staticmetho
    @staticmethod
    def static_methos():
        print(" i am static method ")



    def __init__(self,fname,mname,lname,gender):
        self.f_name=fname
        self.m_name=mname
        self.l_name=lname
        self.Gender=gender
        

        #return print( f"your name is {self.f_name} {self.m_name} {self.l_name}")


    def  full_name_toGender (self):

        if( self.Gender=="male"):
           print(f"hello mr {self.f_name}")

        elif (self.Gender=="female"):
            print(f" hello miss {self.f_name}")

        else:
            print(f"hello {self.f_name}")
            

me1=member("ahmed","refat","abdelmoaty  " ,"male")

#me1.full_name_toGender()
me1.static_methos()
#me1.class_method ()
"""""

# inheritance

class car:
    def __init__(self,color,model,year):
       self. Color =color
       self. Model= model 
       self. Year=year

    def car_color (self):
        print(f"this color have a {self.Color} color ")

    def car_model (self):
        print(f"this color have a {self.Model} model ")
  
    def car_Year (self):
        print(f"this color have a {self.Year} year ")
  


class kia(car):
    def __init__(self, color, model, year,high):
        super().__init__(color, model, year)
        self.high=high

    def speed(self):
        print(f"this car has hig speed")

    def car_high (self):
        print(f"car high is {self.high}")


car1=kia("kia","sportage","2025",50)
car2=car("kia","sportage","2025")
# car1.car_color()
# print(car1.Model)
car1.car_high()

