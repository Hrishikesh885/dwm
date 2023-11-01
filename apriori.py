from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Collect transaction data from the user
num_transactions = int(input("Enter the number of transactions: "))
transactions = []

for i in range(1, num_transactions + 1):
    transaction = input(f"Enter items for Transaction {i} (comma-separated): ").split(',')
    transactions.append(transaction)

data = {'TransactionID': list(range(1, num_transactions + 1)),
        'Items': transactions}

df = pd.DataFrame(data)

# One-hot encoding
oht = df['Items'].str.join('|').str.get_dummies()

# Convert confidence and support percentages to proportions
min_support_percent = float(input("Enter the minimum support percentage (e.g., 20%): ")) / 100
min_confidence_percent = float(input("Enter the minimum confidence percentage (e.g., 50%): ")) / 100

# Apply the Apriori algorithm to find frequent item sets
frequent_itemsets = apriori(oht, min_support=min_support_percent, use_colnames=True)

if frequent_itemsets.empty:
    print("No frequent itemsets found.")
else:
    # Generate association rules
    association_rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_confidence_percent)
    
    if association_rules.empty:
        print("No association rules found.")
    else:
        print("Frequent Item Sets:")
        print(frequent_itemsets)

        print("\nAssociation Rules:")
        print(association_rules)
