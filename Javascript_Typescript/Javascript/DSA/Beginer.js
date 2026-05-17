/**
 * Beginner DSA - Arrays & Strings
 * ================================
 * Two Sum, Contains Duplicate, Valid Anagram, Intersection of Arrays,
 * Disappeared Numbers, Majority Element, Move Zeroes, Best Time to Buy/Sell,
 * Valid Palindrome, Reverse String.
 *
 * Each problem keeps every approach I tried so the learning progression
 * stays visible: Approach 1 = first idea, Approach 2+ = improvements.
 */

// ============================================================================
// 1. TWO SUM
// ============================================================================
/**
 * Given an array of integers, find two numbers whose sum equals `target`.
 *
 * Input : nums = [2, 7, 11, 15], target = 9
 * Output: [0, 1]   (2 + 7 = 9)
 */

/**
 * Approach 1 - Brute Force (first idea from the beginning of my journey)
 * Nested loop trying every pair.
 * Time: O(n^2), Space: O(1)
 */
// function two_sum(nums, target) {
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = 0; j < nums.length; j++) {
//       if (nums[i] + nums[j] === target) {
//         return [i, j];
//       }
//     }
//   }
// }

/**
 * Approach 2 - HashMap (better: trade space for time)
 * For each number, check if its complement (target - num) was seen before.
 * Time: O(n), Space: O(n)
 */
// function two_sum(nums, target) {
//   const freq = new Map();
//   for (let i = 0; i < nums.length; i++) {
//     const value = target - nums[i];
//     if (freq.has(value)) {
//       return [freq.get(value), i];
//     }
//     freq.set(nums[i], i);
//   }
// }

/**
 * Approach 3 - Two Pointer (after sorting)
 * Note: returned indices refer to the SORTED array, not the original.
 * Time: O(n log n) for sort, Space: O(1) extra
 */
function two_sum(nums, target) {
  const sorted = [...nums].sort((a, b) => a - b);
  let left = 0;
  let right = sorted.length - 1;

  while (sorted[left] + sorted[right] !== target) {
    if (sorted[left] + sorted[right] > target) {
      right--;
    } else {
      left++;
    }
  }
  return [left, right];
}

console.log("--- Two Sum ---");
console.log(two_sum([2, 7, 11, 15], 9));

// ============================================================================
// 2. CONTAINS DUPLICATE
// ============================================================================
/**
 * Check if any value appears more than once.
 *
 * Input : [1, 2, 3, 1]
 * Output: true
 *
 * Key Idea: track what's already been seen; repeat -> duplicate.
 *
 * Approach 1 - Map for frequency tracking.
 * Time: O(n), Space: O(n)
 */
function duplicate(nums) {
  const freq = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (freq.has(nums[i])) return true;
    freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
  }
  return false;
}

console.log("\n--- Contains Duplicate ---");
console.log(duplicate([1, 2, 3, 1]));

// ============================================================================
// 3. VALID ANAGRAM
// ============================================================================
/**
 * Check if two strings are anagrams (same letters, any order).
 *
 * Input : s = "anagram", t = "nagaram"
 * Output: true
 *
 * Key Idea: compare character counts, not order.
 */

/**
 * Approach 1 - First attempt: two separate frequency maps
 * Build a Map for each string, then compare entries.
 * Issue I hit: the comparison loop returned `true` too early
 * (returned inside the for-loop on the first match).
 * Time: O(n), Space: O(n)
 */
// function validAnagram(s, t) {
//   if (s.length !== t.length) return false;
//   const freS = new Map();
//   const freT = new Map();
//
//   for (let i = 0; i < s.length; i++) {
//     freS.set(s[i], (freS.get(s[i]) || 0) + 1);
//     freT.set(t[i], (freT.get(t[i]) || 0) + 1);
//   }
//
//   for (const [key, val] of freS) {
//     if (freT.get(key) !== val) return false;
//   }
//   return true;
// }

/**
 * Approach 2 - Single map: add for `s`, subtract for `t`
 * Empty map at the end means anagram.
 * Time: O(n), Space: O(n)
 */
// function validAnagram(s, t) {
//   if (s.length !== t.length) return false;
//   const freq = new Map();
//
//   for (let i = 0; i < s.length; i++) {
//     freq.set(s[i], (freq.get(s[i]) || 0) + 1);
//   }
//   for (let i = 0; i < t.length; i++) {
//     if (freq.has(t[i])) freq.set(t[i], freq.get(t[i]) - 1);
//     if (freq.get(t[i]) === 0) freq.delete(t[i]);
//   }
//   return freq.size === 0;
// }

