def power(a, b):
    if not ((isinstance(a, int) or isinstance(a, float)) and isinstance(b, int)):
        return 'invalid input'
    
    if b == 0 or a == 1:
        return 1
    if a == 0:
        return 0
    if b >= 1:
        return a*power(a, b-1)
    b = abs(b)
    return 1/(a*power(a, b-1))

if __name__=='__main__':
    print(power(2,3))

