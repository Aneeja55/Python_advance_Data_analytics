dict_={}
keys=[]
i=0
with open("emp.csv","r") as f:
    data=f.readlines()
headers=data[0].strip().split(",")
dict_ ={h: [] for h in headers}
for line in data[1:]:
    values=line.strip().split(",")
    for key, value in zip(headers,values):
        dict_[key].append(value)
print(dict_)