/**
 * Sliding Window Patterns
 * ========================
 * Fixed-size and dynamic sliding window problems:
 * Maximum Sum Subarray of Size K, Anagram Indices, Longest Substring
 * Without Repeats, Minimum Subarray Sum, Longest Substring with K
 * Distinct Chars, Minimum Window Substring.
 *
 * Each problem preserves the progression - Approach 1 = naive/first idea,
 * Approach 2+ = optimized sliding-window version.
 */

// ============================================================================
// 1. MAXIMUM SUM SUBARRAY OF SIZE K (Fixed Window)
// ============================================================================
/**
 * Given an array of integers and integer K, find the maximum sum of
 * any contiguous subarray of size K.
 *
 * Input : arr = [2, 1, 5, 1, 3, 2], k = 3
 * Output: 9  (subarray [5, 1, 3])
 */

/**
 * Approach 1 - Standard nested loop (the way I learned first)
 * Recompute the sum for each starting position.
 * Issues:
 *   1. Hardcoded to k=3 - logic must change if K grows.
 *   2. Recomputes overlapping elements - O(n * k).
 */
// const arr = [2, 1, 5, 1, 3, 2];
// const k = 3;
// let max = 0;
// for (let i = 0; i < arr.length; i++) {
//   if (i < arr.length - 2) {
//     const sum = arr[i] + arr[i + 1] + arr[i + 2];
//     if (sum > max) max = sum;
//   }
// }
// console.log(max);

/**
 * Approach 2 - Sliding Window (optimised)
 * Build the first window, then slide one element at a time:
 *   newSum = oldSum + arr[i] - arr[i - k]
 * Time: O(n), Space: O(1)
 *
 * @param {number[]} arr - Input array
 * @param {number}   k   - Window size
 * @returns {{ maxSum: number, combination: number[] }}
 */
function maxSumSubarray(arr, k) {
  let windowSum = 0;
  for (let i = 0; i < k; i++) windowSum += arr[i];

  let maxSum = windowSum;
  let combinationIndex = 0;

  for (let i = k; i < arr.length; i++) {
    windowSum += arr[i] - arr[i - k];
    if (windowSum > maxSum) {
      maxSum = windowSum;
      combinationIndex = i - k + 1;
    }
  }
  return { maxSum, combination: arr.slice(combinationIndex, combinationIndex + k) };
}

console.log("--- Max Sum Subarray Size K ---");
console.log(maxSumSubarray([2, 1, 5, 1, 3, 2], 3));

// ============================================================================
// 2. COUNT OCCURRENCES OF ANAGRAMS (Fixed Window)
// ============================================================================
/**
 * Given strings s and p, find all start indices in s where a substring
 * is an anagram of p.
 *
 * Input : s = "cbaebabacd", p = "abc"
 * Output: [0, 6]
 *
 * Insight:
 *   Fixed window of size p.length over s; compare frequency maps each step.
 * Time : O(n)
 * Space: O(k) where k = distinct chars
 *
 * @param {string} s - Source string
 * @param {string} p - Pattern string
 * @returns {number[]} Start indices of anagram matches
 */
function find_anagrams(s, p) {
  const output = [];
  const pCount = {};
  const windowCount = {};

  // Prime maps with the first window
  for (let i = 0; i < p.length; i++) {
    pCount[p[i]] = (pCount[p[i]] || 0) + 1;
    windowCount[s[i]] = (windowCount[s[i]] || 0) + 1;
  }

  const matches = (a, b) => {
    for (const key in a) {
      if (a[key] !== b[key]) return false;
    }
    return true;
  };

  if (matches(pCount, windowCount)) output.push(0);

  // Slide one character at a time
  for (let i = p.length; i < s.length; i++) {
    const charIn = s[i];
    const charOut = s[i - p.length];

    windowCount[charIn] = (windowCount[charIn] || 0) + 1;
    windowCount[charOut]--;
    if (windowCount[charOut] === 0) delete windowCount[charOut];

    if (matches(pCount, windowCount)) output.push(i - p.length + 1);
  }
  return output;
}

console.log("\n--- Anagram Indices ---");
console.log(find_anagrams("cbaebabacd", "abc"));

// ============================================================================
// 3. LONGEST SUBSTRING WITHOUT REPEATING CHARS (Dynamic Window)
// ============================================================================
/**
 * Length of the longest substring with all unique characters.
 *
 * Input : "pwwkew"
 * Output: 3   ("wke")
 *
 * Insight:
 *   Expand right until duplicate appears, then shrink left until duplicate
 *   is removed. Track seen chars in a Set.
 * Time: O(n), Space: O(k)
 *
 * @param {string} str - Input string
 * @returns {number} Length of longest unique-char substring
 */
function longest_substring(str) {
  const seen = new Set();
  let left = 0;
  let longest = 0;

  for (let right = 0; right < str.length; right++) {
    while (seen.has(str[right])) {
      seen.delete(str[left]);
      left++;
    }
    seen.add(str[right]);
    longest = Math.max(longest, right - left + 1);
  }
  return longest;
}

