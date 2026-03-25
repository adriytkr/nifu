from manim import Dot,WHITE,DashedLine,MathTex,DOWN,Line

from utils.geometry import make_tangent_line
from utils.custom_types import ScalarFunc

class CoordinateSystemManager:
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

  def build_tangent_line(
    self,
    x:float,
    f:ScalarFunc,
    derivative:ScalarFunc,
    length:float,
    color=WHITE
  )->Line:
    return make_tangent_line(
      self.axes,
      x,
      f,
      derivative,
      length,
      color
    )
