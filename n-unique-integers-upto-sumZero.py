class Solution:
    def sumZero(self, nums: int) -> List[int]:
        ans=[]
        if nums%2!=0:
            ans.append(0)
        for i in range(1,nums//2+1):
            ans.append(-i)
            ans.append(i)
        return ans