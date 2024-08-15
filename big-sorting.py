def bigSorting(unsorted):
    sorted_list = sorted(unsorted, key=lambda x: (len(x), x))
    return sorted_list


# Example usage:
n = int(input())  # Number of strings
unsorted = input().strip().split()  # Split input line into a list of strings
sorted_list = bigSorting(unsorted)
print("\n".join(sorted_list))