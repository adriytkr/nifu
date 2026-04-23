from manim import *

from src.scenes.quick_hull.quick_hull_scene_assets import QuickHullSceneAssets

class QuickHullScene(QuickHullSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Start Buff ----------------
    self.wait(1)



    # ---------------- End Buff ----------------
    self.wait(1)
