from manim import *


class ElectricField(Scene):
    def construct(self):
        title = Tex(r"\text{charge in a uniform electric field (gravity-free)}").scale(0.5).move_to(3*UP)
        f_lines = VGroup()        
        for i in range(6):
            f_line = Arrow(
                    start=2*UP, 
                    end=DOWN, 
                    tip_shape=StealthTip, 
                    max_stroke_width_to_length_ratio=0.5,
                    max_tip_length_to_length_ratio=0.03)
            f_lines.add(f_line)

       
        E = MathTex(r"\vec{E}").scale(0.5).move_to(2*DOWN)
        u = 5
        g = 4
        t = ValueTracker(0)
        q = Dot().scale(1.25)
        q.add_updater(
                lambda m: m.set_x(-3+u*t.get_value())
                )
        q.add_updater(
                lambda m: m.set_y(-1.5+u*t.get_value() - g*(t.get_value())**2)
                )
        

        path = TracedPath(q.get_center)

        self.add(q,t,E, f_lines.arrange(direction=np.array([1., 0., 0.]), buff=0.6))
        self.add(title, path)
        self.play(
                t.animate.set_value(5),
                run_time=10,
                rate_func=rate_functions.linear
                )
        
        
class RelativeAV(Scene):
        def construct(self):
                tp = ValueTracker(PI/4)
                tq = ValueTracker(PI/4)
                cp = Circle(radius=2.5, color=WHITE)
                cq = Circle(radius=1.5, color=WHITE)
                def get_linePQ():
                        Q = cq.point_at_angle(tq.get_value())
                        P = cp.point_at_angle(tp.get_value())
                        dp = Dot(point=P)
                        dq = Dot(point=Q)
                        RP = Line(cp.get_center(), P, stroke_width=1.75)
                        RQ = Line(cq.get_center(), Q, stroke_width=1.75)
                        #angle = Angle(RP, RQ, radius=0.4)
                        #value = DecimalNumber(angle.get_value(degrees=True), unit="^{\circ}")
                        #value.next_to(angle, UR)
                        TP = Arrow(
                                start=P, 
                                end=UP, 
                                buff=0, 
                                tip_shape=StealthTip, 
                                max_stroke_width_to_length_ratio=1.25,
                                max_tip_length_to_length_ratio=0.05).set_angle(tp.get_value()+PI/2)
                        TQ = Arrow(
                                start=Q, 
                                end=UP, 
                                buff=0, 
                                tip_shape=StealthTip,
                                max_stroke_width_to_length_ratio=1.5,
                                max_tip_length_to_length_ratio=0.05).set_angle(tq.get_value()+PI/2)
                        group = VGroup(Line(P, Q, stroke_width=1.5), RP, RQ, TP, TQ, dp, dq)
                        return group
                
                PQ = always_redraw(get_linePQ)
                self.add(cp, cq, PQ)
                
                self.play(
                        tp.animate.set_value(15*PI), 
                        tq.animate.set_value(10*PI), 
                        run_time=15, 
                        rate_func=rate_functions.linear)
                




from manim import *

class SineCurveUnitCircle(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

