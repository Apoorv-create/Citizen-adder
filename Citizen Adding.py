class Citizen:
    def __init__(self, Name, Age, DOB, Id):
        self.Citizen_Name = Name
        self.Citizen_Age = Age
        self.Citizen_DOB = DOB
        self.Citizen_Id = Id
   
    def add_citizen(self):
        print("Name:" + self.Citizen_Name)
        print("Age:" + str(self.Citizen_Age))
        print("D.O.B:" + str(self.Citizen_DOB))
        print("Id_Number:" + str(self.Citizen_Id))
        print("Citizen Added")
    
citizen1 = Citizen("Miles", "13", "14.07.2009", 1923)
citizen1.add_citizen()

citizen2 = Citizen("Clark", "12", "29.03.2010", 1000)        
citizen2.add_citizen()