class Person:
    def __init__(self, name, age, job) -> None:
        self._name = name
        self._age = age
        self._job = job

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def job(self):
        return self._job
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"

class Student(Person):
    def __init__(self, name, age, job, grade) -> None:
        super().__init__(name, age, job)
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        self._grade = value
    
    def get_details(self):
        return f"{super().get_details()}, Grade: {self.grade}"

class Professor(Person):
    def __init__(self, name, age, job, courses) -> None:
        super().__init__(name, age, job)
        self._courses = courses
        
    @property
    def courses(self):
        return self._courses
    
    def get_details(self):
        return f"{super().get_details()}, Courses: {self.courses}"

class Employee(Person):
    def __init__(self, name, age, job, department) -> None:
        super().__init__(name, age, job)
        self._department = department

    @property
    def department(self):
        return self._department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"

class StudentProfessor(Student, Professor):
    def __init__(self, name, age, job, courses, grade) -> None:
        print("StudentProfessor : init called")
        Professor.__init__(self,name=name, age=age, job=job, courses=courses)
        self.grade = grade
        
    def get_details(self):
        return f"{Professor.get_details(self)}, Grade: {self._grade}"

class Location:
    __slots__ = "_name", "_latitude", "_longitude"

    def __init__(self, name, latitude, longitude) -> None:
        self._name = name
        self._longitude = longitude
        self._latitude = latitude

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude
    
    def get_coordinates(self):
        return (self.latitude, self.longitude)