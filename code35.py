def searchInsert(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
        elif nums[i] < target:
            continue
    return len(nums)


lis = [int(input("Input: ")) for i in range(4)]
t = int(input("Target: "))

print(searchInsert(lis, t))
