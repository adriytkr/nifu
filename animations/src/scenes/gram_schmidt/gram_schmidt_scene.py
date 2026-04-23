from manim import *

from src.scenes.gram_schmidt.gram_schmidt_scene_assets import GramSchmidtSceneAssets

class GramSchmidtScene(GramSchmidtSceneAssets):
  def construct(self):
    self.camera.background_color=self.BG_COLOR

    self.wait(1)
    self.add(self.coords)



    # ---------------- Original Vectors ----------------
    origin=self.coords.c2p(0,0)

    v1_arrow=self.build_vector(
      origin,
      self.coords.c2p(*self.v1),
      self.VECTOR_COLOR
    )
    v2_arrow=self.build_vector(
      origin,
      self.coords.c2p(*self.v2),
      BLUE
    )

    v1_label=MathTex('v_1')\
      .next_to(
        v1_arrow.get_end(),
        DOWN
      )\
      .scale(0.7)
    v2_label=MathTex('v_2')\
      .next_to(
        v2_arrow.get_end(),
        UP
      )\
      .scale(0.7)

    self.play(
      GrowArrow(v1_arrow),
      GrowArrow(v2_arrow),
    )
    self.play(
      Write(v1_label),
      Write(v2_label)
    )



    # ---------------- Span ----------------
    span_v1=self.build_span(self.v1)
    self.play(Create(span_v1))



    # ---------------- Projection ----------------
    perp_line,proj_arrow,proj_s,v1_s,v2_s,origin=self.build_projection_screen()

    proj_label=MathTex(r'\text{proj}_{\text{span}(v_1)}(v_2)')\
      .scale(0.7)\
      .next_to(proj_arrow.get_end(),DOWN*1.5)

    self.play(Create(perp_line))
    self.play(GrowArrow(proj_arrow))
    self.play(Write(proj_label))



    # ---------------- Orthogonal Component ----------------
    orth_s=v2_s-proj_s
    proj_point=origin+proj_s

    orth_arrow=Arrow(
      start=proj_point,
      end=proj_point+orth_s,
      buff=0,
      color=self.ORTHOGONAL_VECTOR_COLOR,
      stroke_width=6
    ).set_z_index(2)

    orth_label=MathTex(r'v_2 - \text{proj}_{\text{span}(v_1)}(v_2)')
    orth_label.scale(0.7)
    orth_label.next_to(
      (orth_arrow.get_start()+orth_arrow.get_end())/2,
      RIGHT
    )

    self.play(GrowArrow(orth_arrow))
    self.play(Write(orth_label))



    # ---------------- Fade clutter ----------------
    self.play(
      FadeOut(v2_arrow),
      FadeOut(v2_label),
      FadeOut(span_v1),
      FadeOut(perp_line),
      FadeOut(proj_arrow),
      FadeOut(proj_label)
    )



    # ---------------- Move to Origin ----------------
    orth_arrow_origin=Arrow(
      start=origin,
      end=origin+orth_s,
      buff=0,
      color=self.ORTHOGONAL_VECTOR_COLOR,
      stroke_width=6
    ).set_z_index(2)

    self.play(
      Transform(orth_arrow,orth_arrow_origin),
      orth_label.animate.next_to(orth_arrow_origin.get_end(),UP)
    )



    # ---------------- End Buff ----------------
    self.wait(1)