console.log("\n--- Longest Substring Without Repeats ---");
console.log(longest_substring("pwwkew"));

// ============================================================================
// 4. MINIMUM SIZE SUBARRAY SUM (Dynamic Window)
// ============================================================================
/**
 * Smallest contiguous subarray whose sum is >= target.
 *
 * Input : target = 7, arr = [2, 3, 1, 2, 4, 3, 7]
 * Output: 1   (subarray [7])
 *
 * Insight:
 *   All numbers are positive, so adding always grows the sum and removing
 *   always shrinks it. That monotonic property is what makes sliding
 *   window valid here.
 * Time: O(n), Space: O(1)
 *
 * @param {number} target - Required minimum sum
 * @param {number[]} array - Array of positive integers
 * @returns {number} Length of the smallest valid subarray (0 if none)
 */
function min_subarray_len(target, array) {
  let left = 0;
  let windowSum = 0;
  let minLen = Infinity;

  for (let right = 0; right < array.length; right++) {
    windowSum += array[right];

    while (windowSum >= target) {
      minLen = Math.min(minLen, right - left + 1);
      windowSum -= array[left];
      left++;
    }
  }
  return minLen === Infinity ? 0 : minLen;
}

console.log("\n--- Min Subarray Length >= Target ---");
console.log(min_subarray_len(7, [2, 3, 1, 2, 4, 3, 7]));

// ============================================================================
// 5. LONGEST SUBSTRING WITH AT MOST K DISTINCT CHARS (Dynamic Window)
// ============================================================================
/**
 * Longest substring containing at most K distinct characters.
 *
 * Input : "eceba", k = 2
 * Output: 3   ("ece")
 *
 * Insight:
 *   Expand right; if distinct count exceeds k, shrink left while
 *   decrementing the evicted character's count and dropping it at zero.
 * Time: O(n), Space: O(k)
 *
 * @param {string} string - Input string
 * @param {number} k      - Max distinct characters allowed
 * @returns {number} Length of longest valid substring
 */
function longest_k_distinct(string, k) {
  const freq = new Map();
  let left = 0;
  let longest = 0;

  for (let right = 0; right < string.length; right++) {
    freq.set(string[right], (freq.get(string[right]) || 0) + 1);

    while (freq.size > k) {
      const charLeft = string[left];
      freq.set(charLeft, freq.get(charLeft) - 1);
      if (freq.get(charLeft) === 0) freq.delete(charLeft);
      left++;
    }
    longest = Math.max(longest, right - left + 1);
  }
  return longest;
}

console.log("\n--- Longest Substring with K Distinct ---");
console.log(longest_k_distinct("eceba", 2));

// ============================================================================
// 6. MINIMUM WINDOW SUBSTRING (Dynamic Window)
// ============================================================================
/**
 * Smallest window in `s` that contains every character of `t`
 * (including duplicates).
 *
 * Input : s = "ADOBECODEBANC", t = "ABC"
 * Output: 4   (window "BANC")
 *
 * Insight:
 *   Track how many of t's characters are satisfied. Expand until satisfied,
 *   then shrink to find the minimum.
 * Time : O(|s| + |t|)
 * Space: O(|s| + |t|)
 *
 * @param {string} string - Source string
 * @param {string} t      - Pattern whose characters must all appear
 * @returns {number} Length of the minimum valid window (Infinity if none)
 */
function min_window(string, t) {
  const freq = new Map();
  const tFreq = new Map();
  let left = 0;
  let minWindow = Infinity;

  for (const ch of t) {
    tFreq.set(ch, (tFreq.get(ch) || 0) + 1);
  }

  const matches = (need, have) => {
    for (const [char, count] of need) {
      if ((have.get(char) || 0) < count) return false;
    }
    return true;
  };

  for (let right = 0; right < string.length; right++) {
    const ch = string[right];
    freq.set(ch, (freq.get(ch) || 0) + 1);

    while (matches(tFreq, freq)) {
      minWindow = Math.min(minWindow, right - left + 1);
      const out = string[left];
      freq.set(out, freq.get(out) - 1);
      if (freq.get(out) === 0) freq.delete(out);
      left++;
    }
  }
  return minWindow;
}

console.log("\n--- Minimum Window Substring ---");
console.log(min_window("ADOBECODEBANC", "ABC"));

// ============================================================================
// KEY TAKEAWAYS
// ============================================================================
/**
 * FIXED WINDOW:
 *   - Prime the first window, then slide by one: newSum = oldSum + in - out.
 *
 * DYNAMIC WINDOW:
 *   - Expand `right`, shrink `left` while some constraint is broken/met.
 *   - Track state with Map (frequency) or Set (membership).
 *
 * MONOTONIC PROPERTY:
 *   - Sliding window relies on adding/removing changing state in a
 *     predictable direction (positive nums, distinct count, etc.).
 *
 * MAP-COMPARISON HELPERS:
 *   - Anagram / minimum window problems benefit from a `matches(need, have)`
 *     helper to check whether all required counts are satisfied.
 */
