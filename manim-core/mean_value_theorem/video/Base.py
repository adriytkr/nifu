from manim import *

from utils.coordinate_system import CoordinateSystemManager
from utils.custom_types import scalarFunc
from utils.geometry import make_secant_line

class BaseScene(Scene):
  axes=Axes(
    x_range=[0,10],
    y_range=[0,6]
  )

  coords=CoordinateSystemManager(axes)

  x_A=2
  x_B=9
  x_C=5.5

  def s(self,t):
    return (0.4*t-1.5)**2+1

  def v(self,t):
    return 0.8*(0.4*t-1.5)

  def L(self,t):
    return 0.56*(t-self.x_A)+self.s(self.x_A)

  def h(self,t):
    return self.L(t)-self.s(t)

  def h_derivative(self,t):
    return 0.56-0.8*(0.4*t-1.5)

  def s_build_tangent_line(
    self,
    x:float,
    color=WHITE
  )->Line:
    return self.coords.build_tangent_line(
      x,
      self.s,
      self.v,
      length=5,
      color=color
    )
    
  def s_build_tangent_point(
    self,
    x:float,
    color=WHITE
  )->Dot:
    return self.coords.build_graph_dot(
      x,
      self.s,
      color=color
    )

  def build_bird(
    self,
    x:float,
    f:scalarFunc,
    color=YELLOW_E
  )->Dot:
    return self.coords.build_graph_dot(
      x,
      f,
      color=color
    )
  
  def build_height(
    self,
    x:float,
    color=WHITE
  )->Line:
    return make_secant_line(
      self.coords.to_graph_point(x,self.s),
      self.coords.to_graph_point(x,self.L),
      color=color
    )
  
  def h_build_tangent_line(
    self,
    x:float,
    color=WHITE
  )->Line:
    return self.coords.build_tangent_line(
      x,
      self.h,
      self.h_derivative,
      length=5,
      color=color
    )
