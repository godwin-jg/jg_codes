package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{5, 3, 1, 4, 2}

	// Option 1: Using sort.Slice with an anonymous function
	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
	fmt.Println(nums) // Output: [5 4 3 2 1]

	// Option 2: Using sort.Ints with reverse flag
	nums2 := []int{2,34, -1, 4, 2}
	sort.Sort(sort.Reverse(sort.IntSlice(nums2)))
	fmt.Println(nums2) // Output: [5 4 3 2 1]
}
