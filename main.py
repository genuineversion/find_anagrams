
string1=input("Enter word here e.g listen \n")
string2=input("Enter second word here e.g silent \n")

def find_anagrams(word,anagram):

    sortedWord=sorted(word)
    sortedAnagram=sorted(anagram)

    if len(sortedWord)==len(sortedAnagram):
        print(sortedWord==sortedAnagram)

    else:
        print(False)



find_anagrams(string1, string2)
