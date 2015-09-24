def starts_with(haystack, needle):
    if len(haystack) != len(needle):
        return False
    for i in range(0, len(needle) + 1):
        z = 0            
        if haystack[i] != needle[i] :
            z = 1
        if z == 1:
            return False
        else:
            return True
