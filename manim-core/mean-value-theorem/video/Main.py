from manim import *

from utils.geometry import make_secant_line
from utils.coordinate_system import CoordinateSystemManager
from utils.theme import HIGHLIGHT_COLOR,NEUTRAL_COLOR,HIGHLIGHT_COLOR2

class MainScene(Scene):
  axes=Axes(
    x_range=[0,10],
    y_range=[0,6]
  )

  coords=CoordinateSystemManager(axes)

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
    self.play(FadeIn(self.axes))

    s_graph=self.axes.plot(lambda x:self.s(x))

    self.play(Create(s_graph))

    point_A=self.coords.build_graph_dot(
      self.x_A,
      self.s,
      color=NEUTRAL_COLOR
    )
    point_B=self.coords.build_graph_dot(
      self.x_B,
      self.s,
      color=NEUTRAL_COLOR
    )

    proj_A,label_A=self.coords.build_projection(
      self.x_A,
      self.s(self.x_A),
      'a'
    )
    proj_B,label_B=self.coords.build_projection(
      self.x_B,
      self.s(self.x_B),
      'b'
    )

    self.play(
      Create(point_A),
      Create(proj_A),
      Create(point_B),
      Create(proj_B)
    )

    self.play(Write(label_A),Write(label_B))

    static_secant_line=make_secant_line(
      point_A.get_center(),
      point_B.get_center()
    )

    self.play(Create(static_secant_line))

    highlight=ValueTracker(0)
    t=ValueTracker(self.x_A)

    def build_ruby(color=WHITE)->Dot:
      return self.coords.build_graph_dot(t.get_value(),self.s,color).set_z_index(6)

    def build_dynamic_ruby():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)
      return build_ruby(color)

    def build_lailah(color=WHITE)->Line:
      return self.coords.build_tangent_line(
        t.get_value(),
        self.s,
        self.v,
        length=10,
        color=color
      )

    def build_dynamic_lailah():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)
      return build_lailah(color)

    static_ruby=build_ruby()
    static_lailah=build_lailah()

    dynamic_ruby=always_redraw(build_dynamic_ruby)
    dynamic_lailah=always_redraw(build_dynamic_lailah)

    self.play(
      Create(static_lailah),
      FadeIn(static_ruby)
    )

    self.remove(static_lailah,static_ruby)
    self.add(dynamic_lailah,dynamic_ruby)

    self.play(t.animate.set_value(self.x_B))
    self.play(t.animate.set_value(self.x_A))
    self.play(t.animate.set_value(self.c))

    # Highlight when Tangent and Secant become parallel to each other
    proj_C,label_C=self.coords.build_projection(
      self.c,
      self.s(self.c),
      'c'
    )

    self.play(
      highlight.animate.set_value(1),
      static_secant_line.animate.set_color(HIGHLIGHT_COLOR),
      Create(proj_C),
      run_time=0.5
    )
    self.play(Write(label_C))

    self.play(
      highlight.animate.set_value(0),
      static_secant_line.animate.set_color(WHITE),
      FadeOut(
        dynamic_lailah,
        dynamic_ruby,
        proj_C,
        label_C
      ),
      run_time=0.5
    )

    def build_RolleLine():
      return Line(
        self.coords.to_graph_point(t.get_value(),self.s),
        self.coords.to_graph_point(t.get_value(),self.L),
      )

    t.set_value(4)
    static_RolleLine=build_RolleLine()
    dynamic_rolle_line=always_redraw(build_RolleLine)
    static_ruby=build_ruby()

    self.play(
      Create(static_RolleLine),
      FadeIn(static_ruby)
    )

    self.remove(static_RolleLine,static_ruby)
    self.add(dynamic_rolle_line,dynamic_ruby)

    self.play(t.animate.set_value(self.x_B))
    self.play(t.animate.set_value(self.x_A))
    self.play(t.animate.set_value(self.x_B))

    self.play(t.animate.set_value(self.c))
    self.play(Create(proj_C))
    self.play(Write(label_C))

    h_graph=self.axes.plot(lambda x:self.h(x))

    self.play(
      Create(h_graph),
      FadeOut(
        s_graph,
        static_secant_line,
        dynamic_ruby,
        dynamic_rolle_line,
        point_A,
        proj_A,
        point_B,
        proj_B,
        label_C,
        proj_C,
      ),
    )

    blake=Line(
      self.coords.to_point(-5,self.h(self.c)),
      self.coords.to_point(10,self.h(self.c)),
      color=HIGHLIGHT_COLOR2
    )
    blake.set_z_index(7)
    point_C=self.coords.build_dot(
      self.c,
      self.h(self.c),
      color=HIGHLIGHT_COLOR2
    )

    self.play(
      FadeIn(point_C),
      Create(blake)
    )

    proj_C,label_C=self.coords.build_projection(self.c,self.h(self.c),'c')

    self.play(Create(proj_C))
    self.play(Write(label_C))

    t.set_value(self.c)
    static_secant_line.set_color(HIGHLIGHT_COLOR)
    static_ruby=build_ruby(HIGHLIGHT_COLOR)
    static_lailah=build_lailah(HIGHLIGHT_COLOR)

    self.play(
      FadeIn(
        s_graph,
        point_A,
        point_B,
        static_secant_line,
        static_lailah,
        static_ruby
      )
    )

    def end(opacity:float)->None:
      self.play(
        s_graph.animate.set_stroke(opacity=opacity),
        h_graph.animate.set_stroke(opacity=opacity),
        static_secant_line.animate.set_opacity(opacity),
        point_A.animate.set_opacity(opacity),
        label_A.animate.set_opacity(opacity),
        point_B.animate.set_opacity(opacity),
        label_B.animate.set_opacity(opacity),
        self.axes.animate.set_opacity(opacity),
      )

    end(0.25)
    end(1)
