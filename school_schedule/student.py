class Student:
    """
    Student class needs attributes: name, grade, class_list
    Student class needs methods: add_class(), get_num_classes(), and summary()
    """

    def __init__(self, name, grade, class_list):
        self.name = name
        self.grade = grade
        self.class_list = class_list

    def add_class(self, class_name):
        self.class_list.append(class_name)
        return self.class_list

    def get_num_classes(self):
        return len(self.class_list)

    def display_classes(self):
        return ', '.join(self.class_list)

    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classess: {self.display_classes()}"
