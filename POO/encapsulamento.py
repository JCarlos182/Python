class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")


carlos = Employee("Carlos", 4500)
figueroa = Employee("Figueroa", 5000)
carlos.show()
figueroa.show()

# os dois __ torna a metodo privado é possivel visualizar mas não auterar o valor
carlos.__salary = 6000
carlos.show()