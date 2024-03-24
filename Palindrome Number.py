def isPalindrome(x):
        x = str(x)
        new_num=x[::-1]
        if x == new_num:
                return True
        else:
                return False


