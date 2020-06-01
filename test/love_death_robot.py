from manimlib.imports import *

class Love_Death_Robots(Scene):

    def construct(self):
        circle01 = Circle(color=RED, fill_color=RED, fill_opacity=0.4, radius = 1)
        circle02 = Circle(color=RED, fill_color=RED, fill_opacity=0.4, radius = 1)
        square01 = Square(color=RED, fill_color=RED, fill_opacity=0.4)
        square01.rotate(PI/4)
        circle01.shift(LEFT/(2**0.5) + UP/(2**0.5))
        circle02.shift(RIGHT/(2**0.5) + UP/(2**0.5))
        group01 = VGroup(circle01, circle02, square01)
        self.play(ShowCreation(circle01), ShowCreation(circle02), ShowCreation(square01))
        self.wait(0.5)

        self.play(ApplyMethod(group01.shift, LEFT*4))
        self.wait(0.5)

        rectangle01 = Rectangle(color=RED, fill_color=RED, fill_opacity=0.4, width=0.7, height=3.5)
        rectangle02 = Rectangle(color=RED, fill_color=RED, fill_opacity=0.4, width=0.7, height=3.5)
        rectangle01.rotate(45*DEGREES)
        rectangle02.rotate(45*DEGREES, IN)
        group02 = VGroup(rectangle01, rectangle02)
        self.play(ShowCreation(rectangle01), ShowCreation(rectangle02))
        self.wait(0.5)

        square02 = Square(color=RED, fill_color=RED, fill_opacity=0.4, side_length=3.2)
        circle03 = Circle(color=RED, fill_color=BLACK, fill_opacity=0.4, radius = 0.5)
        circle04 = Circle(color=RED, fill_color=BLACK, fill_opacity=0.4, radius = 0.5)
        circle03.shift(UL*0.7)
        circle04.shift(UR*0.7)
        group03 = VGroup(square02, circle03, circle04)
        group03.shift(RIGHT*4)
        self.play(ShowCreation(square02), ShowCreation(circle03), ShowCreation(circle04))
        self.wait(0.5)

        self.play(ApplyMethod(group01.set_opacity, 1), ApplyMethod(group02.set_opacity, 1),  \
        ApplyMethod(square02.set_opacity, 1), ApplyMethod(circle03.set_opacity, 1), ApplyMethod(circle04.set_opacity, 1))
        self.wait(0.5)

        line01 = Line(np.array([-6, -2.4, 0]), np.array([6, -2.4, 0]), color=RED)
        line01.set_height(0.2)

        text01 = TextMobject("LOVE\nDEATH\n+\nROBOTS", color=RED)
        text01.scale(1.8)
        text01.shift(DOWN * 2.5)

        group_all = VGroup(group01, group02, group03, line01, text01)
        self.play(ShowCreation(line01))
        self.wait(0.5)

        self.play(Transform(line01, text01))
        self.wait(1)
        self.play(ApplyMethod(group_all.shift, UP * 0.5))
        self.wait(2)

        #self.play(FadeOut(group_all))
        #self.wait(0.5)

        text02 = TextMobject("Author: 魏玉印", color=BLUE)
        self.play(Transform(group_all, text02))
        self.wait(2)


