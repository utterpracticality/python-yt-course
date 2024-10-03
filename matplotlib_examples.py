

# Simple line plot
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a simple line plot with grid
plt.plot(x, y)
# plt.grid()  # Adds grid lines
plt.title("Plot with Grid")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# plt.savefig("/Users/call/Documents/python_essentials_udemy/mat plot lib/myfigure.png")
plt.show()




# Bar Chart
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create a bar chart
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Scatter Plot
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 12, 11, 15]

# Create a scatter plot
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Pie Chart
import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 30, 15, 10]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Programming Language Popularity")
plt.grid()
plt.show()


# Animate a sin wave
# Matplotlib can be combined with other libraries like NumPy and Pandas for advanced plotting
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

ani = FuncAnimation(fig, update, frames=range(100), interval=50)
plt.title("Interactive Sine Wave Animation")
plt.xlabel("X-axis")
plt.ylabel("Amplitude")
plt.show()
