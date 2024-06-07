class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationsMinutes):
        self.name = name
        self.yearLauch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationsMinutes = durationsMinutes

    def __str__(self):
        return f"Filme: {self.name}"

    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLauch}")
        print(f"Está no plano? {self.includePlan}")
        print(f"Avaliação do Filme: {self.note}")
        print(f"Duração do Filme: {self.durationsMinutes}\n")


mario = Movie("Super Mario Bros", 2023, False, 5.0, 125)
top_gun = Movie("Top Gun Maverick", 2022, True, 4.5, 160)
mario.techinal_sheet()
top_gun.techinal_sheet()
