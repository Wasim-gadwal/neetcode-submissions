class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const temp = []
        let duplicate = false

        for (const num of nums) {
            if (!temp.includes(num)) {
                temp.push(num)
            }
            else {
                duplicate = true
                return duplicate
            }
        }
            return duplicate
        }
}