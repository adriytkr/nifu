from manim import *

class GrahamScanSceneAssets(Scene):
  BG_COLOR=ManimColor('#1a1b26')

  def play(
    self,
    *args,
    **kwargs
  ):
    if 'run_time' not in kwargs:
      kwargs['run_time']=0.5

    super().play(*args,**kwargs)

  def setup(self):
    pass
