# # import streamlit as st
# # from polymino import Grid,generate_polyminoes,generate_polymino_positions,unique_grids
# # from dlx import DLX
# # from hexa_rotation_flip import P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13
# # from itertools import product
# # from svgwrite import Drawing,text
# # import numpy as np  

# # st.title("Shatkon Paheli Level-3")

# # def solutions_svg(solutions, filename, columns=1, size=5, padding=10,
# #                   colour=lambda _: "white",stroke_colour="black",
# #                   stroke_width=10, empty=' '):
# #     """Format polyomino tilings as an SVG image.

# #     Args:
# #         solutions (list): List of polyomino solution grids.
# #         filename (str): Filename for the SVG image.
# #         columns (int, optional): Number of columns in the image (Default: 1).
# #         size (int, optional): Size of each hexagon (default: 25).
# #         padding (int, optional): Padding around the image (default: 5)
# #         colour (function, optional): Function taking a piece name and returning its colour (Default: a function returning white for each piece).
# #         stroke_colour (str, optional): Stroke colour (default: black).
# #         stroke_width (int, optional): Width of strokes between pieces (default: 3).
# #         empty (str, optional): String for empty grid point.
# #     """
# #     solutions = list(solutions)

# #     height, width = solutions[0].size

# #     rows = (len(solutions) + columns - 1) // columns

# #     drawing_size = (2 * padding + (columns * (3/2 * size) - 0.5) * width,
# #                     2 * padding + (rows * (np.sqrt(3) * size) - 0.5) * height)

# #     drawing = Drawing(debug=False, filename=filename, size=drawing_size)
# #     for i, solution in enumerate(solutions):
# #         y, x = divmod(i, columns)
# #         oj = padding + (x * (3/2 * size) - 0.5) * width
# #         oi = padding + (y * (np.sqrt(3) * size) - 0.5) * height
# #         group = drawing.g(stroke=stroke_colour, stroke_linecap="round",
# #                           stroke_width=1)
# #         drawing.add(group)

# #         grid = [[empty] * width for _ in range(height)]
# #         num=0
# #         for polymino in solution.polyminoes:
# #             piece = drawing.g(fill=colour(polymino.name))
# #             group.add(piece)
# #             for i, j in polymino.coord:
# #                 x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
# #                 y_coord = i * (np.sqrt(2) * size) + oi
# #                 # Calculate the points for a pointed top hexagon
# #                 points = [
# #                     (x_coord + size * np.cos(np.radians(angle)),
# #                      y_coord + size * np.sin(np.radians(angle)))
# #                     for angle in range(30, 360, 60)

# #                 ]
# #                 piece.add(drawing.polygon(points))

# #         # put in "empty" pieces
# #         for i, j in solution.coord:
# #             if grid[i][j] == " ":
# #                 x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
# #                 y_coord = i * (np.sqrt(2.2) * size) + oi
# #                 text_element = text.Text(num+1, insert=(x_coord,y_coord), fill='white', font_size=3)
# #                 num+=1
# #                 drawing.add(text_element)




# #         edges = drawing.path(stroke_width=stroke_width)
# #         group.add(edges)
# #         for i, j in product(range(height + 1), range(width)):
# #             if ((empty if i == 0 else grid[i-1][j])
# #                 != (empty if i == height else grid[i][j])):
# #                 x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
# #                 y_coord = i * (np.sqrt(3) * size) + oi
# #                 edges.push(['M', x_coord + size * np.cos(np.radians(30)),
# #                             y_coord + size * np.sin(np.radians(30)),
# #                             'l', size * np.cos(np.radians(30)),
# #                             -size * np.sin(np.radians(30))])
# #         for i, j in product(range(height), range(width + 1)):
# #             if ((empty if j == 0 else grid[i][j-1])
# #                 != (empty if j == width else grid[i][j])):
# #                 x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
# #                 y_coord = i * (np.sqrt(3) * size) + oi
# #                 edges.push(['M', x_coord, y_coord, 'l', 0, size])

# #     drawing.save()

