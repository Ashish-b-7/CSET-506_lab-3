class Employee:
  def __init__(self,eid="",n="",age=0,salary=0):
    self._Id=eid
    self._name=n
    self._age=age
    self._salary=salary

  def __str__(self) -> str:
     return f"Employee ID: {self._Id} | Name: {self._name} | Age: {self._age} | Salary: {self._salary} |"


  def displayDetails(self):
    print(f"Employee ID: {self._Id} | Name: {self._name} | Age: {self._age} | Salary: {self._salary} |")

e1=Employee("161E90","Raman",41,56000)
e1.displayDetails()

e2=Employee("161F91","Himadri",38,67500)
e2.displayDetails()


e3=Employee("161F99","Jaya",51,82100)
e3.displayDetails()


e4=Employee("171E20","Tejas",30,55000)
e4.displayDetails()

e5=Employee("171G30","Ajay",45,44000)
e5.displayDetails()

l1=[e1, e2, e3, e4 , e5]


while True:
    result  = []
    
    print("Menu \n")
    print("-"*30)
    print("Enter what you want to search")
    field = input()
    

    
    print("Enter input: ")
    n=input( )

    if field=="age":
        for employee in l1:
            if(employee._age==int(n)):
                result.append(employee)
    elif field=="eid":
        for employee in l1:
            if(employee._Id==int(n)):
                result.append(employee)
    elif field=="name":
        for employee in l1:
            if(employee._name==n):
                result.append(employee)
    for emp in result:
        print(emp)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


