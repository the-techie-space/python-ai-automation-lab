<!-- # Every operation you need to know -->

# --- Creation ---
d = {}                          # empty dict
d = dict()                      # same
d = {"a": 1, "b": 2}           # with initial values

# --- Insert / Update ---
d["key"] = value                # O(1) average

# --- Safe read (3 ways — know all 3!) ---
d["key"]                        # KeyError if missing ← dangerous
d.get("key")                    # returns None if missing ← safe
d.get("key", 0)                 # returns 0 if missing  ← best for counting

# --- Check existence ---
"key" in d                      # O(1) — use this, NOT d.keys()
"key" not in d

# --- Delete ---
del d["key"]                    # KeyError if missing
d.pop("key", None)              # safe delete, returns None if missing

# --- Iterate (all 3 ways) ---
for k in d:            pass     # keys only
for v in d.values():   pass     # values only
for k, v in d.items(): pass     # both — most common in interviews

# --- Length ---
len(d)                          # O(1)


<!-- The 3 special HashMap types Python gives you -->

from collections import defaultdict, Counter, OrderedDict

# 1. defaultdict — never get KeyError, auto-initialises
graph = defaultdict(list)        # for adjacency lists
freq  = defaultdict(int)         # for counting
graph["a"].append("b")           # no KeyError even if "a" didn't exist

# 2. Counter — frequency map supercharged
c = Counter("aabbcc")            # Counter({'a':2,'b':2,'c':2})
c.most_common(2)                 # [('a',2), ('b',2)] — top 2
c["a"] -= 1                      # decrement safely (goes to 0, not KeyError)
c + Counter("abc")               # merge two counters
c1 == c2                         # compare — perfect for anagram check!

# 3. OrderedDict — insertion order guaranteed (Python 3.7+ dict does this too)
# Still used for: LRU Cache implementation (most famous interview problem)
from collections import OrderedDict
lru = OrderedDict()
lru.move_to_end("key")           # move to most-recently-used end
lru.popitem(last=False)          # evict least-recently-used

<!-- The 6 patterns every SDET must know -->
<!-- Pattern 1 — Frequency counting -->
# Count char frequencies — foundation of all string problems
freq = Counter(s)

# Manual version (write this in interviews, shows you understand)
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

<!-- Pattern 2 — Existence check (trading space for time) -->

# Brute: O(n²) — nested loop checking if element was seen
# HashMap: O(n) — check in O(1) using a set or dict

seen = set()
for num in nums:
    if num in seen:        # O(1) lookup
        return True
    seen.add(num)

<!-- Pattern 3 — Grouping by computed key -->

# Group anagrams — same sorted letters = same group
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))          # "eat","tea","ate" → ('a','e','t')
        groups[key].append(w)
    return list(groups.values())
# Time O(n·k·log k),  Space O(n·k)

<!-- Interview questions interviewers actually ask -->

Question Answer to give

Why is lookup O(1)?Hash fn maps key to bucket index directly — no iteration

What causes O(n) worst case?All keys collide into one bucket → linear scan

How does Python handle collisions?Open addressing — probes to next available slot

When does resizing happen?Load factor > 0.67 → table doubles, all keys rehashed

Are dict keys ordered in Python?Yes, since Python 3.7 — insertion order guaranteed

Can a list be a dict key?No — keys must be hashable (immutable). Use tuple instead

What's the difference between dict and set?Set is just keys, no values — same hash table internally

<!-- SDET edge cases checklist -->

# Always test these before saying "done" in an interview:

d = {}
d.get("missing")          # → None, not crash
d.get("missing", 0)       # → 0, safe default
"x" in d                  # → False, not crash
d.pop("missing", None)    # → None, safe delete

# Mutable default trap — NEVER do this:
def bad(d={}):             # same dict reused across calls!
    d["x"] = 1

# Correct:
def good(d=None):
    if d is None: d = {}

