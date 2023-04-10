# from app1.models import Person
from app11.models import *
from django.contrib.auth.models import User
#exec(open(r'D:\python program\firstapp\app1\db_shell.py').read())
# all person get :-
# obj = Person.objects.all()
# print(obj)

#to get all data backend query :-
# obj = Person.objects.all() # Querryset
# print(objs.query)

# all objects in list :-
# objs = Person.objects.all()
# for i in objs:
#     print(list(objs))

# object in single name and address:-
# objs = Person.objects.all()
# for person in objs:
#     print(person)

# object in all dict:-
# objs = Person.objects.all()
# for person in objs:
#     print(person.__dict__)

# to get first record:-
# first_record = Person.objects.first()
# print(first_record)

# to get record by passing id:-
# obj = Person.objects.get(id=3) # single record
# print(obj)

#useing exceptin handling:-
# try:
#     obj = Person.objects.get(id=5) # single record
#     print(obj)
# except Person.DoesNotExist:
#     print('Record does not exist.')

# to get multiple record by passing file name:-
# Person.object.get(age=25) # it is not use to get
# objs = Person.objects.filter(age=23)
# print(objs)

# to get single age and address:- 
# objs = Person.objects.filter(age=23 , address="pune" ) # , :- and
# print(objs.query)

# p1 get in dict:-
# p1=Person.objects.get(id=1)
# print(p1.__dict__)

# mobile number fetch:-
# p1=Person.objects.get(id=1)
# print(p1.__dict__)
# print(p1.mobile_num)

# to change mobile number update/change:-
# p1=Person.objects.get(id=1)
# print(p1.__dict__)
# p1.mobile_num = 48754458498
# p1.save()

# to delete the person 5 number:-
# p1=Person.objects.get(id=5)
# p1.delete()

# 1st way to new create the person and save:-
# p1 = Person(name="abc" , age=24 , mobile_num=9877874546 , address= "nanded" )
# p1.save()

# 2nd way to save data:-
# Person.objects.create(name="XYZ" , age=24 , mobile_num=9821466500 , address= "nanded")

# to check the person objects to types:-
# print(dir(Person.objects))

# bulk_create:-
# p1 = Person(name="Naru" , age=24 , mobile_num=8180021800 , address= "Nagpur" )
# p2 = Person(name="shripad" , age=23 , mobile_num=9877874456 , address= "Akola" )
# p3 = Person(name="Nana" , age=22 , mobile_num=8767912291 , address= "parli" )
# p4 = Person(name="vaishnavi" , age=25 , mobile_num=8484926834 , address= "nanded" )

# Person.objects.bulk_create([p1 , p2 ,p3 ,p4])

# person count:-
# print(Person.objects.count())

# to delete multiple records:-
# Person.object.filter(age=25).delete()

# to get data with name from the person table:-
# print(Person.objects.filter(name__startswith="p"))

#to get data with name from end with person table:-
# print(Person.objects.filter(name__endswith="y"))

# to get data with exclude name from person table:- 
# print(Person.objects.exclude(name__startswith="H"))

#to check the data in table is exists :- TRUE or FALSE
# print(Person.objects.filter(id=1).exists())

# to get data using filter name is exists or Not:-
# print(Person.objects.filter(name="vyankatesh").exists())

# to get the person data in order:-
# print(Person.objects.all().order_by("id"))

# to get data in disending order:-
# print(Person.objects.all().order_by("-id"))

# to get data in order by name:-
# print(Person.objects.all().order_by("-name"))


# person object():-
# Person.objects.get(id=1).show_details()

#
# for per_obj in Person.objects.all():
#     per_obj.show_details()

#
# print(Person.get_data_above_age())

#
# print(Person.objects.all())

#
# print(Person.objects.filter(name__contains="v"))

#

# data = Person.objects.all().values()
# print(data)

#
# data = Person.objects.all().values()
# for i in data:
#     print(i,type(i))

#
# data = Person.objects.all().values("id","name","age")
# for i in data:
#     print(i)

#
# data = Person.objects.all().values("id","name","age")
# name_list =[]
# for i in data:
#     name_list.append(i["name"])
# print(name_list)

#
# data = Person.objects.all().values("id","name","age")
# lst = list(map(lambda x : x["age"],list(data)))
# print(sum(lst)//len(lst)) # average age of all person

#list of tuple containing values only
# data = Person.objects.all().values_list() # use in values_list("name")
# print(data)
# print(list(data))

# database change mysqul
# exec(open(r'D:\python program\firstapp\app1\db_shell.py').read())

# User.objects.create_user(username="vyankatesh",password="Kulkarni@97") # always use

# 33:11 python 63

# print(Person.objects.all())

# delete :- soft delete , hard delete
#-------------
# data = Person.objects.filter(id__in=[3,5])
# print(data)
# p1 = Person.objects.get(id=3)
# p1.mobile_num = 888888888
# p1.age = 24
# p1.is_active = True
# p1.save()

# -------------
# data = Person.objects.filter(id__in=[3,5]).update(is_active = True )# using filter 
# print(data)

# print(Person.objects.filter(is_active=False))

# print(Person.get_active_data())

