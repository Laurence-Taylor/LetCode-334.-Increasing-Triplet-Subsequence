class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Declare three variables as infinit (upperbounds)
        first = second = third = float('inf')
        #  for ecah number in the list of numbers lets find the three elementes such as first < second < third
        # using the for and the if elif sequentially we achieve the result. 
        for number in nums: 
            if number <= first: 
                first = number
            elif number <= second:
                second = number
            elif number <= third:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.increasingTriplet([1,5,0,4,1,3]))
    print(sol.increasingTriplet([1,5,0,4,3]))