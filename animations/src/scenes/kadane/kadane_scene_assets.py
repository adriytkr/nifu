from manim import *

from typing import Optional

class KadaneSceneAssets(Scene):
  array=[4,-7,2,3,-6,1,5,-2]

  BG_COLOR=ManimColor('#1a1b26')
  CELL_COLOR=BLACK
  BEST_SUM_DISPLAY_COLOR=ManimColor("#8ed245")
  CURRENT_SUM_DISPLAY_COLOR=ManimColor("#4b7be5")

  SUBARRAY_COLORS=[
    ManimColor('#e06c75'),
    ManimColor('#e5c07b'),
    ManimColor('#56b6c2'),
    ManimColor('#c678dd'),
    ManimColor('#98c379')
  ]

  def play(
    self,
    *args,
    **kwargs
  ):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.5

    super().play(*args,**kwargs)

  def setup(self):
    self.el_array=self.build_array(self.array)

    self.el_best_sum_display=self.build_display(
      self.array[0],
      self.BEST_SUM_DISPLAY_COLOR
    )

    self.el_current_sum_display=self.build_display(
      self.array[0],
      self.CURRENT_SUM_DISPLAY_COLOR
    )

    self.pointer=self.build_pointer()

    self._ks_best=float('-inf')
    self._ks_current=0
    self._ks_color=0

  def build_pointer(self):
    return Triangle(
      fill_opacity=1,
      fill_color=PURE_YELLOW,
      stroke_width=0
    ).scale(0.1)

  def move_pointer_to(self,target:int)->None:
    el=self.el_array[target]

    self.play(
      self.pointer.animate.next_to(
        el,
        DOWN,
        buff=0.3
      ),
    )

  def build_array(self,array:list[int]):
    elements=[]

    for idx,n in enumerate(array):
      square=Square(
        side_length=1,
        fill_color=self.CELL_COLOR,
        fill_opacity=1,
        stroke_width=1.6,
        stroke_color=self.CELL_COLOR,
      )

      label=MathTex(str(n)).scale(0.75)
      label.move_to(square.get_center())

      el_index=MathTex(idx)\
        .scale(0.75)\
        .next_to(
          square,
          DOWN,
          buff=0.16
        )

      element=VGroup(square,label,el_index)
      elements.append(element)

    return VGroup(*elements).arrange(RIGHT,buff=0.1)

  def kadane_step(
    self,
    i:int,
    start:int=0
  )->list:
    n=self.array[i]

    if i==start:
      self._ks_current=n
    elif self._ks_current+n<n:
      self._ks_current=n
      self._ks_color=(self._ks_color+1)%len(self.SUBARRAY_COLORS)
    else:
      self._ks_current+=n

    if self._ks_current>self._ks_best:
      self._ks_best=self._ks_current

    color=self.SUBARRAY_COLORS[self._ks_color]

    return [
      *self.highlight(i,i+1,color=color),
      *self.update_display(
        best=self._ks_best,
        curr=self._ks_current
      ),
    ]

  def highlight(
    self,
    start:int,
    end:int,
    color:ManimColor
  )->None:
    return [
      el[0].animate.set_color(color)
      for el in self.el_array[start:end]
    ]

  def build_display(
    self,
    initial_value:Optional[int],
    color:ManimColor
  ):
    square=Square(
      side_length=1,
      color=color,
      fill_opacity=1,
      stroke_width=0
    )

    if initial_value is None:
      label=MathTex('').scale(0.75)
    else:
      label=MathTex(str(initial_value)).scale(0.75)

    label.move_to(square.get_center())

    return VGroup(square,label)

  def update_display(
    self,
    best:int,
    curr:int
  ):
    new_best_label=MathTex(str(best))\
      .scale(0.75)\
      .move_to(self.el_best_sum_display[0].get_center())

    new_cur_label=MathTex(str(curr))\
      .scale(0.525)\
      .move_to(self.el_current_sum_display[0].get_center())

    return (
      Transform(
        self.el_best_sum_display[1],
        new_best_label
      ),
      Transform(
        self.el_current_sum_display[1],
        new_cur_label
      )
    )
