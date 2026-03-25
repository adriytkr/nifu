from manim import *

from utils.geometry import make_secant_line
from utils.coordinate_system import CoordinateSystemManager
from utils.theme import NEUTRAL_COLOR,HIGHLIGHT_COLOR

class IntroScene(Scene):
  axes=Axes(
    x_range=[-3,4],
    y_range=[0,12]
  )

  x_A=-1
  x_B=2

  def f(self,x:float)->float:
    return x**2+3
  
  def derivative(self,x:float)->float:
    return x*2

  def setup(self):
    self.coords=CoordinateSystemManager(self.axes)

  def construct(self):
    # Setup
    self.play(FadeIn(self.axes))

    graph=self.axes.plot(lambda x:self.f(x))
    self.play(Create(graph))

    point_A=self.coords.build_dot(self.x_A,self.f(self.x_A),NEUTRAL_COLOR)
    point_B=self.coords.build_dot(self.x_B,self.f(self.x_B),NEUTRAL_COLOR)
    self.play(Create(point_A),Create(point_B))

    secant_line=make_secant_line(point_A.get_center(),point_B.get_center())
    self.play(Create(secant_line))

    proj_A,label_A=self.coords.build_projection(self.x_A,self.f(self.x_A),'a')
    proj_B,label_B=self.coords.build_projection(self.x_B,self.f(self.x_B),'b')

    self.play(
      Create(proj_A),
      Create(proj_B),
      run_time=0.5
    )

    self.play(
      Write(label_A),
      Write(label_B)
    )

    highlight=ValueTracker(0)
    t=ValueTracker(-1.5)

    def build_ruby(color=WHITE):
      return self.coords.build_graph_dot(t.get_value(),self.f,color)

    def build_dynamic_ruby():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)
      return build_ruby(color)
    
    def build_lailah(color=WHITE)->Line:
      return self.coords.build_tangent_line(
        t.get_value(),
        self.f,
        self.derivative,
        length=10,
        color=color
      )

    def build_dynamic_lailah()->Line:
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)
      return build_lailah(color)

    static_ruby=build_ruby()
    dynamic_ruby=always_redraw(build_dynamic_ruby)

    static_lailah=build_lailah()
    dynamic_lailah=always_redraw(build_dynamic_lailah)

    self.play(FadeIn(static_ruby))
    self.remove(static_ruby)
    self.add(dynamic_ruby)

    self.next_section('DEMO')

    self.play(Create(static_lailah))
    self.remove(static_lailah)
    self.add(dynamic_lailah)

    self.play(t.animate.set_value(1.5))
    self.play(t.animate.set_value(0))

    # Highlight when Tangent and Secant become parallel to each other
    self.play(t.animate.set_value(0.5))
    self.play(
      highlight.animate.set_value(1),
      secant_line.animate.set_color(HIGHLIGHT_COLOR),
      run_time=0.5
    )