# # number = st.selectbox("Select a Date", options=list(range(1, 32)), index=0)
# # month = st.selectbox("Select a Month", options=["January","February","March","April","May","June","July","August","September","October","November","December"], index=0)
# # day = st.selectbox("Select a Day", options=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], index=0)

# # day_map={
# #     "Monday":(0,7),
# #     "Tuesday":(1,7),
# #     "Wednesday":(2,7),
# #     "Thursday":(3,7),
# #     "Friday":(4,6),
# #     "Saturday":(5,6),
# #     "Sunday":(6,6)
# # }

# # month_map={
# #     "January":(0,1),
# #     "February":(0,2),
# #     "March":(0,3),
# #     "April":(0,4),
# #     "May":(0,5),
# #     "June":(0,6),
# #     "July":(1,1),   
# #     "August":(1,2),
# #     "September":(1,3),
# #     "October":(1,4),
# #     "November":(1,5),      
# #     "December":(1,6)
# # }

# # date_map={
# #     1:(2,1),
# #     2:(2,2),
# #     3:(2,3),
# #     4:(2,4),
# #     5:(2,5),
# #     6:(2,6),
# #     7:(3,0),
# #     8:(3,1),
# #     9:(3,2),
# #     10:(3,3),
# #     11:(3,4),
# #     12:(3,5),
# #     13:(3,6),
# #     14:(4,0),
# #     15:(4,1),
# #     16:(4,2),
# #     17:(4,3),
# #     18:(4,4),
# #     19:(4,5),
# #     20:(5,0),
# #     21:(5,1),
# #     22:(5,2),
# #     23:(5,3),
# #     24:(5,4),
# #     25:(5,5),
# #     26:(6,0),
# #     27:(6,1),
# #     28:(6,2),
# #     29:(6,3),
# #     30:(6,4),
# #     31:(6,5),
# # }
# # date_row_col=date_map[number]
# # month_row_col=month_map[month]
# # day_row_col=day_map[day]

# # def sortkey(x):
# #     x = str(x)
# #     return (len(x), x)

# # COLOURS = dict(I="#B8255F", F="#FF7600", L="#FAD000",
# #             P="#00FF00", N="#299438", T="#00CE87",
# #             U="#96C3EB", V="#884DFF", W="#EB96EB",
# #             X="#808080", Y="#FF0000", Z="#0000FF",D="#7ECC49")
# # GRID = Grid((7, 8), holes=[(0,0),(1,0),(2,0),(4,7),(5,7),(6,7),date_row_col,month_row_col,day_row_col])
# # print(GRID)
# # main_polyminoes=[]

# # pieces=[P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13]
# # shade=['I','F','L','P','N','T','U','V','W','X','Y','Z','D']

# # all_solutions = []  
# # j=0

# # for SHAPES in pieces:
# #     polyminoes=[]
# #     for piece in generate_polyminoes(SHAPES):
# #         for position in generate_polymino_positions(piece, GRID):
# #             if position not in polyminoes:
# #                 polyminoes.append(position)
# #     polyminoes = [polymino.aslist for polymino in polyminoes]
# #     polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
# #     for i in polyminoes:
# #         i.pop()
# #         i.append(shade[j])
# #     j+=1
# #     polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
# #     main_polyminoes+=polyminoes

# # LABELS = list(set([element for polymino in main_polyminoes for element in polymino]))
# # LABELS = sorted(LABELS, key=sortkey)

# # COVER = DLX(LABELS, main_polyminoes)
# # for i, SOLUTION in enumerate(COVER.generate_solutions()):
# #     solution_grid = Grid.from_DLX(SOLUTION)
# #     all_solutions.append(solution_grid)
# #     break

# # solutions_svg([all_solutions[0]], filename='first_solution.svg', columns=5,colour=COLOURS.get)
# # svg_content = open("first_solution.svg", "r").read()
# # st.write(f"solution for DATE: {number}{month}{day}")
# # st.image(svg_content, width=1100)


