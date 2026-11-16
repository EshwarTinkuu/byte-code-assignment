import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales = [120, 150, 180, 140, 200, 250]
expenses = [80, 100, 120, 90, 150, 170]
profit = [40, 50, 60, 50, 50, 80]
customers = [50, 60, 75, 65, 90, 110]
orders = [35, 45, 50, 40, 65, 80]

fig, ax = plt.subplots(2, 3, figsize=(15, 9))


ax[0, 0].plot(months, sales, marker='v')
ax[0, 0].set_title("Line Chart - Sales")


ax[0, 1].bar(months, expenses)
ax[0, 1].set_title("Bar Chart - Expenses")


ax[0, 2].pie(sales, labels=months, autopct='%1.1f%%')
ax[0, 2].set_title("Pie Chart - Sales")


ax[1, 0].barh(months, profit)
ax[1, 0].set_title("Horizontal Bar - Profit")

ax[1, 1].scatter(customers, sales)
ax[1, 1].set_title("Scatter Plot - Customers vs Sales")


ax[1, 2].boxplot(orders)
ax[1, 2].set_title("Box Plot - Orders")

plt.tight_layout()
plt.show()