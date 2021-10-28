import matplotlib.pyplot as plt
with open('population.json', encoding= 'ascii') as f:
    text = f.read()
import json
population= json.loads(text)

x = []
for index in population[1]:
    x.append(index['date'])

y = []
for index in population[1]:
    y.append(index["value"])

plt.figure(figsize= (15,6))
plt.bar(x,y, color= "#444444")
plt.xticks(rotation = 90)

plt.title("Population Of India over the Years")
plt.xlabel("Year")
plt.ylabel("Population")
spacing = 0.100

plt.subplots_adjust(bottom=spacing)

plt.tick_params(axis='x', which= 'major', labelsize= 10)

plt.tight_layout()

plt.show()
plt.legend(4,1)






