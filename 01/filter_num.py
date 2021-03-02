ls = [1,2,'a','b']
lst = [int(i) if i.isdigit() else i for i in ls ] 

print(lst)