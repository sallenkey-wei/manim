from manimlib.imports import *

class Hello_World(Scene):

    def construct(self):
        helloworld = TextMobject("Hello World!", color=YELLOW)
        rectangle = Rectangle(color=BLUE)

        rectangle.surround(helloworld)
        group = VGroup(helloworld, rectangle)

        hellomanim = TextMobject("Hello You Manim!", color=BLUE)
        hellomanim.scale(2.5)

        self.play(Write(helloworld))
        self.wait(1)

        self.play(FadeIn(rectangle))
        self.wait(1)

        self.play(ApplyMethod(group.scale, 2.5))
        self.wait(1)

        self.play(Transform(helloworld, hellomanim), ApplyMethod(rectangle.surround, hellomanim))
        self.wait(1)