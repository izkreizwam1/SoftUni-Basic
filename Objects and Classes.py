# class Movie:
#     __watched_movies = 0
#
#     def __init__(self,name,director):
#         self.name=name
#         self.director=director
#         self.watched=False
#
#
#     def change_name(self,new_name):
#         self.name=new_name
#     def change_director(self,new_diector):
#         self.director=new_diector
#     def watch(self):
#         if not self.watched:
#             self.watched=True
#             Movie.__watched_movies+=1
#     def __repr__(self):
#         return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"
#
# first_movie = Movie("Inception", "Christopher Nolan")
# second_movie = Movie("The Matrix", "The Wachowskis")
# third_movie = Movie("The Predator", "Shane Black")
# first_movie.change_director("Me")
# third_movie.change_name("My Movie")
# first_movie.watch()
# third_movie.watch()
# first_movie.watch()
# print(first_movie)
# print(second_movie)
# print(third_movie)

# class Vehicle:
#     def __init__(self,type,model,price):
#         self.type=type
#         self.model=model
#         self.price=price
#         self.owner=None
#     def buy(self,money,name):
#         if self.owner==None and money>=self.price:
#             self.owner=name
#             return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
#         elif money<self.price: return ("Sorry, not enough money")
#         elif self.owner!=None: return ("Car already sold")
#     def sell(self):
#         if self.owner is None:
#             return "Vehicle has no owner"
#         self.owner=None
#
#     def __repr__(self):
#         if self.owner is None:
#             return f"{self.model} {self.type} is on sale: {self.price}"
#
#         return f"{self.model} {self.type} is owned by: {self.owner}"
#
#
# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)


# class Article:
#     def __init__(self,title,content, author):
#         self.title=title
#         self.content=content
#         self.author=author
#     def edit(self,new_content):
#         self.content=new_content
#     def change_author(self,new_author):
#         self.author=new_author
#     def rename(self,new_name):
#         self.title=new_name
#     def __repr__(self):
#         return f"{self.title} - {self.content}: {self.author}"


# class Inventory:
#     def __init__(self,capacity):
#         self.__capacity=capacity
#         self.items=[]
#     def add_item(self,item):
#         if len(self.items)<self.__capacity:
#             self.items.append(item)
#         else: return "not enough room in the inventory"
#     def get_capacity(self):
#         return self.__capacity
#     def __repr__(self):
#         return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity-len(self.items)}"
#
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)

# class Class:
#     __students_count = 22
#
#     def __init__(self,name):
#         self.name=name
#         self.students=[]
#         self.grades=[]
#     def add_student(self, name, grade):
#         if len(self.students)<Class.__students_count:
#             self.students.append(name)
#             self.grades.append(grade)
#     def get_average_grade(self):
#         return round(sum(self.grades)/len(self.grades),2)
#     def __repr__(self):
#         return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self)}"
#
# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)


# class Town:
#     def __init__(self,name):
#         self.name = name
#         self.latitude = '0°N'
#         self.longitude = '0°E'
#
#     def set_latitude(self, latitude) :
#         self.latitude=latitude
#     def set_longitude(self, longitude):
#         self.longitude=longitude
#     def __repr__(self):
#         return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
#
# town = Town("Sofia")
# town.set_latitude("42° 41\' 51.04\" N")
# town.set_longitude("23° 19\' 26.94\" E")
# print(town)

# class Catalogue:
#
#     def __init__(self,name):
#         self.name=name
#         self.products=[]
#
#     def add_product(self,product_name):
#         self.products.append(product_name)
#
#     def get_by_letter(self,first_letter):
#         return [product for product in self.products if product[0].lower()==first_letter.lower()]
#
#     def __repr__(self):
#         result=f'Items in the {self.name} catalogue:'
#         for i in sorted(self.products):
#             result+= '\n'+ i
#         return result
#         # print(f'Items in the {self.name} catalogue:')
#         # for i in sorted(self.product):
#         #     print(i)
#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)

# class Weapon:
#     def __init__(self, bullets):
#         self.bullets=bullets
#     def shoot(self):
#         if self.bullets>0:
#             self.bullets-=1
#             return 'shooting...'
#         else: return 'no bullets left'
#     def __repr__(self):
#         return f'Remaining bullets: {self.bullets}'
#
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)



# class Storage:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.storage=[]
#     def add_product(self,product):
#         self.product=str(product)
#         if len(self.storage)<self.capacity:
#             self.storage.append(product)
#     def get_products(self):
#         # l=Storage.__storage
#         # st='\", \"'.join(l)
#         # st='[\"'+st+'"]'
#         # return st
#         return self.storage
#
# storage = Storage(2)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())


# class Circle:
#     __pi=3.14
#     def __init__(self, diameter):
#         self.diameter=diameter
#         self.radius=diameter/2
#
#     def calculate_circumference(self):
#         return Circle.__pi*self.diameter
#     def calculate_area(self):
#         return Circle.__pi*self.radius*self.radius
#     def calculate_area_of_sector(self,angle):
#         area=Circle.calculate_area(self)
#         return (angle/360)*area
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")
#

# class Zoo:
#     def __init__(self,name):
#         self.name=name
#         self.mammals=[]
#         self.fishes=[]
#         self.birds=[]
#     def add_animal(self,spcies, name):
#         if spcies=='mammal':
#             self.mammals.append((name))
#         elif spcies=='fish':
#             self.fishes.append(name)
#         elif  spcies=='bird':
#             self.birds.append(name)
#     def get_info(self,species):
#         if species=='mammal':
#             print(f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {len(self.mammals)+len(self.fishes)+len(self.birds)}" )
#         elif species=='fish':
#             print(f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {len(self.mammals)+len(self.fishes)+len(self.birds)}" )
#         elif  species=='bird':
#             print(f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {len(self.mammals)+len(self.fishes)+len(self.birds)}" )
#
# name= input()
# n= int(input())
# zoo=Zoo(name)
#
# for i in range(n):
#     type,name=input().split(' ')
#     zoo.add_animal(type,name)
# zoo.get_info(input())



# class Email:
#     def __init__(self, sender, receiver,content, is_sent=False):
#         self.sender=sender
#         self.receiver=receiver
#         self.content=content
#         self.is_sent=is_sent
#
#     def send(self):
#         self.is_sent=True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
# mails=[]
# line= input()
# while line!='Stop':
#     s,r,c= line.split(' ')
#     mail=Email(s,r,c)
#     mails.append(mail)
#     line=input()
#
# idx=[int(i) for i in input().split(', ')]
#
# for i in idx:
#     mails[i].send()
#
# for i in mails:
#     print(i.get_info())


# class Party:
#     def __init__(self):
#         self.people=[]
#         self.age=0
#
#
# name=input()
# party=Party()
#
# while name!='End':
#     party.people.append(name)
#     name = input()
#
# print(f"Going: {', '.join(party.people)}")
# print(f'Total: {len(party.people)}')
#
# class Comment:
#     def __init__(self, username, content, likes=0):
#         self.username= username
#         self.content= content
#         self.likes=likes
