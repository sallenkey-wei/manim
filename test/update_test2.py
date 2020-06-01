from manimlib.imports import *

class Update_test(Scene):
    CONFIG = {
        "vector_config": {
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.35,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 2,
        },
    }
    def __init__(self, **kwargs):
        self.num1 = 0
        self.slow_factor = 0.1
        super(Update_test, self).__init__(**kwargs)
        
    def construct(self):
        vector = Vector(RIGHT, **self.vector_config)
        vector.add_updater(self.update_vector)
        self.add(vector)
        self.wait(10/self.slow_factor)

    '''
    系统每隔dt秒就会自动调用update_vector, 调用间隔dt应该是可以设置的，未深入研究
    '''
    def update_vector(self, vector, dt):
        vector.set_length(3)
        vector.set_angle(self.num1 * dt * TAU / 10 * self.slow_factor)
        #vector.set_angle(0)
        self.num1 += 1
        return vector