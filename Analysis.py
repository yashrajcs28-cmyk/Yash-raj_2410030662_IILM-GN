import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

print("===== Student Data =====")
print(data)

# Calculate total marks
data["Total"] = data["Maths"] + data["Science"] + data["English"]

# Calculate average marks
print("\n===== Average Marks =====")
print(data[["Maths", "Science", "English"]].mean())

# Find topper
topper = data.loc[data["Total"].idxmax()]

print("\n===== Topper Details =====")
print(topper)

# Save updated file
data.to_csv("updated_data.csv", index=False)

print("\nUpdated data saved as 'updated_data.csv'")
