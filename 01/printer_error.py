import re
s="aaaxbbbbyyhwawiwjjjwwm"
x = re.findall("[^a-m]", s)
all = [i for i in s]
print(str(len(x))+'/'+str(len(all)))