#1 area and circumfrance of circle
class Circle :
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
         print(3.14*self.radius*self.radius)

    def getCircumference(self):

         print(2*3.14*self.radius)

radius = int(input("Enter the radius: "))
c = Circle(radius)
c.getArea()
c.getCircumference()

#Q.2 display all information of student
class student :
  def __init__(self,roll,name):
     self.name=name
     self.roll=roll
  def show(self) :
     print(self.name,self.roll)
roll=int(input("ener roll no"))
name=input("enter name")

s1=student(roll,name)
s1.show()

#Q.3 temprature conversion celcius to farenhit and farenhit to celcius
class temp :
    def __init__(self,celcius,farenheit):
       self.farenheit=farenheit
       self.celcius=celcius
    def getfarenheit(self):
       print("farenheit=",(1.8*self.celcius)+32)
    def getcelcius(self):
       print("celcius=",(self.farenheit-32)*0.55)
farenheit=int(input("enter farenheit"))
celcius=int(input("enter celcius"))
t=temp(celcius,farenheit)
t.getfarenheit()
t.getcelcius()

#Q.4 print movie name and updation
class movie :
 def __init__(self,moviename,artistname,year,rating):
    self.moviename=moviename
    self.artistname=artistname
    self.year=year
    self.rating=rating
 def getdisplay(self) :
    print(self.moviename,self.artistname,self.year,self.rating)
	
 def update(self,moviename,artistname,year,rating):
    self.moviename=moviename
    self.artistname=artistname
    self.year=year
    self.rating=rating
	
	
m=movie("marry kom","priyanka chopra",2016,5)
m.getdisplay()
m.update("superstar","aamir",2017,4)
m.getdisplay()

#Q.5 print expendetiure ,saving and total salary
class Expenditure :
    def __init__(self,expenditure,saving) :
        self.expenditure=expenditure
        self.saving=saving
    def getdisplay(self):
        print("expend is",self.expenditure,"saving is",self.saving)
    def getcalculatio(self) :
        print("total salary=",self.expenditure+self.saving)
s=Expenditure(40000,50000)
s.getdisplay()
s.getcalculatio()