# import streamlit as st
# from polymino import Grid, generate_polyminoes, generate_polymino_positions, unique_grids
# from dlx import DLX
# from hexa_rotation_flip import P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13
# from itertools import product
# from svgwrite import Drawing, text
# import numpy as np

# st.title("Shatkon Paheli Level-3")

# def solutions_svg(solutions, filename, columns=1, size=5, padding=10,
#                   colour=lambda _: "white", stroke_colour="black",
#                   stroke_width=10, empty=' ', date_text='', month_text='', day_text=''):
#     """Format polyomino tilings as an SVG image.
    
#     Args:
#         solutions (list): List of polyomino solution grids.
#         filename (str): Filename for the SVG image.
#         columns (int, optional): Number of columns in the image (Default: 1).
#         size (int, optional): Size of each hexagon (default: 25).
#         padding (int, optional): Padding around the image (default: 5)
#         colour (function, optional): Function taking a piece name and returning its colour (Default: a function returning white for each piece).
#         stroke_colour (str, optional): Stroke colour (default: black).
#         stroke_width (int, optional): Width of strokes between pieces (default: 3).
#         empty (str, optional): String for empty grid point.
#         date_text (str, optional): Text for the date to be displayed on the SVG.
#         month_text (str, optional): Text for the month to be displayed on the SVG.
#         day_text (str, optional): Text for the day to be displayed on the SVG.
#     """
#     solutions = list(solutions)
#     height, width = solutions[0].size

#     rows = (len(solutions) + columns - 1) // columns
#     drawing_size = (2 * padding + (columns * (3/2 * size) - 0.5) * width,
#                     2 * padding + (rows * (np.sqrt(3) * size) - 0.5) * height)

#     drawing = Drawing(debug=False, filename=filename, size=drawing_size)
#     for i, solution in enumerate(solutions):
#         y, x = divmod(i, columns)
#         oj = padding + (x * (3/2 * size) - 0.5) * width
#         oi = padding + (y * (np.sqrt(3) * size) - 0.5) * height
#         group = drawing.g(stroke=stroke_colour, stroke_linecap="round", stroke_width=1)
#         drawing.add(group)

#         grid = [[empty] * width for _ in range(height)]
#         num = 0
#         for polymino in solution.polyminoes:
#             piece = drawing.g(fill=colour(polymino.name))
#             group.add(piece)
#             for i, j in polymino.coord:
#                 x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
#                 y_coord = i * (np.sqrt(2) * size) + oi
#                 # Calculate the points for a pointed top hexagon
#                 points = [
#                     (x_coord + size * np.cos(np.radians(angle)),
#                      y_coord + size * np.sin(np.radians(angle)))
#                     for angle in range(30, 360, 60)
#                 ]
#                 piece.add(drawing.polygon(points))

#         # Add the text for date, month, and day
#         date_x = oj + 1.5 * size
#         date_y = oi + 2 * size
#         drawing.add(text.Text(date_text, insert=(date_x, date_y), fill='black', font_size=10))

#         month_x = oj + 3 * size
#         month_y = oi + 2 * size
#         drawing.add(text.Text(month_text, insert=(month_x, month_y), fill='black', font_size=10))

#         day_x = oj + 4.5 * size
#         day_y = oi + 2 * size
#         drawing.add(text.Text(day_text, insert=(day_x, day_y), fill='black', font_size=10))

#         edges = drawing.path(stroke_width=stroke_width)
#         group.add(edges)
#         for i, j in product(range(height + 1), range(width)):
#             if ((empty if i == 0 else grid[i-1][j]) != (empty if i == height else grid[i][j])):
#                 x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
#                 y_coord = i * (np.sqrt(3) * size) + oi
#                 edges.push(['M', x_coord + size * np.cos(np.radians(30)),
#                             y_coord + size * np.sin(np.radians(30)),
#                             'l', size * np.cos(np.radians(30)),
#                             -size * np.sin(np.radians(30))])
#         for i, j in product(range(height), range(width + 1)):
#             if ((empty if j == 0 else grid[i][j-1]) != (empty if j == width else grid[i][j])):
#                 x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
#                 y_coord = i * (np.sqrt(3) * size) + oi
#                 edges.push(['M', x_coord, y_coord, 'l', 0, size])

