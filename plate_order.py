import re

count = 1
cols="ABCDEFGH"
rows=list(range(1,13))
position={}

for i in range(12):
  for j in range(8):
    position[str(rows[i])+cols[j]]=str(count)
    count+=1
    
pattern = re.compile('_\d+[A-H]_') #for efficient downstream
