

def two_sum_faster(nums, target):
	sums = []
	hastable = {}
	for i in range(0, len(nums)):
		sum_minus_el = target - nums[i]
		if sum_minus_el in hastable:
			sums.append([nums[i], sum_minus_el])
		hastable[nums[i]] = nums[i]

	return sums 

print(two_sum_faster([3,5,2,-4,8,11], 7))

