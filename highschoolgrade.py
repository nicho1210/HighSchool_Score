import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('high_score.csv')
plt.plot(dataset.grade,dataset.overall , 'r', label='ALL')
plt.plot(dataset.grade,dataset.math_score , 'cornflowerblue', label='Math')
plt.plot(dataset.grade,dataset.physics_score , 'b', label='Physics')
plt.plot(dataset.grade,dataset.english_score , 'g', label='English')
plt.plot(dataset.grade,dataset.computer_score , 'y', label='Computer')
plt.plot(dataset.grade,dataset.chinese_score , 'm', label='Chinese')
plt.xlabel('semester')
plt.ylabel('percentage(%)')
plt.title('score')
plt.legend()
plt.show()
