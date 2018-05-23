func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, v := range nums {
		if _, ok := m[v]; ok && v**2 == target {
			return []int{i, m[v]}
		}
		m[v] = i
	}
	for k, v1 := range m {
		if v2, ok := m[target-k]; v1 != v2 && ok {
			return []int{v1, v2}
		}
	}
	return []int{}
}
	
