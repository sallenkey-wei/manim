from manimlib.imports import *

class Graph2D(GraphScene):
    ''''''
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-10, 12, 2),
    }
    def construct(self):
        self.setup_axes(animate =True)
        sin_graph = self.get_graph(self.sin_func, self.function_color)
        cos_graph = self.get_graph(self.cos_func)
        self.play(ShowCreation(sin_graph), ShowCreation(cos_graph))

        sin_lable = self.get_graph_label(sin_graph, label="sin(x)", x_val=5, direction=UP)
        self.play(ShowCreation(sin_lable))
        self.wait()

    def sin_func(self, x):
        return np.sin(x)
    def cos_func(self, x):
        return np.cos(x)