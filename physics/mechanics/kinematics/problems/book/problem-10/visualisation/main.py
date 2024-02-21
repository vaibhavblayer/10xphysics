from manim import *
from manim_physics import *

class SineCurveUnitCircle(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        t = ValueTracker(0)
        def r_dot(mobject):
            mobject.set_x(-2 + np.cos(t.get_value()))
            mobject.set_y(np.sin(t.get_value()))
            
        def m_dot(mobject):
            mobject.set_x(t.get_value())
            mobject.set_y(np.tan(t.get_value()))
            
        def d_line():
            line = Line(rdot.get_center(), mdot.get_center())
            return line
            
        rdot = Dot().move_to(2*LEFT)
        mdot = Dot().move_to(LEFT)
        
        line = always_redraw(d_line)
        rdot.add_updater(r_dot)
        mdot.add_updater(m_dot)
        t_circle = TracedPath(rdot.get_center)
        t_curve = TracedPath(mdot.get_center)
        group = VGroup(t_circle, t_curve)
        
        self.play(self.camera.frame.animate.scale(1).move_to(mdot))
        def update_curve(mob):
            mob.move_to(mdot.get_center()-np.array([0.6*t.get_value(), 0, 0]))
            mob.set(width = 10 + t.get_value())
        
        self.camera.frame.add_updater(update_curve)
        
        self.add(t, rdot, mdot, t_circle, t_curve, line)
        t.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(25)






class TexFalling(SpaceScene):
    def construct(self):
        ground = Line(LEFT * 3, RIGHT * 3, color=WHITE).shift(2.5*DOWN)
        self.add(ground)
        self.make_static_body(ground)
        forms = [
            r"\textit{average of a function}",
            r"<f(x)>=\dfrac{\int_{x_i}^{x_f} f(x) d\!x}{\int_{x_i}^{x_f} d\!x}"
        ]
        cols = [WHITE, WHITE]
        nums = [1, 2]
        for n, f, col in zip(nums, forms, cols):
            text = MathTex(f, color=col).shift(2.5*UP)
            if n == 1:
                text.scale(0.8)
                self.add(text)
                self.wait(3)
            else:
                self.add(text)
                self.wait(6)
            self.make_rigid_body(text[0])
            self.wait(3)
            
        
        