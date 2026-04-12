from manim import *
from manim_slides import Slide

class Presentation(Slide):
  def construct(self):
    grid=NumberPlane()
    self.add(grid)

    vec=Arrow(
      ORIGIN,
      RIGHT+UP,
      buff=0
    )

    self.play(GrowArrow(vec))

    self.next_slide()

    vec2=Arrow(
      ORIGIN,
      RIGHT*2+UP,
      buff=0
    )

    self.play(ReplacementTransform(vec,vec2))

    self.next_slide()

    ort=Arrow(
      RIGHT*2,
      RIGHT*2+UP,
      buff=0
    )

    self.play(FadeIn(ort))

    self.next_slide()
