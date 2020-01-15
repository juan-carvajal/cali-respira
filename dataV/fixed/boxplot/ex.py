import  numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.randn(10000)
ax = sns.distplot(x, hist_kws=dict(edgecolor="k", linewidth=2))
plt.show()