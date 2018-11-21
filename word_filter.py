class WordFilter:
    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, my_filter):
        a = my_filter
        if "アーセナル" in a:
            return True

        else:
            return False


my_filter = WordFilter("アーセナル")
my_filter.detect("昨日のアーセナルの試合は楽しかった")
my_filter.detect("昨日のバイエルンの試合は楽しかった")
