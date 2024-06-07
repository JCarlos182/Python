class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")

    # Método para buscar dados
    def get_salary(self):
        return self.__salary

    # Método para modificar atribuição privado
    def set_salary(self, salary):
        self.__salary = salary

carlos = Employee("Carlos", 4000)
figueroa = Employee("Figueroa", 7000)
carlos.show()
figueroa.show()
carlos.set_salary(8500)
carlos.show()