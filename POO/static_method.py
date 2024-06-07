"""
1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar mas não pode modificar o estado da classe.
3 - Usamos o decorator @staticmethod para criar um método estático
"""
class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def courses_trail(trail):
        if trail == "python Fundamentos":
            courses = ["Dominando o python", "Módulos e pip", "Orientação a Onjetos"]
        elif trail == "Automação com o python":
            courses = ["Automação de Tarefas", "Web Scraping", "Assistente Virtual em python"]
        else:
            courses = ["A definir"]
        return courses


print(Course.courses_trail("python Fundamentos"))
print(Course.courses_trail("Análise de Dados com python"))
print(Course.courses_trail("Automação com o python"))

