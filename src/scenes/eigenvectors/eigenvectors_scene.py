from manim import *
import numpy as np
from src.scenes.eigenvectors.eigenvectors_scene_assets import EigenvectorsSceneAssets


class EigenvectorsScene(EigenvectorsSceneAssets):

  def construct(self):

    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR

    # ---------------- Start Buff ----------------
    self.wait(1)

    # ---------------- Axes ----------------
    self.play(FadeIn(self.coords))

    # ---------------- Non-eigenvector example ----------------
    el_non_eigen=self.build_vec(self.non_eigen_v)
    self.play(GrowArrow(el_non_eigen))

    lbl_non_eigen=self.build_vec_label('u')\
      .next_to(
        el_non_eigen.get_end(),
        DOWN*2,
        buff=0.15
      )
    self.play(FadeIn(lbl_non_eigen))

    el_non_eigen_span=self.build_span(self.non_eigen_v)
    lbl_non_eigen_span=self.build_span_label('u')\
      .next_to(
        self.span_label_pos(self.non_eigen_v),
        RIGHT+DOWN*0.2,
        buff=0.15
      )
    self.play(
      FadeIn(
        el_non_eigen_span,
        lbl_non_eigen_span
      )
    )

    self.play(
      *self.mv(
        self.matrix,el_non_eigen,
        labels=[lbl_non_eigen]
      )
    )

    self.play(
      FadeOut(
        el_non_eigen,
        lbl_non_eigen,
        el_non_eigen_span,
        lbl_non_eigen_span
      )
    )

    # ---------------- Eigenvector 1 ----------------
    el_eigen_v1=self.build_vec(self.eigen_v1)
    self.play(GrowArrow(el_eigen_v1))

    lbl_eigen_v1=self.build_vec_label('v')\
      .next_to(
        el_eigen_v1.get_end(),
        DOWN*2,
        buff=0.15
      )
    self.play(FadeIn(lbl_eigen_v1))

    el_v1_span=self.build_span(self.eigen_v1)
    lbl_v1_span=self.build_span_label('v')\
      .next_to(
        self.span_label_pos(self.eigen_v1),
        DOWN*2,
        buff=0.15
      )
    self.play(
      FadeIn(
        el_v1_span,
        lbl_v1_span
      ),
    )

    self.play(
      *self.mv(
        self.matrix,el_eigen_v1,
        labels=[lbl_eigen_v1]
      )
    )

    self.play(
      FadeOut(
        el_eigen_v1,
        lbl_eigen_v1
      )
    )

    family=self.build_eigen_family(self.eigen_v1)
    self.play(GrowArrow(v) for v in family)

    self.play(
      *self.mv(
        self.matrix,
        *family
      )
    )

    self.remove(el_v1_span)
    self.play(
      FadeOut(
        *family,
        lbl_v1_span
      )
    )

    # ---------------- No eigenvectors (rotation) ----------------
    no_eigen_family=self.build_circle_family()
    self.play(GrowArrow(v) for v in no_eigen_family)

    self.play(
      *self.mv(
        self.rotation_matrix,
        *no_eigen_family
      )
    )

    self.play(FadeOut(*no_eigen_family))

    # ---------------- End Buff ----------------
    self.wait(1)
