var= 'mom'
def palindrome(var):
    length = len(var)
    for i in range(length):
        if (var[i] !=  var[-(i+1)]):
            return False
    return True


if palindrome(var):
    print("It is palindrome")
else:
    print('It is not palindrome')