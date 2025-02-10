import matplotlib.pyplot as plt
regions = ["North", "South", "East", "West"]
revenue = [50000, 60000, 45000, 70000]
plt.bar(regions, revenue, color='skyblue')
plt.title("Sales Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue ($)")
plt.show()