from manim import *
import numpy as np
import typing as npt

from utils.custom_types import scalarFunc,coordinates

def make_line_from_point_direction(
  p:coordinates,
  direction:coordinates,
  length:float,
  color=WHITE
)->Line:
  direction_unit=direction/np.linalg.norm(direction)
  distance=direction_unit*length

  line=Line(
    start=p-distance,
    end=p+distance,
    color=color
  )

  return line

def make_tangent_line(
  axes:Axes,
  x:float,
  f:scalarFunc,
  derivative:scalarFunc,
  length:float,
  color=WHITE
)->Line:
  p1=axes.c2p(x,f(x))
  p2=axes.c2p(x+0.01,f(x)+derivative(x)*0.01)
  direction=p2-p1

  return make_line_from_point_direction(
    p1,
    direction,
    length=length,
    color=color
  )

def make_secant_line(
  point_A:coordinates,
  point_B:coordinates,
  color=WHITE
)->Line:
  secant_line=Line(
    start=point_A,
    end=point_B,
    color=color
  )

  return secant_line
