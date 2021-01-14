from django.db import models
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:

# python manage.py shell

# from first_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()

# Create your models here.
class Topic(models.Model):                                          #We inherit from models.Model which is the base class, Topic is the derived class
    top_name = models.CharField(max_length=264,unique=True)         #max_length is a constraint of this character field top_name
                                                                    #Some max_length is recommended as otherwise, users can enter countless charecters which we'll have to save
    def __str__(self):                                              #Usually we'll also want to have some string representation of the model, so if we ever have to print out some instance of topic, we'll be able to do that without an error
        return self.top_name

class Webpage(models.Model):                                        #Has 3 columns - topic,name and url
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)                              #Only allows URLs in the URL field

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()                                       #To store when the webpage was actually accessed

    def __str__(self):
        return str(self.date)                                       #We return it as a string as its a DateTime object
