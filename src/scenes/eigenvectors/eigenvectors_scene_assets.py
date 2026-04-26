from manim import *

import numpy as np

class EigenvectorsSceneAssets(Scene):
  BG_COLOR=ManimColor('#1a1b26')

  VECTOR_COLOR=ManimColor('#00e676')
  SPAN_COLOR=ManimColor('#00e676')

  coords=NumberPlane(
    x_range=[-10,10],
    y_range=[-6,6],
    background_line_style={
      "stroke_opacity":0
    }
  )

  matrix=np.array([
    [5,-6],
    [3,-4]
  ])

  rotation_matrix=np.array([
    [
      np.cos(np.radians(30)),
      -np.sin(np.radians(30))
    ],
    [
      np.sin(np.radians(30)),
      np.cos(np.radians(30))
    ]
  ])

  eigen_v1=np.array([2,1])
  eigen_v2=np.array([1,1])
  non_eigen_v=np.array([3,2])

  def play(self,*args,**kwargs):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.6

    super().play(*args,**kwargs)

  def build_vec(self,vec)->Arrow:
    return Arrow(
      start=ORIGIN,
      end=self.coords.c2p(vec[0],vec[1]),
      buff=0,
      color=self.VECTOR_COLOR
    ).set_z_index(999)

  def build_span(self,vec)->DashedLine:
    u=vec/np.linalg.norm(vec)

    return DashedLine(
      start=self.coords.c2p(*(u*10)),
      end=self.coords.c2p(*(-u*10)),
      color=self.SPAN_COLOR
    )

  def mv(self,matrix,*vectors)->list:
    animations=[]

    for el_v in vectors:
      math_coords=self.coords.p2c(el_v.get_end())
      new_v=matrix@math_coords

      el_new_v=Arrow(
        start=ORIGIN,
        end=self.coords.c2p(new_v[0],new_v[1]),
        buff=0,
        color=self.VECTOR_COLOR
      )

      animations.append(Transform(el_v,el_new_v))

    return animations

  def build_eigen_family(self,eigen_v,scalar_range=range(-4,4))->list:
    return [
      Arrow(
        start=ORIGIN,
        end=self.coords.c2p(*(eigen_v*i)),
        buff=0,
        color=self.VECTOR_COLOR
      )
      for i in scalar_range
    ]

  def build_circle_family(self,n_vectors=8)->list:
    return [
      Arrow(
        start=ORIGIN,
        end=self.coords.c2p(*(4*np.array([np.cos(a),np.sin(a)]))),
        buff=0,
        color=self.VECTOR_COLOR
      )
      for a in np.linspace(0,2*np.pi,n_vectors,endpoint=False)
    ]
