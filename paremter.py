snake_speed = 5  # 贪吃蛇的速度
windows_width = 800
windows_height = 600  # 游戏窗口的大小
cell_size = 20  # 贪吃蛇身体方块大小,注意身体大小必须能被窗口长宽整除

# 格子化
map_width = int(windows_width / cell_size)
map_height = int(windows_height / cell_size)

# 颜色定义
black = (0, 0, 0)  # background
dark_gray = (40, 40, 40)  # line
white = (255, 255, 255)  # map center / return button unactive
gray = (210, 210, 210)  # map edge
green = (0, 255, 0)  # snake head center / text
dark_green = (0, 155, 0)  # snake head edge
blue = (0, 0, 255)  # snake body center
dark_blue = (0, 0, 139)  # snake body edge
red = (255, 0, 0)  # food normal
light_blue = (0, 176, 240)  # food cut
orange = (255, 192, 0)  # food cross / return button active

# 游戏背景颜色
BG_COLOR = black

# 定义方向
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# 果实种类
normal = 0
cut = 1
cross = 2

# 游戏模式
break_through = 0
classic = 1
endless = 2

# 最高分函数运行模式
write = 0
read = 1

# 结束模式
dead = 0
change_map = 1

# 贪吃蛇头部下标
HEAD = 0
