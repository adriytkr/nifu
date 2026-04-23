from manim import *

class GramSchmidtSceneAssets(Scene):
  BG_COLOR=ManimColor('#1a1b26')
  VECTOR_COLOR=WHITE
  ORTHOGONAL_VECTOR_COLOR=RED
  BASIS_COLOR=PURE_BLUE

  coords=NumberPlane(
    x_range=[-1,6,1],
    y_range=[-1,13,1],
    x_length=config.frame_width*(3/4),
    y_length=config.frame_height*(3/4),
    background_line_style={'stroke_opacity':0},
    axis_config={'stroke_color':WHITE}
  ).set_z_index(1)

  v1=np.array([2,2])
  v2=np.array([4,10])

  def play(self,*args,**kwargs):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.6
    super().play(*args,**kwargs)

  def build_vector(self,start,end,color):
    return Arrow(
      start=start,
      end=end,
      buff=0,
      color=color,
      stroke_width=6
    ).set_z_index(2)

  def build_span(self,vec):
    start=-10*vec
    end=10*vec
    return DashedLine(
      start=self.coords.c2p(*start),
      end=self.coords.c2p(*end),
      dash_length=0.2,
      color=self.VECTOR_COLOR
    ).set_z_index(1)

  def build_projection_screen(self):
    origin=self.coords.c2p(0,0)

    v1_s=self.coords.c2p(*self.v1)-origin
    v2_s=self.coords.c2p(*self.v2)-origin

    proj_s=(np.dot(v2_s,v1_s)/np.dot(v1_s,v1_s))*v1_s

    proj_point=origin+proj_s
    v2_point=origin+v2_s

    perp_line=DashedLine(
      start=v2_point,
      end=proj_point,
      dash_length=0.2,
      color=self.ORTHOGONAL_VECTOR_COLOR
    ).set_z_index(2)

    proj_arrow=Arrow(
      start=origin,
      end=proj_point,
      buff=0,
      color=self.ORTHOGONAL_VECTOR_COLOR,
      stroke_width=6
    ).set_z_index(2)

    return perp_line,proj_arrow,proj_s,v1_s,v2_s,origin
