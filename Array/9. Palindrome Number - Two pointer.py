class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        if len(num) == 1:
            return True
        left, right = 0, len(num) - 1
        while left < right:
            print(num[left], num [right])
            if num[left] != num [right]:
                return False
            else:
                left+=1
                right-=1
        return True