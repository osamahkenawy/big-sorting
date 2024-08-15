
# Big Sorting

This Python script solves the "Big Sorting" problem, where the goal is to sort a list of large numbers given as strings. The challenge is to sort these numbers in ascending order based on their numeric value.

## Problem Description

Given a list of large numbers (represented as strings), sort them in ascending order. The numbers are so large that they cannot be handled by standard integer types in some programming languages, so the sorting must be done directly on the strings.

### Input

- The first line contains an integer `n`, the number of numbers.
- The second line contains `n` space-separated numbers as strings.

### Output

- Print the numbers in ascending order, each on a new line.

## Implementation

The `bigSorting` function takes a list of strings `unsorted` as input and returns a list of strings sorted by their numeric values.

### Example

```python
def bigSorting(unsorted):
    sorted_list = sorted(unsorted, key=lambda x: (len(x), x))
    return sorted_list

# Example usage:
n = int(input())  # Number of strings
unsorted = input().strip().split()  # Split input line into a list of strings
sorted_list = bigSorting(unsorted)
print("
".join(sorted_list))
```

### Explanation

1. **Sorting by Length and Lexicographically:**
   - The list is sorted by the length of the strings first, ensuring that shorter numbers come before longer ones.
   - For numbers with the same length, they are sorted lexicographically (which works because they have the same number of digits).

2. **Lambda Function:**
   - `key=lambda x: (len(x), x)` is a custom sorting key using a lambda function.
   - A **lambda function** is an anonymous, one-line function defined using the `lambda` keyword. Here, `lambda x: (len(x), x)` takes a string `x` and returns a tuple `(len(x), x)`:
     - `len(x)` sorts the strings by their length.
     - `x` sorts the strings lexicographically if their lengths are the same.

3. **Input Handling:**
   - The input numbers are read as a single line, split into individual strings, and then sorted.

### Usage

To use this function, input your numbers as a space-separated string, and call the `bigSorting` function:

```python
n = int(input())  # Number of strings
unsorted = input().strip().split()  # Split input line into a list of strings
sorted_list = bigSorting(unsorted)
print("
".join(sorted_list))
```

### Output

For the input:

```
6
31415926535897932384626433832795 1 3 10 3 5
```

The output will be:

```
1
3
3
5
10
31415926535897932384626433832795
```