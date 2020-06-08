from manimlib.imports import *
from test.fourier_series import FourierOfMySVG

class FourierOfBadapple(FourierOfMySVG):
    CONFIG = {
        "n_vectors": 501,
        "start_drawn": True,
        "file_name": "badapple.svg",
        "height": 7.5,
        "time_per_symbol": 5,
        "slow_factor": 1 / 15,
        "parametric_function_step_size": 0.01,
        "drawn_color": YELLOW,
        "drawn_path_stroke_width": 2,
    }
