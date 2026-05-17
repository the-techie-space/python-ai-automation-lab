/**
 * JavaScript Core Concepts - Practice
 * ====================================
 * Polyfills (map / filter / reduce), debounce, throttle, call/bind/apply,
 * currying, deep clone, array flatten.
 *
 * Each topic preserves the progression - Approach 1 = first idea,
 * Approach 2+ = fixes/improvements (e.g. binding `this`, handling args).
 */

// ============================================================================
// 1. ARRAY POLYFILLS - map / filter / reduce
// ============================================================================

/**
 * Polyfill of Array.prototype.map
 * Applies callback to each element and returns a new array of results.
 *
 * @param {(value, index, array) => any} callback
 * @returns {any[]} New array of mapped values
 */
// Array.prototype.myMap = function (callback) {
//   const result = [];
//   for (let i = 0; i < this.length; i++) {
//     result.push(callback(this[i], i, this));
//   }
//   return result;
// };

/**
 * Polyfill of Array.prototype.filter
 * Keeps elements where callback returns truthy.
 *
 * @param {(value, index, array) => boolean} callback
 * @returns {any[]} Filtered array
 */
// Array.prototype.myFilter = function (callback) {
//   const result = [];
//   for (let i = 0; i < this.length; i++) {
//     if (callback(this[i], i, this)) result.push(this[i]);
//   }
//   return result;
// };

/**
 * Polyfill of Array.prototype.reduce
 * Folds the array into a single accumulator value.
 *
 * @param {(acc, value) => any} callback
 * @param {any} [initialValue=0]
 * @returns {any} Final accumulator
 */
// Array.prototype.myReducer = function (callback, initialValue = 0) {
//   let accumulator = initialValue;
//   for (let i = 0; i < this.length; i++) {
//     accumulator = callback(accumulator, this[i]);
//   }
//   return accumulator;
// };

// const arr = [1, 2, 3, 4];
// console.log(arr.myMap((item) => item * 2));        // [2, 4, 6, 8]
// console.log(arr.myFilter((item) => item % 2 === 0)); // [2, 4]

// ============================================================================
// 2. DEBOUNCE
// ============================================================================
/**
 * Debounce: delay execution until `delay` ms of silence has passed
 * since the last call. Useful for search inputs, resize handlers.
 */

/**
 * Approach 1 - First attempt
 * Issue: `this` context is lost; arguments are not forwarded.
 */
// function debounce(fn, delay) {
//   let timer;
//   return function () {
//     clearTimeout(timer);
//     timer = setTimeout(() => {
//       fn();
//     }, delay);
//   };
// }

/**
 * Approach 2 - Fixed version (preserves `this` and args)
 * Uses `function` (not arrow) to keep `this`, and forwards `...args`.
 *
 * @param {Function} fn    - Function to debounce
 * @param {number}   delay - Delay in ms
 * @returns {Function} Debounced wrapper
 */
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}

// ============================================================================
// 3. THROTTLE
// ============================================================================
/**
 * Throttle: call fn at most once per `delay` ms - ignore extra calls
 * during the cooldown. Useful for scroll/mousemove handlers.
 *
 * @param {Function} fn    - Function to throttle
 * @param {number}   delay - Cooldown in ms
 * @returns {Function} Throttled wrapper
 */
function throttle(fn, delay) {
  let wait = false;
  return function (...args) {
    if (wait) return;
    fn.apply(this, args);
    wait = true;
    setTimeout(() => {
      wait = false;
    }, delay);
  };
}

// ============================================================================
// 4. CALL / BIND / APPLY
// ============================================================================
/**
 * Explicitly set `this` for a function call.
 *   call(ctx, a, b)   - invoke now with arguments listed
 *   apply(ctx, [a,b]) - invoke now with arguments as array
 *   bind(ctx, a)      - returns a new function with `this` (and args) locked
 */
// function caller(name) {
//   console.log("hi", name);
//   console.log("this", this, this.age);
// }
// const obj = { name: "syamu", age: 21 };
// caller.call(obj, "syam");

// ============================================================================
// 5. CURRYING
// ============================================================================
/**
 * Currying: transform a function taking multiple arguments into a chain of
 * single-argument functions.
 */

/**
 * Approach 1 - Normal multi-arg function (before currying)
 */
// function multiplier(a, b) {
//   return a * b;
// }
// console.log(multiplier(2, 3));

/**
 * Approach 2 - Curried version
 * Lets you partially apply: const double = multiplier(2); double(3)
 */
// function multiplier(a) {
//   return function (b) {
//     return a * b;
//   };
// }
// const double = multiplier(2);
// console.log(double(3)); // 6
// console.log(double(5)); // 10

// ============================================================================
// 6. DEEP CLONE
// ============================================================================
/**
 * Deep-clone an object or array recursively so nested references
 * are not shared between the original and the copy.
 *
 * Note: handles plain objects + arrays. Does not handle Date/Map/Set/circular.
 *
 * @template T
 * @param {T} value - Value to clone
 * @returns {T} Deep copy of `value`
 */
function deepClone(value) {
  if (value === null || typeof value !== "object") {
    return value;
  }

  const copy = Array.isArray(value) ? [] : {};
  for (const key in value) {
    copy[key] = deepClone(value[key]);
  }
  return copy;
}

// Demonstrates the reference vs. clone problem
// const user = { name: "syam", address: { city: "vij" } };
// function copyUser(user) {
//   const clone = deepClone(user);
//   clone.address.city = "HYD";
//   console.log(clone, user); // original.city stays "vij"
// }
// copyUser(user);

// ============================================================================
// 7. FLATTEN ARRAY (Recursive)
// ============================================================================
/**
 * Flatten an arbitrarily nested array into a single-level array.
 *
 * Input : [1, [2, 3], [4, [5, 6]]]
 * Output: [1, 2, 3, 4, 5, 6]
 *
 * @param {any[]} array - Nested array
 * @returns {any[]} Flat array
 */
function flatten(array) {
  const result = [];
  for (const element of array) {
    if (Array.isArray(element)) {
      result.push(...flatten(element));
    } else {
      result.push(element);
    }
  }
  return result;
}

// console.log(flatten([1, [2, 3], [4, [5, 6]]]));

// ============================================================================
// KEY TAKEAWAYS
// ============================================================================
/**
 * POLYFILLS (map/filter/reduce):
 *   - Use a regular function (not arrow) so `this` refers to the array.
 *   - Forward (value, index, array) to the callback.
 *
 * DEBOUNCE vs THROTTLE:
 *   - Debounce: wait for quiet (e.g. typing pause).
 *   - Throttle: cap rate (e.g. scroll events at most every X ms).
 *   - Both need `function(...args)` + `fn.apply(this, args)` to keep context.
 *
 * CALL / APPLY / BIND:
 *   - call/apply invoke immediately; bind returns a new function.
 *
 * CURRYING:
 *   - Enables partial application and cleaner composition.
 *
 * DEEP CLONE:
 *   - Recurse through objects/arrays; primitives return themselves.
 *
 * FLATTEN:
 *   - Recursion + spread is the simplest flatten; iterate + stack for an
 *     iterative version.
 */
