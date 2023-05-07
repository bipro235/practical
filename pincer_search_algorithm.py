def pincer_search(transactions, min_support):
    # Create a dictionary of items with their frequency
    item_frequency = {}
    for transaction in transactions:
        for item in transaction:
            if item in item_frequency:
                item_frequency[item] += 1
            else:
                item_frequency[item] = 1

    # Remove items that do not meet minimum support
    items = set(item for item in item_frequency if item_frequency[item] >= min_support)

    # Sort items by frequency
    sorted_items = sorted(items, key=lambda item: (-item_frequency[item], item))

    # Create a list of frequent sets
    frequent_sets = []
    for i, item in enumerate(sorted_items):
        # Create a new frequent set containing only this item
        frequent_set = [item]

        # Add other items to the frequent set
        for j in range(i + 1, len(sorted_items)):
            other_item = sorted_items[j]
            if pincer_search_join(frequent_set, other_item):
                frequent_set.append(other_item)

        # Add the frequent set to the list of frequent sets
        frequent_sets.append(frequent_set)

    return frequent_sets

def pincer_search_join(frequent_set, other_item):
    # Check if adding other_item to frequent_set would result in a valid frequent set
    for i in range(len(frequent_set)):
        if not pincer_search_subset(frequent_set[:i] + frequent_set[i + 1:], other_item):
            return False

    return True

def pincer_search_subset(s, t):
    # Check if s is a subset of t
    i = 0
    for x in s:
        while i < len(t) and x != t[i]:
            i += 1
        if i == len(t):
            return False
        i += 1
    return True

transactions = [
    [1, 2, 3],
    [1, 2],
    [2, 3],
    [1, 3],
    [2],
]

min_support = 2

frequent_sets = pincer_search(transactions, min_support)

print(frequent_sets)