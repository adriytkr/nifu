from manim import *

from src.scenes.rmq.rmq_scene_assets import RMQSceneAssets

class RMQScene(RMQSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Start Buff ----------------
    self.wait(1)



    # ---------------- Begin ----------------
    self.play(FadeIn(self.array_vgroup))



    # ---------------- Traverse subarray ----------------
    self.play(
      *self.highlight_subarray(2,6,self.HIGHLIGHT_COLOR),
    )
    pointer=self.create_pointer()
    pointer.next_to(
      self.array_vgroup[2],
      DOWN,
      buff=0.3
    )
    self.play(FadeIn(pointer))

    current_min=self.array[2]
    min_display=self.create_min_display(current_min)
    self.play(FadeIn(min_display))

    for row in range(3,6):
      target_el=self.array_vgroup[row]
      target_pos=pointer.copy().next_to(
        target_el,
        DOWN,
        buff=0.3
      )

      self.play(pointer.animate.move_to(target_pos.get_center()))

      if self.array[row]<current_min:
        current_min=self.array[row]

        new_min_tex=MathTex(str(current_min)).scale(0.75)
        new_min_tex.move_to(min_display[0].get_center())

        self.play(Transform(min_display[1],new_min_tex))
        self.wait(0.2)

    self.play(
      *self.highlight_subarray(2,6,self.CELL_COLOR),
      FadeOut(min_display),
      FadeOut(pointer),
    )



    # ---------------- Give room to Sparse Table ----------------
    self.array_vgroup.generate_target()
    for el in self.array_vgroup.target:
      el[2].next_to(
        el[0],
        LEFT,
        buff=0.3
      )

    self.array_vgroup.target\
      .scale(0.7)\
      .arrange(
        DOWN,
        buff=0.1
      )

    self.play(MoveToTarget(self.array_vgroup))
    self.wait(0.3)



    # ---------------- Draw Sparse Table ----------------
    col_labels=VGroup(*[
      MathTex(str(j)).scale(0.5)
      for j in range(self.COLUMN_COUNT)
    ])

    row_labels=VGroup(*[
      MathTex(str(i)).scale(0.5)
      for i in range(self.ROW_COUNT)
    ])

    table_group=VGroup(
      self.st_grid,
      col_labels,
      row_labels
    )
    
    table_group.next_to(
      self.array_vgroup,
      RIGHT,
      buff=1.6
    )

    for row_idx in range(self.ROW_COUNT):
      self.st_grid[row_idx].align_to(
        self.array_vgroup[row_idx][0],
        UP
      )
      row_labels[row_idx].next_to(
        self.st_grid[row_idx],
        LEFT,
        buff=0.25
      )

    for j, lbl in enumerate(col_labels):
      lbl.next_to(
        self.st_grid[0][j],
        UP,
        buff=0.25
      )

    table_group.set_opacity(0)
    all_content=VGroup(
      self.array_vgroup,
      table_group
    )

    all_content.generate_target()
    all_content.target.move_to(ORIGIN)
    
    all_content.target[1].set_opacity(1)

    for row in all_content.target[1][0]: 
      for cell in row:
        cell[1].set_opacity(0)

    self.play(MoveToTarget(all_content))



    # ---------------- Get the gist of how Sparse Table works ----------------
    self.play(self.highlight_st_cell(3,2,self.HIGHLIGHT_COLOR))
    self.play(*self.highlight_subarray(3,7,self.HIGHLIGHT_COLOR))
    self.play(self.st_grid[3][2][1].animate.set_opacity(1))
    self.play(
      self.highlight_st_cell(3,2,self.CELL_COLOR),
      self.st_grid[3][2][1].animate.set_opacity(0),
      *self.highlight_subarray(3,7,self.CELL_COLOR)
    )



    # ---------------- Fill first two columns (exp=0),(exp=1) ----------------
    animations=[]

    for col in [0,1]:
      for row in range(self.ROW_COUNT):
        cell_label=self.st_grid[row][col][1]

        if cell_label.tex_string=='':
          continue

        animations.append(cell_label.animate.set_opacity(1))

    self.play(
      LaggedStart(*animations,lag_ratio=0.15),
      run_time=1.5
    )



    # ---------------- Example to see how to fill Sparse Table correctly ----------------
    self.play(self.highlight_st_cell(0,2,self.HIGHLIGHT_COLOR))
    self.play(*self.highlight_subarray(0,4,self.HIGHLIGHT_COLOR))
    self.play(
      *self.highlight_subarray(0,2,self.HIGHLIGHT_COLOR2),
      *self.highlight_subarray(2,4,self.HIGHLIGHT_COLOR3)
    )
    self.play(
      self.highlight_st_cell(0,1,self.HIGHLIGHT_COLOR2),
      self.highlight_st_cell(2,1,self.HIGHLIGHT_COLOR3)
    )
    self.play(self.st_grid[0][2][1].animate.set_opacity(1))
    self.play(
      *self.highlight_subarray(0,4,self.CELL_COLOR),
      self.highlight_st_cell(0,1,self.CELL_COLOR),
      self.highlight_st_cell(2,1,self.CELL_COLOR),
      self.highlight_st_cell(0,2,self.CELL_COLOR)
    )



    # ---------------- Fill rest of the Sparse Table ----------------
    animations=[]

    for col in [2]:
      for row in range(1,self.ROW_COUNT):
        cell_label=self.st_grid[row][col][1]

        if cell_label.tex_string=='':
          continue

        animations.append(cell_label.animate.set_opacity(1))

    self.play(LaggedStart(*animations,lag_ratio=0.15))



    # ---------------- Example 1 ----------------
    # ---------------- Highlight subarray ----------------
    self.play(*self.highlight_subarray(1,5,self.HIGHLIGHT_COLOR))
    self.play(self.highlight_st_cell(1,2,self.HIGHLIGHT_COLOR))
    self.play(
      *self.highlight_subarray(1,5,self.CELL_COLOR),
      self.highlight_st_cell(1,2,self.CELL_COLOR)
    )



    # ---------------- Example 2 ----------------
    # ---------------- Highlight subarray ----------------
    self.play(*self.highlight_subarray(1,6,self.HIGHLIGHT_COLOR))


    # ---------------- Left Lookup ----------------
    self.play(*self.highlight_subarray(1,5,self.HIGHLIGHT_COLOR2))
    self.play(self.highlight_st_cell(1,2,self.HIGHLIGHT_COLOR2))
    self.play(*self.highlight_subarray(1,5,self.HIGHLIGHT_COLOR))


    # ---------------- Right Lookup ----------------
    self.play(*self.highlight_subarray(2,6,self.HIGHLIGHT_COLOR3))
    self.play(self.highlight_st_cell(2,2,self.HIGHLIGHT_COLOR3))
    self.play(*self.highlight_subarray(2,6,self.HIGHLIGHT_COLOR))


    # ---------------- End Buff ----------------
    self.wait(1)
