def removeElement(nums: list[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            count+=1
        else:
            nums[i-count] = nums[i]

    return (len(nums) - count)

n = int(input("Len: "))
lis = [int(input("Input: ")) for i in range(n)]

valu = int(input("Val: "))
print(removeElement(lis, valu))
