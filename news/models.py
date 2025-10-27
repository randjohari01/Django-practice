from django.db import models
from django.utils import timezone
from datetime import date

class reporter(models.Model):
    full_name = models.CharField(max_length = 70)

    def __str__(self):
        return self.full_name
    
  
class article(models.Model):
    date = models.DateField()
    line = models.CharField(max_length = 70)
    content = models.TextField()
    link_with_report = models.ForeignKey( reporter ,verbose_name= "linked article with its reproter", on_delete = models.CASCADE)
    publication = models.ManyToManyField("Publication")

    class Meta:
        ordering = ["line"]

    def __str__(self):
        return self.line
    
class Publication(models.Model):
    title = models.CharField(max_length = 50)

    class Meta: 
        ordering = ["title"]

    def __str__(self):
        return self.title      

class personshirt(models.Model):
    SHIRT_SIZE = {
        "S" : "Small",
        "M" : "Medium",
        "L" : "Large"
    }
    person_name = models.CharField("person's first name", max_length = 70)
    shirt_size = models.CharField(max_length = 1, choices =SHIRT_SIZE)


class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BROUNZE")
    name = models.CharField(unique= True, max_length=60)
    medal = models.CharField(help_text= "the blank allow", blank=True, choices=MedalType, max_length=10)
    created_at = models.DateTimeField(default = timezone.now)

class Fruit(models.Model):
    name = models.CharField(primary_key= True, max_length= 20)


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name   
    
class Groups(models.Model):
    name = models.CharField(max_length= 30)
    member = models.ManyToManyField(Person , through = "MemberShip" , through_fields = ("group" , "person"),)

    def __str__(self):    
        return self.name
    
class MemberShip(models.Model):
    person = models.ForeignKey(Person , on_delete = models.CASCADE)
    group = models.ForeignKey (Groups, on_delete = models.CASCADE)
    date_joined = models.DateField(null = True)
    invited_by  = models.ForeignKey(Person , null = True , on_delete = models.SET_NULL , related_name="invited_by_memberships")


    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields = [ "person" ,"group" ], name = "unique_person_group"
                )
        ]


class Place(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length =30)

    def __str__(self):
        return f"{self.name} the place"

class Restaurant(models.Model):
    name = models.CharField(max_length = 30)
    place = models.OneToOneField(Place,  on_delete = models.CASCADE , primary_key = True )
    serves_hotdog = models.BooleanField(default = False)
    serves_potato = models.BooleanField(default =False)

    def __str__(self): 
        return "%s the restautant" % self.place.name
    

class Waiter (models.Model):
    name = models.CharField(max_length = 30 )
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)

    def __str__(self):
        return "%s the waiter at %s" % (self.name , self.restaurant)

    