#     drawing.save()

# number = st.selectbox("Select a Date", options=list(range(1, 32)), index=0)
# month = st.selectbox("Select a Month", options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=0)
# day = st.selectbox("Select a Day", options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=0)

# day_map = {
#     "Monday": (0, 7),
#     "Tuesday": (1, 7),
#     "Wednesday": (2, 7),
#     "Thursday": (3, 7),
#     "Friday": (4, 6),
#     "Saturday": (5, 6),
#     "Sunday": (6, 6)
# }

# month_map = {
#     "January": (0, 1),
#     "February": (0, 2),
#     "March": (0, 3),
#     "April": (0, 4),
#     "May": (0, 5),
#     "June": (0, 6),
#     "July": (1, 1),
#     "August": (1, 2),
#     "September": (1, 3),
#     "October": (1, 4),
#     "November": (1, 5),
#     "December": (1, 6)
# }

# date_map = {
#     1: (2, 1),
#     2: (2, 2),
#     3: (2, 3),
#     4: (2, 4),
#     5: (2, 5),
#     6: (2, 6),
#     7: (3, 0),
#     8: (3, 1),
#     9: (3, 2),
#     10: (3, 3),
#     11: (3, 4),
#     12: (3, 5),
#     13: (3, 6),
#     14: (4, 0),
#     15: (4, 1),
#     16: (4, 2),
#     17: (4, 3),
#     18: (4, 4),
#     19: (4, 5),
#     20: (5, 0),
#     21: (5, 1),
#     22: (5, 2),
#     23: (5, 3),
#     24: (5, 4),
#     25: (5, 5),
#     26: (6, 0),
#     27: (6, 1),
#     28: (6, 2),
#     29: (6, 3),
#     30: (6, 4),
#     31: (6, 5),
# }

# date_row_col = date_map[number]
# month_row_col = month_map[month]
# day_row_col = day_map[day]

# def sortkey(x):
#     x = str(x)
#     return (len(x), x)

# COLOURS = dict(I="#B8255F", F="#FF7600", L="#FAD000",
#             P="#00FF00", N="#299438", T="#00CE87",
#             U="#96C3EB", V="#884DFF", W="#EB96EB",
#             X="#808080", Y="#FF0000", Z="#0000FF", D="#7ECC49")
# GRID = Grid((7, 8), holes=[(0, 0), (1, 0), (2, 0), (4, 7), (5, 7), (6, 7), date_row_col, month_row_col, day_row_col])

# main_polyminoes = []
# pieces = [P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13]
# shade = ['I', 'F', 'L', 'P', 'N', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'D']

# all_solutions = []
# j = 0

# for SHAPES in pieces:
#     polyminoes = []
#     for piece in generate_polyminoes(SHAPES):
#         for position in generate_polymino_positions(piece, GRID):
#             if position not in polyminoes:
#                 polyminoes.append(position)
#     polyminoes = [polymino.aslist for polymino in polyminoes]
#     polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
#     for i in polyminoes:
#         i.pop()
#         i.append(shade[j])
#     j += 1
#     polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
#     main_polyminoes += polyminoes

# LABELS = list(set([element for polymino in main_polyminoes for element in polymino]))
# LABELS = sorted(LABELS, key=sortkey)

# COVER = DLX(LABELS, main_polyminoes)
# for i, SOLUTION in enumerate(COVER.generate_solutions()):
#     solution_grid = Grid.from_DLX(SOLUTION)
#     all_solutions.append(solution_grid)
#     break

# solutions_svg([all_solutions[0]], filename='first_solution.svg', columns=5, colour=COLOURS.get,
#               date_text=str(number), month_text=month, day_text=day)

# svg_content = open("first_solution.svg", "r").read()
# st.write(f"Solution for Date: {number} {month} {day}")
# st.image(svg_content, width=1100)


