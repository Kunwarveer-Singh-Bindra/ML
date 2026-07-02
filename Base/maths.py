import pandas as pd
import numpy as np
import statistics
import seaborn as sns
import matplotlib.pyplot as plt

dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10, 13, 12, 14, 12, 108, 12, 11, 14, 13, 15, 10, 15, 12, 10, 14, 13, 15, 10]
outliers = []

def interquartile_range(data):
    ds = data
    ds.sort()
    q1 = np.percentile(ds, 25)
    q3 = np.percentile(ds, 75)
    iqr = q3 - q1
    lower_fence = q1-(1.5 * iqr)
    upper_fence = q3+(1.5 * iqr)
    sns.boxplot(ds, orient = 'h')
    plt.show()
    for i in ds:
        if i < lower_fence or i > upper_fence:
            outliers.append(i)
    return outliers

def remove_outlier(data, outliers):
    for i in outliers:
        data.remove(i)
    sns.boxplot(data, orient = 'h')
    plt.show()
    return data


outlier = interquartile_range(dataset)
print(remove_outlier(dataset, outlier))
