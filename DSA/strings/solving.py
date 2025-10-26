class SortingMethods:
    def __init__(self, str):
        self.str = str

    def reverseString(self):
        str = self.str
        return str[::-1]

    def anagram(self):
        
        str = self.str


res = SortingMethods("vamshi")


print(res.reverseString())
