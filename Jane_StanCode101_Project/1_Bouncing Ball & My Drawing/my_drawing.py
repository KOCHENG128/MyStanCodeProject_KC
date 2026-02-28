"""
File: my_drawing.py
Name: Jane Huang
----------------------
TODO: The file uses the campy module to draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GRoundRect, G3DRect, GArc, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    This program draw the image which mimics <Girl with a Pearl Earring>
    Title: Girl with Pearl Earring
    This is the Girl with Pearl Earring, a master piece by Dutch Golden Age artist Johannes Vermeer
    This is an art piece on my bucket list for my travel to Netherlands
    """
    window = GWindow(width=800, height=800, title='Girl with Pearl Earring')
    background = GRect(800, 800)
    background.filled = True
    background.fill_color = 'black'
    background.color = 'black'
    window.add(background)
    # add shoulder, which is a right triangle
    shoulder = GPolygon()
    shoulder.add_vertex((300, 500))
    shoulder.add_vertex((400, 500))
    shoulder.add_vertex((400, 450))
    shoulder.filled = True
    shoulder.fill_color = 'wheat'
    shoulder.color = 'wheat'
    window.add(shoulder)
    # add a chest, which is a right triangle
    chest = GPolygon()
    chest.add_vertex((200, 800))
    chest.add_vertex((300, 800))
    chest.add_vertex((300, 500))
    chest.filled = True
    chest.fill_color = 'wheat'
    chest.color = 'wheat'
    window.add(chest)
    # add left hand side, which is a rectangle
    left_hand = GRect(100, 300, x=300, y=500)
    left_hand.filled = True
    left_hand.fill_color = 'wheat'
    left_hand.color = 'wheat'
    window.add(left_hand)
    # add a back, which is a quadrilateral(connect the dot by clock-wise)
    back = GPolygon()
    back.add_vertex((400, 450))
    back.add_vertex((500, 425))
    back.add_vertex((520, 800))
    back.add_vertex((400, 800))
    back.filled = True
    back.fill_color = 'burly wood'
    back.color = 'burly wood'
    window.add(back)
    # add a scarf_upper_tail, which is a triangle
    scarf_upper_tail = GPolygon()
    scarf_upper_tail.add_vertex((505, 200))
    scarf_upper_tail.add_vertex((650, 570))
    scarf_upper_tail.add_vertex((500, 630))
    scarf_upper_tail.filled = True
    scarf_upper_tail.fill_color = 'yellow'
    scarf_upper_tail.color = 'yellow'
    window.add(scarf_upper_tail)
    # add a scarf_lower_brim, which is a quadrilateral
    scarf_lower_brim = GPolygon()
    scarf_lower_brim.add_vertex((500, 630))
    scarf_lower_brim.add_vertex((650, 570))
    scarf_lower_brim.add_vertex((657.1, 588.1))
    scarf_lower_brim.add_vertex((502.4, 650))
    scarf_lower_brim.filled = True
    scarf_lower_brim.fill_color = 'white'
    scarf_lower_brim.color = 'white'
    window.add(scarf_lower_brim)
    # add scarf_top, which is a triangle
    scarf_top = GPolygon()
    scarf_top.add_vertex((500, 100))
    scarf_top.add_vertex((505, 200))
    scarf_top.add_vertex((380, 125))
    scarf_top.filled = True
    scarf_top.fill_color = 'yellow'
    scarf_top.color = 'yellow'
    window.add(scarf_top)
    # add back_head, which is a triangle
    back_head = GPolygon()
    back_head.add_vertex((380, 125))
    back_head.add_vertex((505, 200))
    back_head.add_vertex((460, 350))  # 這邊底下要放珍珠
    back_head.filled = True
    back_head.fill_color = 'dodger blue'
    back_head.color = 'dodger blue'
    window.add(back_head)
    #  add a pearl, which is a circle
    pearl = GOval(20, 20, x=450, y=350)
    pearl.filled = True
    pearl.fill_color = 'floral white'
    pearl.color = 'bisque'
    window.add(pearl)
    # add back_head2, which is a triangle (same color as fore_head)
    back_head2 = GPolygon()
    back_head2.add_vertex((380, 125))
    back_head2.add_vertex((460, 350))
    back_head2.add_vertex((350, 215))
    back_head2.filled = True
    back_head2.fill_color = 'light blue'
    back_head2.color = 'light blue'
    window.add(back_head2)
    # add a cheek, which is a triangle
    cheek = GPolygon()
    cheek.add_vertex((350, 215))
    cheek.add_vertex((460, 350))
    cheek.add_vertex((340, 365))
    cheek.filled = True
    cheek.fill_color = 'bisque'
    cheek.color = 'bisque'
    window.add(cheek)
    # add a fore_head, which is a quadrilateral
    fore_head = GPolygon()
    fore_head.add_vertex((330, 150))
    fore_head.add_vertex((380, 125))
    fore_head.add_vertex((350, 215))
    fore_head.add_vertex((300, 210))
    fore_head.filled = True
    fore_head.fill_color = 'light blue'
    fore_head.color = 'light blue'
    window.add(fore_head)
    # add a fore_head2, which is a triangle
    fore_head2 = GPolygon()
    fore_head2.add_vertex((330, 150))
    fore_head2.add_vertex((300, 210))
    fore_head2.add_vertex((225, 202.5))
    fore_head2.filled = True
    fore_head2.fill_color = 'light blue'
    fore_head2.color = 'light blue'
    window.add(fore_head2)
    # a triangle for right face
    face1 = GPolygon()
    face1.add_vertex((225, 203))
    face1.add_vertex((350, 215))
    face1.add_vertex((340, 365))
    face1.filled = True
    face1.fill_color = 'corn silk'
    face1.color = 'corn silk'
    window.add(face1)
    # a triangle for left face
    face2 = GPolygon()
    face2.add_vertex((225, 203))
    face2.add_vertex((340, 365))
    face2.add_vertex((215, 330))
    face2.filled = True
    face2.fill_color = 'corn silk'
    face2.color = 'corn silk'
    window.add(face2)
    # a triangle for jaw
    jaw = GPolygon()
    jaw.add_vertex((215, 330))
    jaw.add_vertex((340, 365))
    jaw.add_vertex((250, 400))
    jaw.filled = True
    jaw.fill_color = 'corn silk'
    jaw.color = 'corn silk'
    window.add(jaw)


if __name__ == '__main__':
    main()
