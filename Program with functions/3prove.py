import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    # tree_center = scene_left + 500
    # tree_top = scene_top + 100
    # tree_height = 150
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


# def draw_pine_tree(canvas, peak_x, peak_y, height):
#     """Draw a single pine tree.
#     Parameters
#         canvas: The tkinter canvas where this
#             function will draw a pine tree.
#         peak_x, peak_y: The x and y location in pixels where
#             this function will draw the top peak of a pine tree.
#         height: The height in pixels of the pine tree that
#             this function will draw.
#     Return: nothing
#     """
#     trunk_width = height / 10
#     trunk_height = height / 8
#     trunk_left = peak_x - trunk_width / 2
#     trunk_right = peak_x + trunk_width / 2
#     trunk_bottom = peak_y + height

#     skirt_width = height / 2
#     skirt_height = height - trunk_height
#     skirt_left = peak_x - skirt_width / 2
#     skirt_right = peak_x + skirt_width / 2
#     skirt_bottom = peak_y + skirt_height

#     # Draw the trunk of the pine tree.
#     canvas.create_rectangle(trunk_left, skirt_bottom,
#             trunk_right, trunk_bottom,
#             outline="gray20", width=1, fill="tan3")

#     # Draw the crown (also called skirt) of the pine tree.
#     canvas.create_polygon(peak_x, peak_y,
#             skirt_right, skirt_bottom,
#             skirt_left, skirt_bottom,
#             outline="gray20", width=1, fill="dark green")
    draw_sky(canvas)
    draw_sun(canvas)
    draw_clouds(canvas)
    draw_ground(canvas)
    draw_house(canvas)
    for i in range(400, 750, 25):
        draw_fence(canvas, i, 350)

def draw_sky(canvas):
    canvas.create_rectangle(0, 0, 800, 500, fill = 'steel blue')

def draw_sun(canvas):
    canvas.create_oval(50, 100, 300, 350, width = 0, fill = 'yellow')

def draw_clouds(canvas):
    canvas.create_oval(10, 10, 100, 80, width = 0, fill = 'white')
    canvas.create_oval(300, 170, 500, 200, width = 0, fill = 'white')
    canvas.create_oval(250, 10, 400, 100, width = 0, fill = 'white')
    canvas.create_oval(550, 35, 700, 100, width = 0, fill = 'white')
    canvas.create_oval(575, 205, 725, 275, width = 0, fill = 'white')
    canvas.create_oval(25, 200, 200, 275, width = 0, fill = 'white')

def draw_ground(canvas):
    canvas.create_rectangle(0, 300, 800, 500, outline = 'green', fill = 'green')

def draw_house(canvas,):
    
    canvas.create_rectangle(450,200,700,400, width = 0, fill = 'salmon3')
    canvas.create_rectangle(500, 250, 550, 300, width = 0, fill = 'SkyBlue1')
    canvas.create_line(500, 275, 550, 275, width = 4)
    canvas.create_line(525, 250, 525, 300, width = 4)
    canvas.create_rectangle(600, 275, 675, 400, width = 0, fill = 'IndianRed3')
    canvas.create_oval(660, 335, 670, 345, width = 0, fill = 'black')
    canvas.create_polygon(425, 200, 725, 200, 575, 150, width = 0, fill = 'IndianRed4')

def draw_fence(canvas, x, y):
    x1 = x + 20
    y1 = y + 75

    canvas.create_rectangle(x, y, x1, y1, width = 0, fill = 'azure')
    


# Call the main function so that
# this program will start executing.
main()

