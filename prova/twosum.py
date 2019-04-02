class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	i = nums[0]
    	j = nums[len(nums)]
    	lista_retorno = set()
    	controle = 1	
    	while controle == 1:
    		if nums[i] + nums[j] == target:
    			lista_retorno.add(i)
    			lista_retorno.add(j)
    			controle = 0
    		if nums[i] + nums[j] > target:
    			j = j-1

    		if nums[i] + nums[j] < target:
    			i = i+1
    	return lista_retorno

#meu nome é Marlus Marcos