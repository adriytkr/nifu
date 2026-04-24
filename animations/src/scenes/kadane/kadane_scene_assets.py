from manim import *

class KadaneSceneAssets(Scene):
  BG_COLOR=ManimColor('#1a1b26')

  CELL_COLOR=ManimColor('#24283b')

  SUBARRAY_COLORS=[
    ManimColor('#f7768e'),
    ManimColor('#bb9af7'),
    ManimColor('#73daca'),
    ManimColor('#ff9e64'),
    ManimColor('#9ece6a')
  ]

  BEST_SUM_DISPLAY_COLOR=ManimColor('#ffd700')
  CURRENT_SUM_DISPLAY_COLOR=ManimColor('#00e676')

  array=[4,-7,2,3,-6,1,5,-2]

  def play(
    self,
    *args,
    **kwargs
  ):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.6

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

    self.el_pointer=self.build_pointer()

    self._ks_best=float('-inf')
    self._ks_current=0
    self._ks_color=0

  def build_pointer(self)->Triangle:
    el_pointer=Triangle(
      fill_opacity=1,
      fill_color=PURE_YELLOW,
      stroke_width=0
    )
    el_pointer.scale(0.1)

    return el_pointer

  def move_pointer_to(
    self,
    target:int
  )->None:
    el=self.el_array[target]

    self.play(
      self.el_pointer.animate.next_to(
        el,
        DOWN,
        buff=0.3
      ),
    )

  def build_array(
    self,
    array:list[int]
  )->VGroup:
    elements=[]

    for idx,n in enumerate(array):
      el_square=Square(
        side_length=1,
        color=self.CELL_COLOR,
        fill_opacity=1,
        stroke_width=1.6,
      )

      el_value=MathTex(r'\boldsymbol{'+str(n)+'}')\
        .scale(0.8)\
        .move_to(el_square.get_center())

      el_index=MathTex(str(idx))\
        .scale(0.67)\
        .next_to(
          el_square,
          DOWN,
          buff=0.16
        )

      element=VGroup(el_square,el_value,el_index)
      elements.append(element)

    return VGroup(*elements).arrange(
      RIGHT,
      buff=0.1
    )

  def _advance_kadane(self,i:int)->bool:
    n=self.array[i]
    reset=i>0 and self._ks_current+n<n

    if i==0:
      self._ks_current=n
    elif reset:
      self._ks_current=n
      self._ks_color=(self._ks_color+1)%len(self.SUBARRAY_COLORS)
    else:
      self._ks_current+=n

    if self._ks_current>self._ks_best:
      self._ks_best=self._ks_current

    return reset

  def kadane_step(self,i:int)->list:
    reset=self._advance_kadane(i)
    color=self.SUBARRAY_COLORS[self._ks_color]

    return [
      *self.highlight_cell(i,color),
      *self.update_display(
        best=self._ks_best,
        curr=self._ks_current
      ),
    ]

  def highlight_cell(
    self,
    index:int,
    color:ManimColor
  )->list:
    return [self.el_array[index][0].animate.set_color(color)]

  def build_display(
    self,
    initial_value:int,
    color:ManimColor
  ):
    el_square=Square(
      side_length=1,
      color=color,
      fill_opacity=1,
      stroke_width=0
    )

    el_label=MathTex(r'\boldsymbol{'+str(initial_value)+'}')\
      .scale(0.75)\
      .move_to(el_square.get_center())

    return VGroup(el_square,el_label)

  def update_display(
    self,
    best:int,
    curr:int
  )->list:
    el_new_best_label=MathTex(r'\boldsymbol{'+str(best)+'}')\
      .scale(0.75)\
      .move_to(self.el_best_sum_display[0].get_center())

    el_new_cur_label=MathTex(r'\boldsymbol{'+str(curr)+'}')\
      .scale(0.75)\
      .move_to(self.el_current_sum_display[0].get_center())

    return [
      Transform(
        self.el_best_sum_display[1],
        el_new_best_label
      ),
      Transform(
        self.el_current_sum_display[1],
        el_new_cur_label
      )
    ]
