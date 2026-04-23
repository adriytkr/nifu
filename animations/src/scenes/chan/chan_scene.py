from manim import *

from src.scenes.chan.chan_scene_assets import ChanSceneAssets

class ChanScene(ChanSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Start Buff ----------------
    self.wait(1)



    # ---------------- End Buff ----------------
    self.wait(1)
