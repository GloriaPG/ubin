from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.TextField(max_length=100)
  

class States(models.Model):
    name = models.TextField(max_length=100)
    country = models.ForeignKey(Countries)

class Towns(models.Model):
    name = models.TextField(max_length=100)
    state = models.ForeignKey(States)

class Coins(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Immovables(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Property(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Advisors(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Providers(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Contacts(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Events(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Documents(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Photos(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Administrators(models.Model):
    user = models.TextField(max_length=100)
    password = models.TextField(max_length=250)
    permit_handbag = models.BooleanField(default=False)
    permit_diary = models.BooleanField(default=False)
    permit_notary = models.BooleanField(default=False)
    permit_broker = models.BooleanField(default=False)
    permit_proficient = models.BooleanField(default=False)
    permit_events = models.BooleanField(default=False)
    permit_documents = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Users(models.Model):
    profile_name = models.TextField(max_length=250)
    email = models.EmailField(max_length=100)
    password = models.TextField(max_length=250)
    birthday = models.DateField()
    gender = models.TextField(max_length=50)
    phone = models.TextField(max_length=20)
    type_advisor= models.ForeignKey(Types_Advisors)
    immovable_name = models.TextField(max_length=250)
    immovable_phone = models.TextField(max_length=20)
    photo = models.FilePathField(max_length=100)
    register_date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

class Providers(models.Model):
    name = models.TextField(max_length=100)
    type_provider= models.ForeignKey(Types_Providers)
    town= models.ForeignKey(Towns)
    register_date= models.DateField(auto_now_add=True)
    location= models.TextField(max_length=100)
    address= models.TextField(max_length=250)
    phone = models.TextField(max_length=20)
    email = models.EmailField(max_length=50)
    web_page = models.URLField(max_length=200)
    status = models.BooleanField(default=True)

class Classification_Providers(models.Model):
    score = models.IntegerField()
    user= models.ForeignKey(Users)
    provider=models.ForeignKey(Providers)

class Property(models.Model):
    canvas_number = models.IntegerField()
    user= models.ForeignKey(Users)
    type_property= models.ForeignKey(Types_Property)
    type_immovable= models.ForeignKey(Types_Immovables)
    town= models.ForeignKey(Towns)
    location=models.TextField(max_length=200)
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=500)
    one_price=models.DecimalField(decimal_places=2,max_digits=10)
    two_price=models.DecimalField(decimal_places=2,max_digits=10)
    coin=models.ForeignKey(Coins)
    bathrooms=models.IntegerField()
    old=models.IntegerField()
    ground_surface=models.TextField(max_length=50)
    construction_area=models.TextField(max_length=50)
    type_advisor=models.ForeignKey(Types_Advisors)
    country=models.ForeignKey(Countries)
    state=models.ForeignKey(States)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


class Comments(models.Model):
    property= models.ForeignKey(Property)
    user= models.ForeignKey(Users)
    provider=models.ForeignKey(Providers)
    commet= models.TextField(max_length=1000)
    date= models.DateField(auto_now_add=True)

class Contacts(models.Model):
    name= models.TextField(max_length=100)
    lastname= models.TextField(max_length=100)
    phone= models.TextField(max_length=20)
    email = models.EmailField(max_length=50)
    user= models.ForeignKey(Users)
    type_contact= models.ForeignKey(Types_Contacts)
    note = models.TextField(max_length=200)

class Documents(models.Model):
    name= models.TextField(max_length=100)
    administrator=models.ForeignKey(Administrators)
    type_document= models.ForeignKey(Types_Documents)
    state=models.ForeignKey(States)
    town=models.ForeignKey(Towns)
    path=models.FilePathField(max_length=100)

class Events(models.Model):
    name= models.TextField(max_length=200)
    description= models.TextField(max_length=1000)
    administrator=models.ForeignKey(Administrators)
    type_event= models.ForeignKey(Types_Events)
    state=models.ForeignKey(States)
    town=models.ForeignKey(Towns)
    path=models.FilePathField(max_length=100)

class Favorites(models.Model):
    property=models.ForeignKey(Property)
    user= models.ForeignKey(Users)
    status = models.BooleanField(default=False)

class Notifications(models.Model):
    property=models.ForeignKey(Property)
    user= models.ForeignKey(Users)
    message= models.TextField(max_length=200)
    date= models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

class Notifications_Push(models.Model):
    property=models.ForeignKey(Property)
    user= models.ForeignKey(Users)
    device_token= models.TextField(max_length=200)
    device= models.TextField(max_length=20)
    status = models.BooleanField(default=True)
    date= models.DateField(auto_now_add=True)

class Favorites_Providers(models.Model):
    user=models.ForeignKey(Users)
    provider=models.ForeignKey(Providers)

class Photos(models.Model):
    name=models.TextField(max_length=60)
    path=models.FilePathField(max_length=100)
    order = models.IntegerField()
    property=models.ForeignKey(Property)
    provider=models.ForeignKey(Providers)
    type_photo=models.ForeignKey(Types_Photos)

class Types_Reports(models.Model):
    name=models.TextField(max_length=60)
    status=models.BooleanField(default=True)

class Reports(models.Model):
    user=models.ForeignKey(Users)
    type_report=models.ForeignKey(Types_Reports)
    message=models.TextField(max_length=500)
    date= models.DateField(auto_now_add=True)
    
class User_Ubication(models.Model):
    user=models.ForeignKey(Users)
    country=models.ForeignKey(Countries)
    state=models.ForeignKey(States)
    date= models.DateField(auto_now_add=True)

class Types_Customers(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Customers(models.Model):
    name= models.TextField(max_length=50)
    LastName= models.TextField(max_length=50)
    phone= models.TextField(max_length=0)
    email= models.EmailField(max_length=100)
    contact=models.ForeignKey(Contacts)
    type_customer=models.ForeignKey(Types_Customers)

class Favorites_Customers(models.Model):
    customer=models.ForeignKey(Customers)
    user= models.ForeignKey(Users)

class Tasks(models.Model):
    description= models.TextField(max_length=300)
    date= models.DateField(auto_now_add=True)
    hour= models.TimeField(auto_now=False, auto_now_add=False)
    contact=models.ForeignKey(Contacts)
    user= models.ForeignKey(Users)



            
            
            
            
            