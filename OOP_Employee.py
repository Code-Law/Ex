#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    'All class Employee'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, "; Salary: ", self.salary)

"Create an Object"
emp1 = Employee("Zara", 2000)
"Create another Object"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: %d" % Employee.empCount)