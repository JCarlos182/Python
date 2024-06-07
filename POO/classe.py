# 1- Criando classe Filme
# 2- Atributos contendo caracteristica do filme
class Movie:
    name = "" # campo para nome
    yearLaunch = 0 # ano de lançamento
    includePlan = False # plano incluso
    note = 0 # nota do filme
    durationsMinutes = 0 # tempo de duração do filme

# Instanciando Classe
# Primeiro filme
filme = Movie()
filme.name = "Super Mario Bros"
filme.yearLaunch = 2023
filme.includePlan = False
filme.note = 5.0
filme.durationsMinutes = 130
print(">>> Dados do Filme <<<")
print(f"Nome do filme: {filme.name} \n Ano de lançamento é: {filme.yearLaunch}")

print("==========================")

# Segundo FIlme
filme2 = Movie()
filme2.name = "John Wick"
filme2.yearLaunch = 2023
filme2.includePlan = False
filme2.note = 5.0
filme2.durationsMinutes = 200
print(">>> Dados do filme <<<")
print(f"Nome do filme: {filme2.name} \n Ano de lançamento é: {filme2.yearLaunch} \n e tem duração de: {filme2.durationsMinutes}")

