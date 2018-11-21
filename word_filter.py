class WordFilter:
    def __init__(self, my_filter):
        self.my_filter = my_filter

    def ng_word(self):
        word_hit = input("NGワードにヒットしたときの表示文字を設定してください")
        return word_hit

    def censor(self, my_filter):
        a = my_filter
        if "アーセナル" in a:
            return a.replace("アーセナル", self.ng_word())
        else:
            return a

my_filter = WordFilter("アーセナル")
print(my_filter.censor("昨日のアーセナルの試合アツかった！"))
print(my_filter.censor("昨日のリバプールの試合アツかった！"))
