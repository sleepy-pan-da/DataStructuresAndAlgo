class Person:
  def __init__(self, fname : str, lname : str):
    self.firstname : str = fname
    self.lastname : str  = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        super().printname()

