from manim import Line,WHITE

from utils.custom_types import ScalarFunc

import numpy as np

def make_line_from_point_direction(
  p,
  direction,
  length:float,
  color=WHITE
)->Line:
  direction_unit=direction/np.linalg.norm(direction)

  line=Line(
    start=p-direction_unit*length,
    end=p+direction_unit*length,
    color=color
  )

  return line

def make_tangent_line(
  axes,
  x:float,
  f:ScalarFunc,
  derivative:ScalarFunc,
  length:float,
  color=WHITE
)->Line:
  p1=axes.c2p(x,f(x))
  p2=axes.c2p(x+0.01,f(x)+derivative(x)*0.01)
  direction=p2-p1

  return make_line_from_point_direction(p1,direction,length,color=color)

def make_secant_line(
  A,
  B,
  color=WHITE
)->Line:
  direction=A-B
  direction_unit=direction/np.linalg.norm(direction)

  secant_line=Line(
    start=A+direction_unit*3,
    end=B-direction_unit*3,
    color=color
  )

  return secant_line
