class Solution(object):
    def longestCommonPrefix(self, strs):
        #ordering matters, list is probably optimal
        #for this particular problem i had to learn colon slicing, s[0:3] means from 0 to 3, or just :3, default is 0

        prefix = strs[0]

        for i in range(len(strs)):
            while strs[i][0:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix

        #O(n^2) worst case? -> technically n * m but technically worst case could be m = n so im not wrong
