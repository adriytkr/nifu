from typing import Callable
from manim import Line,Dot,WHITE,DashedLine,MathTex,DOWN
import numpy as np

ScalarFunc=Callable[[float], float]

class CoordinateSystem:
  def __init__(self,axes):
    self.axes=axes

  def to_point(self,x,y):
    return self.axes.c2p(x,y)

  def to_graph_point(self,x,f):
    return self.axes.c2p(x,f(x))
  
  def build_dot(self,x,y,color=WHITE)->Dot:
    dot=Dot(self.to_point(x,y),color=color)
    dot.set_z_index(5)
    return dot

  def build_graph_dot(self,x,f,color=WHITE)->Dot:
    dot=Dot(self.to_graph_point(x,f),color=color)
    dot.set_z_index(5)
    return dot

  def build_projection(self,x,y,label):
    projection=DashedLine(self.to_point(x,y),self.to_point(x,0))
    label=MathTex(label).next_to(projection,DOWN)
    label.set_z_index(5)
    return projection,label

def make_line_from_point_direction(
  p,
  direction,
  length:float
)->Line:
  dir_unit=direction/np.linalg.norm(direction)

  return Line(
    start=p-dir_unit*length,
    end=p+dir_unit*length
  )

def make_tangent_line(
  coords:CoordinateSystem,
  x:float,
  f:ScalarFunc,
  derivative:ScalarFunc,
  length:float
)->Line:
  p1=coords.to_point(x,f(x))
  p2=coords.to_point(x+0.01,f(x)+derivative(x)*0.01)
  dir=p2-p1

  return make_line_from_point_direction(p1,dir,length)

def make_secant_line(A,B):
  dir=A-B
  dir_unit=dir/np.linalg.norm(dir)
  secant_line=Line(
    start=A+dir_unit*3,
    end=B-dir_unit*3
  )

  return secant_line
