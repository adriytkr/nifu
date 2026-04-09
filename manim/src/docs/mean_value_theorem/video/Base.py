from manim import *

from src.utils.coordinate_system import CoordinateSystemManager
from src.utils.theme import HIGHLIGHT_COLOR

class BaseScene(Scene):
  BIRD_COLOR=ManimColor('#ffdd21')

  axes=Axes(
    x_range=[0,10],
    y_range=[0,6]
  )

  coords=CoordinateSystemManager(axes)

  x_A=2
  x_B=9
  x_C=5.5

  def position(self,t):
    return (0.4*t-1.5)**2+1

  def velocity(self,t):
    return 0.8*(0.4*t-1.5)

  def secant_line(self,t):
    return 0.56*(t-self.x_A)+self.position(self.x_A)





  def s_build_secant_line(self)->Line:
    secant_line=Line(
      start=self.coords.to_graph_point(self.x_A,self.position),
      end=self.coords.to_graph_point(self.x_B,self.position)
    )

    return secant_line

  def s_build_tangent_line(self,t:float)->Line:
    dt=0.1
    y=self.velocity(t)*dt+self.position(t)

    a=self.coords.to_graph_point(t,self.position)
    b=self.coords.to_point(t+dt,y)
    direction=b-a

    tangent_line=Line(
      start=self.coords.to_graph_point(t,self.position)+direction*-40,
      end=self.coords.to_point(t+dt,y)+direction*40
    )

    return tangent_line

  def s_build_tangent_point(self,t:float)->Dot:
    tangent_point=self.coords.build_graph_dot(t,self.position)

    return tangent_point

  def s_build_bird(self,t:float)->Dot:
    bird=self.coords.build_graph_dot(
      t,
      self.position,
      color=self.BIRD_COLOR
    )

    bird.set_z_index(60)

    return bird
  
  def s_build_height(self,t:float)->Line:
    height=Line(
      start=self.coords.to_graph_point(t,self.position),
      end=self.coords.to_graph_point(t,self.secant_line),
    )

    return height
  
  def s_build_velocity(self,t:float)->Arrow:
    dt=0.1
    tip=self.velocity(t)*dt+self.position(t)

    from_coords=self.coords.to_graph_point(t,self.position)
    tip_coords=self.coords.to_point(t+dt,tip)

    magnitude=2
    direction=tip_coords-from_coords
    unit_direction=direction/np.linalg.norm(direction)

    velocity=Arrow(
      start=self.coords.to_graph_point(t,self.position),
      end=self.coords.to_point(t+dt,tip)+unit_direction*magnitude,
      buff=0,
      color=HIGHLIGHT_COLOR
    )

    velocity.set_z_index(50)

    return velocity
