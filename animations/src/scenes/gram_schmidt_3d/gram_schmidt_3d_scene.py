from manim import *

from src.scenes.gram_schmidt_3d.gram_schmidt_3d_scene_assets import GramSchmidt3DAssets

class GramSchmidt3DScene(GramSchmidt3DAssets):
  def construct(self):
    self.camera.background_color=self.BG_COLOR

    self.set_camera_orientation(
      phi=70*DEGREES,
      theta=45*DEGREES
    )



    # ---------------- Planes ----------------
    xy_plane=self.build_xy_plane()
    xz_plane=self.build_xz_plane()

    self.play(
      Create(xy_plane),
      Create(xz_plane)
    )



    # ---------------- Point arrows ----------------
    v1_point=self.build_point_arrow(self.VECTOR_COLOR)
    v2_point=self.build_point_arrow(self.VECTOR_COLOR)
    v3_point=self.build_point_arrow(self.VECTOR_COLOR)

    self.add(v1_point,v2_point,v3_point)



    # ---------------- Full arrows ----------------
    v1_full=self.build_arrow(self.v1,self.VECTOR_COLOR)
    v2_full=self.build_arrow(self.v2,self.VECTOR_COLOR)
    v3_full=self.build_arrow(self.v3,self.VECTOR_COLOR)



    # ---------------- Grow via Transform ----------------
    self.play(
      Transform(v1_point,v1_full),
      Transform(v2_point,v2_full),
      Transform(v3_point,v3_full)
    )



    self.wait(1)
