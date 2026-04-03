from manim import *

from utils.theme import HIGHLIGHT_COLOR,NEUTRAL_COLOR
from mean_value_theorem.video.Base import BaseScene

class MainScene(BaseScene):
  def construct(self):
    self.wait(0.5)

    # Part I
    s_graph=self.coords.axes.plot(lambda t:self.s(t))

    self.play(Create(self.axes))
    self.play(Create(s_graph))

    point_A=self.coords.build_graph_dot(
      self.x_A,
      self.s,
      color=NEUTRAL_COLOR
    )
    proj_A,label_A=self.coords.build_graph_projection(
      self.x_A,
      self.s,
      'a'
    )

    point_B=self.coords.build_graph_dot(
      self.x_B,
      self.s,
      color=NEUTRAL_COLOR
    )
    proj_B,label_B=self.coords.build_graph_projection(
      self.x_B,
      self.s,
      'b'
    )

    self.play(
      Create(point_A),
      Create(point_B)
    )

    self.play(
      Create(proj_A),
      Create(proj_B)
    )

    self.play(
      Create(label_A),
      Create(label_B)
    )

    secant_line=self.coords.build_secant_line(
      self.x_A,
      self.x_B,
      f=self.s,
    )
    self.play(Create(secant_line))

    t=ValueTracker(self.x_A)

    tangent_line=self.s_build_tangent_line(t.get_value())
    tangent_point=self.s_build_tangent_point(t.get_value())

    self.play(Create(tangent_point))
    self.play(Create(tangent_line))

    tangent_line_dynamic=always_redraw(
      lambda:self.s_build_tangent_line(t.get_value())
    )
    tangent_point_dynamic=always_redraw(
      lambda:self.s_build_tangent_point(t.get_value())
    )

    self.remove(
      tangent_line,
      tangent_point
    )
    self.add(
      tangent_line_dynamic,
      tangent_point_dynamic
    )

    self.play(
      t.animate.set_value(self.x_B),
      run_time=2.5
    )
    self.wait(0.5)
    self.play(
      t.animate.set_value(self.x_C),
      run_time=2.5
    )

    tangent_line=self.s_build_tangent_line(self.x_C)
    self.remove(tangent_line_dynamic)
    self.add(tangent_line)
    self.play(
      Blink(tangent_line,blinks=2),
      Blink(secant_line,blinks=2),
      run_time=0.6
    )

    # Part II
    self.remove(
      secant_line,
      tangent_line,
      tangent_point_dynamic
    )

    tangent_line=self.s_build_tangent_line(t.get_value())
    tangent_point=self.s_build_tangent_point(t.get_value())

    self.add(
      tangent_line,
      tangent_point
    )

    self.play(
      FadeOut(
        secant_line,
        tangent_line,
        tangent_point
      )
    )

    self.play(Create(secant_line))

    t.set_value(self.x_A)

    bird=self.build_bird(
      t.get_value(),
      self.s
    )
    height=self.build_height(t.get_value())

    self.play(
      Create(bird),
      Create(height)
    )

    self.remove(
      bird,
      height
    )

    bird_dynamic=always_redraw(
      lambda:self.build_bird(
        t.get_value(),
        self.s
      )
    )
    height_dynamic=always_redraw(
      lambda:self.build_height(t.get_value())
    )

    self.add(
      bird_dynamic,
      height_dynamic
    )

    self.play(
      t.animate.set_value(self.x_B),
      run_time=2.5
    )
    self.play(t.animate.set_value(self.x_A))

    self.wait(0.5)

    self.play(
      t.animate.set_value(self.x_B),
      run_time=5
    )

    self.wait(0.5)

    self.play(t.animate.set_value(self.x_C))

    self.remove(
      bird_dynamic,
      height_dynamic
    )

    bird=self.build_bird(
      t.get_value(),
      self.s
    )
    height=self.build_height(t.get_value())

    self.add(
      bird,
      height
    )

    self.wait(0.5)

    self.play(
      FadeOut(
        bird,
        height
      )
    )

    t.set_value(self.x_A)

    tangent_line=self.s_build_tangent_line(t.get_value())
    bird=self.build_bird(t.get_value(),self.s)

    self.play(Create(bird))
    self.play(Create(tangent_line))

    self.remove(
      bird,
      tangent_line,
    )
    self.add(
      bird_dynamic,
      height_dynamic,
      tangent_line_dynamic
    )

    self.play(
      t.animate.set_value(self.x_B),
      run_time=5
    )

    point_C=self.coords.build_graph_dot(
      self.x_C,
      self.s,
      color=HIGHLIGHT_COLOR
    )
    point_C.set_z_index(4)

    self.play(Create(point_C))
    self.play(t.animate.set_value(self.x_C))

    self.wait(0.5)

    self.remove(tangent_line_dynamic)

    tangent_line=self.s_build_tangent_line(t.get_value())

    self.add(tangent_line)
    self.play(
      Blink(secant_line,blinks=2),
      Blink(tangent_line,blinks=2),
      run_time=0.6
    )

    # Part III
    self.remove(
      point_C,
      tangent_line,
      tangent_line_dynamic,
      bird_dynamic,
      height_dynamic
    )

    tangent_line=self.s_build_tangent_line(t.get_value())
    bird=self.build_bird(
      t.get_value(),
      self.s
    )
    height=self.build_height(t.get_value())

    self.add(
      tangent_line,
      bird,
      height
    )

    self.play(
      FadeOut(
        tangent_line,
        s_graph,
        secant_line,
        point_A,
        proj_A,
        point_B,
        proj_B,
        bird,
        height,
      )
    )

    h_graph=self.coords.axes.plot(lambda x:self.h(x))
    self.play(Create(h_graph))

    t.set_value(self.x_A)

    bird=self.build_bird(
      t.get_value(),
      self.h
    )
    h_tangent_line=self.h_build_tangent_line(t.get_value())

    self.play(Create(bird))
    self.play(Create(h_tangent_line))
    self.remove(
      bird,
      h_tangent_line
    )

    h_bird_dynamic=always_redraw(
      lambda:self.build_bird(
        t.get_value(),
        self.h
      )
    )
    h_tangent_line_dynamic=always_redraw(
      lambda:self.h_build_tangent_line(t.get_value())
    )

    self.add(
      h_bird_dynamic,
      h_tangent_line_dynamic
    )

    self.play(
      t.animate.set_value(self.x_B),
      run_time=2.5
    )
    self.play(t.animate.set_value(self.x_C))
    self.wait(0.5)
