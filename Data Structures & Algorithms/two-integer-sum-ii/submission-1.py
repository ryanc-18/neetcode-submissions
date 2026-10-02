class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i at the start ; j at the end
        # if target under i++ ; if target over j--
        # make sure i != j
        # at least one solution, so if not under or over then its equal
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
                
        return [i + 1, j + 1]
            


        