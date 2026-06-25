class Solution(object):
    def containsDuplicate(self, nums):
        memory = {}

        for i in range(len(nums)):
            if nums[i] in memory:
                return True
            
            memory[nums[i]] = True

        return False

        #i got TLE using a list DS for memory, O(n^2) worst case
        #using a set its n checks x O(1) because lookup with sets is fast so O(n) time
        #i think using dictionary is also O(n) time, the boolean value on line 9 doesn't matter, just using it for the key. I think the set version was optimal but wtv