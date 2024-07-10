class Solution:
    def findMin(self, a: List[int]) -> int:
        
        def solve(l,h):
            while l<h:
                m=(l+h)//2
                
                if a[m]<a[m-1]:
                    return a[m]
                
                elif a[m]>a[h-1]:
                    l=m+1
                
                elif a[m]<a[h-1]:
                    h=m
                
                else:
                
                    if len(set(a[l:m+1]))==1:
                        return min(a[m],solve(m+1,h))
                    
                    else:
                        return min(a[m],solve(l,m))
            
            return a[min(l,len(a)-1)]
        
        return solve(0,len(a))