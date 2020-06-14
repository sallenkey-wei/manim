from manimlib.imports import *
from test.fourier_series import FourierOfMySVG
from test.fourier_series import FourierOfTexPaths
from test.long_fourier_scenes import *


class FourierOfBadapple(FourierOfMySVG):
    CONFIG = {
        "n_vectors": 101,
        "start_drawn": True,
        "file_name": "badapple.svg",
        "height": 7.5,
        "slow_factor": 1 / 15,
        "parametric_function_step_size": 0.01,
        "drawn_color": YELLOW,
        "drawn_path_stroke_width": 2,
    }


class FourierOfLuoXiaoHei(FourierOfMySVG):
    CONFIG = {
        "n_vectors": 101,
        "start_drawn": True,
        "file_name": "luoxiaohei.svg",
        "height": 7.5,
        "slow_factor": 1/5,
        "parametric_function_step_size": 0.01,
        "drawn_color": PINK,
        "drawn_path_stroke_width": 2,
    }


class FourierOfPanda(FourierOfMySVG):
    CONFIG = {
        "n_vectors": 101,
        "start_drawn": True,
        "file_name": "panda.svg",
        "height": 7.5,
        "slow_factor": 1/5,
        "parametric_function_step_size": 0.01,
        "drawn_color": YELLOW,
        "drawn_path_stroke_width": 2,
    }

    def get_path(self):
        shape = self.get_shape()
        shape.rotate(PI)
        path = shape.family_members_with_points()
        self.shape_point_num = 0
        subpath_heightList = []
        for subpath in path:
            subpath_heightList.append(subpath.get_height())
            subpath.set_fill(opacity=0)
            subpath.set_stroke(WHITE, 0)
            self.shape_point_num += subpath.get_num_points()

        max_subpath_height = max(subpath_heightList)
        scale_factor = self.height / max_subpath_height

        for subpath in path:
            subpath.scale(scale_factor, about_point=self.center_point)
        return path


