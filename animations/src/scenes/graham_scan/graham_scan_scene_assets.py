from manim import *
import numpy as np

class GrahamScanSceneAssets(Scene):
  BG_COLOR=ManimColor('#1a1b26')
  DOT_COLOR=ManimColor('#a9b1d6')
  CURRENT_COLOR=ManimColor('#e0af68')
  CANDIDATE_COLOR=ManimColor('#7dcfff')
  REJECT_COLOR=ManimColor('#f7768e')
  ACCEPT_COLOR=ManimColor('#9ece6a')
  HULL_COLOR=ManimColor('#f7768e')
  STACK_COLOR=ManimColor('#bb9af7')

  points=[
    np.array([-2.0,-3.5,0]),
    np.array([-4.0,-1.0,0]),
    np.array([-3.0,2.0,0]),
    np.array([3.5,1.5,0]),
    np.array([4.0,-1.5,0]),
    np.array([0.0,3.0,0]),
    np.array([2.0,-2.5,0]),
    np.array([0.0,0.5,0]),
    np.array([-0.5,-1.0,0]),
  ]

  def play(self,*args,**kwargs):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.6

    super().play(*args,**kwargs)

  def setup(self):
    pass

  def build_dot(
    self,
    pos,
    color:ManimColor
  )->Dot:
    return Dot(
      point=pos,
      color=color,
      radius=0.08
    )

  def build_line(
    self,
    start,
    end,
    color:ManimColor
  )->Line:
    return Line(
      start=start,
      end=end,
      color=color,
      stroke_width=2.5
    )

  def build_dashed_line(
    self,
    start,
    end,
    color:ManimColor
  )->DashedLine:
    return DashedLine(
      start=start,
      end=end,
      color=color,
      stroke_width=2,
      dash_length=0.15,
      dashed_ratio=0.5
    )

  def cross2d(self,o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

  def play_hull_finish(
    self,
    hull_dots,
    hull_lines,
    positions
  ):
    polygon=Polygon(
      *positions,
      fill_color=self.HULL_COLOR,
      fill_opacity=0,
      stroke_width=0
    )

    self.add(polygon)

    self.play(
      polygon.animate.set_fill(opacity=0.5),
      *[d.animate.scale(1.8) for d in hull_dots],
      *[l.animate.set_stroke(width=5) for l in hull_lines],
      run_time=0.3
    )

    self.play(
      polygon.animate.set_fill(opacity=0.15),
      *[d.animate.scale(1/1.8) for d in hull_dots],
      *[l.animate.set_stroke(width=2.5) for l in hull_lines],
      run_time=0.5
    )
