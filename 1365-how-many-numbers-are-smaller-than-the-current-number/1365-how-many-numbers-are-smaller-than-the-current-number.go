func smallerNumbersThanCurrent(nums []int) []int {
    result := []int{}
    count := 0
    for i := range nums{
        for j := range nums{
            if j != i && nums[j] < nums[i]{
                 count++
                 }
        }
        result = append(result, count)
        count = 0
    }
    return result
}