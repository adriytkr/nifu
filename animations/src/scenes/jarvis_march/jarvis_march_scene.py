from manim import *
import numpy as np

from src.scenes.jarvis_march.jarvis_march_scene_assets import JarvisMarchSceneAssets

class JarvisMarchScene(JarvisMarchSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Begin Buff----------------
    self.wait(1)



    # ---------------- Points ----------------
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

    self.play(
      dots[start_idx].animate
        .set_color(self.CURRENT_COLOR)
        .scale(1.5)
    )



    # ---------------- Jarvis March ----------------
    hull_indices=[start_idx]
    current_idx=start_idx
    current_pos=start
    prev_dir=np.array([1.0,0.0,0.0])
    hull_lines=[]

    while True:
      ref_ray=self.build_dashed_line(
        start=current_pos,
        end=current_pos+prev_dir*1.5,
        color=self.CURRENT_COLOR
      )

      self.play(Create(ref_ray))

      others=[
        i for i in range(len(self.points))
        if i!=current_idx and (i not in hull_indices or i==start_idx)
      ]

      best_idx=None
      best_pos=None
      best_dir=None
      check_line=None
      arc=None
      best_line=None
      prev_angle=np.arctan2(
        prev_dir[1],
        prev_dir[0]
      )

      for i in others:
        pos=self.points[i]
        cand_dir=(pos-current_pos)/np.linalg.norm(pos-current_pos)

        cand_angle=np.arctan2(
          cand_dir[1],
          cand_dir[0]
        )

        swept=(cand_angle-prev_angle)%(2*np.pi)

        new_check=self.build_dashed_line(
          start=current_pos,
          end=pos,
          color=self.CANDIDATE_COLOR
        )

        new_arc=Arc(
          radius=0.5,
          start_angle=prev_angle,
          angle=swept,
          color=self.CANDIDATE_COLOR,
          arc_center=current_pos
        )

        if check_line is None:
          check_line=new_check
          arc=new_arc

          self.play(
            Create(check_line),
            Create(arc)
          )
        else:
          self.play(
            Transform(check_line,new_check),
            Transform(arc,new_arc)
          )

        is_better=(best_idx is None) or (np.cross(best_dir,cand_dir)[2]>0)

        if is_better:
          new_best=self.build_dashed_line(
            start=current_pos,
            end=pos,
            color=self.BEST_COLOR
          )

          if best_line is None:
            best_line=new_best
            self.play(Create(best_line))
          else:
            self.play(Transform(best_line,new_best))

          best_idx=i
          best_pos=pos
          best_dir=cand_dir

      hull_line=self.build_line(
        start=current_pos,
        end=best_pos,
        color=self.HULL_COLOR
      )
      hull_lines.append(hull_line)

      self.play(
        Create(hull_line),
        FadeOut(check_line,arc,best_line,ref_ray)
      )

      self.play(
        dots[best_idx].animate.set_color(self.HULL_COLOR)
      )

      if best_idx==start_idx:
        break

      current_idx=best_idx
      current_pos=best_pos
      prev_dir=best_dir
      hull_indices.append(current_idx)

    

    # ---------------- Finale ----------------
    hull_positions=[
      self.points[i]
      for i in hull_indices+[start_idx]
    ]
    hull_dots=[
      dots[i]
      for i in hull_indices+[start_idx]
    ]

    self.play_hull_finish(hull_dots,hull_lines,hull_positions)



    # ---------------- End Buff ----------------
    self.wait(1)
