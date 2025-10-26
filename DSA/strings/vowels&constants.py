def countVandC(str):
    vowels = 0
    constants = 0
    for ch in str:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            vowels += 1
        else:
            constants += 1
    return [f"Vowels - {vowels}, Constants - {constants}"]


print(countVandC("vamshi"))
