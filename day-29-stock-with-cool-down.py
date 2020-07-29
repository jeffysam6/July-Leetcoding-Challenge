class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        
        mini = float('inf')

        maxi = 0


        max_prof = 0

        i = 0

        while(i < len(arr)):

            mini = min(mini,arr[i])

            # print(mini)

            if(arr[i] > mini):
                max_prof += (arr[i] -mini)
                mini = arr[i]

                i += 1

            i += 1
            
        return max_prof
