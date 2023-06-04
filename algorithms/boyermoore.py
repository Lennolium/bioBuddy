#!/usr/bin/env python3

"""
Privat/Projekte/GeneHound/algorithms/boyermoore.py: ...

This module is responsible for ...
"""

# Header.
__author__ = "Lennart Haack"
__email__ = "lennart-haack@stud.uni-frankfurt.de"
__license__ = "GNU GPLv3"
__version__ = "TODO: X.Y.Z"
__date__ = "2023-05-23"
__status__ = "TODO: Prototype/Development/Production"


# Imports.


def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    s = 0
    results = []

    lambdaa = bad_character(pattern)
    gamma = good_suffix(pattern)

    while s <= (n - m):
        j = m - 1  # -1 weg eigt laut pseudo

        while j > 0 and pattern[j] == text[s + j]:
            j = j - 1

            if j == 0:
                results.append(s)

                s = s + gamma[0]

            else:
                s = s + max(gamma[j], j - lambdaa[text[s + j]])

    return results


# Bad character rule (last occurrence).
def bad_character(pattern):
    # Length of pattern.
    m = len(pattern)

    # Create a dictionary for storing the shift of each character.
    shift_dict = {}

    for i in range(0, m):
        # Shift is the distance between the last occurrence of the
        # character and the end of the pattern.
        shift = max(1, (m - i - 1))

        # Store the shifts with corresponding character as key in the
        # dictionary.
        shift_dict[pattern[i]] = shift

    # Return the resulting dictionary.
    return shift_dict


# Good suffix rule.
def compute_prefix(pattern):
    # Defining character length of pattern.
    m = len(pattern)

    # Initializing prefix function. [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pi = [0] * m

    # Initializing variable k to store length of the longest prefix.
    k = 0

    # Iterating over pattern.
    for q in range(1, m):
        # Checking if next character match. If not, reset k to last
        # matching character.
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]

        # If next character match, increment k.
        if pattern[k] == pattern[q]:
            k = k + 1

        # Storing length of the longest prefix.
        pi[q] = k

    # Returning prefix function.
    return pi


def good_suffix(pattern):
    m = len(pattern)
    gamma = [0] * m

    pi = compute_prefix(pattern)
    print("pi:", pi)
    pattern_rev = pattern[::-1]
    pi_rev = compute_prefix(pattern_rev)
    print("pi_rev:", pi_rev)

    for j in range(0, m):
        gamma[j] = (m - 1) - pi[m - 1]

    for l in range(1, m):
        j = (m - 1) - pi_rev[l]
        if gamma[l] > l - pi_rev[l]:
            gamma[j] = l - pi_rev[l]

    return gamma


# Main.
text_inp = "testeinestextesabababcaabtext"
pattern_inp = "abababcaab"

if __name__ == "__main__":
    print(f"result: {boyer_moore(text_inp, pattern_inp)}")
    bad_character(pattern_inp)
    compute_prefix(pattern_inp)
    good_suffix(pattern_inp)