class FourierOfElephant(FourierSeriesExampleWithRectForZoom):
    CONFIG = {
        "slow_factor": 0.1,
        "file_name": "elephant"
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.circles.set_stroke(opacity=0.5)
        rect = self.rect = self.get_rect()
        rect.set_height(self.rect_scale_factor * FRAME_HEIGHT)
        rect.add_updater(lambda m: m.move_to(
            self.get_rect_center()
        ))
        self.add(rect)
        time = 1 / 2 / self.slow_factor
        self.wait(time)
        self.slow_factor = 0.01
        self.slow_factor_tracker.set_value(self.slow_factor)
        time = 1 / 2 / self.slow_factor
        self.wait(10)
        print("vector_clock", self.vector_clock.get_value())


class FourierOfElephant2(FourierSeriesExampleWithRectForZoom):
    CONFIG = {
        "slow_factor": 0.01,
        "file_name": "elephant"
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.circles.set_stroke(opacity=0.5)
        rect = self.rect = self.get_rect()
        rect.set_height(self.rect_scale_factor * FRAME_HEIGHT)
        rect.add_updater(lambda m: m.move_to(
            self.get_rect_center()
        ))

        self.vector_clock.set_value(1.9026)
        self.add(rect)
        self.wait(10)
        static_vectors = VMobject().become(self.vectors)
        static_circles = VMobject().become(self.circles)
        static_rect = VMobject().become(self.rect)
        static_drawn_path = VMobject().become(self.drawn_path)
        self.remove(self.vectors)
        self.remove(self.circles)
        self.remove(self.rect)
        self.remove(self.drawn_path)
        self.play(FadeOut(static_vectors), FadeOut(static_circles), FadeOut(static_rect), FadeOut(static_drawn_path), run_time=2)


class FourierOfElephant_slow10x(ZoomedInFourierSeriesExample):
    CONFIG = {
        "slow_factor": 0.01,
        "file_name": "elephant"
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.circles.set_stroke(opacity=0.5)
        rect = self.rect = self.get_rect()
        rect.set_height(self.rect_scale_factor * FRAME_HEIGHT)
        rect.add_updater(lambda m: m.move_to(
            self.get_rect_center()
        ))
        TextContent = TextMobject("10x Zoom")
        TextContent.scale(0.2)
        TextContent.add_updater(self.text_update)
        self.add(TextContent)
        self.add(rect)
        self.vector_clock.set_value(1.593)
        self.wait(5)
        self.play(FadeOut(TextContent))
        self.wait(20)
        print("vector_clock", self.vector_clock.get_value())

    def text_update(self, m):
        m.move_to(self.rect.get_corner(UP+RIGHT) + DL * 0.1, aligned_edge=RIGHT+UP)



class FourierOfElephant_slow100x(ZoomedInFourierSeriesExample100x):
    CONFIG = {
        "slow_factor": 0.002,
        "file_name": "elephant"
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.circles.set_stroke(opacity=0.5)
        rect = self.rect = self.get_rect()
        rect.set_height(self.rect_scale_factor * FRAME_HEIGHT)
        rect.add_updater(lambda m: m.move_to(
            self.get_rect_center()
        ))

        TextContent = TextMobject("100x Zoom")
        TextContent.scale(0.02)
        TextContent.add_updater(self.text_update)
        self.add(TextContent)
        self.add(rect)

        self.vector_clock.set_value(1.851)
        self.wait(3)
        self.play(FadeOut(TextContent))
        self.wait(22)
        print("vector_clock", self.vector_clock.get_value())

    def text_update(self, m):
        m.move_to(self.rect.get_corner(UP+RIGHT) + DL * 0.01, aligned_edge=RIGHT+UP)

class VideoBegin(Scene):

    def construct(self):
        title = TextMobject("盖将自其变者而观之，则天地曾不能以一瞬；", color=BLUE)
        title2 = TextMobject("自其不变者而观之， 则物与我皆无尽也。", color=BLUE)
        author = TextMobject("-苏轼 《前赤壁赋》", color=YELLOW)


        title.shift(UP*2.5)
        title2.next_to(title, DOWN)
        title2.shift(LEFT*1.5)
        author.next_to(title2.get_corner(DOWN + RIGHT), DOWN)
        group1 = VGroup(title, title2, author)

        self.play(Write(title), run_time=5)
        self.play(Write(title2), run_time=5)
        self.play(Write(author), run_time=2)
        self.wait()


        textContent1 = TextMobject("仔细想来，这是否与傅里叶变换中时域和频域的转换有略微相似之处呢？")
        textContent1.set_color(GREEN)
        textContent2 = TextMobject("但傅里叶变换并不是这里的重点，接下来我只是使用傅里叶级数做一些有")
        textContent2.set_color(GREEN)
        textContent3 = TextMobject("趣的事情。")
        textContent3.set_color(GREEN)

        textContent1.scale(0.7)
        textContent1.next_to(author, DOWN)
        textContent1.move_to(title, aligned_edge=LEFT, coor_mask=np.array([1, 0, 0]))
        textContent1.shift(DOWN*0.5 + LEFT*0.4)

        textContent2.scale(0.7)
        textContent2.next_to(textContent1, DOWN)
        textContent2.move_to(title2, aligned_edge=LEFT, coor_mask=np.array([1, 0, 0]))

        textContent3.scale(0.7)
        textContent3.next_to(textContent2, DOWN)
        textContent3.move_to(textContent2, aligned_edge=LEFT, coor_mask=np.array([1, 0, 0]))
        self.play(Write(textContent1), run_time=5)
        self.wait()
        self.play(Write(textContent2), run_time=5)
        self.play(Write(textContent3))
        self.wait(3)

        group1.add(textContent1, textContent2, textContent3)

        textContent3 = TextMobject("什么是傅里叶级数呢？", color=BLUE)
        textContent3.shift(1.5*UP)
        textContent4 = TextMobject("这里只是给出简单的公式想要详细了解的话", color=YELLOW)
        textContent5 = TextMobject("可以观看3Blue1Brown的相关视频。", color=YELLOW)
        textContent4.shift(1.5*UP)
        textContent5.next_to(textContent4.get_bottom(), DOWN)
        group2 = VGroup(textContent4, textContent5)

        texformula1 = TexMobject("c_{n}=\\int_{0}^{1}f_{T}(t)e^{-jn\\omega_{0}t}dt (n=0,\\pm 1,\\pm 2,\\cdot \\cdot \\cdot )")
        texformula2 = TexMobject("f_{T}(t)=\\sum_{n=-\\infty}^{+\\infty}c_{n}e^{jn\\omega _{0}t}")
        texformula1.shift(UP*2)
        texformula1.set_color(YELLOW)
        texformula2.set_color(RED)
        group3 = VGroup(texformula1, texformula2)
        self.play(ReplacementTransform(group1, textContent3))
        self.wait(2)
        self.play(ReplacementTransform(textContent3, group2))
        self.wait(2)
        self.play(ReplacementTransform(group2, group3))
        self.wait(5)
        self.play(Uncreate(group3))
        self.wait()


class VideoEnd(FourierOfTexPaths):
    CONFIG = {
        "n_vectors": 100,
        "name_color": BLUE,
        "animated_name": "Author WeiYuyin",
        "time_per_symbol": 5,
        "slow_factor": 1,
        "parametric_function_step_size": 0.01,
    }
