from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt


var = pd.read_excel("graph.xlsx")
print(var)

x = list(var['Iteration'])
y = list(var['score'])

x2 = list(var['Iteration1'])
y2 = list(var['score1'])

plt.figure(figsize=(9,9))
plt.style.use('seaborn')
plt.plot(x,y,label ='SARSA')
plt.plot(x2,y2, label = 'Q-Learning')
plt.title("agents performance comparison")
plt.xlabel('Iteration')
plt.ylabel('Scores')
plt.legend()
plt.show()