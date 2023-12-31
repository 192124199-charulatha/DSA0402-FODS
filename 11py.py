import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1000, 1200, 1100, 1300, 1400, 1600]
plt.figure(figsize=(10, 6))  
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))  
plt.scatter(months, sales, color='g', label='Monthly Sales', marker='o')
plt.title('Monthly Sales Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6)) 
plt.bar(months, sales, color='r', label='Monthly Sales')
plt.title('Monthly Sales Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y')
plt.show()
