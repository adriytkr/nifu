from manim import *
from src.scenes.graham_scan.graham_scan_scene_assets import GrahamScanSceneAssets
import numpy as np
class GrahamScanScene(GrahamScanSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Begin Buff ----------------
    self.wait(1)



    # ---------------- Begin ----------------
    dots=[
      self.build_dot(p,self.DOT_COLOR)
      for p in self.points
    ]

    self.play(
      LaggedStart(
        *[FadeIn(d) for d in dots],
        lag_ratio=0.1
      )
    )



    # ---------------- Start point ----------------
    start_idx=min(
      range(len(self.points)),
      key=lambda i:(
        self.points[i][1],
        self.points[i][0]
      )
    )
    start=self.points[start_idx]

    self.play(dots[start_idx].animate.set_color(self.CURRENT_COLOR).scale(1.5))




    # ---------------- Sort by polar angle ----------------
    others=[i for i in range(len(self.points)) if i!=start_idx]

    def polar_angle(i):
      d=self.points[i]-start

      return np.arctan2(d[1],d[0])

    sorted_indices=sorted(others,key=polar_angle)



    # animate sorting: draw dashed lines in polar order
    sort_lines=[]

    for i in sorted_indices:
      line=self.build_dashed_line(
        start=start,
        end=self.points[i],
        color=self.CANDIDATE_COLOR
      )

      sort_lines.append(line)
      self.play(
        Create(line),
        dots[i].animate.set_color(self.CANDIDATE_COLOR),
        run_time=0.3
      )

    self.play(*[FadeOut(l) for l in sort_lines])
    self.play(
      *[
        dots[i].animate.set_color(self.DOT_COLOR)
        for i in sorted_indices
      ]
    )



    # ---------------- Stack walk ----------------
    stack_indices=[start_idx,sorted_indices[0]]
    self.play(
      dots[sorted_indices[0]].animate.set_color(self.STACK_COLOR)
    )

    stack_lines=[]

    init_line=self.build_line(
      start=start,
      end=self.points[sorted_indices[0]],
      color=self.STACK_COLOR
    )

    stack_lines.append(init_line)

    self.play(Create(init_line))

    for i in sorted_indices[1:]:
      pos=self.points[i]

      self.play(dots[i].animate.set_color(self.CURRENT_COLOR))

      # show candidate line
      cand_line=self.build_dashed_line(
        start=self.points[stack_indices[-1]],
        end=pos,
        color=self.CANDIDATE_COLOR
      )

      self.play(Create(cand_line))



      # check and pop
      while len(stack_indices)>=2:
        o=self.points[stack_indices[-2]]
        a=self.points[stack_indices[-1]]
        b=pos
        turn=self.cross2d(o,a,b)

        if turn<=0:
          # right turn or collinear — pop
          popped=stack_indices.pop()

          self.play(
            dots[popped].animate.set_color(self.REJECT_COLOR),
            FadeOut(stack_lines.pop())
          )
        else:
          break



      # push
      new_line=self.build_line(
        start=self.points[stack_indices[-1]],
        end=pos,
        color=self.STACK_COLOR
      )

      stack_lines.append(new_line)

      self.play(
        FadeOut(cand_line),
        Create(new_line),
        dots[i].animate.set_color(self.STACK_COLOR)
      )
      stack_indices.append(i)



    # ---------------- Close hull ----------------
    close_line=self.build_line(
      start=self.points[stack_indices[-1]],
      end=start,
      color=self.STACK_COLOR
    )

    self.play(Create(close_line))
    stack_lines.append(close_line)



    # ---------------- Repaint hull ----------------
    self.play(
      *[
        l.animate.set_color(self.HULL_COLOR)
        for l in stack_lines
      ],
      *[
        dots[i].animate.set_color(self.HULL_COLOR)
        for i in stack_indices
      ]
    )

    hull_positions=[
      self.points[i]
      for i in stack_indices
    ]

    hull_dots=[
      dots[i]
      for i in stack_indices
    ]

    self.play_hull_finish(
      hull_dots,
      stack_lines,
      hull_positions
    )



    # ---------------- End Buff ----------------
    self.wait(1)
