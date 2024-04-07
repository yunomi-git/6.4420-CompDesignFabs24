# An example script to use your DSL and compile to an SVG

from tab import Tab, generate_root_tab, generate_child_tab, draw_svg
import numpy as np

root = generate_root_tab(width=20, length=20, angle=0)
child1 = generate_child_tab(root, width=20, length=20, offset=0, side=0, angle=0, bend_angle=np.pi/2)
child2 = generate_child_tab(root, width=20, length=20, offset=0, side=1, angle=0, bend_angle=np.pi/2)
child3 = generate_child_tab(root, width=20, length=20, offset=0, side=2, angle=0, bend_angle=np.pi/2)
child4 = generate_child_tab(root, width=20, length=20, offset=0, side=3, angle=0, bend_angle=np.pi/2)
child5 = generate_child_tab(child1, width=20, length=20, offset=0, side=2, angle=0, bend_angle=np.pi/2)

draw_svg(root, "cube.svg")