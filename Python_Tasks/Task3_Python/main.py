from solutions import (
    all_two_sum_pairs,
    are_anagrams,
    char_frequency,
    closest_to_zero,
    common_elements,
    find_missing_number,
    first_non_repeating_char,
    first_repeating_char,
    max_consecutive_sum,
    move_zeros_to_end,
    remove_duplicates,
    rotate_right,
    second_highest,
    two_sum_first,
    word_frequency,
)

print("--- Q1 ---")
print(word_frequency("python is easy and python is powerful"))[cite: 4]
print(word_frequency("hello world hello"))

print("\n--- Q2 ---")
print(char_frequency("banana"))[cite: 4]
print(char_frequency("engineering"))

print("\n--- Q3 ---")
print(first_non_repeating_char("swiss"))[cite: 4]
print(first_non_repeating_char("racecar"))

print("\n--- Q4 ---")
print(are_anagrams("listen", "silent"))[cite: 4]
print(are_anagrams("hello", "world"))

print("\n--- Q5 ---")
print(first_repeating_char("programming"))[cite: 4]
print(first_repeating_char("abcdef"))

print("\n--- Q6 ---")
print(move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))[cite: 4]
print(move_zeros_to_end([0, 0, 5, 6]))

print("\n--- Q7 ---")
print(second_highest([10, 20, 40, 30, 40, 20]))[cite: 4]
print(second_highest([5, 5, 5]))

print("\n--- Q8 ---")
print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))[cite: 4]
print(remove_duplicates([1, 2, 3, 1, 2]))

print("\n--- Q9 ---")
print(find_missing_number([1, 2, 4, 5, 6], 6))[cite: 4]
print(find_missing_number([1, 3, 4, 5], 5))

print("\n--- Q10 ---")
print(two_sum_first([2, 7, 11, 15], 9))[cite: 4]
print(two_sum_first([3, 2, 4], 6))

print("\n--- Q11 ---")
print(closest_to_zero([-8, -3, 2, 5, -2]))[cite: 4]
print(closest_to_zero([-1, 1]))

print("\n--- Q12 ---")
print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))[cite: 4]
print(common_elements([10, 20], [20, 30]))

print("\n--- Q13 ---")
print(rotate_right([1, 2, 3, 4, 5], 2))[cite: 4]
print(rotate_right([1, 2, 3], 4))

print("\n--- Q14 ---")
print(max_consecutive_sum([4, 7, 2, 9, 5]))[cite: 4]
print(max_consecutive_sum([1, 2, 3, 4]))

print("\n--- Q15 ---")
print(all_two_sum_pairs([2, 4, 3, 5, 7, 8, 1], 9))[cite: 4]
print(all_two_sum_pairs([1, 1, 2, 2], 3))