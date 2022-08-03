class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = x
        number = int(num)
        if number < 0:
            return False
        huiwen = 0
        # count = 0
        while number:
            # count += 1
            b = number % 10
            number = number // 10
            huiwen = huiwen * 10 + b

        if huiwen == num:
            return True
        else:
            return False

