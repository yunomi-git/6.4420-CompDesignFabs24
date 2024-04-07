import numpy as np
from typing import Optional, Union
from dataclasses import dataclass
from functools import cache
import svgwrite
from svgwrite.shapes import Polygon
from pathlib import Path


@dataclass
class Tab:
    """
    A structure that represents a tab and a bend with respect to the parent tab.

    Hint: See figure 2 on some guidance to what parameters need to be put here.
    """

    parent: Optional["Tab"]
    children: list["Tab"]
    width: float
    length: float
    angle: float
    offset: float
    side: Optional[int]
    bend_angle: float
    # TODO 3.2: Add attributes as needed.

    def __hash__(self):
        return id(self)

    @cache
    def compute_corner_points(self) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Computes the four corner points in 2D (2,) based on the attributes.

        Hint: You may want to specify the convention on how you order these points.
        Hint: You can call this function on the parent to help get started.
        """
        # TODO 3.2: Implement this function
        # First determine reference frame of new tab
        if self.parent is None:
            # Default
            child_edge_vector = np.array([1, 0])
            child_orthogonal_vector = np.array([0, -1])
            origin = np.array([0, 0])
        else:
            # Find parent edge
            parent_corners = self.parent.compute_corner_points()
            parent_start = parent_corners[self.side]
            parent_end = parent_corners[(self.side + 1) % 4]
            parent_edge_vector = parent_end - parent_start

            # Compute reference frame wrt parent edge
            child_edge_vector = - parent_edge_vector / np.linalg.norm(parent_edge_vector)
            child_orthogonal_vector = np.array([child_edge_vector[1], -child_edge_vector[0]])
            origin = parent_end + self.offset * child_edge_vector

        # Compute corner points using the new reference frame
        child_corner_0 = origin
        child_corner_1 = child_corner_0 + child_edge_vector * self.width
        angle_distance_offset = self.length * np.tan(self.angle)
        child_corner_2 = child_corner_1 + self.length * child_orthogonal_vector - angle_distance_offset * child_edge_vector
        child_corner_3 = child_corner_2 - self.width * child_edge_vector

        return (child_corner_0, child_corner_1, child_corner_2, child_corner_3)

    def compute_all_corner_points(self) -> list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
        """
        Computes all four corner points of all tabs in the current subtree.
        """
        cps = [self.compute_corner_points()]
        for child in self.children:
            cps.extend(child.compute_all_corner_points())
        return cps


def generate_root_tab(width, length, angle) -> Tab:
    """
    Generate a new parent tab
    """
    # TODO: 3.2: Update the arguments and implement this function.
    return Tab(parent=None, children=[], width=width, length=length, angle=angle, offset=0, side=0, bend_angle=0)


def generate_child_tab(parent: Tab, width, length, angle, offset, side, bend_angle) -> Tab:
    """
    Generate a child tab. Make sure to update the children of parent accordingly.
    """
    # TODO: 3.2: Update the arguments and implement this function.
    child = Tab(parent=parent, children=[], width=width, length=length, angle=angle, offset=offset, side=side, bend_angle=bend_angle)
    parent.children.append(child)
    return child
    # raise NotImplementedError()


def draw_svg(root_tab: Tab, output: Union[str, Path], stroke_width: float = 1):
    cps = root_tab.compute_all_corner_points()
    points = np.array(cps).reshape(-1, 2)
    min_point = points.min(axis=0)  # (2,)
    max_point = points.max(axis=0)  # (2,)
    points -= min_point
    points += 2 * stroke_width
    size = max_point - min_point  # (2,)
    size += 4 * stroke_width
    rects = points.reshape(-1, 4, 2)

    dwg = svgwrite.Drawing(str(output), size=(size[0], size[1]), profile="tiny")

    for rect in rects:
        dwg.add(Polygon(rect, stroke="black", fill="lightgray", stroke_width=stroke_width))

    dwg.save()
