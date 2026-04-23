from manim import *

from src.scenes.graham_scan.graham_scan_scene_assets import GrahamScanSceneAssets

class GrahamScanScene(GrahamScanSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR



    # ---------------- Start Buff ----------------
    self.wait(1)



    # ---------------- End Buff ----------------
    self.wait(1)
