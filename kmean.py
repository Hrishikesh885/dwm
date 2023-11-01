import random

# Take user input for the cluster
cluster = input("Enter a list of numbers separated by spaces: ").split()
cluster = [int(c) for c in cluster]

m1 = random.choice(cluster)
m2 = random.choice(cluster)

prem1 = 0
prem2 = 0

k1 = []
k2 = []

def newmean(cluster, m1, m2):
    k1.clear()
    k2.clear()
    for c in cluster:
        if abs(m1 - c) < abs(m2 - c):
            k1.append(c)
        else:
            k2.append(c)

def submission(clus):
    if len(clus) == 0:
        return 0
    total = sum(clus)
    return total / len(clus)

iteration = 0

while prem1 != m1 and prem2 != m2:
    prem1 = m1
    prem2 = m2
    newmean(cluster, m1, m2)
    m1 = submission(k1)
    m2 = submission(k2)
    print(f'Iteration {iteration}: m1={m1}, m2={m2}')
    print(f'k1={k1}')
    print(f'k2={k2}')
    iteration += 1

print("Final m1 and m2:", float(m1), "  and  ", float(m2))
print(k1)
print(k2)
