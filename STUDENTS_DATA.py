import pandas as pd
df=pd.read_csv("students.csv")
print(df.head())
print(df.shape)
print(df[["name","GPA"]])
print(df[df["GPA"]>=3.5])
print(df.sort_values("GPA",ascending=False))
print(df.groupby("major")["GPA"].mean())

s = pd.read_csv("students.csv")
c = pd.read_csv("scores.csv")

print(s.isna().sum())
print(c.isna().sum())

s["age"] = s["age"].fillna(s["age"].median())
s["GPA"] = s["GPA"].fillna(s.groupby("major")["GPA"].transform("mean"))
for col in ["python", "math", "database"]:
    c[col] = c[col].fillna(c[col].mean())
m = s.merge(c, on="student_id")
m["avg_score"] = m[["python", "math", "database"]].mean(axis=1)
print(m.nlargest(5, "avg_score")[["student_id", "name", "major", "avg_score"]])
print(m.groupby("major")["avg_score"].mean().round(2))
