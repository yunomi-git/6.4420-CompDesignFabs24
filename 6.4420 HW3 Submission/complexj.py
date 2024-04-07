# An example script to use your DSL and compile to an SVG

from tab import Tab, generate_root_tab, generate_child_tab, draw_svg
import numpy as np

side = 120
width = 80
base_angle = np.pi/9
base_length = side * np.cos(base_angle)
cap_angle = np.pi/6
cap_length = side * np.cos(cap_angle)
root = generate_root_tab(width=width, length=base_length, angle=base_angle)
cap1 = generate_child_tab(root, width=side, length=cap_length, offset=0, side=1, angle=cap_angle, bend_angle=0)
panel2 = generate_child_tab(root, width=width, length=base_length, offset=0, side=2, angle=-base_angle, bend_angle=0)
cap2 = generate_child_tab(root, width=side, length=cap_length, offset=0, side=3, angle=cap_angle, bend_angle=0)
panel3 = generate_child_tab(cap2, width=side, length=width * np.cos(base_angle), offset=0, side=2, angle=-base_angle, bend_angle=0)

panel4 = generate_child_tab(panel3, width=width, length=base_length, offset=0, side=1, angle=-base_angle, bend_angle=0)
panel5 = generate_child_tab(panel4, width=width, length=base_length, offset=0, side=2, angle=base_angle, bend_angle=0)
panel6 = generate_child_tab(panel5, width=width, length=base_length, offset=0, side=2, angle=-base_angle, bend_angle=0)
cap3 = generate_child_tab(panel6, width=side, length=cap_length, offset=0, side=1, angle=-cap_angle, bend_angle=0)
cap4 = generate_child_tab(panel4, width=side, length=cap_length, offset=0, side=3, angle=-cap_angle, bend_angle=0)

# cap3 = generate_child_tab(panel2, width=side, length=cap_length, offset=0, side=3, angle=-cap_angle, bend_angle=0)

draw_svg(root, "complexj.svg")