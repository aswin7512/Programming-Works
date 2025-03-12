import matplotlib.pyplot as plt

# Data
x = []
y = []
for i in range(1,30):
    a = input(f"Enter the date for day {i} (e.g., '2024-04-{i}'): ")  # Input date
    x.append(a)
    b = int(input(f"Enter the humidity for day {i}: "))  # Input humidity
    y.append(b)

# Create a scatter plot
plt.scatter(x, y, color="red", label="Humidity Data")

# Connect points with a line
plt.plot(x, y, color="blue", linestyle="-", label="Line Connecting Points")

plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.title('Humidity Scatter Plot with Connecting Line')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.yticks(range(0, max(y) + 1, 5))  # Set y-axis ticks to increment by 5
plt.show()
