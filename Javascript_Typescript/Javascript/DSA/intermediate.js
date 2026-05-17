/**
 * Intermediate DSA - Arrays, Strings & Sliding Window
 * ====================================================
 * Group anagrams, anagram indices, longest substring, minimum
 * subarray, product except self, merge sort, quick sort,
 * three-sum, run-length counting, and string manipulation drills.
 */

// ============================================================================
// GROUP ANAGRAMS
// ============================================================================
/**
 * Group words that are anagrams of each other.
 *
 * Input : ["eat","tea","tan","ate","nat","bat"]
 * Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
 *
 * Key Idea:
 *   Words with the same character frequency belong together.
 *   Build a signature (count of each letter) and bucket by signature.
 *
 * Time : O(n * k) where k = average word length
 * Space: O(n * k)
 *
 * @param {string[]} array - List of lowercase words
 * @returns {Map<string, string[]>} Map of signature -> anagram group
 */
function groupAnagram(array) {
  const freq = new Map();

  for (const element of array) {
    // Count letters into a 26-slot array (a..z)
    const filter = new Array(26).fill(0);
    for (const letter of element) {
      const index = letter.charCodeAt(0) - "a".charCodeAt(0);
      filter[index]++;
    }

    // Build a stable signature from the counts
    let signature = "";
    for (const word of filter) {
      signature += "#" + word;
    }

    if (freq.has(signature)) {
      freq.get(signature).push(element);
    } else {
      freq.set(signature, [element]);
    }
  }
  return freq;
}

console.log("--- Group Anagrams ---");
console.log(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]));

// ============================================================================
// FIND ALL ANAGRAM INDICES (Sliding Window)
// ============================================================================
/**
 * Find every start index in `s` where a substring is an anagram of `p`.
 *
 * Input : s = "cbaebabacd", p = "abc"
 * Output: [0, 6]
 *   - index 0: "cba" is an anagram of "abc"
 *   - index 6: "bac" is an anagram of "abc"
 *
 * Approach:
 *   Maintain frequency maps for `p` and a sliding window over `s`.
 *   Slide one character at a time and compare maps.
 *
 * Time : O(n)
 * Space: O(k) where k = distinct chars
 *
 * @param {string} s - Source string
 * @param {string} p - Pattern string
 * @returns {number[]} Starting indices of anagram matches
 */
function anagramIndex(s, p) {
  const freqP = new Map();
  const freqS = new Map();
  const output = [];
  let left = 0;

  const matcher = (a, b) => {
    if (a.size !== b.size) return false;
    for (const [key, val] of a) {
      if (b.get(key) !== val) return false;
    }
    return true;
  };

  // Prime both maps with the first window
  for (let i = 0; i < p.length; i++) {
    freqP.set(p[i], (freqP.get(p[i]) || 0) + 1);
    freqS.set(s[i], (freqS.get(s[i]) || 0) + 1);
  }

  if (matcher(freqP, freqS)) output.push(0);

  // Slide the window one step at a time
  for (let right = p.length; right < s.length; right++) {
    const letter = s[right];
    const leftWord = s[left];

    freqS.set(letter, (freqS.get(letter) || 0) + 1);
    freqS.set(leftWord, (freqS.get(leftWord) || 0) - 1);

    if (freqS.get(leftWord) === 0) freqS.delete(leftWord);

    left++;
    if (matcher(freqP, freqS)) output.push(left);
  }
  return output;
}

console.log("\n--- Anagram Indices ---");
console.log(anagramIndex("cbaebabacd", "abc"));

// ============================================================================
// LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
// ============================================================================
/**
 * Length of the longest substring with all unique characters.
 *
 * Input : "abcabcbb"
 * Output: 3   ("abc")
 *
 * Approach:
 *   Sliding window with a Set; shrink from the left while a duplicate exists.
 *
 * Time : O(n)
 * Space: O(k)
 *
 * @param {string} string - Input string
 * @returns {number} Length of longest unique-character substring
 */
function longSubString(string) {
  const seen = new Set();
  let left = 0;
  let maxLen = 0;

  for (let right = 0; right < string.length; right++) {
    const word = string[right];

    while (seen.has(word)) {
      seen.delete(string[left]);
      left++;
    }

    seen.add(word);
    maxLen = Math.max(maxLen, right - left + 1);
  }
  return maxLen;
}

