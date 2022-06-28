##
##class Brands:               #parent_class
##    brand_name_1 = "Amazon"
##    brand_name_2 = "Ebay"
##    brand_name_3 = "OLX"
##    
##class Products:            #child_class
##    prod_1 = "Online Ecommerce Store"
##    prod_2 = "Online Store"
##    prod_3 = "Online Buy Sell Store"
##
##class Popularity(Brands,Products):
##    prod_1_popularity = 100
##    prod_2_popularity = 70
##    prod_3_popularity = 60
##    
##obj_1 = Popularity()          #Object_creation
##print(obj_1.brand_name_1+" is an "+obj_1.prod_1+" price is "+str(obj_1.prod_1_popularity))
##print(obj_1.brand_name_2+" is an "+obj_1.prod_2+" price is "+str(obj_1.prod_2_popularity))
##print(obj_1.brand_name_3+"is  an "+obj_1.prod_3+" price is "+str(obj_1.prod_3_popularity))
##

class car:
    def __init__(self,colour,model):
        self.colour=colour
        self.model=model
        c=car("blue","honda city")
    def car(self):
        print(self.model)
class bike:
    def __init__(self,colour,model):
        self.colour=colour
        self.model=model
        c=car("black","ford")
    def bike(self):
        print(self.model)
class vehicles(car,bike):
    def vehicles(self):
        print("vehjicle")
a=vehicles()
a.car()
    
        




























    
