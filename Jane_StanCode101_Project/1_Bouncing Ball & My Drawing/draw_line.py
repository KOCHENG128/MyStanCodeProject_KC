"""
File: Draw Line
Name: Jane Huang
-------------------------
TODO: This program draws lines by clicking on the window
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant
SIZE = 10

# Global Variables
previous_click_count = 0
window = GWindow()
start_x = 0
start_y = 0
start = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_a_line)


def draw_a_line(mouse):
    global previous_click_count, start_x, start_y, start  # 為什麼把一個東西設為global 後，他不會抓初始值，會抓新的值?
    if previous_click_count % 2 == 0:  # 表示這次是第奇數次點擊
        # store the start point
        start_x = mouse.x - SIZE / 2
        start_y = mouse.y - SIZE / 2
        # make a hallow circle at start
        start = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        start.fill_color = False  # hallow circle
        start.color = 'black'
        window.add(start)
        previous_click_count += 1
    elif previous_click_count % 2 == 1:  # 表示這次是第偶數次點擊
        end = GLine(start_x, start_y, mouse.x-SIZE/2, mouse.y-SIZE/2)
        end.color = 'black'
        window.add(end)
        window.remove(start)
        previous_click_count += 1


if __name__ == "__main__":
    main()
