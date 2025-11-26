from django.db import models

# A model tells django how to work with the data that will be stored in the app
# codewise a model is just a class, it has attributes and methods

class Topic(models.Model):#the class inherits from Model, defines the model's basic functionality
    # A topic the user is learning about

    text = models.CharField(max_length=200)# charfield is used when you want to store a small amount of text, we define it in order to tell django how much space it should reserve in the db
    date_added = models.DateTimeField(auto_now_add=True)# records date and time, which tells django to automatically set to current date and time whenever user creates a new topic

    def __str__(self):
        return self.text