# print(Person.activep.all())

# print(Person.all_data.all())


# lectuer:-64
# exec(open(r'D:\python program\firstapp\app1\db_shell.py').read())

# clgs = College.objects.all()
# princ = Principal.objects.all()
# depts = Department.objects.all()
# studs = Student.objects.all()
# subjs = Subject.objects.all()

# print(clgs)
# print(princ)
# print(depts)
# print(studs)
# print(subjs)
# college using for loop in get all data access
# for clg in clgs:
#     print(clg.__dict__)

# **Principal using for loop in get all data access
# for prin in princ:
#     print(prin.__dict__)
# **department using for loop in get all data access
# for dept in depts:
    # print(dept. __dict__)

# **students using for loop in get all data access
# for stud in studs:
    # print(stud.__dict__)
    # print(stud)

# **subject using for loop in get all data access
# for subj in subjs:
#     print(subj)
    # print(subj.__dict__)

# clg = clgs[0]
# print(clg.principal)

#*** principal to college get data
# vyankatesh_obj = Principal.objects.first()
# print(vyankatesh_obj.College)

# **college to department get data 
# print(clg)
# print(clg.department_set.all())


# dept to college get data
# dept = Department.objects.first() # error
# print(dept.College) # error

# dept to student get data 
# dept = Department.objects.first()
# print(dept.student_set.all())

# get all student detp wise
# all_depts = Department.objects.all()
# d = {}
# for dept in all_depts:
    # print(f"Department name:- {dept.name} , Studs:- {list(dept.student_set.all())}")
    # print(f"Department name:- {dept.name} , Studs:- {list(dept.student_set.all())}")
#      d[dept.name] = list(dept.student_set.all())
# print(d)

# s1 =Student.objects.first()
# s1 =Student.objects.get(id=15)
# print(s1.dept)

# get department from students
# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
    # print(stud) # *****
    # print(f"{stud.name} Department:-{stud.dept}") # *****
#     stud_dept_dict[stud.name] = stud.dept.name
# print(stud_dept_dict)

# clg = College.objects.get(id=1)
# print(clg.principal)
# print(clg.depts.all()).

# dept = Department.objects.get(id=3)
# print(dept)
# print(dept.subjs.all())

# department to subject get all
# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subjs.all())
# print([list(dept.subjs.all()) for dept in Department.objects.all()])

# college to department through student get data
# clg = College.objects.get(id=1)
# print(clg.depts.all()[1].studs.all())
# for dept in clg.depts.all():
#     print(dept.studs.all())

# clg = College.objects.get(id=1)
# studs_list = []
# for dept in clg.depts.all():
#     studs_list.extend(dept.studs.all())
# print(studs_list)

#student to college name get 
# s1 = Student.objects.get(id=9)
# print(s1.dept.College)


## addition 
# College.objects.create(name="COPE" ,adr="shivajinagar")
# c1= College.objects.get(id=2)
# p1 = Principal (name="Pallavi",exp=16,qual="phd", College=c1)
# p1.save()

# make sure that college id in present in table
# Department.objects.create(name="petrochemical",dept_str = 60, College_id=2)

# department row create student

# Student.objects.create(name="suraj",marks=65 , age=19, dept_id=26)
# Student.objects.create(name="shubham",marks=54 , age=21, dept_id= 26)
# Student.objects.create(name="ketan",marks=55 , age=22, dept_id=26)

# get student name we have add students print name 
# s1 , s2 , s3 = Student.objects.filter(id__gt=15)
# print(s1,s2,s3)

# select related python 66 15/12/22

# studs = Student.objects.all()[5]
# print(studs)

# studs = Student.objects.all() # ***
# studs = Student.objects.select_related("dept")
# for studs in studs:
#     print(studs.dept)


#  16/12/22  no session 16/12
# python 67 17/12/22

# exec(open(r'D:\python program\firstapp\app1\db_shell.py').read())


# from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM student''')
# data = cursor.fetchall()
# data = cursor.fetchmany(3)
# print(data)
# data = cursor.fetchmany(3)
# print(data)

# second way
# data = Student.objects.raw('SELECT * FROM student')
# for i in data:
#     print(i)



# Multiple Database
# MySQL , SQLite

# data = Student.objects.all()
# print(data) 

SECOND_DATABASE ="second_db"
# data = Student.objects.using(SECOND_DATABASE).all()
# print(data) 

# data = Student.objects.using(SECOND_DATABASE).create()

# c1=College.objects.using(SECOND_DATABASE).create(name="MIT",adr="karve Nagar")
# Principal.objects.create()
# d1=Department.objects.using(SECOND_DATABASE).create(name="ENTS",dept_str=60,College=c1)
# s1=Student.objects.using(SECOND_DATABASE).create(name="vyankatesh",marks=78,age=24,dept=d1)
# s2=Subject.objects.using(SECOND_DATABASE).create(name="digital Signal",is_practical=True,dept=d1)
# s1=Student.objects.using(SECOND_DATABASE).create(name="sagar",marks=87,age=24,dept=d1)

# studs = Student.objects.using(SECOND_DATABASE).all()
# print(studs)






# atomic transaction