while True:
 def has_unique_chars(s):
    seen = {}

    for char in s:
        if char in seen:
            return False
        seen[char] = True

    return True
 value = input("Enter the string : ")
 result = has_unique_chars(value)
 print(result)