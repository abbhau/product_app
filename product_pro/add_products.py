import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_pro.settings')
django.setup()

from product_app.models import Product, Brand

# # products = []
# # for i in range(1, 100000000001):
# #     name = f'Product-{i}'
# #     quantity = random.randint(1, 100)
# #     prize = round(random.uniform(10.0, 100.0), 2)
# #     total_prize = quantity * prize
# #     products.append(
# #         Product(
# #             name=name,
# #             quantity=quantity,
# #             prize=prize,
# #             total_prize=total_prize,
# #         )
# #     )
# # Product.objects.bulk_create(products, batch_size=1000)
# # print('100,000 products added successfully!')


# from datetime import date
# from excel_app.models import School, Student, Teacher, Class, Subject

# # Adding 5 schools
# schools_data = [
#     {'name': 'Green Valley High', 'address': '123 Elm St', 'city': 'Springfield', 'state': 'Illinois'},
#     {'name': 'Sunrise Elementary', 'address': '456 Maple Rd', 'city': 'Dayton', 'state': 'Ohio'},
#     {'name': 'Oakwood Academy', 'address': '789 Oak St', 'city': 'Chicago', 'state': 'Illinois'},
#     {'name': 'Riverside High', 'address': '123 River Rd', 'city': 'Miami', 'state': 'Florida'},
#     {'name': 'Lakeside College', 'address': '999 Lakeview Dr', 'city': 'Seattle', 'state': 'Washington'}
# ]

# # Create schools
# for school_data in schools_data:
#     School.objects.create(**school_data)

# # Adding 6 students for each school
# students_data = [
#     {'name': 'John Doe', 'age': 16, 'grade_level': '10'},
#     {'name': 'Jane Smith', 'age': 15, 'grade_level': '9'},
#     {'name': 'Alice Brown', 'age': 17, 'grade_level': '11'},
#     {'name': 'Bob Johnson', 'age': 16, 'grade_level': '10'},
#     {'name': 'Charlie Davis', 'age': 15, 'grade_level': '9'},
#     {'name': 'Emma White', 'age': 17, 'grade_level': '12'}
# ]

# # Fetch all schools to link with students
# schools = School.objects.all()

# # Create students and link them to each school
# for school in schools:
#     for student_data in students_data:
#         Student.objects.create(school=school, **student_data)

# # Adding 7 teachers for each school
# teachers_data = [
#     {'name': 'Mr. Anderson', 'subject': 'Math', 'hire_date': date(2020, 1, 15)},
#     {'name': 'Ms. Taylor', 'subject': 'Science', 'hire_date': date(2018, 6, 22)},
#     {'name': 'Mrs. Davis', 'subject': 'History', 'hire_date': date(2019, 4, 12)},
#     {'name': 'Mr. Johnson', 'subject': 'English', 'hire_date': date(2021, 2, 3)},
#     {'name': 'Ms. Brown', 'subject': 'Art', 'hire_date': date(2022, 8, 19)},
#     {'name': 'Dr. Green', 'subject': 'Chemistry', 'hire_date': date(2020, 11, 30)},
#     {'name': 'Ms. Blue', 'subject': 'Physics', 'hire_date': date(2021, 5, 17)}
# ]

# # Create teachers and link them to each school
# for school in schools:
#     for teacher_data in teachers_data:
#         Teacher.objects.create(school=school, **teacher_data)

# # Adding 5 classes for each school
# classes_data = [
#     {'name': 'Math 101', 'schedule_time': '9:00 AM - 10:00 AM'},
#     {'name': 'Science Lab', 'schedule_time': '10:30 AM - 11:30 AM'},
#     {'name': 'History Lecture', 'schedule_time': '12:00 PM - 1:00 PM'},
#     {'name': 'English Grammar', 'schedule_time': '1:30 PM - 2:30 PM'},
#     {'name': 'Art Workshop', 'schedule_time': '3:00 PM - 4:00 PM'}
# ]

# # Create classes and link them to each school
# for school in schools:
#     for class_data in classes_data:
#         Class.objects.create(school=school, **class_data)

# # Adding 8 subjects for each school
# subjects_data = [
#     {'name': 'Algebra', 'description': 'Mathematical concepts and operations'},
#     {'name': 'Biology', 'description': 'Study of life and living organisms'},
#     {'name': 'World History', 'description': 'History of human civilization'},
#     {'name': 'Literature', 'description': 'Study of written works'},
#     {'name': 'Painting', 'description': 'Artistic painting techniques and history'},
#     {'name': 'Chemistry', 'description': 'Study of the composition and behavior of substances'},
#     {'name': 'Physics', 'description': 'Study of matter and energy'},
#     {'name': 'Art', 'description': 'General study of visual arts'}
# ]

# # Create subjects and link them to each school
# for school in schools:
#     for subject_data in subjects_data:
#         Subject.objects.create(school=school, **subject_data)

# print("Data added successfully!")


# brand_objects = []
# for i in range(1, 200001):  # Generate 200,000 records
#     brand_objects.append(Brand(brand_name=f"Brand {i}"))



# # Bulk create in batches
# batch_size = 10000

# for start in range(0, len(brand_objects), batch_size):
#     Brand.objects.bulk_create(brand_objects[start:start+batch_size])




