from manim import *


class RMQSceneAssets(Scene):
  BG_COLOR=ManimColor('#1a1b26')

  CELL_COLOR=BLACK
  CELL_GAP=0.1

  HIGHLIGHT_COLOR=ManimColor('#7a41e4')
  HIGHLIGHT_COLOR2=ManimColor('#ffd700')
  HIGHLIGHT_COLOR3=ManimColor('#00e676')

  array=[1,3,7,4,2,-2,-3]
  st_table=[
    [1,1,1],
    [3,3,2],
    [7,4,-2],
    [4,2,-3],
    [2,2],
    [-2,-3],
    [-3],
  ]

  COLUMN_COUNT=3
  ROW_COUNT=len(array)

  def play(self,*args,**kwargs):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.6
    super().play(*args,**kwargs)

  def setup(self):
    elements=[]

    for idx,n in enumerate(self.array):
      square=Square(
        side_length=1,
        color=self.CELL_COLOR,
        fill_opacity=1,
        stroke_width=1.6,
      )
      label=MathTex(r'\mathbf{'+str(n)+'}').scale(0.75)
      label.move_to(square.get_center())
      el_index=(
        MathTex(idx)
        .scale(0.75)
        .next_to(square,DOWN,buff=0.15)
      )
      element=VGroup(square,label,el_index)
      elements.append(element)

    self.array_vgroup=VGroup(*elements).arrange(RIGHT,buff=self.CELL_GAP)

    st_rows=[]

    for row in range(self.ROW_COUNT):
      row_els=[]

      for col in range(self.COLUMN_COUNT):
        square=Square(
          side_length=0.7,
          color=self.CELL_COLOR,
          fill_opacity=1,
          stroke_width=1.6,
        )

        try:
          st_val=self.st_table[row][col]
        except IndexError:
          st_val=None

        label=(
          MathTex('' if st_val is None else r'\mathbf{'+str(st_val)+'}')
          .scale(0.5)
          .set_opacity(0)
          .move_to(square.get_center())
        )
        element=VGroup(square,label)
        row_els.append(element)

      row_vgroup=VGroup(*row_els).arrange(RIGHT,buff=self.CELL_GAP)
      st_rows.append(row_vgroup)

    self.st_grid=VGroup(*st_rows).arrange(DOWN,buff=self.CELL_GAP)

  def highlight_subarray(self,start:int,end:int,color:ManimColor):
    return [
      self.array_vgroup[i][0].animate.set_color(color)
      for i in range(start,end)
    ]

  def highlight_st_cell(self,row:int,col:int,color:ManimColor):
    return self.st_grid[row][col][0].animate.set_color(color)
