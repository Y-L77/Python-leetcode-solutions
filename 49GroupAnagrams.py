class Solution(object):
    def groupAnagrams(self, strs):
        dict = {} # i need this to be sortedStr : [word, ...]
        formatAns = []

        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr in dict:
                continue
            else:
                dict[sortedStr] = []

        dictIndex = set() #everything on and below this line could have been done with dict.values()

        for i in range(len(strs)):
            anagramCheck = ''.join(sorted(strs[i]))
            dict[anagramCheck].append(strs[i])
            dictIndex.add(anagramCheck)
        
        #okay, return dict gave a dict but i need a list
        listDictIndex = list(dictIndex)

        for i in range(len(dictIndex)):
            formatAns.append(dict[listDictIndex[i]])

        return formatAns
        #this solution does a lot of unnecessary work but wtv