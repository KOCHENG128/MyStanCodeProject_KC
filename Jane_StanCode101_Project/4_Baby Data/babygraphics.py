"""
File: babygraphics.py
Name: 
--------------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, this function returns the x coordinate
    of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 均分年線
    number_years = len(YEARS)
    width = CANVAS_WIDTH
    width_each_year = (width - 2 * GRAPH_MARGIN_SIZE) / (number_years - 1)
    x_coordinate = GRAPH_MARGIN_SIZE + width_each_year * year_index
    return int(x_coordinate)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # 頂部的線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH-GRAPH_MARGIN_SIZE),
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    # 底部的線
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), (CANVAS_WIDTH-GRAPH_MARGIN_SIZE),
                       (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), width=LINE_WIDTH, fill='black')

    # 垂直年線 & 年份標記
    for i in range(len(YEARS)):  # eg: i=0
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]),
                           anchor=tkinter.NW, fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for name, name_index in enumerate(lookup_names):
        # set up colors
        color = COLORS[name_index % len(lookup_names)]

        # check if target name in name_data
        if name not in name_data:
            continue

        # draw lines in each intercept
        for i in range(len(YEARS)-1):  # 13個年份，只有12條線，從x=0~x=1....x=12~x=13
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1)

            # important: must change the list into str or int data type
            year1 = str(YEARS[i])
            year2 = str(YEARS[i + 1])

            # First, check if target year exist, and find the rank
            if year1 in name_data[name]:
                rank1 = int(name_data[name][year1])
            else:
                rank1 = 1001  # if not exist

            if year2 in name_data[name]:
                rank2 = int(name_data[name][year2])
            else:
                rank2 = 1001

            # get y1, y2 coordinate and text
            if rank1 < 1000:
                y1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank1 / MAX_RANK
                text = str(name) + ' ' + str(rank1)
            else:
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                text = str(name) + ' *'

            if rank2 < 1000:
                y2 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) * rank2 / MAX_RANK
            else:
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            # Draw lines
            canvas.create_line(x1, x2, y1, y2, width=LINE_WIDTH, fill=color)
            canvas.create_text(x1 + TEXT_DX, y1, text=text,
                               anchor=tkinter.NW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
