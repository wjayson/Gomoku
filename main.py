import tkinter  as tk
from itertools import groupby
import sys


board=[]
# 创建主窗口
type=0
root = tk.Tk()
root.geometry("500x500")
# 设置窗口标题
root.title("Tkinter 示例")
canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
canvas.pack()
state=1
draws=0
# 设置窗口大小
def on_mouse_click(event):
    global board, state

    """处理鼠标点击事件，返回点击的坐标"""
    x, y = event.x, event.y
    x=x//20*20
    y=y//20*20

    if [(x/10)-10,(y/10)-10,0] in board:
        new=[[(x/10)-10,(y/10)-10,state]]
        board.remove([(x/10)-10,(y/10)-10,0])
        board.append([(x/10)-10,(y/10)-10,state])
        if state == 1:
            state = 2
        else:
            state = 1
        #print (new)
        #print(board)
        draw(new)
        eliminate(board)
    #print(x,y)

# 绑定鼠标点击事件
root.bind("<Button-1>", on_mouse_click)  # 左键点击
root.bind("<Button-3>", on_mouse_click)
#运行主循环

def eliminate_x(board):
    global type
    arr = sorted(board, key=lambda sub: (sub[1], sub[0]))
    groups = []
    current_group = [arr[0]]  # 初始化第一组
    # 遍历数组
    for i in range(1, len(arr)):
        if arr[i][2] == arr[i - 1][2] and arr[i][2]!=0:
            current_group.append(arr[i])  # 当前元素加入当前组
        else:
            if len(current_group) >= 5:  # 如果当前组满足长度条件，保存
                groups.append(current_group)
            current_group = [arr[i]]  # 开始新组
    # 检查最后一组
    if len(current_group) >= 5:
        groups.append(current_group)
    if groups!=[]:
        type = groups[0][0][2]
        return True



def eliminate_y(board):
    global type
    arr = sorted(board, key=lambda sub: (sub[0], sub[1]))
    groups = []
    current_group = [arr[0]]  # 初始化第一组
    # 遍历数组
    for i in range(1, len(arr)):
        if arr[i][2] == arr[i - 1][2] and arr[i][2]!=0:
            current_group.append(arr[i])  # 当前元素加入当前组
        else:
            if len(current_group) >= 5:  # 如果当前组满足长度条件，保存
                groups.append(current_group)
            current_group = [arr[i]]  # 开始新组
    # 检查最后一组
    if len(current_group) >= 5:
        groups.append(current_group)
    if groups!=[]:
        type=groups[0][0][2]
        return True

def eliminate(board):
    if eliminate_x(board) or eliminate_y(board):
        print(type)
        sys.exit()

def draw(board):
    global draws
    if draws==0:
        canvas.create_line(100, 100, 100, 100+ 320, fill="black")
        canvas.create_line(100, 100, 100+320, 100, fill="black")
        draws=1
    for i in range(len(board)):
        x = board[i][0] + 10
        y = board[i][1] + 10
        if board[i][2]!=0:
            x=board[i][0]+10
            y=board[i][1]+10
            if board[i][2]==1:
                canvas.create_oval(10*x, 10*y, 10*x+15, 10*y+15, fill="black", outline="black")
            if board[i][2]==2:
                canvas.create_oval(10 * x, 10 * y, 10 * x + 15, 10 * y + 15, fill="red", outline="red")
        canvas.create_line(10*x+18,10*y,10*x+18,10*y+20,fill="black")
        canvas.create_line(10*x, 10*y+18, 10*x+20, 10*y + 18, fill="black")
def spawn():
    global board

    for y in range(0,32,2):
        for x in range(0,32,2):
            a=[x,y,0]
            board.append(a)

    draw(board)
    #print (board)

spawn()

root.mainloop()


