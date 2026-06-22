class Solution(object):
    def twoSum(self, nums, target):
        seen = {} #dictionary for fast lookup

        for i, x in enumerate(nums): #this is the same thing as for pair in enum(n), i,x = pair
            needed = target - x #case 1 i = 0, 9 - 2 so needed=7

            if needed in seen: #remember this operator, in, "is element in collection?"
                return(i, seen[needed])
            
            seen[x] = i #dictionaries (python hashmaps) are kinda like reverse lists, value : index
            #key takeaway, dicts are value mapping collections.