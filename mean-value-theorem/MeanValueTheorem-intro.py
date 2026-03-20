from manim import *
from utils.tangent import make_tangent_line
from utils.theme import NEUTRAL_COLOR,HIGHLIGHT_COLOR

class IntroScene(Scene):
  def construct(self):
    # Draw axes
    axes=Axes(
      x_range=[-3,4],
      y_range=[0,12]
    )

    self.play(FadeIn(axes))

    # Draw x^2
    f=lambda x:x**2+3
    graph=axes.plot(f)

    self.play(Create(graph))

    # Draw point A and point B
    x_A=-1
    point_A=Dot(axes.c2p(x_A,f(x_A)),color=NEUTRAL_COLOR)
    x_B=2
    point_B=Dot(axes.c2p(x_B,f(x_B)),color=NEUTRAL_COLOR)

    self.play(Create(point_A),Create(point_B))

    # Draw secant line
    dir=point_B.get_center()-point_A.get_center()
    secant_line=Line(
      start=point_A.get_center()-dir,
      end=point_B.get_center()+dir
    )

    self.play(Create(secant_line))

    # Draw point projections
    point_A_proj=axes.c2p(x_A,0)
    line_A=DashedLine(
      start=point_A.get_center(),
      end=point_A_proj
    )
    point_B_proj=axes.c2p(x_B,0)
    line_B=DashedLine(
      start=point_B.get_center(),
      end=point_B_proj
    )

    self.play(
      Create(line_A),
      Create(line_B),
      run_time=0.5
    )

    # Write point labels
    label_A=MathTex("a").next_to(point_A_proj,DOWN)
    label_B=MathTex("b").next_to(point_B_proj,DOWN)

    self.play(
      Write(label_A),
      Write(label_B)
    )

    # Draw movable point
    highlight=ValueTracker(0)
    t=ValueTracker(-1.5)

    def make_dot():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)

      x=t.get_value()
      dot=Dot(
        axes.c2p(x,f(x)),
        color=HIGHLIGHT_COLOR if highlight else WHITE
      )
      dot.set_color(color)

      return dot

    moving_point=always_redraw(make_dot)

    self.play(FadeIn(moving_point))

    # Draw tangent line
    derivative=lambda x:x*2
    static_tangent_line=make_tangent_line(axes.c2p,t.get_value(),f,derivative,5)

    self.play(Create(static_tangent_line))

    # Animate tangent line and point moving
    self.next_section('DEMO')

    def movable_tangent_line_logic():
      alpha=highlight.get_value()
      color=interpolate_color(WHITE,HIGHLIGHT_COLOR,alpha)

      x=t.get_value()
      line=make_tangent_line(axes.c2p,x,f,derivative,10)
      line.set_color(color)

      return line

    moving_tangent_line=always_redraw(movable_tangent_line_logic)

    self.remove(static_tangent_line)
    self.add(moving_tangent_line)

    self.play(t.animate.set_value(1.5))
    self.play(t.animate.set_value(0))

    # Highlight when tangent and secant lines become parallel
    self.play(t.animate.set_value(0.5))
    self.play(
      highlight.animate.set_value(1),
      secant_line.animate.set_color(HIGHLIGHT_COLOR),
      point_A.animate.set_opacity(0.5),
      point_B.animate.set_opacity(0.5),
      run_time=0.5
    )