console.log("\n--- Longest Unique Substring ---");
console.log(longSubString("abcabcbb"));

// ============================================================================
// MINIMUM SUBARRAY WITH GIVEN SUM
// ============================================================================
/**
 * Smallest contiguous subarray whose sum is exactly `target`.
 *
 * Input : target = 7, nums = [2,3,1,2,4,3]
 * Output: 2     (subarray [4,3])
 *
 * Approach:
 *   Expand right pointer; once windowSum >= target, shrink from the left.
 *
 * Time : O(n)
 * Space: O(1)
 *
 * @param {number[]} array - Array of positive integers
 * @param {number}   target - Desired sum
 * @returns {number} Length of the smallest matching subarray (Infinity if none)
 */
function minSubarray(array, target) {
  let left = 0;
  let windowSum = 0;
  let minLen = Infinity;

  for (let right = 0; right < array.length; right++) {
    windowSum += array[right];

    while (windowSum >= target) {
      if (windowSum === target) {
        minLen = Math.min(minLen, right - left + 1);
      }
      windowSum -= array[left];
      left++;
    }
  }
  return minLen;
}

console.log("\n--- Minimum Subarray ---");
console.log(minSubarray([2, 3, 1, 2, 4, 3], 7));

// ============================================================================
// PRODUCT OF ARRAY EXCEPT SELF
// ============================================================================
/**
 * For each index, return the product of all other elements (no division).
 *
 * Input : [1, 2, 3, 4]
 * Output: [24, 12, 8, 6]
 *
 * Approach:
 *   Two passes - left products, then multiply by right products on the fly.
 *
 * Time : O(n)
 * Space: O(1) extra (output excluded)
 *
 * @param {number[]} array - Input numbers
 * @returns {number[]} Products excluding self at each index
 */
function productExceptSelf(array) {
  const output = [];
  let leftProduct = 1;
  let rightProduct = 1;

  // Left pass: output[i] = product of everything before i
  for (let i = 0; i < array.length; i++) {
    output[i] = leftProduct;
    leftProduct *= array[i];
  }

  // Right pass: multiply by product of everything after i
  for (let i = array.length - 1; i >= 0; i--) {
    output[i] *= rightProduct;
    rightProduct *= array[i];
  }
  return output;
}

console.log("\n--- Product Except Self ---");
console.log(productExceptSelf([1, 2, 3, 4]));

// ============================================================================
// MERGE SORT
// ============================================================================
/**
 * Sort an array using merge sort (divide & conquer).
 *
 * Time : O(n log n)
 * Space: O(n)
 *
 * @param {number[]} array - Array to sort
 * @returns {number[]} New sorted array
 */
function mergeSort(array) {
  if (array.length <= 1) return array;

  const mid = Math.floor(array.length / 2);
  const left = mergeSort(array.slice(0, mid));
  const right = mergeSort(array.slice(mid));

  return merge(left, right);
}

/**
 * Merge two sorted arrays into a single sorted array.
 *
 * @param {number[]} left
 * @param {number[]} right
 * @returns {number[]} Merged sorted array
 */
function merge(left, right) {
  const result = [];
  let i = 0;
  let j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i++]);
    } else {
      result.push(right[j++]);
    }
  }
  return [...result, ...left.slice(i), ...right.slice(j)];
}

console.log("\n--- Merge Sort ---");
console.log(mergeSort([3, 4, 6, 2, 1, 5]));

// ============================================================================
// QUICK SORT
// ============================================================================
/**
 * Sort an array in-place using quick sort (Lomuto partition).
 *
 * Time : O(n log n) average, O(n^2) worst
 * Space: O(log n) recursion stack
 *
 * @param {number[]} array - Array to sort in-place
 * @param {number}   [low=0] - Start index
 * @param {number}   [high=array.length-1] - End index
 * @returns {number[]} The sorted array (same reference)
 */
function quickSort(array, low = 0, high = array.length - 1) {
  if (low < high) {
    const pivotIndex = partition(array, low, high);
    quickSort(array, low, pivotIndex - 1);
    quickSort(array, pivotIndex + 1, high);
  }
  return array;
}

/**
 * Lomuto partition: place pivot at its sorted position.
 *
 * @param {number[]} array
 * @param {number}   low
 * @param {number}   high - Pivot index
 * @returns {number} Final pivot index
 */
