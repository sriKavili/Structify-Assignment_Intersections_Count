# -*- coding: utf-8 -*-
"""Structify Assignment_Intersections_Count.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10iULaD0QbryMf1ltBg7S34FW3Pk98i9l
"""

import numpy as np

def generate_points(start, end, step=0.01):
    points = []  # Keeping track of the generated points
    while start != end:  # We will loop until the start point reaches the end point
        points.append(round(start, 2))  # Next, append the rounded start point to the points list
        start += step  # Incrementing the start point by the step value
        # Using the modulo operation with 2π in this context is a method of normalizing angles or radian measures within the range of a circle.
        # This will help in two things
        # 1) When the current initial value is 6.25, if we add 0.1, It will be 6.35, It will go beyond 2*pi. Which violates the rule. In cases like this, normalization will help.
        # 2) By making every point go through "Normalization", we are making sure that we are accurately executing the circular nature of the problem and ensuring that the
        # algorithm's logic remains consistent and correct, especially as points approach and exceed the 2*pi boundary. Ultimately, in this circular motion the points again comes back
        # to "0th" radian
        start = round(start % (2 * np.pi), 2)  # Ensure the start point wraps around 2*pi and is rounded
    return points  # Return the list of generated and rounded points

def is_valid_combination(s_point, e_point, used_points):
    # Check if the combination of s_point and e_point is valid by ensuring:
    # 1. The absolute difference is at least 0.1 (ensuring minimum distance and non-equality)
    # 2. The e_point is not already used (to prevent re-using points in other chords)
    return abs(s_point - e_point) >= 0.1 and s_point != e_point and e_point not in used_points

def find_intersections_and_chords(initial_value):
    MAX_RADIAN = round(2 * np.pi, 2)  # Define the maximum radian value (2*pi) rounded to 2 decimal places
    # Assuming initial_value is 3.14 (approximately),
    # The function will generate points starting from 3.14 radians, with each subsequent point incremented by 0.01 radians.
    # The ending condition for these points would be 3.14 - 0.01 = 3.13 radians, so points will be generated up to just before reaching 3.13 radians again,
    # ensuring the sequence doesn't loop back to the starting point.
    # If the initial_value were 0.1, points would be generated from 0.1 radians up to just before reaching 2*pi radians, covering the entire circle.
    s1 = generate_points(initial_value, initial_value - 0.01 if initial_value != 0.1 else MAX_RADIAN, 0.01)
    chords = []  # Initialize an empty list to store the chords found
    used_points = set()  # Initialize a set to keep track of used points
    count = 0  # Initialize a counter for the number of intersections found

    for s1_point in s1:  # Iterate over each starting point in s1
        if s1_point in used_points: continue  # Skip the point if it has already been used
        e1_candidates = generate_points(s1_point + 0.01, s1_point, 0.01)  # Generate candidate ending points (e1)

        for e1_point in e1_candidates:  # Iterate over each candidate ending point in e1
            if not is_valid_combination(s1_point, e1_point, used_points): continue  # Check if the combination is valid

            s2_candidates = generate_points(e1_point + 0.01, s1_point, 0.01)  # Generate candidate starting points (s2)
            for s2_point in s2_candidates:  # Iterate over each candidate starting point in s2
                if not is_valid_combination(e1_point, s2_point, used_points): continue  # Check if the combination is valid

                e2_candidates = generate_points(s2_point + 0.01, e1_point, 0.01)  # Generate candidate ending points (e2)
                for e2_point in e2_candidates:  # Iterate over each candidate ending point in e2
                    if not is_valid_combination(s2_point, e2_point, used_points): continue  # Check if the combination is valid

                    # If a valid combination is found, update the used points and increment the count
                    used_points.update([s1_point, e1_point, s2_point, e2_point])
                    count += 1  # Increment the intersection count

                    # Map each point to its label and sort them by their values
                    points_labels = {'s1': s1_point, 's2': s2_point, 'e1': e1_point, 'e2': e2_point}
                    # the key parameter to the left of the = sign in the sorted() function call does not refer to the "key" part of a (key, value) pair in a dictionary.
                    # Instead, it's a named parameter of the sorted() function that specifies a function to be applied to each element in the iterable before making
                    # comparisons for sorting.
                    # The key=lambda x: x[1] part means: "For each element x in items, use x[1] (the second element of x, assuming x is a tuple or list) as the value to
                    # compare when sorting."
                    # The key here is not referring to the "key" part of the (key, value) tuples that are being sorted; it's specifying that the sorting should be based
                    #  on the value obtained from the key function applied to each element.
                    sorted_points_labels = sorted(points_labels.items(), key=lambda x: x[1])
                    sorted_labels, sorted_points = zip(*sorted_points_labels)  # Unzip the sorted pairs

                    # Append the sorted points and their corresponding labels to the chords list
                    chords.append((sorted_points, sorted_labels))

    return count, chords  # Return the total count of intersections and the list of chords

initial_value = 3.07  # Set the initial value for generating points
count, chords = find_intersections_and_chords(initial_value)  # Find intersections and chords
print(f"Total intersections found: {count}")  # Print the total number of intersections found
for sorted_points, labels in chords:  # Iterate over each chord
    print(f"Sorted Points: {sorted_points}, Labels: {labels}")  # Print the sorted points and their labels