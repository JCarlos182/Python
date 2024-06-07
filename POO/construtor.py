# Criando classes com Construtores

class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationsMinutes):
        self.name = name
        self.yearLauch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationsMinutes = durationsMinutes

    def __str__(self):
        return f"Filme: {self.name}"





madmax = Movie("MadMax", 2020, True, 5.0, 120)
print(f"O filme {madmax.name}\n foi lançado no ano de {madmax.yearLauch} e tem nota {madmax.note}")


