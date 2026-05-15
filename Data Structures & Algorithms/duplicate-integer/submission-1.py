class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisset = set()

        for i in nums:
            if i in thisset:
                return True
            else:
                thisset.add(i) 
        return False
        