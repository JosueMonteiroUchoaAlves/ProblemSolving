def search(nums: list, target: int) -> int:
    min_, max_ = 0, len(nums) -1
    while min_ <= max_:
        mid = (min_ + max_) // 2
        if nums[mid] > target: max_ = mid - 1
        elif nums[mid] < target: min_ = mid + 1
        else: return mid
    return -1
             # 0 1 2 3 4  5
print(search([-1,0,3,5,9,12], 9))
