class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        j = len(nums)-1
        aux = []
        i=0
        return_null = [-1,-1]
        control = 1
        while control==1:
            if nums[i] == target:
                aux.append(i)
                control = 0
            i = i+1
        control = 1
        if len(aux) == 0:
            return return_null
        while control==1:
            if nums[j] == target:
                aux.append(j)
                control = 0
            j = j-1
        return aux
