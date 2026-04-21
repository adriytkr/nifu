from manim import *

from src.scenes.rmq.video_scene_assets import VideoSceneAssets

class VideoScene(VideoSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    BG_COLOR=ManimColor('#121212')
    CELL_COLOR=BLACK
    HIGHLIGHT_COLOR=PURPLE
    HIGHLIGHT_COLOR2=GREEN
    HIGHLIGHT_COLOR3=BLUE

    self.camera.background_color=BG_COLOR


    # ---------------- Start Buff ----------------
    self.wait(1)


    # ---------------- Initial Array ----------------
    elements=[]
    for idx,n in enumerate(self.array):
      square=Square(
        side_length=1,
        fill_color=CELL_COLOR,
        fill_opacity=1,
        stroke_width=1.6,
        stroke_color=CELL_COLOR
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

    array_vgroup=VGroup(*elements)
    array_vgroup.arrange(
      RIGHT,
      buff=0.1
    )

    self.play(FadeIn(array_vgroup))


    # ---------------- Draw subarray ----------------
    start=2
    end=6
    animations=[]
    for row in range(start,end):
      animations.append(
        array_vgroup[row][0]
          .animate
          .set_color(HIGHLIGHT_COLOR)
      )

    self.play(*animations)


    # ---------------- Pointer Triangle ----------------
    pointer=Triangle(
      color=PURE_YELLOW,
      fill_color=PURE_YELLOW,
      fill_opacity=1
    )
    pointer.scale(0.1)

    first_el=array_vgroup[start]
    pointer.next_to(
      first_el,
      DOWN,
      buff=0.3
    )

    self.play(FadeIn(pointer))
    self.wait(0.3)


    # ---------------- Min Display ----------------
    current_min=self.array[start]

    min_display=Square(
      side_length=1,
      color=GREEN,
      stroke_width=1.6,
      fill_opacity=1
    )

    min_tex=MathTex(str(current_min)).scale(0.75)
    min_tex.move_to(min_display.get_center())

    min_display=VGroup(min_display,min_tex)
    min_display.next_to(
      array_vgroup,
      UP,
      buff=0.5
    )

    self.play(FadeIn(min_display))
    self.wait(0.3)


    # ---------------- Traverse subarray ----------------
    for row in range(start+1,end):
      target_el=array_vgroup[row]
      target_pos=pointer.copy().next_to(
        target_el,
        DOWN,
        buff=0.3
      )

      self.play(
        pointer.animate.move_to(target_pos.get_center()),
        run_time=0.5
      )
      self.wait(0.2)

      if self.array[row]<current_min:
        current_min=self.array[row]

        new_min_tex=MathTex(str(current_min)).scale(0.75)
        new_min_tex.move_to(min_display[0].get_center())

        self.play(Transform(min_tex,new_min_tex))
        self.wait(0.2)


    # ---------------- RESET ----------------
    animations=[]
    for row in range(start,end):
      animations.append(
        array_vgroup[row][0]
          .animate
          .set_color(CELL_COLOR)
      )

    self.play(
      *animations,
      FadeOut(min_display),
      FadeOut(pointer),
    )
    self.wait(0.5)


    # ---------------- Move array up and scale down ----------------
    array_vgroup.generate_target()
    for el in array_vgroup.target:
      el[2].next_to(
        el[0],
        LEFT,
        buff=0.3
      )

    array_vgroup.target\
      .scale(0.7)\
      .arrange(
        DOWN,
        buff=0.1
      )

    self.play(MoveToTarget(array_vgroup))
    self.wait(0.3)


    # ---------------- Sparse Table ----------------
    row_count=len(self.array)
    col_count=3
    cell_buff=0.1


    # ---------------- Rows ----------------
    st_rows=[]
    for row in range(row_count):
      row_els=[]
      for col in range(col_count):
        square=Square(
          side_length=0.7,
          color=CELL_COLOR,
          fill_opacity=1,
          stroke_width=1.6
        )

        try:
          st_val=self.st_table[row][col]
        except IndexError:
          st_val=None

        label=MathTex('' if st_val is None else st_val)\
          .scale(0.5)\
          .set_opacity(0)\
          .move_to(square.get_center())

        element=VGroup(square,label)
        row_els.append(element)

      row_vgroup=VGroup(*row_els)
      row_vgroup.arrange(
        RIGHT,
        buff=cell_buff
      )
      st_rows.append(row_vgroup)

    st_grid=VGroup(*st_rows)
    st_grid.arrange(
      DOWN,
      buff=cell_buff
    )


    # ---------------- Exponent Label ----------------
    col_labels=VGroup(*[
      MathTex(str(j)).scale(0.5)
      for j in range(col_count)
    ])


    # ---------------- Index Label ----------------
    row_labels=VGroup(*[
      MathTex(str(i)).scale(0.5)
      for i in range(row_count)
    ])


    # ---------------- Draw Sparse Table ----------------
    table_group=VGroup(
      st_grid,
      col_labels,
      row_labels
    )
    table_group.next_to(
      array_vgroup,
      RIGHT,
      buff=1.6
    )

    for row_idx in range(row_count):
        st_grid[row_idx].align_to(
          array_vgroup[row_idx][0],
          UP
        )
        row_labels[row_idx]\
          .move_to(
            st_grid[row_idx],
            LEFT
          )\
          .shift(LEFT*0.4)

    for j,lbl in enumerate(col_labels):
      lbl.next_to(
        st_rows[0][j],
        UP,
        buff=0.16
      )

    for row,lbl in enumerate(row_labels):
      lbl.next_to(
        st_rows[row][0],
        LEFT,
        buff=0.16
      )

    self.play(
      FadeIn(st_grid),
      FadeIn(row_labels),
      FadeIn(col_labels)
    )

    # ---------------- Align Center ----------------
    main=VGroup(array_vgroup,table_group)
    self.play(main.animate.move_to(ORIGIN))


    # ---------------- Highlight (idx=3,exp=2) ----------------
    self.play(
      st_grid[3][2][0]
        .animate
        .set_color(HIGHLIGHT_COLOR)
    )


    # ---------------- Highlight N[3:7] ----------------
    self.play(*[
      elements[row][0]
        .animate
        .set_fill(HIGHLIGHT_COLOR,opacity=1)
        .set_stroke(HIGHLIGHT_COLOR)
      for row in range(3,7)
    ])


    # ---------------- Write cell(idx=3,exp=2) ----------------
    self.play(st_grid[3][2][1].animate.set_opacity(1))


    # ---------------- RESET ----------------
    self.play(
      st_rows[3][2][0]
        .animate
        .set_color(CELL_COLOR),
      st_grid[3][2][1].animate.set_opacity(0),
      *[
        elements[row][0]
          .animate
          .set_color(CELL_COLOR)
        for row in range(3,7)
      ]
    )


    # ---------------- Fill first two columns (exp=0),(exp=1) ----------------
    animations=[]

    for col in [0,1]:
      for row in range(row_count):
        cell_label=st_grid[row][col][1]

        if cell_label.tex_string=='':
          continue

        animations.append(
          cell_label.animate.set_opacity(1)
        )

    self.play(
      LaggedStart(*animations,lag_ratio=0.15),
      run_time=1.5
    )

    # ---------------- Example: st_table[2][0] ----------------

    # ---------------- Highlight st_table[2][0] ----------------
    self.play(st_grid[0][2][0].animate.set_color(PURPLE))


    # ---------------- Highlight N[0:4] ----------------
    self.play(*[
      elements[row][0]
        .animate
        .set_color(HIGHLIGHT_COLOR)
      for row in range(0,4)
    ])


    # ---------------- Two subarrays ----------------
    self.play(
      *[
        elements[row][0]
          .animate
          .set_color(HIGHLIGHT_COLOR2)
        for row in range(0,2)
      ],
      *[
        elements[row][0]
          .animate
          .set_color(HIGHLIGHT_COLOR3)
        for row in range(2,4)
      ]
    )


    # ---------------- Highlight (idx=0,exp=1), (idx=2,exp=1) ----------------
    self.play(
      st_grid[0][1][0].animate.set_color(HIGHLIGHT_COLOR2),
      st_grid[2][1][0].animate.set_color(HIGHLIGHT_COLOR3),
    )


    # ---------------- Write (idx=0,exp=2) ----------------
    self.play(st_grid[0][2][1].animate.set_opacity(1))


    # ---------------- RESET ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(CELL_COLOR)
        for row in range(0,4)
      ],
      st_grid[0][1][0].animate.set_color(CELL_COLOR),
      st_grid[2][1][0].animate.set_color(CELL_COLOR),
      st_grid[0][2][0].animate.set_color(CELL_COLOR)
    )


    # ---------------- Fill Rest of the table ----------------
    animations=[]

    for col in [2]:
      for row in range(1,row_count):
        cell_label=st_grid[row][col][1]

        if cell_label.tex_string=='':
          continue

        animations.append(cell_label.animate.set_opacity(1))

    self.play(
      LaggedStart(*animations,lag_ratio=0.15),
      run_time=1.5
    )


    # ---------------- Example 1 ----------------

    # ---------------- Highlight subarray ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(HIGHLIGHT_COLOR)
        for row in range(1,5)
      ]
    )

    # ---------------- Highlight cell ----------------
    self.play(st_grid[1][2][0].animate.set_color(HIGHLIGHT_COLOR))


    # ---------------- RESET ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(CELL_COLOR)
        for row in range(1,5)
      ],
      st_grid[1][2][0].animate.set_color(CELL_COLOR)
    )


    # ---------------- Example 2 ----------------

    # ---------------- Highlight subarray ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(HIGHLIGHT_COLOR)
        for row in range(1,6)
      ]
    )


    # ---------------- Leftmost lookup ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(HIGHLIGHT_COLOR2)
        for row in range(1,5)
      ]
    )


    # ---------------- Leftmost lookup: highlight cell ----------------
    self.play(st_grid[1][2][0].animate.set_color(HIGHLIGHT_COLOR2))


    # ---------------- Reset Leftmost lookup ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(HIGHLIGHT_COLOR)
        for row in range(1,5)
      ]
    )


    # ---------------- Rightmost lookup ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(HIGHLIGHT_COLOR3)
        for row in range(2,6)
      ]
    )


    # ---------------- Rightmost lookup: highlight cell ----------------
    self.play(st_grid[2][2][0].animate.set_color(HIGHLIGHT_COLOR3))


    # ---------------- Reset rightmost lookup ----------------
    self.play(
      *[
        elements[row][0].animate.set_color(HIGHLIGHT_COLOR)
        for row in range(2,6)
      ]
    )


    # ---------------- End Buff ----------------
    self.wait(1)
