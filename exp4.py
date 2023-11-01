color = ["red","red","red","yellow","yellow","yellow","yellow","yellow","red","red"]
type = ["sports","sports","sports","sports","sports","suv","suv","suv","suv","sports"]
origin = ["domestic","domestic","domestic","domestic","imported","imported","imported","domestic","imported","imported"]
stolen = ["yes","no","yes","no","yes","no","yes","no","no","yes"]
data_set=10
stole = 0
notstole =0
for i in range(data_set):
    if stolen[i]=="yes":
        stole+=1
        sp=stole/data_set
    else:
        notstole+=1
        np=notstole/data_set
print("Probability of stolen:- ",stole,"/",data_set," or ",sp)
print("Probability of not stolen:- ",notstole,"/",data_set," or ",np)

x1=input("Enter the colour:- ")
x2 = input("Enter the type:- ")
x3 = input("Enter the origin:- ")

val=0
if x1=="red":
    for i in range(data_set):
        if color[i] == "red" and stolen[i] == "yes":
            val+=1
    prob1 = val/stole
    print ("Probability of red nd stolen is :- ",prob1," or ",val,"/",stole)

elif x2 == "yellow":
    for i in range(data_set):
        if color[i]=="yellow" and stolen[i] == "yes":
            val+=1
    prob1 = val/stole
    print("Probability of yellow and stolen is :- ",prob1," or ",val,"/",stole)

else:
    print("Inavlid color")

val=0
if x2=="suv":
    for i in range(data_set):
        if type[i]=="suv" and stolen[i]=="yes":
            val+=1
    prob2=val/stole
    print("Probability of suv and stolen is:- ",prob2," or ",val,"/",stole)

elif x2=="sports":
    for i in range(data_set):
        if type[i]=="sports" and stolen[i]=="yes":
            val+=1
    prob2=val/stole
    print("Probability of stolen and sports is :- ",prob2," or ",val,"/",stole)

else:
    print("invalid")

val=0
if x3=="domestic":
    for i in range(data_set):
        if origin[i]=="domestic" and stolen[i]=="yes":
            val+=1
    prob3 = val/stole
    print("Probabilty of domestic and stolen is :- ",prob3," or ",val,"/",stole)

elif x3=="imported":
    for i in range(data_set):
        if origin[i]=="imported" and stolen[i]=="yes":
            val+=1
    prob3=val/stole
    print("Probability of imported and stolen is :- ",prob3," or ",val,"/",stole)

else:
    print("invalid")

val=0
if x1=="red":
    for i in range(data_set):
        if color[i]=="red" and stolen[i]=="no":
            val+=1
    prob4=val/notstole
    print("Probability of red and not stolen is:- ",prob4," or ",val,"/",notstole)

elif x1=="yellow":
    for i in range(data_set):
        if color[i]=="yellow" and stolen[i]=="no":
            val+=1
    prob4=val/notstole
    print("Probability of yellow and not stole is:- ",prob4," or ",val,"/",notstole)

else:
    print("invalid")

val=0
if x2=="suv":
    for i in range(data_set):
        if type[i]=="suv" and stolen[i]=="no": 
            val+=1
    prob5=val/notstole
    print("Probability of suv and not stolen is :- ",prob5," or ",val,"/",notstole)

elif x2=="sports":
    for i in range(data_set):
        if type[i]=="sports" and stolen[i]=="no":
            val+=1
    prob5=val/notstole
    print("Probability of sports and not stolen is :- ",prob5," or ",val,"/",notstole )

else:
    print("invalid")

val=0
if x3=="domestic":
    for i in range(data_set):
        if origin[i]=="domestic" and stolen[i]=="no":
            val+=1
    prob6=val/notstole
    print("Probability of domestic and not stolen is :- ",prob6," or ",val,"/",notstole)

elif x3=="imported":
    for i in range(data_set):
        if origin[i]=="imported" and stolen[i]=="no":
            val+=1
    prob6=val/notstole
    print("Probability of imported and not stole is:- ",prob6," or ",val,"/",notstole)
else:
    print("invalid")

pc1=prob1*prob2*prob3*sp
pc2=prob4*prob5*prob6*np

if pc1>pc2:
    print("stolen")
else:
    print("not stolen")