from manim import *
from src.scenes.quick_hull.quick_hull_scene_assets import QuickHullSceneAssets
import numpy as np
class QuickHullScene(QuickHullSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Begin Buff ----------------
    self.wait(1)



    # ---------------- Begin ----------------
    n=len(self.points)
    dots=[
      self.build_dot(p,self.DOT_COLOR)
      for p in self.points
    ]

    self.play(
      LaggedStart(*[
        FadeIn(d) for d in dots],
        lag_ratio=0.1
      )
    )



    # ---------------- Leftmost and rightmost ----------------
    left_idx=min(
      range(n),
      key=lambda i:self.points[i][0]
    )
    right_idx=max(
      range(n),
      key=lambda i:self.points[i][0]
    )

    self.play(
      dots[left_idx].animate
        .set_color(self.HULL_COLOR)
        .scale(1.5),
      dots[right_idx].animate
        .set_color(self.HULL_COLOR)
        .scale(1.5)
    )



    # ---------------- Initial dividing line ----------------
    init_div=self.build_dashed_line(
      start=self.points[left_idx],
      end=self.points[right_idx],
      color=self.DIVIDER_COLOR
    )

    self.play(Create(init_div))

    inner=[
      i for i in range(n)
      if i!=left_idx and i!=right_idx
    ]

    upper=[
      i for i in inner
      if self.signed_dist(
        self.points[i],
        self.points[left_idx],
        self.points[right_idx]
      )>0
    ]

    lower=[
      i for i in inner
      if self.signed_dist(
        self.points[i],
        self.points[right_idx],
        self.points[left_idx]
      )>0
    ]

    self.play(FadeOut(init_div))



    # ---------------- Stack-based quick hull ----------------
    stack=[
      (left_idx,right_idx,upper),
      (right_idx,left_idx,lower),
    ]

    hull_lines=[]
    hull_dot_indices=set([left_idx,right_idx])

    while stack:
      a_idx,b_idx,candidates=stack.pop()
      a=self.points[a_idx]
      b=self.points[b_idx]

      if not candidates:
        hl=self.build_line(a,b,self.HULL_COLOR)
        hull_lines.append(hl)

        self.play(Create(hl))
        continue

      # ---------------- Show dividing line and candidates ----------------
      div_line=self.build_dashed_line(
        start=a,
        end=b,
        color=self.DIVIDER_COLOR
      )

      self.play(Create(div_line))
      self.play(*[
        dots[i].animate.set_color(self.CANDIDATE_COLOR) for i in candidates],
        run_time=0.3
      )

      # ---------------- Find and show max distance point ----------------
      max_idx=max(
        candidates,
        key=lambda i:self.signed_dist(
          self.points[i],
          a,
          b
        )
      )

      ab=b-a
      ab_norm=ab/np.linalg.norm(ab)

      foot=a+np.dot(self.points[max_idx]-a,ab_norm)*ab_norm

      dist_line=self.build_dashed_line(
        start=self.points[max_idx],
        end=foot,
        color=self.BEST_COLOR
      )

      self.play(
        Create(dist_line),
        dots[max_idx].animate
          .set_color(self.BEST_COLOR)
          .scale(1.3)
      )
      hull_dot_indices.add(max_idx)

      # ---------------- Split and reject ----------------
      remaining=[i for i in candidates if i!=max_idx]

      left_of_ap=[
        i for i in remaining
        if self.signed_dist(
          self.points[i],
          a,
          self.points[max_idx]
        )>0
      ]

      left_of_pb=[
        i for i in remaining
        if self.signed_dist(
          self.points[i],
          self.points[max_idx],
          b
        )>0
      ]

      rejected=[i for i in remaining if i not in left_of_ap and i not in left_of_pb]

      animations=[]

      if rejected:
        animations+=[
          dots[i].animate.set_color(self.REJECT_COLOR)
          for i in rejected
        ]

      self.play(
        FadeOut(
          div_line,
          dist_line
        ),
        *animations
      )

      stack.append((a_idx,max_idx,left_of_ap))
      stack.append((max_idx,b_idx,left_of_pb))



    # ---------------- Finale ----------------
    hull_idx_list=list(hull_dot_indices)
    centroid=np.mean([
      self.points[i]
      for i in hull_idx_list],
      axis=0
    )

    hull_idx_list.sort(
      key=lambda i:np.arctan2(
        self.points[i][1]-centroid[1],
        self.points[i][0]-centroid[0]
      )
    )

    hull_positions=[
      self.points[i]
      for i in hull_idx_list
    ]

    hull_dots_list=[
      dots[i]
      for i in hull_idx_list
    ]

    self.play_hull_finish(
      hull_dots_list,
      hull_lines,
      hull_positions
    )



    # ---------------- End Buff ----------------
    self.wait(1)
