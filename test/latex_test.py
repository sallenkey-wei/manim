from manimlib.imports import *

class Latex(Scene):

    def construct(self):
        title = TextMobject("This is some \\LaTeX", color=BLUE)
        base1 = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}",
        )
        base1.match_color(title)
        VGroup(title, base1).arrange(DOWN)
        self.play(Write(title), FadeInFrom(base1, UP))
        self.wait(1)