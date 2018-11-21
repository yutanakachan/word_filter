from dataclasses import replace


class WordFilter:
    def __init__(self, my_filter):
        self.my_filter = my_filter

    def censor(self, my_filter):
        a = my_filter
        if "アーセナル" in a:
            return a.replace("アーセナル", "<censored>")
        else:
            return a

my_filter = WordFilter("アーセナル")
my_filter.censor("昨日のアーセナルの試合は楽しかった")
print(my_filter.censor("昨日のアーセナルの試合は楽しかった"))
print(my_filter.censor("昨日のリバプールの試合アツかった！"))
