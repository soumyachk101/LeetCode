class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
        i=0
        pivotl=0
        while(i<len(nums)):
            if nums[i]==pivot and pivotl!=i:
                nums.insert(pivotl,nums.pop(i))
                

            elif nums[i]<pivot:
                nums.insert(pivotl,nums.pop(i))
                pivotl+=1
                
            i=i+1

        return nums
        '''
        ll=[]
        gl=[]
        p=[]
        for i in nums:
            if i<pivot:
                ll.append(i)
            elif i==pivot:
                p.append(pivot)
            else:
                gl.append(i)
        return ll+p+gl
        

        
        