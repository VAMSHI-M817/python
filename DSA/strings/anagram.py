def is_anagram(str1, str2):
    word1 = str1.replace(" ", "").lower()
    word2 = str2.replace(" ", "").lower()
    print(sorted(word1), sorted(word2))
    return sorted(word1) == sorted(word2)


# print(is_anagram("silent", "listen"))

is_anagram("dbcae", "dcaeb")
