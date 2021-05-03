"""
Name: 李佳謙 Chiachien Li
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE+year_index*((width-2*GRAPH_MARGIN_SIZE)//len(YEARS))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Draw the upper and lower border of the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # Draw all the vertical lines and text for each year
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


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

    # Write your code below this line
    #################################
    # The index of COLOR list
    color_index = 0
    # Check all the names in lookup_names list
    for name in lookup_names:
        # Draw the lines between each year in YEARS list
        for year in YEARS:
            # Draw lines between the year and year+10 except for 2010
            if int(year) < 2010:
                # Coordinate x for two points
                point1_x = get_x_coordinate(CANVAS_WIDTH, (int(year) - 1900) // 10)
                point2_x = point1_x + (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
                # The name is in top 1000 for the year
                if str(year) in name_data[name]:
                    point1_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(year)]) * (
                                (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000)
                    # The name is in top 1000 for the year+10
                    if str(int(year)+10) in name_data[name]:
                        point2_y = GRAPH_MARGIN_SIZE +\
                                   int(name_data[name][str(int(year)+10)])*((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000)
                    # The name is out of top 1000 for the year+10
                    else:
                        point2_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_line(point1_x, point1_y, point2_x, point2_y, fill=COLORS[color_index % 4], width=LINE_WIDTH)
                    canvas.create_text(point1_x + TEXT_DX, point1_y, anchor=tkinter.SW,
                                       text=str(name + ' ' + name_data[name][str(year)]), fill=COLORS[color_index % 4])
                # The name is out of top 1000 for the year
                else:
                    point1_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    # The name is in top 1000 for the year+10
                    if str(int(year)+10) in name_data[name]:
                        point2_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(int(year) + 10)]) * (
                                    (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000)
                    # The name is out of top 1000 for the year+10
                    else:
                        point2_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_line(point1_x, point1_y, point2_x, point2_y,
                                       fill=COLORS[color_index % 4], width=LINE_WIDTH)
                    canvas.create_text(point1_x + TEXT_DX, point1_y, anchor=tkinter.SW,
                                       text=str(name+' *'), fill=COLORS[color_index % 4])
            # Add the text for 2010
            else:
                point1_x = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)
                # The name is in the top 1000 for the year
                if str(year) in name_data[name]:
                    point1_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(year)]) * (
                            (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000)
                    canvas.create_text(point1_x + TEXT_DX, point1_y, anchor=tkinter.SW,
                                       text=str(name + ' ' + name_data[name][str(year)]), fill=COLORS[color_index % 4])
                # The name is out of top 1000 for the year
                else:
                    point1_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(point1_x + TEXT_DX, point1_y, anchor=tkinter.SW,
                                       text=str(name + ' *'), fill=COLORS[color_index % 4])
        color_index += 1


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
