from manim import *

from manim_physics import *


class MagneticFieldExample(ThreeDScene):
    def construct(self):
        wire = Wire(Circle(2).rotate(PI / 2, UP))
        mag_field = MagneticField(
            wire,
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.set_camera_orientation(PI / 3, PI / 4)
        self.add(wire, mag_field)


class MagneticFieldLine(ThreeDScene):
    def construct(self):
        wire = Wire(Line(3*LEFT, 3*RIGHT).rotate(PI / 2, UP))
        mag_field = MagneticField(
            wire,
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.set_camera_orientation(PI / 3, PI / 4)
        self.add(wire, mag_field)


class MagneticFieldArc(ThreeDScene):
    def construct(self):
        wire = Wire(Arc().scale(3).rotate(PI / 2, UP))
        mag_field = MagneticField(
            wire,
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.set_camera_orientation(PI / 3, PI / 4)
        self.add(wire, mag_field)


class MagneticFiledBarMagnet(ThreeDScene):
    def construct(self):
        bar_magnenet = Wire(Circle().rotate(PI/2, UP))

        magnetic_field = MagneticField(
            bar_magnenet,
            x_range=[-4, 4],
            y_range=[-4, 4]
        )

        self.add(bar_magnenet, magnetic_field)
