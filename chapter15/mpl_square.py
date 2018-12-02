import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25];
plt.plot(squares, linewidth=5)

# 设置标题
plt.title("Squares Number", fontsize=24)

# X轴加上Label
plt.xlabel("Value", fontsize=14)

# Y轴加上Label
plt.ylabel("Squares Number", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

plt.show()
