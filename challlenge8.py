import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
def generate_data(n):
    data = []
    for i in range(1, n+1):
        m = random.randint(0, 100)
        a = random.randint(0, 100)
        ass = random.randint(0, 50)
        p = math.sqrt(m * ass) + (a / 2)
        data.append((i, m, a, ass, p))
    return data
def classify_students(data):
    d = {"At Risk": [], "Average": [], "Good": [], "Top Performer": []}
    for x in data:
        id, m, a, _, _ = x
        if m < 40 or a < 50:
            d["At Risk"].append(id)
        elif m <= 70:
            d["Average"].append(id)
        elif m <= 90:
            d["Good"].append(id)
        elif m > 90 and a > 80:
            d["Top Performer"].append(id)

    return d
def analyze_data(data):
    df = pd.DataFrame(data,
        columns=["ID","Marks","Attendance","Assignment","Perf_Index"])
    marks = df["Marks"]
    mean = sum(marks) / len(marks)
    median = np.median(marks)
    std = np.std(marks)
    max_m = max(marks)
    corr = np.corrcoef(df["Marks"], df["Attendance"])[0][1]
    df["Normalized"] = [(x - min(marks)) / (max(marks) - min(marks)) for x in marks]
    unique_marks = set(marks)
    top_performers = df[(df["Marks"] > 90) & (df["Attendance"] > 80)]
    if std < 15 and len(top_performers) >= 2:
        insight = "Stable Academic System"
    elif len(df[df["Attendance"] < 50]) > 3:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"

    return df, mean, median, std, max_m, corr, insight
digit = int(input("Enter your roll number last digit: "))
n = 10 + (digit ** 2)
data = generate_data(n)
cat = classify_students(data)
df, mean, median, std, max_m, corr, insight = analyze_data(data)
print(df)
print(cat)
print(mean, median, std, corr)
print((mean, std, max_m))
print(insight)
plt.hist(df["Marks"])
plt.show()