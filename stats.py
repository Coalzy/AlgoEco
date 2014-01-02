import sys
import math

with open('avg_balance.csv') as f:
  contents = f.readlines()

strippedcontent = []
traders = {}

for content in contents:
  strippedcontent.append(content.replace(' ','').split(','))
  
  
for i in range(2, len(strippedcontent[0])-3):
  if (((i-2)%6) == 0):
    traders[strippedcontent[0][i]] = float(strippedcontent[0][i+4])
    
for i in range(1, len(strippedcontent)):
  for j in range(2, len(strippedcontent[i])-3):
    if (((j-2)%6) == 0):
      traders[strippedcontent[i][j]] += float(strippedcontent[i][j+4])
      
for k,v in traders.iteritems():
  traders[k] = v/len(strippedcontent)
  print('Avg profit for %s: %f'%(k,traders[k]))
    
#print traders