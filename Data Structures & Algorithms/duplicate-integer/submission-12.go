func hasDuplicate(nums []int) bool {
    var freq = make(map[int]bool)

    for _, num := range nums {
        if freq[num] {
            return true
        }
        freq[num] = true
    }
    return false
}
