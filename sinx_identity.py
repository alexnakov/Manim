from manimlib import *
from manim import *
import math


class MainScene(Scene):
    """ Shows the animation of sin(x) = sin(pi - x) slowly.
        A teacher should be a able to explain what is happening """
    def construct(self):
        self.construct_text()
        self.construct_plane()
        self.construct_graph()

        # Animating:

        self.wait(1)
        self.play(ShowCreation(self.plane), run_time=3)
        self.play(ShowCreation(self.sine), run_time=6)
        self.play(FadeInFrom(self.f, np.array((0, -3, 0))))
        self.wait(1.5)
        self.play(Transform(self.f, self.f_minus_x))
        self.wait()
        self.play(Write(self.reflection), run_time=1.5)
        self.wait(0.5)
        self.play(Rotating(self.sine, radians=PI, axis=UP, about_point=ORIGIN, run_time=2))
        self.wait(0.3)
        self.play(FadeOut(self.reflection))
        self.wait(0.3)
        self.play(Transform(self.f, self.f_minus_x_plus_pi))
        self.wait(1)
        self.play(Write(self.shift), run_time=1.5)
        self.wait(0.5)
        self.play(ApplyMethod(self.sine.shift, LEFT*PI), run_time=2)
        self.wait(1)
        self.play(FadeOut(self.shift), FadeOut(self.f))
        self.wait(1)
        self.play(Write(self.this_is_sinx))
        self.wait(0.3)
        self.play(Write(self.sinx_equals))
        self.wait(2)

    def construct_plane(self):
        axes = Axes(
            x_min=-2 * PI,
            x_max=2 * PI,
            y_min=-1.5,
            y_max=1.5,
            axis_config={
                "include_tip": False,
            },
            y_axis_config={
                "include_numbers": False,
            },
            x_axis_config={
                "tick_frequency": PI / 2,
            },
        )

        x = {
            "pi": MathTex(r"\pi").scale(0.75).shift(DOWN * 0.3 + RIGHT * PI),
            "2pi": MathTex(r"2\pi").scale(0.75).shift(DOWN * 0.3 + RIGHT * 2 * PI * 1.02),
            "-pi": MathTex(r"-\pi").scale(0.75).shift(DOWN * 0.3 + LEFT * PI * 1.03),
            "-2pi": MathTex(r"-2\pi").scale(0.75).shift(DOWN * 0.3 + LEFT * 2 * PI),
        }  # labels of x-axis (multiples of pi)
        y = {"1": MathTex("1").scale(0.6).shift(UP + LEFT * 0.25),
             "-1": MathTex("-1").scale(0.6).shift(DOWN + LEFT * 0.3)}  # labels of y-axis (1 and -1)

        plane = VGroup(axes, x["-2pi"], x["-pi"], x["pi"], x["2pi"], y["1"], y["-1"]).shift(0.5*DOWN)
        self.plane = plane

    def construct_graph(self):
        sine = FunctionGraph(lambda x: math.sin(x), x_max=3.5 * PI, x_min=-3.5 * PI).shift(0.5*DOWN)
        self.sine = sine

    def construct_text(self):
        pi = MathTex("\pi").scale(1.2)

        f = MathTex("f(x)=sin(x)").shift(3*UP)
        f_minus_x = MathTex("f(-x)=sin(-x)").shift(3*UP)
        f_minus_x_plus_pi = MathTex(r"f(\pi-x)=sin(\pi-x)").shift(3*UP)

        # Combining text for the shift transformation
        text1 = Text("Transformation: Shift the curve by ").scale(0.7)
        text2 = Text("radians to the left").scale(0.7)
        shift = VGroup(text1, pi).arrange(RIGHT)

        # Transformation descriptions
        shift = VGroup(shift, text2).arrange(RIGHT).shift(2*UP)
        reflection = Text("Transformation: Reflection about the y-axis").shift(2*UP)

        # Conclusion text:
        sinx_text = MathTex("sin(x)")
        this_is_sinx = Text("This is")
        this_is_sinx = VGroup(this_is_sinx, sinx_text).arrange(RIGHT).shift(3*UP)

        sinx_equals = MathTex("\mathrm{therefore} \ sin(x)=sin(\pi-x)").shift(2*UP)

        self.pi = pi
        self.f = f
        self.f_minus_x = f_minus_x
        self.f_minus_x_plus_pi = f_minus_x_plus_pi

        self.reflection = reflection
        self.shift = shift

        self.this_is_sinx = this_is_sinx
        self.sinx_equals = sinx_equals