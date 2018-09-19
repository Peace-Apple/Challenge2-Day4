def sum(listp):
    if not isinstance(listp, list):
        return 'Invalid argument. It should be a list'

    total=0
    for b in listp:
        if isinstance(b,int):
            total+=b

        elif isinstance(b,list):
            total+=sum(b)
        
    return total

if __name__=='__main__':
    print(sum([1,2,3,[3,1]]))