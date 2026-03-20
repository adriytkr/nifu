from manim import *
from utils.theme import HIGHLIGHT_COLOR,NEUTRAL_COLOR
from utils.tangent import make_tangent_line,ScalarFunc,make_secant_line,CoordinateSystem

class MainScene(Scene):
  axes=Axes(
    x_range=[0,10],
    y_range=[0,6]
  )
  coords=CoordinateSystem(axes)
  x_A=2
  x_B=9
  c=5.5

  def s(self,t):
    return (0.4*t-1.5)**2+1

  def v(self,t):
    return 0.8*(0.4*t-1.5)

  def L(self,t):
    return 0.56*(t-self.x_A)+self.s(self.x_A)

  def h(self,t):
    return self.L(t)-self.s(t)

  def construct(self):
    # Draw axes
    self.play(FadeIn(self.axes))

    # Draw s(t)
    s_graph=self.axes.plot(lambda x:self.s(x))
    self.play(Create(s_graph))

    # Draw A and B
    A=self.coords.build_graph_dot(self.x_A,self.s,color=NEUTRAL_COLOR)
    B=self.coords.build_graph_dot(self.x_B,self.s,color=NEUTRAL_COLOR)
    self.play(Create(A),Create(B))

    # Draw projection and label of A and B
    proj_A,label_A=self.coords.build_projection(self.x_A,self.s(self.x_A),'a')
    proj_B,label_B=self.coords.build_projection(self.x_B,self.s(self.x_B),'b')
    self.play(Create(proj_A),Create(proj_B))
    self.play(Write(label_A),Write(label_B))

    # Draw secant line
    static_secant_line=make_secant_line(A.get_center(),B.get_center())
    self.play(Create(static_secant_line))

    highlight=ValueTracker(0)
    t=ValueTracker(self.x_A)

    def TangentPoint(color=WHITE)->Dot:
      dot=Dot(
        self.coords.to_graph_point(t.get_value(),self.s),
        color=color
      )
      dot.set_z_index(6)
      return dot

    def make_dynamic_dot():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)
      return TangentPoint(color)

    static_tangent_point=TangentPoint()
    static_tangent_line=make_tangent_line(
      self.coords,
      t.get_value(),
      self.s,
      self.v,
      5
    )

    self.play(
      Create(static_tangent_line),
      FadeIn(static_tangent_point)
    )

    # Animate moving tangent line and point
    def dynamic_tangent_line_logic():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)

      line=make_tangent_line(
        self.coords,
        t.get_value(),
        self.s,
        self.v,
        10
      )
      line.set_color(color)

      return line

    dynamic_tangent_point=always_redraw(make_dynamic_dot)
    dynamic_tangent_line=always_redraw(dynamic_tangent_line_logic)

    self.remove(static_tangent_line,static_tangent_point)
    self.add(dynamic_tangent_line,dynamic_tangent_point)

    self.play(t.animate.set_value(self.x_B))
    self.play(t.animate.set_value(self.x_A))
    self.play(t.animate.set_value(self.c))

    self.play(
      highlight.animate.set_value(1),
      static_secant_line.animate.set_color(HIGHLIGHT_COLOR),
      run_time=0.5
    )

    self.play(
      highlight.animate.set_value(0),
      static_secant_line.animate.set_color(WHITE),
      FadeOut(dynamic_tangent_line,dynamic_tangent_point),
      run_time=0.5
    )

    def RolleLine():
      return Line(
        self.coords.to_graph_point(t.get_value(),self.s),
        self.coords.to_graph_point(t.get_value(),self.L),
      )

    static_rolle_line=RolleLine()
    static_point=TangentPoint()
    self.play(
      Create(static_rolle_line),
      FadeIn(static_point)
    )

    dynamic_rolle_line=always_redraw(RolleLine)
    self.remove(static_rolle_line,static_point)
    self.add(dynamic_rolle_line,dynamic_tangent_point)
    self.play(t.animate.set_value(self.x_B))
    self.play(t.animate.set_value(self.x_A))
    self.play(t.animate.set_value(self.x_B))

    h_graph=self.axes.plot(lambda x:self.h(x))
    self.play(
      Create(h_graph),
      FadeOut(
        s_graph,
        static_secant_line,
        dynamic_tangent_point,
        A,
        proj_A,
        B,
        proj_B,
      ),
    )

    horizontal_line=Line(
      self.coords.to_point(-5,self.h(self.c)),
      self.coords.to_point(10,self.h(self.c))
    )

    C=self.coords.build_dot(self.c,self.h(self.c))
    self.play(
      FadeIn(C),
      Create(horizontal_line)
    )

    proj_C,label_C=self.coords.build_projection(self.c,self.h(self.c),'c')

    self.play(Create(proj_C))
    self.play(Write(label_C))

    static_secant_line.set_color(HIGHLIGHT_COLOR)
    static_tangent_point=self.coords.build_graph_dot(self.c,self.s,HIGHLIGHT_COLOR)
    self.play(
      FadeIn(
        s_graph,
        A,
        B,
        static_secant_line,
        dynamic_tangent_line,
        static_tangent_point
      )
    )
    
