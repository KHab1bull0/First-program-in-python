def findMedianSortedArrays(nums1, nums2) -> float:
        list3 = []
        list3 = nums1 + nums2
        list3.sort()
        jam = float()
        if len(list3) % 2  == 0:
            jam = list3[len(list3)//2] + list3[(len(list3)//2)-1]
        else:
            jam = list3[(len(list3)//2)]
            return jam
        return jam / 2

lis1 = [ int(input()) for i in range(2)]
lis2 = [ int(input()) for i in range(2)]

n = findMedianSortedArrays(lis1, lis2)
print(n)
