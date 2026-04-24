from manim import *
from src.scenes.kadane.kadane_scene_assets import KadaneSceneAssets
class KadaneScene(KadaneSceneAssets):
  def construct(self):
    # ---------------- Config ----------------
    self.camera.background_color=self.BG_COLOR

    # ---------------- Start Buff ----------------
    self.wait(1)

    # ---------------- Begin ----------------
    self.play(FadeIn(self.el_array))

    # ---------------- Set up Kadane ----------------
    self.el_best_sum_display.next_to(
      self.el_array,
      UP,
      buff=0.5
    )

    self.el_current_sum_display.next_to(
      self.el_best_sum_display,
      RIGHT,
      buff=0.3
    )

    self.el_pointer.next_to(
      self.el_array[0],
      DOWN,
      buff=0.3
    )

    self.play(
      FadeIn(self.el_pointer),
      *self.kadane_step(0),
      GrowFromPoint(
        self.el_best_sum_display,
        self.el_best_sum_display.get_center()
      ),
      GrowFromPoint(
        self.el_current_sum_display,
        self.el_current_sum_display.get_center()
      )
    )

    # ---------------- Kadane ----------------
    for i in range(1,len(self.array)):
      self.move_pointer_to(i)
      self.play(*self.kadane_step(i))

    # ---------------- End Buff ----------------
    self.wait(1)