/**
 * Approach 3 - Single pass, add & subtract in same loop (cleanest)
 * `+1` for s[i], `-1` for t[i]; if every value ends at 0, it's an anagram.
 * Time: O(n), Space: O(n)
 */
function validAnagram(s, t) {
  if (s.length !== t.length) return false;
  const freq = new Map();

  for (let i = 0; i < s.length; i++) {
    freq.set(s[i], (freq.get(s[i]) || 0) + 1);
    freq.set(t[i], (freq.get(t[i]) || 0) - 1);
  }
  for (const val of freq.values()) {
    if (val !== 0) return false;
  }
  return true;
}

console.log("\n--- Valid Anagram ---");
console.log(validAnagram("anagram", "nagaram"));

// ============================================================================
// 4. INTERSECTION OF TWO ARRAYS
// ============================================================================
/**
 * Return the unique elements common to both arrays.
 *
 * Input : nums1 = [1, 2, 2, 1], nums2 = [2, 2]
 * Output: [2]
 */

/**
 * Approach 1 - Two frequency maps (first idea from my head)
 * Walk one map, push key if it exists in the other.
 * Time: O(n + m), Space: O(n + m)
 */
// function IntersectionElementTwo(nums1, nums2) {
//   const freq1 = new Map();
//   const freq2 = new Map();
//   const output = [];
//
//   for (const n of nums1) freq1.set(n, (freq1.get(n) || 0) + 1);
//   for (const n of nums2) freq2.set(n, (freq2.get(n) || 0) + 1);
//
//   for (const [el] of freq1) {
//     if (freq2.has(el)) output.push(el);
//   }
//   return output;
// }

/**
 * Approach 2 - Single Set (cleaner)
 * Put nums1 in a Set, iterate nums2, delete after match to keep uniqueness.
 * Time: O(n + m), Space: O(n)
 */
function IntersectionElementTwo(nums1, nums2) {
  const sets = new Set(nums1);
  const output = [];

  for (const element of nums2) {
    if (sets.has(element)) {
      output.push(element);
      sets.delete(element);
    }
  }
  return output;
}

console.log("\n--- Intersection of Two Arrays ---");
console.log(IntersectionElementTwo([1, 2, 2, 1], [2, 2]));

// ============================================================================
// 5. FIND ALL NUMBERS DISAPPEARED IN AN ARRAY
// ============================================================================
/**
 * Find numbers missing from [1, n] where n = array length.
 *
 * Input : [4, 3, 2, 7, 8, 2, 3, 1]
 * Output: [5, 6]
 *
 * Approach - Use a Set for O(1) lookup, then scan 1..n.
 * Time: O(n), Space: O(n)
 */
function numberDisappear(array) {
  const sets = new Set(array);
  const output = [];

  for (let i = 1; i <= array.length; i++) {
    if (!sets.has(i)) output.push(i);
  }
  return output;
}

console.log("\n--- Disappeared Numbers ---");
console.log(numberDisappear([4, 3, 2, 7, 8, 2, 3, 1]));

// ============================================================================
// 6. MAJORITY ELEMENT
// ============================================================================
/**
 * Find element appearing more than n/2 times.
 *
 * Input : [3, 2, 3]
 * Output: 3
 *
 * Approach 1 - Frequency Map (first thought)
 * Count, then scan map for count > n/2.
 * Time: O(n), Space: O(n)
 */
function majority(array) {
  const freq = new Map();
  const threshold = array.length / 2;

  for (const element of array) {
    freq.set(element, (freq.get(element) || 0) + 1);
  }
  for (const [key, value] of freq) {
    if (value > threshold) return key;
  }
}

console.log("\n--- Majority Element ---");
console.log(majority([3, 2, 3]));

// ============================================================================
// 7. MOVE ZEROES
// ============================================================================
/**
 * Move all 0s to the end, preserving order of non-zeros.
 *
 * Input : [0, 1, 0, 3, 12]
 * Output: [1, 3, 12, 0, 0]
 */

/**
 * Approach 1 - Filter + separate zero bucket (first idea)
 * Build two lists then concatenate. Not in-place.
 * Time: O(n), Space: O(n)
 */
// function zeroForward(array) {
//   const zeros = [];
//   const nonZeros = array.filter(item => {
//     if (item > 0) return true;
//     zeros.push(item);
//     return false;
//   });
//   return [...nonZeros, ...zeros];
// }

