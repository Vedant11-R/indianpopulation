import matplotlib.pyplot as plt
with open('gdp.json', encoding= 'ascii') as f:
    text = f.read()
import json
gdp= json.loads(text)
with open('population.json', encoding= 'ascii') as f1:
    text1 = f1.read()
#import json
population= json.loads(text1)

x1 = []
for index in gdp[1]:
    x1.append(index['date'])

y1 = []
for index in gdp[1]:
    y1.append(index["value"])
x2 = []
for index in population[1]:
    x2.append(index["date"])
y2 = []
for index in population[1]:
    y2.append(index["value"])      
#print(z)
plt.figure(figsize= (15,6))
plt.plot(x1,y1, color= "blue",label = "gdp")
plt.plot(x2,y2, color= "red",label = "population")         
plt.xticks(rotation = 90)

plt.title("Population vs gdp")
plt.xlabel("Year")
plt.ylabel("value")
plt.legend()
plt.show()