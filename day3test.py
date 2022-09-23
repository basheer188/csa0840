def Anagrams( strs ):

       dictionary = {}
       for word in li:
           sortedWord = ''.join(sorted(word))

           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]

           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]

li = ['banana']
print(Anagrams(str))
