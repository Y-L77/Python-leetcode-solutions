class Solution(object):
    def isAnagram(self, s, t):
        #i think ill solve this with a dictionary, key value pairs
        #ill do char : int

        if len(s) == len(t): #get rid of easy cases, does this help my time complexity for LC?
            lettersInS = {}
            for i in range(len(s)):
                lettersInS[s[i]] = lettersInS.get(s[i], 0) + 1

            for i in range(len(t)):
                if(t[i] in lettersInS):
                    lettersInS[t[i]] -= 1
                else:
                    return False
            
            for i in range(len(t)):
                if(lettersInS[t[i]] != 0):
                    return False
            
            return True
        return False

        #i think this code is very shitty and i had to use documentation to figure out this i can do with dictionary
        #O(n) time complexity i think? too many loops i feel like theres an easier way to do this