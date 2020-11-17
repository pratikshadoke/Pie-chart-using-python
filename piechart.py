import matplotlib.pyplot as plt
import pandas as pd
user_list=pd.read_csv("user-languages.csv")
user_list=user_list[['java',"c++","c#","python","javascript","kotlin"]].sum()
label_legend= ["java", "c++",
              "c#",
              "python",
              "javascript",
              "kotlin"]
slices = [2,3,2,8,7,1]
colors = ['r', 'cyan', 'yellow', 'b','orange','pink']

plt.pie(slices, labels = label_legend, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.0, 0.2,0.0,0.0),
        radius = 1.2, autopct = '%1.1f%%')
plt.legend(loc='lower right')
plt.show()

