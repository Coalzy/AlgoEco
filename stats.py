import sys
import math
import operator

with open('avg_balance.csv') as f:
  contents = f.readlines()

strippedcontent = []
profit = {}
trades = {}
nontrades = {}

for content in contents:
  strippedcontent.append(content.replace(' ','').split(','))
  
parameters = 7
profitloc = 4
tradesloc = 5
nontradesloc = 6

for i in range(2, len(strippedcontent[0])-3):
  if (((i-2)%parameters) == 0):
    profit[strippedcontent[0][i]] = float(strippedcontent[0][i+profitloc])
    trades[strippedcontent[0][i]] = float(strippedcontent[0][i+tradesloc])
    nontrades[strippedcontent[0][i]] = float(strippedcontent[0][i+nontradesloc])
    
for i in range(1, len(strippedcontent)):
  for j in range(2, len(strippedcontent[i])-3):
    if (((j-2)%parameters) == 0):
      profit[strippedcontent[i][j]] += float(strippedcontent[i][j+profitloc])
      trades[strippedcontent[i][j]] += float(strippedcontent[i][j+tradesloc])
      nontrades[strippedcontent[i][j]] += float(strippedcontent[i][j+nontradesloc])
      
for k,v in profit.iteritems():
  profit[k] = v/len(strippedcontent)
  
for k,v in trades.iteritems():
  trades[k] = v/len(strippedcontent)
  
for k,v in nontrades.iteritems():
  nontrades[k] = v/len(strippedcontent)
  
sorted_profit = sorted(profit.iteritems(), key=operator.itemgetter(1), reverse=True)

print('      PROFIT  TRADES  MISSED')
  
for k in sorted_profit:
  print('%4s %7.2f %7.2f %7.2f'%(k[0],k[1],trades[k[0]],nontrades[k[0]]))
    
#print profit