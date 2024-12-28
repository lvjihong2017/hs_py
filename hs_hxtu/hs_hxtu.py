import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建一个新的图形
fig, ax = plt.subplots()

# 创建一个直径为20米的圆
circle_radius = 10  # 半径为10米
circle = plt.Circle((0, 0), circle_radius, color='blue', fill=False)

# 添加圆到图形中
ax.add_patch(circle)

# 创建长20米、宽1米的长方形
rectangle_width = 20
rectangle_height = 1

# 计算圆内可以放置的长方形的数量
num_rectangles = int(circle_radius * 2 / (rectangle_height + 1))  # 每个长方形之间间隔1米

# 计算第一个长方形的中心坐标
x = 0
y = 0

# 放置多个长方形
for i in range(num_rectangles):
    rectangle = patches.Rectangle((x - rectangle_width / 2, y - rectangle_height / 2), rectangle_width,
                                  rectangle_height, color='red')
    ax.add_patch(rectangle)
    y = y + rectangle_height + 1  # 下一个长方形的y坐标向上偏移1米

y = 0
# 放置多个长方形
for i in range(num_rectangles):
    rectangle = patches.Rectangle((x - rectangle_width / 2, y - rectangle_height / 2), rectangle_width,
                                  rectangle_height, color='red')
    ax.add_patch(rectangle)
    y = y - rectangle_height - 1  # 下一个长方形的y坐标向上偏移1米

# 设置图形的坐标轴范围
ax.set_xlim(-circle_radius - 1, circle_radius + 1)
ax.set_ylim(-circle_radius - 1, circle_radius + 1)

# 显示图形
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
