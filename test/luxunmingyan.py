from manimlib.imports import *

class luxunmingyan(Scene):

    def construct(self):
        quote = TextMobject("使用manim制作数学动画很有意思")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("Making animation by manim is funny.")
        quote2.set_color(BLUE)
        author = TextMobject("-鲁迅", color=PINK)
        author2 = TextMobject("-鲁迅")
        author2.match_color(quote2)
        author2.scale(1.3)

        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)
        author2.move_to(quote2.get_corner(DOWN + RIGHT) + DOWN + LEFT)

        #self.add(quote)
        #self.add(author)
        self.play(ShowCreation(quote))
        self.play(FadeIn(author))
        self.wait(2)

        self.play(Transform(quote, quote2), Transform(author, author2))
        self.wait(2)

