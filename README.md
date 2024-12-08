# Inheritance Example

This project demonstrates the use of inheritance in Python through a simple implementation of a class hierarchy involving `Person`, `Student`, `Professor`, `Employee`, and `Location`.

## Classes

### Person
- **Attributes**: 
  - `_name`: The name of the person.
  - `_age`: The age of the person.
  - `_job`: The job title of the person.
- **Methods**:
  - `get_details()`: Returns a string with the person's details.

### Student (inherits from Person)
- **Attributes**:
  - `_grade`: The grade of the student.
- **Methods**:
  - `get_details()`: Extends the `get_details()` method from `Person` to include the student's grade.

### Professor (inherits from Person)
- **Attributes**:
  - `_courses`: The courses taught by the professor.
- **Methods**:
  - `get_details()`: Extends the `get_details()` method from `Person` to include the courses taught.

### Employee (inherits from Person)
- **Attributes**:
  - `_department`: The department of the employee.
- **Methods**:
  - `get_details()`: Extends the `get_details()` method from `Person` to include the department.

### StudentProfessor (inherits from Student and Professor)
- **Attributes**:
  - Combines attributes from both `Student` and `Professor`.
- **Methods**:
  - `get_details()`: Combines details from both `Professor` and the student's grade.

### Location
- **Attributes**:
  - `_name`: The name of the location.
  - `_latitude`: The latitude of the location.
  - `_longitude`: The longitude of the location.
- **Methods**:
  - `get_coordinates()`: Returns the coordinates of the location as a tuple.

## Usage

You can create instances of these classes and call their methods to retrieve information. For example:

python
student = Student("Alice", 20, "Student", "A")
print(student.get_details())


This will output the details of the student including their name, age, job, and grade.
