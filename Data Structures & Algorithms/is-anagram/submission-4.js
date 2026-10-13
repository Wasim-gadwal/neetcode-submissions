class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) { return false }

        let letterFreq = {}
        
        for (const char of s) {
            letterFreq[char] = (letterFreq[char] ?? 0) + 1
        }

        for (const char of t) {
            if (!letterFreq[char]) { return false }
            letterFreq[char] = letterFreq[char] - 1
        }

        const allZero = Object.values(letterFreq).every(char => char === 0)
        if (allZero) { return true } else { return false }

    }
}