import streamlit as st
from polymino import Grid,generate_polyminoes,generate_polymino_positions,unique_grids
from dlx import DLX
from hexa_rotation_flip import P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13
from itertools import product
from svgwrite import Drawing,text
import numpy as np  

st.title("Shatkon Paheli Level-3")

def solutions_svg(solutions, filename, date_number, month_name, day_name, date_position, month_position, day_position, columns=1, size=5, padding=10,
                  colour=lambda _: "white", stroke_colour="black", stroke_width=10, empty=' '):
    """Format polyomino tilings as an SVG image.

    Args:
        solutions (list): List of polyomino solution grids.
        filename (str): Filename for the SVG image.
        columns (int, optional): Number of columns in the image (Default: 1).
        size (int, optional): Size of each hexagon (default: 25).
        padding (int, optional): Padding around the image (default: 5)
        colour (function, optional): Function taking a piece name and returning its colour (Default: a function returning white for each piece).
        stroke_colour (str, optional): Stroke colour (default: black).
        stroke_width (int, optional): Width of strokes between pieces (default: 3).
        empty (str, optional): String for empty grid point.
    """
    solutions = list(solutions)

    height, width = solutions[0].size

    rows = (len(solutions) + columns - 1) // columns

    drawing_size = (2 * padding + (columns * (3/2 * size) - 0.5) * width,
                    2 * padding + (rows * (np.sqrt(3) * size) - 0.5) * height)

    drawing = Drawing(debug=False, filename=filename, size=drawing_size)
    for i, solution in enumerate(solutions):
        y, x = divmod(i, columns)
        oj = padding + (x * (3/2 * size) - 0.5) * width
        oi = padding + (y * (np.sqrt(3) * size) - 0.5) * height
        group = drawing.g(stroke=stroke_colour, stroke_linecap="round",
                          stroke_width=1)
        drawing.add(group)

        grid = [[empty] * width for _ in range(height)]
        num=0
        for polymino in solution.polyminoes:
            piece = drawing.g(fill=colour(polymino.name))
            group.add(piece)
            for i, j in polymino.coord:
                x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
                y_coord = i * (np.sqrt(2) * size) + oi
                # Calculate the points for a pointed top hexagon
                points = [
                    (x_coord + size * np.cos(np.radians(angle)),
                     y_coord + size * np.sin(np.radians(angle)))
                    for angle in range(30, 360, 60)

                ]
                piece.add(drawing.polygon(points))

        date_row, date_col = date_position
        x_coord = date_col * (1.69 * size) + oj + ((date_row + (date_col % 8) / 8) * size)
        y_coord = date_row * (np.sqrt(2) * size) + oi
        drawing.add(drawing.text(str(date_number), insert=(x_coord, y_coord+1), fill='white', font_size=4, text_anchor="middle"))

        month_row, month_col = month_position
        x_coord_month = month_col * (1.69 * size) + oj + ((month_row + (month_col % 8) / 8) * size)
        y_coord_month = month_row * (np.sqrt(2) * size) + oi
        drawing.add(drawing.text(month_name, insert=(x_coord_month, y_coord_month), fill='white', font_size=4, text_anchor="middle"))

        day_row, day_col = day_position
        x_coord_day = day_col * (1.69 * size) + oj + ((day_row + (day_col % 8) / 8) * size)
        y_coord_day = day_row * (np.sqrt(2) * size) + oi
        drawing.add(drawing.text(day_name, insert=(x_coord_day, y_coord_day), fill='white', font_size=4, text_anchor="middle"))

        edges = drawing.path(stroke_width=stroke_width)
        group.add(edges)
        for i, j in product(range(height + 1), range(width)):
            if ((empty if i == 0 else grid[i-1][j])
                != (empty if i == height else grid[i][j])):
                x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
                y_coord = i * (np.sqrt(3) * size) + oi
                edges.push(['M', x_coord + size * np.cos(np.radians(30)),
                            y_coord + size * np.sin(np.radians(30)),
                            'l', size * np.cos(np.radians(30)),
                            -size * np.sin(np.radians(30))])
        for i, j in product(range(height), range(width + 1)):
            if ((empty if j == 0 else grid[i][j-1])
                != (empty if j == width else grid[i][j])):
                x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
                y_coord = i * (np.sqrt(3) * size) + oi
                edges.push(['M', x_coord, y_coord, 'l', 0, size])

    drawing.save()

