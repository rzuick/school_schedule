from school_schedule.student import Student
# from filename.file import ClassName
#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

print(quinn.add_class("Painting"))
print(quinn.get_num_classes())
print(quinn.summary())

# second instance
claire = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

claire.get_num_classes()
claire.summary()

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function