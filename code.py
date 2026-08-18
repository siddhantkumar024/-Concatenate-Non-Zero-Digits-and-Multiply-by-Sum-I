class Solution:
    def sumAndMultiply(self, n: int) -> int:
        d=str(n)
        s=0
        i=''
        for ni in d:
            if int(ni)!=0:
                i+=ni
                s+=int(ni)
        if i=='':
            return 0
        return int(i)*s
        
