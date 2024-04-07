# An example script to use your DSL and compile to an SVG

from tab import Tab, generate_root_tab, generate_child_tab, draw_svg
import numpy as np

root = generate_root_tab(width=20, length=20, angle=np.pi/4)
child1 = generate_child_tab(root, width=10, length=10, offset=5, side=0, angle=np.pi/3, bend_angle=0)
# child2 = generate_child_tab(root, ...)
child3 = generate_child_tab(child1, width=10, length=10, offset=5, side=2, angle=0, bend_angle=0)

draw_svg(root, "example.svg")