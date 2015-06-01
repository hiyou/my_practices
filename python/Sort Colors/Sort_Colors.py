class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        r = 0 # ��??��?????��?????��??
        b = n - 1 #?????????????��??
        i = 0
        while i <= b:
            if A[i] == 0:
                A[i],A[r] = A[r],A[i]
                r += 1
                i += 1 # ��????????????��?????��????????1?��0???????��?????????��??
            elif A[i] == 2:
                A[i],A[b] = A[b],A[i]
                b -= 1
            # ????i??????1 ?��?????��????????????????????0??1??2????????????         
            else:
                i += 1
solu = Solution()
solu.sortColors([1,0])