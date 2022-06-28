##class Polygon:
##    def __init__(self, no_of_sides):
##        self.n = no_of_sides
##        self.sides = [0 for i in range(no_of_sides)]
##
##    def inputSides(self):
##        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
##
##    def dispSides(self):
##        for i in range(self.n):
##            print("Side",i+1,"is",self.sides[i])
# Python program to demonstrate
# single inheritance

####SINGLE INHERITANCE
##class Parent:
##	def func1(name1):
##		print("wasim.")
##class Child(Parent):
##	def func2(name2):
##		print("aslam")
####class Child(Parent):
####        def func3(name3):
####                print("nagaraj")
##self= Child()
##self.func1()
##self.func2()
######MULTIPLE INHERITANCR
##class mother:
##    def mother(name1):
##        print(name1.mothername)
##        
##class father:
##    def father(name2):
##        print(name2.fathername)
####class son:
####    def son(name3):
####        print(name3.sonname)
##class family(mother,father):
##    def parents(name,):
##        print("motehr=>", name.mothername)
##        print("father=>", name.fathername)
####        print("son=>",    self.sonname)
##a=family()
##a.mothername="Jubaitha"
##a.fathername="Thameen"
##a.parents()
##a.sonname="wasim aslam"
##
##a.parents()
######MULTILEVEL INHERITANCE
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
        
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
        
class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
        
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
        
s1 = Son('Wasim Aslam', 'Thameen', 'Abdul Razak')
print(s1.sonname)
s1.print_name()

##             
##        
























