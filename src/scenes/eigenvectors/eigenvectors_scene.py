from manim import *

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

    el_non_eigen_span=self.build_span(self.non_eigen_v)
    self.play(FadeIn(el_non_eigen_span))

    self.play(*self.mv(self.matrix,el_non_eigen))

    self.play(FadeOut(el_non_eigen,el_non_eigen_span))

    # ---------------- Eigenvector 1 ----------------
    el_eigen_v1=self.build_vec(self.eigen_v1)
    self.play(GrowArrow(el_eigen_v1))

    el_v1_span=self.build_span(self.eigen_v1)
    self.play(FadeIn(el_v1_span))

    self.play(*self.mv(self.matrix,el_eigen_v1))
    self.play(FadeOut(el_eigen_v1))

    family=self.build_eigen_family(self.eigen_v1)
    self.play(GrowArrow(v) for v in family)

    self.play(*self.mv(self.matrix,*family))

    self.remove(el_v1_span)
    self.play(FadeOut(*family))

    # ---------------- Eigenvector 2 ----------------
    el_eigen_v2=self.build_vec(self.eigen_v2)
    self.play(GrowArrow(el_eigen_v2))

    el_v2_span=self.build_span(self.eigen_v2)
    self.play(FadeIn(el_v2_span))

    self.play(*self.mv(self.matrix,el_eigen_v2))
    self.play(FadeOut(el_eigen_v2,el_v2_span))

    # ---------------- No eigenvectors (rotation) ----------------
    no_eigen_family=self.build_circle_family()
    self.play(GrowArrow(v) for v in no_eigen_family)

    self.play(*self.mv(self.rotation_matrix,*no_eigen_family))
    self.play(FadeOut(*no_eigen_family))

    # ---------------- End Buff ----------------
    self.wait(1)
