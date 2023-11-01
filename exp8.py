import numpy as np
data=input("Enter list of data points seperated by space")
data=list(map(float,data.split()))
data.sort()
n=int(input("Enter the number of intervals: "))
dn=len(data)
bin_size=dn//n
extra_items=dn%n
bins=[]

start=0
for i in range(n):
    end=start+bin_size
    if i < extra_items:
        end+=1
    bin_data=data[start:end]
    bins.append(bin_data)
    start=end

print("Partition in equi depth bins: " )
for i,bin_data in enumerate(bins):
    print(f"Bin{i+1}:{bin_data}")

print("Smooth the data by bin mean: ")
for i,bin in enumerate(bins):
    bin_mean=np.mean(bin)
    smoothed_bin=[bin_mean]*len(bin)
    print(f"Bin{i+1}:{smoothed_bin}")

print("Smoothed by bin boundary: ")
for i,bin in enumerate(bins):
    bin_min=min(bin)
    bin_max=max(bin)
    smoothed_bin=[bin_min if abs(x-bin_min)<= abs(x-bin_max) else bin_max for x in bin] 
    print(f"Bin {i+1}:{smoothed_bin}")

print("Smoothed by bin median")
for i,bin in enumerate(bins):
    bin_median=np.median(bin)
    smoothed_bin=[bin_median]*len(bin)
    print(f"Bin{i+1}:{smoothed_bin}")