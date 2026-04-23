from manim import *
import numpy as np

class GramSchmidt3DAssets(ThreeDScene):
  BG_COLOR=ManimColor('#1a1b26')
  PLANE_COLOR=BLUE_E
  SECOND_PLANE_COLOR=GREEN_E
  VECTOR_COLOR=WHITE

  v1=np.array([3,1,0])
  v2=np.array([1,3,0])
  v3=np.array([4,4,3])

  def build_xy_plane(self):
    return NumberPlane(
      x_range=[-6,6,1],
      y_range=[-6,6,1],
      background_line_style={
        'stroke_opacity':0.3,
        'stroke_color':self.PLANE_COLOR
      }
    )

  def build_xz_plane(self):
    plane=NumberPlane(
      x_range=[-6,6,1],
      y_range=[-6,6,1],
      background_line_style={
        'stroke_opacity':0.3,
        'stroke_color':self.SECOND_PLANE_COLOR
      }
    )
    plane.rotate(PI/2,axis=RIGHT)
    return plane

  def build_point_arrow(self,color):
    return Arrow3D(
      start=ORIGIN,
      end=ORIGIN,
      color=color,
      thickness=0.02
    )

  def build_arrow(self,vec,color):
    return Arrow3D(
      start=ORIGIN,
      end=vec,
      color=color,
      thickness=0.02
    )
