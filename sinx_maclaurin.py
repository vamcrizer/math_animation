from manim import *
import numpy as np

class sinxmaclaurin(Scene):
    def construct(self):
        formula = MathTex(r"f(x) = arctan(x)")
        formula2 = MathTex(r"f'(x) = \frac{1}{1+x^2}?")
        formula2.next_to(formula, 0.1*DOWN)
        formula2.align_to(formula, LEFT)
        formula2.shift(0.06*LEFT)
        self.play(Write(formula), run_time = 1)
        self.wait(1)
        self.play(Write(formula2), run_time = 1)
        self.play(Transform(formula, formula2))

 