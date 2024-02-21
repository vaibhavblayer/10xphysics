__all__ = [
    "Field",
    "HemiSphere",
    "Plane",
    "CircularPlane",
    "RTitle",
    "RAxes",
    "ToggleButton"
]


from typing import Callable, Sequence
from colour import Color
from manim import *
from manim import config
from manim.constants import MED_SMALL_BUFF
import numpy as np
from manim.utils.color import BLUE_D, BLUE_E, LIGHT_GREY


class DCircle(Circle):
    Circle.set_default(color=WHITE)

    def __init__(self, radius, **kwargs) -> None:
        super().__init__(radius, **kwargs)
        from manim import Dot
        dot = Dot()
        dot.move_to(self.get_center())
        self.add(dot)


class Field(VGroup):
    MathTex.set_default(color=WHITE)

    def __init__(
            self,
            field: str = r"\times",
            scale: float = 0.85,
            pointlb: list | np.ndarray = 4*(LEFT + DOWN),
            pointra: list | np.ndarray = 4*(RIGHT + UP),
            ** kwargs) -> None:
        super().__init__(**kwargs)
        from manim import MathTex

        for i in range(int(pointlb[0]), int(pointra[0]) + 1):
            for j in range(int(pointlb[1]), int(pointra[1])+1):
                f = MathTex(field).scale(scale).move_to(i*RIGHT + j*UP)
                self.add(f)


class HemiSphere(Surface):

    def __init__(
        self,
        center: Sequence[float] = ORIGIN,
        radius: float = 1,
        resolution: Sequence[int] = None,
        u_range: Sequence[float] = (0, TAU),
        v_range: Sequence[float] = (0, PI/2),
        **kwargs,
    ) -> None:
        if config.renderer == RendererType.OPENGL:
            res_value = (101, 51)
        elif config.renderer == RendererType.CAIRO:
            res_value = (48, 24)
        else:
            raise Exception("Unknown renderer")

        resolution = resolution if resolution is not None else res_value

        self.radius = radius

        super().__init__(
            self.func,
            resolution=resolution,
            u_range=u_range,
            v_range=v_range,
            **kwargs,
        )

        self.shift(center)
        self.fill_color: Color = GRAY_C
        self.stroke_color: Color = GRAY_C

    def func(self, u: float, v: float) -> np.ndarray:
        return self.radius * np.array(
            [np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -np.cos(v)],
        )


class Plane(Surface):

    def __init__(
        self,
        center: Sequence[float] = ORIGIN,
        radius: float = 1,
        resolution: Sequence[int] = None,
        u_range: Sequence[float] = (-0.5, 0.5),
        v_range: Sequence[float] = (-0.5, 0.5),
        **kwargs,
    ) -> None:
        if config.renderer == RendererType.OPENGL:
            res_value = (101, 51)
        elif config.renderer == RendererType.CAIRO:
            res_value = (48, 24)
        else:
            raise Exception("Unknown renderer")

        resolution = resolution if resolution is not None else res_value

        self.radius = radius

        super().__init__(
            self.func,
            resolution=resolution,
            u_range=u_range,
            v_range=v_range,
            **kwargs,
        )

        self.shift(center)
        self.fill_color: Color = GRAY_C
        self.stroke_color: Color = GRAY_C

    def func(self, u: float, v: float) -> np.ndarray:
        return self.radius * np.array(
            [u, v, 0],
        )


class CircularPlane(Surface):

    def __init__(
        self,
        center: Sequence[float] = ORIGIN,
        radius: float = 1,
        resolution: Sequence[int] = None,
        u_range: Sequence[float] = (0, TAU),
        v_range: Sequence[float] = (0, PI/2),
        **kwargs,
    ) -> None:
        if config.renderer == RendererType.OPENGL:
            res_value = (101, 51)
        elif config.renderer == RendererType.CAIRO:
            res_value = (48, 24)
        else:
            raise Exception("Unknown renderer")

        resolution = resolution if resolution is not None else res_value

        self.radius = radius

        super().__init__(
            self.func,
            resolution=resolution,
            u_range=u_range,
            v_range=v_range,
            **kwargs,
        )

        self.shift(center)
        self.fill_color: Color = GRAY_C
        self.stroke_color: Color = GRAY_C

    def func(self, u: float, v: float) -> np.ndarray:
        return self.radius * np.array(
            [np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), 0]
        )


class RTitle(Title):
    def __init__(
        self,
        *text_parts,
        ** kwargs
    ):
        super().__init__(
            *text_parts,
            include_underline=False,
            ** kwargs
        )
        self.shift(DOWN)


class RAxes(Axes):
    def __init__(
        self,
        x_range: Sequence[float] | None = [-5, 5, 1],
        y_range: Sequence[float] | None = [-5, 5, 1],
        x_length: float | None = 9,
        y_length: float | None = 9,
        axis_config: dict | None = None,
        x_axis_config: dict | None = None,
        y_axis_config: dict | None = None,
        tips: bool = False,
        **kwargs
    ):
        super().__init__(
            x_range,
            y_range,
            x_length,
            y_length,
            axis_config,
            x_axis_config,
            y_axis_config,
            tips,
            **kwargs
        )


class ToggleButton(RoundedRectangle):
    def __init__(
            self,
            corner_radius: float = 0.5,
            state: bool = False,
            **kwargs
    ):

        self.corner_radius = corner_radius
        self.state = state
        super().__init__(
            corner_radius=corner_radius,
            height=2*corner_radius,
            width=5*corner_radius,
            **kwargs
        )
        self.set_fill(color=WHITE, opacity=1)
        self.circle = Circle(radius=self.corner_radius -
                             0.01).set_fill(color=BLACK, opacity=1)
        self.add(self.circle.move_to(self.get_left()+RIGHT*self.corner_radius))

    def toggle(self):
        if self.state == True:
            self.state = False
            self.set_fill(color=WHITE, opacity=1)
            self.circle.set_fill(color=BLACK, opacity=1)
            self.circle.move_to(self.get_left()+RIGHT*self.corner_radius)

        else:
            self.state = True
            self.set_fill(color=PURE_GREEN, opacity=1)
            self.circle.set_fill(color=BLACK, opacity=1)
            self.circle.move_to(self.get_right()+LEFT*self.corner_radius)

        return self
