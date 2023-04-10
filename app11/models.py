from django.db import models

# Create your models here.
#  ORM -- object relational mapper

# class Person(models.Model): # table
# #     #default id 
#     name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     mobile_num = models.IntegerField()
#     address = models.CharField(max_length=100)
    
#     class Meta:
#         db_table ="person"

#     def __str__(self):
#         return f"{self.name} -- {self.address}"

#     def show_details(self):
#         print(f"""-----------------------------
# Person Name:-{self.name}
# Person Age:-{self.age}
# Person Mobile:-{self.mobile_num}
# Person Address:-{self.address}""")

    # @classmethod
    # def get_data_above_age(cls):
    #     return cls.objects.filter(age__gt=21) 

    # @classmethod
    # def get_data_above_age(cls):
    #     data = cls.objects.all().values("id","name","age")
    #     lst = list(map(lambda x : x["age"],list(data)))
    #     return sum(lst)//len(lst)


# startproject , startapp , runserver , makemigartions,
# class User(models.Model):
#     first_name=
#     email.id=
#     is_active=

class ActivePersons(models.Manager): # 
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

# #define class inactive class

class Person(models.Model): # table
    # # default id 
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(null = True)
    date_joined = models.DateTimeField(auto_now= True , null = True)
    date_Updated = models.DateTimeField(auto_now_add=True, null = True)
    is_active = models.BooleanField(default=True)
    activep = ActivePersons()
   # # define inactive class
    all_data = models.Manager()

    class Meta:
        db_table ="person"

    def __str__(self):
        return f"{self.name} -- {self.address}"

    def show_details(self):
        print(f"""-----------------------------
Person Name:-{self.name}
Person Age:-{self.age}
Person Mobile:-{self.mobile_num}
Person Address:-{self.address}""")

    # @classmethod
    # def get_data_above_age(cls):
    #     return cls.objects.filter(age__gt=21) 

    # @classmethod
    # def get_data_above_age(cls):
    #     data = cls.objects.all().values("id","name","age")
    #     lst = list(map(lambda x : x["age"],list(data)))
    #     return sum(lst)//len(lst)
    
    # @classmethod
    # def get_active_data(cls):
    #     return cls.objects.filter(is_active=True)


class CommonClass(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class College (CommonClass):
    adr = models.CharField(max_length = 500)
    est_date = models.DateField(auto_now= True)

    class Meta:
        db_table = "college"

class Principal(CommonClass):
    exp = models.FloatField()
    qual = models.CharField(max_length = 50)
    College = models.OneToOneField(College, on_delete = models.CASCADE , related_name="principal") #onetomanyField
    
    class Meta:
        db_table = "principal"


class Department(CommonClass):
    dept_str = models.IntegerField()
    College = models.ForeignKey(College , on_delete = models.CASCADE , related_name="depts")
    
    class Meta:
        db_table = "dept"
        # unique_together = (("name","college"),)

class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department , on_delete =models.CASCADE, related_name="studs" ) 
    
    class Meta:
        db_table = "student"

class Subject(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE , related_name="subjs")
   
    class Meta:
        db_table = "subject"


# get models from database
# ERD - Entity Relationship dig
