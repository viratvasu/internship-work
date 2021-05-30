from django.db import models

class School(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    principal = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author_name = models.CharField(max_length = 50 , null = True , blank = True)
    date_of_published = models.DateField(null = True , blank = True)
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title

class StudentInfo(models.Model):
    gender_options = (
        ('Male','Male'),
        ('Female','Female'),
        ('NotGiven','NotGiven')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(choices = gender_options,max_length = 10)
    school = models.ForeignKey(School,on_delete = models.CASCADE , null = True , blank = True)
    book = models.ForeignKey(Book,on_delete = models.CASCADE , null = True , blank = True)

    def __str__(self):
        return self.first_name + " " + self.last_name


    