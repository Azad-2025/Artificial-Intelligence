import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [22, 24, 21, 23, 25, 26, 20]
plt.plot(days, temperatures, marker='o')
plt.title("Temperature Variations Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()