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
      'stroke_opacity':0
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

  def _clamp_to_frame(self,u)->np.ndarray:
    fx=config.frame_width/2
    fy=config.frame_height/2

    mx=abs(self.coords.p2c([fx,0,0])[0])
    my=abs(self.coords.p2c([0,fy,0])[1])

    tx=mx/abs(u[0]) if u[0]!=0 else np.inf
    ty=my/abs(u[1]) if u[1]!=0 else np.inf

    return u*min(tx,ty)

  def build_vec(self,vec)->Arrow:
    return Arrow(
      start=ORIGIN,
      end=self.coords.c2p(vec[0],vec[1]),
      buff=0,
      color=self.VECTOR_COLOR
    ).set_z_index(999)

  def build_vec_label(self,name:str)->MathTex:
    return MathTex(
      r'\vec{'+name+r'}',
      color=self.VECTOR_COLOR
    ).scale(0.8)

  def build_span(self,vec)->DashedLine:
    u=vec/np.linalg.norm(vec)
    tip=self._clamp_to_frame(u)

    return DashedLine(
      start=self.coords.c2p(*tip),
      end=self.coords.c2p(*(-tip)),
      color=self.SPAN_COLOR
    )

  def build_span_label(self,name:str)->MathTex:
    return MathTex(
      r'\text{span}('+name+r')',
      color=self.SPAN_COLOR
    ).scale(0.7)

  def mv(
    self,matrix,
    *vectors,
    labels=None
  )->list:
    animations=[]

    for i,el_v in enumerate(vectors):
      math_coords=self.coords.p2c(el_v.get_end())
      new_v=matrix@math_coords
      new_end=self.coords.c2p(new_v[0],new_v[1])

      el_new_v=Arrow(
        start=ORIGIN,
        end=new_end,
        buff=0,
        color=self.VECTOR_COLOR
      )

      animations.append(Transform(el_v,el_new_v))

      if labels is not None and i<len(labels) and labels[i] is not None:
        lbl=labels[i]
        offset=lbl.get_center()-el_v.get_end()
        animations.append(
          lbl.animate.move_to(new_end+offset)
        )

    return animations

  def build_eigen_family(
    self,
    eigen_v,
    scalar_range=range(-4,4)
  )->list:
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

  def span_label_pos(self,vec)->np.ndarray:
    u=vec/np.linalg.norm(vec)

    tx=6.2/abs(u[0]) if u[0]!=0 else np.inf
    ty=3.2/abs(u[1]) if u[1]!=0 else np.inf
    t=min(tx,ty)

    return self.coords.c2p(*(u*t))
