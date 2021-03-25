class Phylm:
    def __init__(self, title="Film 1"):
        self.title = title
        self.year = None

    def runtime(self):
        return 90

    def plot(self):
        return "Things happen"

    def imdb_title(self):
        return "Film 1"

    def imdb_year(self):
        return 2000

    def imdb_score(self):
        return 7

    def imdb_low_confidence(self):
        return False

    def mtc_title(self):
        return "Film 1"

    def mtc_year(self):
        return 2000

    def mtc_score(self):
        return 70

    def mtc_low_confidence(self):
        return False

    def rt_title(self):
        return "Film 1"

    def rt_year(self):
        return 2000

    def rt_tomato_score(self):
        return 70

    def rt_audience_score(self):
        return 70

    def rt_low_confidence(self):
        return False

    def genres(self):
        return ["Comedy"]

    def cast(self):
        return ["Clark Gable"]

    def directors(self):
        return ["Steve McQueen"]