function partition(array, low, high) {
  let i = low - 1;
  const pivot = array[high];

  for (let j = low; j < high; j++) {
    if (array[j] < pivot) {
      i++;
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
  [array[i + 1], array[high]] = [array[high], array[i + 1]];
  return i + 1;
}

console.log("\n--- Quick Sort ---");
console.log(quickSort([7, 3, 4, 6, 2, 1, 5]));

// ============================================================================
// THREE SUM
// ============================================================================
/**
 * Find all unique triplets that sum to zero.
 *
 * Input : [-1, 0, 1, 2, -1, -4]
 * Output: [[-1, -1, 2], [-1, 0, 1]]
 *
 * Approach:
 *   Sort, then for each i use a two-pointer scan over the remainder.
 *   Skip duplicate anchors to keep the result set unique.
 *
 * Time : O(n^2)
 * Space: O(1) extra
 *
 * @param {number[]} array - Input numbers
 * @returns {number[][]} Unique triplets summing to zero
 */
function threeSum(array) {
  const output = [];
  array.sort((a, b) => a - b);

  for (let i = 0; i < array.length - 2; i++) {
    // Skip duplicate anchors
    if (i > 0 && array[i] === array[i - 1]) continue;

    let left = i + 1;
    let right = array.length - 1;

    while (left < right) {
      const sum = array[i] + array[left] + array[right];

      if (sum === 0) {
        output.push([array[i], array[left], array[right]]);
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return output;
}

console.log("\n--- Three Sum ---");
console.log(threeSum([-1, 0, 1, 2, -1, -4]));

// ============================================================================
// COUNT CONSECUTIVE CHARACTERS (Run-Length)
// ============================================================================
/**
 * Print run-length groups for consecutive identical characters.
 *
 * Input : "aabbbbcccaaaddd"
 * Output (logs):
 *   a : 2
 *   b : 4
 *   c : 3
 *   a : 3
 *   d : 3
 *
 * Time : O(n), Space: O(1)
 *
 * @param {string} str - Input string
 * @returns {void}
 */
function countConsecutive(str) {
  let count = 1;

  for (let i = 0; i < str.length; i++) {
    if (str[i] === str[i + 1]) {
      count++;
    } else {
      console.log(`${str[i]} : ${count}`);
      count = 1;
    }
  }
}

console.log("\n--- Count Consecutive ---");
countConsecutive("aabbbbcccaaaddd");

// ============================================================================
// SPLIT CAMEL CASE STRINGS
// ============================================================================
/**
 * Insert spaces before uppercase letters in each camelCase string.
 *
 * Input : ["vietnameseCoffeeIs", "bestIn", "theEntireWorld"]
 * Output: ["vietnamese Coffee Is", "best In", "the Entire World"]
 *
 * @param {string[]} array - Camel-cased strings
 * @returns {string[]} Strings with words separated by spaces
 */
function splitCamelCase(array) {
  for (let i = 0; i < array.length; i++) {
    let str = "";
    for (const word of array[i]) {
      if (word >= "A" && word <= "Z") {
        str += " " + word;
      } else {
        str += word;
      }
    }
    array[i] = str;
  }
  return array;
}

console.log("\n--- Split Camel Case ---");
console.log(splitCamelCase(["vietnameseCoffeeIs", "bestIn", "theEntireWorld"]));

// ============================================================================
// KEY TAKEAWAYS
// ============================================================================
/**
 * GROUP ANAGRAMS:
 *   - Letter-count signature buckets anagrams together in O(n*k).
 *
 * ANAGRAM INDICES:
 *   - Fixed-size sliding window + frequency map comparison.
 *
 * LONGEST UNIQUE SUBSTRING:
 *   - Sliding window with Set; shrink left on duplicates.
 *
 * MINIMUM SUBARRAY:
 *   - Expand right, contract left while window >= target.
 *
 * PRODUCT EXCEPT SELF:
 *   - Two passes (left products, then right products) avoid division.
 *
 * MERGE / QUICK SORT:
 *   - Both O(n log n) average; quick sort is in-place, merge sort is stable.
 *
 * THREE SUM:
 *   - Sort + two pointers; skip duplicates to keep results unique.
 *
 * SLIDING WINDOW PATTERN:
 *   - Two pointers (left, right) + a running aggregate is the core template.
 */