number = st.selectbox("Select a Date", options=list(range(1, 32)), index=0)
month = st.selectbox("Select a Month", options=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"], index=0)
day = st.selectbox("Select a Day", options=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], index=0)

day_map={
    "Mon":(0,7),
    "Tue":(1,7),
    "Wed":(2,7),
    "Thu":(3,7),
    "Fri":(4,6),
    "Sat":(5,6),
    "Sun":(6,6)
}

month_map={
    "Jan":(0,1),
    "Feb":(0,2),
    "Mar":(0,3),
    "Apr":(0,4),
    "May":(0,5),
    "June":(0,6),
    "July":(1,1),   
    "Aug":(1,2),
    "Sep":(1,3),
    "Oct":(1,4),
    "Nov":(1,5),      
    "Dec":(1,6)
}

date_map={
    1:(2,1),
    2:(2,2),
    3:(2,3),
    4:(2,4),
    5:(2,5),
    6:(2,6),
    7:(3,0),
    8:(3,1),
    9:(3,2),
    10:(3,3),
    11:(3,4),
    12:(3,5),
    13:(3,6),
    14:(4,0),
    15:(4,1),
    16:(4,2),
    17:(4,3),
    18:(4,4),
    19:(4,5),
    20:(5,0),
    21:(5,1),
    22:(5,2),
    23:(5,3),
    24:(5,4),
    25:(5,5),
    26:(6,0),
    27:(6,1),
    28:(6,2),
    29:(6,3),
    30:(6,4),
    31:(6,5),
}
date_row_col=date_map[number]
month_row_col=month_map[month]
day_row_col=day_map[day]

def sortkey(x):
    x = str(x)
    return (len(x), x)

COLOURS = dict(I="#B8255F", F="#FF7600", L="#FAD000",
            P="#00FF00", N="#299438", T="#00CE87",
            U="#96C3EB", V="#884DFF", W="#EB96EB",
            X="#808080", Y="#FF0000", Z="#0000FF",D="#7ECC49")
GRID = Grid((7, 8), holes=[(0,0),(1,0),(2,0),(4,7),(5,7),(6,7),date_row_col,month_row_col,day_row_col])
print(GRID)
main_polyminoes=[]

pieces=[P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13]
shade=['I','F','L','P','N','T','U','V','W','X','Y','Z','D']

all_solutions = []  
j=0

for SHAPES in pieces:
    polyminoes=[]
    for piece in generate_polyminoes(SHAPES):
        for position in generate_polymino_positions(piece, GRID):
            if position not in polyminoes:
                polyminoes.append(position)
    polyminoes = [polymino.aslist for polymino in polyminoes]
    polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
    for i in polyminoes:
        i.pop()
        i.append(shade[j])
    j+=1
    polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
    main_polyminoes+=polyminoes

LABELS = list(set([element for polymino in main_polyminoes for element in polymino]))
LABELS = sorted(LABELS, key=sortkey)

COVER = DLX(LABELS, main_polyminoes)
for i, SOLUTION in enumerate(COVER.generate_solutions()):
    solution_grid = Grid.from_DLX(SOLUTION)
    all_solutions.append(solution_grid)
    break

# solutions_svg([all_solutions[0]], filename='first_solution.svg', columns=5,colour=COLOURS.get)
solutions_svg(
    [all_solutions[0]], 
    filename='first_solution.svg', 
    date_number=number, 
    month_name=month,
    day_name=day,
    date_position=date_row_col, 
    month_position=month_row_col,
    day_position=day_row_col,
    columns=5,
    colour=COLOURS.get
)
svg_content = open("first_solution.svg", "r").read()
st.write(f"solution for DATE: {number}{month}{day}")
st.image(svg_content, width=1100)