/**
 * Approach 2 - Two pointer swap (deeper thinking, in-place)
 * `left` marks next slot for non-zero; swap when right finds one.
 * Time: O(n), Space: O(1)
 */
// function zeroForward(array) {
//   let left = 0;
//   for (let right = 0; right < array.length; right++) {
//     if (array[right] > 0) {
//       [array[left], array[right]] = [array[right], array[left]];
//       left++;
//     }
//   }
//   return array;
// }

/**
 * Approach 3 - "Snowball" / two-pass (newer method)
 * Pass 1: shift non-zeros forward. Pass 2: fill the tail with zeros.
 * Time: O(n), Space: O(1)
 */
function zeroForward(array) {
  let lastZero = 0;

  for (let i = 0; i < array.length; i++) {
    if (array[i] !== 0) {
      array[lastZero] = array[i];
      lastZero++;
    }
  }
  for (let i = lastZero; i < array.length; i++) {
    array[i] = 0;
  }
  return array;
}

console.log("\n--- Move Zeroes ---");
console.log(zeroForward([0, 1, 0, 3, 12]));

// ============================================================================
// 8. BEST TIME TO BUY AND SELL STOCK
// ============================================================================
/**
 * Max profit from one buy + one sell.
 *
 * Input : [7, 1, 5, 3, 6, 4]
 * Output: 5   (buy at 1, sell at 6)
 *
 * Approach - Track lowest price so far; update max profit on the fly.
 * Time: O(n), Space: O(1)
 */
function bestPrice(prices) {
  let minBuy = prices[0];
  let maxProfit = 0;

  for (const price of prices) {
    if (price < minBuy) {
      minBuy = price;
    } else {
      maxProfit = Math.max(maxProfit, price - minBuy);
    }
  }
  return maxProfit;
}

console.log("\n--- Best Time to Buy/Sell ---");
console.log(bestPrice([7, 1, 5, 3, 6, 4]));

// ============================================================================
// 9. VALID PALINDROME
// ============================================================================
/**
 * Check if a string is a palindrome ignoring case and non-alphanumerics.
 *
 * Input : "A man, a plan, a canal: Panama"
 * Output: true
 *
 * Approach - Clean string first, then two-pointer compare from both ends.
 * Time: O(n), Space: O(n)
 */
function palindrome(string) {
  const cleanString = (s) => {
    let result = "";
    for (const char of s) {
      const isLower = char >= "a" && char <= "z";
      const isUpper = char >= "A" && char <= "Z";
      const isDigit = char >= "0" && char <= "9";
      if (isLower || isUpper || isDigit) {
        result += char.toLowerCase();
      }
    }
    return result;
  };

  const cleanStr = cleanString(string);
  let left = 0;
  let right = cleanStr.length - 1;

  while (left < right) {
    if (cleanStr[left] !== cleanStr[right]) return false;
    left++;
    right--;
  }
  return true;
}

console.log("\n--- Valid Palindrome ---");
console.log(palindrome("A man, a plan, a canal: Panama"));

// ============================================================================
// 10. REVERSE STRING (in-place)
// ============================================================================
/**
 * Reverse a character array in-place.
 *
 * Input : ["h","e","l","l","o"]
 * Output: ["o","l","l","e","h"]
 *
 * Approach - Two pointers, swap inward.
 * Time: O(n), Space: O(1)
 */
function reverseStr(array) {
  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    [array[left], array[right]] = [array[right], array[left]];
    left++;
    right--;
  }
  return array;
}

console.log("\n--- Reverse String ---");
console.log(reverseStr(["h", "e", "l", "l", "o"]));

// ============================================================================
// KEY TAKEAWAYS
// ============================================================================
/**
 * TWO SUM:
 *   - Brute force is O(n^2); HashMap drops it to O(n) using complement lookup.
 *
 * DUPLICATE / ANAGRAM / INTERSECTION:
 *   - Map/Set is the default tool for frequency or membership.
 *   - Single-map +1/-1 trick is the cleanest for anagram-style problems.
 *
 * DISAPPEARED / MAJORITY:
 *   - Set membership for missing-number scans.
 *   - Map for n/2 threshold counting.
 *
 * MOVE ZEROES:
 *   - Two-pointer swap or two-pass fill are both in-place O(1) extra space.
 *
 * BEST PRICE / PALINDROME / REVERSE:
 *   - One-pass with a running minimum (stocks).
 *   - Clean-then-compare two pointers (palindrome).
 *   - Two-pointer swap (reverse).
 */
