# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
  words = sentence.lower().split()
  freq = {}
  for w in words:
    freq[w] = freq.get(w, 0) + 1
  return freq


# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
  freq = {}
  for c in word:
    freq[c] = freq.get(c, 0) + 1
  return freq


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
  for c in word:
    if word.count(c) == 1:
      return c
  return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
  return sorted(s1) == sorted(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating_char(s):
  seen = []
  for c in s:
    if c in seen:
      return c
    seen.append(c)
  return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
  non_zeros = [x for x in nums if x != 0]
  zeros = [0] * nums.count(0)
  return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest(nums):
  unique = sorted(list(set(nums)), reverse=True)
  return unique[1] if len(unique) >= 2 else None


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
  result = []
  for n in nums:
    if n not in result:
      result.append(n)
  return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
  return (n * (n + 1) // 2) - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [nums[i], nums[j]]
  return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
  closest = nums[0]
  for n in nums:
    if abs(n) < abs(closest) or (abs(n) == abs(closest) and n > closest):
      closest = n
  return closest


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
  result = []
  for n in list1:
    if n in list2 and n not in result:
      result.append(n)
  return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
  if not nums:
    return nums
  k = k % len(nums)
  return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
  max_sum = nums[0] + nums[1]
  for i in range(len(nums) - 1):
    current = nums[i] + nums[i + 1]
    if current > max_sum:
      max_sum = current
  return max_sum


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_two_sum_pairs(nums, target):
  pairs = set()
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        pair = tuple(sorted([nums[i], nums[j]]))
        pairs.add(pair)
  return sorted([list(p) for p in pairs])