Emplsal={"name":["Aneeja", "Anaya", "AnnMary", "Ankita"], "Salary":[12000, 10000, 20000, 25000]}
for i in range(len(Emplsal["name"])):
    name=Emplsal["name"][i]
    sal=Emplsal["Salary"][i]
    if sal>15000:
        print(f"{name} has {sal} salary")
