class Brands:               #parent_class
    brand_name_1 = "mobile"
    brand_name_2 = "bike"
    brand_name_3 = "car"
    
class Products(Brands):       #child_class
    prod_1 = "highly used in peoples"
    prod_2 = "it increasing ur time faster"
    prod_3 = "safty drive and peaceful admosphere"
    
obj_1 = Products()          #Object_creation
print(obj_1.brand_name_1 + obj_1.prod_1)
print(obj_1.brand_name_2 + obj_1.prod_2)
print(obj_1.brand_name_3 + obj_1.prod_3)
