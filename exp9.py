# Function to take user input for transactions
def get_user_transactions():
    transactions = []
    while True:
        transaction = input("Enter items for a transaction (comma-separated), or 'done' to finish: ").strip()
        if transaction.lower() == 'done':
            break
        items = transaction.split(", ")
        transactions.append(set(items))
    return transactions

# Function to generate frequent item sets using Apriori
def generate_frequent_item_sets(transactions, min_support):
    from collections import defaultdict
    from itertools import combinations

    item_counts = defaultdict(int)

    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

    def is_frequent(itemset):
        support = item_counts[itemset[0]]
        for item in itemset[1:]:
            support = min(support, item_counts[item])
        return support >= min_support

    def generate_candidates(itemsets, k):
        candidates = set()
        for itemset in itemsets:
            for item in item_counts.keys():
                new_set = tuple(sorted(set(itemset) | {item}))
                if len(new_set) == k and is_frequent(new_set):
                    candidates.add(new_set)
        return candidates

    k = 1
    frequent_itemsets = [(item,) for item in item_counts.keys() if is_frequent([item], item_counts)]

    while frequent_itemsets:
        k += 1
        candidates = generate_candidates(frequent_itemsets, k)
        frequent_itemsets = [itemset for itemset in candidates if is_frequent(itemset)]
        yield frequent_itemsets

min_support = int(input("Enter the minimum support threshold: "))
user_transactions = get_user_transactions()

frequent_item_sets = list(generate_frequent_item_sets(user_transactions, min_support))

print("Frequent Buying Patterns:")
for itemsets in frequent_item_sets:
    for itemset in itemsets:
        print(sorted(itemset))
