#!/usr/bin/env python
from manimlib.imports import *

class Hello_World(Scene):
    def construct(self):
        ## Making object
        helloworld = TextMobject("Hello World!", color=RED)
        
        ## Position

        ## Showing object
        self.play(Write(helloworld))
        self.wait(1)