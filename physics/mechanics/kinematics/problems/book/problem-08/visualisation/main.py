from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        rhombus_3 = RegularPolygon(4, radius=2).shift(2.5*LEFT)
        rhombus_2 = RegularPolygon(4, radius=1.5).next_to(rhombus_3, buff=0)
        rhombus_1 = RegularPolygon(4).next_to(rhombus_2, buff=0)
        velocity_arrow = Arrow(rhombus_1.get_right(), rhombus_1.get_right()+[1, 0, 0], buff=0)




        self.add(
                rhombus_3,
                rhombus_2,
                rhombus_1,
                velocity_arrow
                )



class Rhombus(Scene):
    def construct(self):
        sides = [3, 2, 1]
        tracker = ValueTracker(60)
        angle = tracker.get_value()
        point_0 = 4.5*LEFT
        point_1 = point_0 + sides[0]*2*np.cos(angle*DEGREES)*RIGHT
        point_2 = point_1 + sides[1]*2*np.cos(angle*DEGREES)*RIGHT
        point_3 = point_2 + sides[2]*2*np.cos(angle*DEGREES)*RIGHT
        
        
        point_01 = point_0 + sides[0]*np.sin(angle*DEGREES)*RIGHT

        def point_m(mobject):
            mobject.become(
                    Dot(point=point_0 + sides[0]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT)
            )
        
        def point_n(mobject):
            point_i = point_0 + sides[0]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            mobject.become(
                    Dot(point=point_i + sides[1]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT)
            )
        def point_o(mobject):
            point_i = point_0 + sides[0]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            point_f = point_i + sides[1]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            mobject.become(
                    Dot(point=point_f + sides[2]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT)
            )

        def v_arrow(mobject):
            point_i = point_0 + sides[0]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            point_f = point_i + sides[1]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            point_ff = point_f + sides[2]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            mobject.become(
                    Arrow(point_ff, point_ff + 1.5*RIGHT, buff=0)
            )


        def rhombus_1(mobject):
            mobject.become(
                    Polygon(
                        point_0,
                        point_0 + np.array([sides[0]*np.cos(tracker.get_value()*DEGREES), sides[0]*np.sin(tracker.get_value()*DEGREES), 0]),
                        point_0 + sides[0]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT,
                        point_0 + np.array([sides[0]*np.cos(tracker.get_value()*DEGREES), -1*sides[0]*np.sin(tracker.get_value()*DEGREES), 0])
                        )
                    )
        def rhombus_2(mobject):
            point_i = point_0 + sides[0]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT
            mobject.become(
                    Polygon(
                        point_i,
                        point_i + np.array([sides[1]*np.cos(tracker.get_value()*DEGREES), sides[1]*np.sin(tracker.get_value()*DEGREES), 0]),
                        point_i + sides[1]*2*np.cos(tracker.get_value()*DEGREES)*RIGHT,
                        point_i + np.array([sides[1]*np.cos(tracker.get_value()*DEGREES), -1*sides[1]*np.sin(tracker.get_value()*DEGREES), 0])
                        )
                    )
        def rhombus_3(mobject):
            theta = tracker.get_value()*DEGREES
            point_i = point_0 + sides[0]*2*np.cos(theta)*RIGHT
            point_f = point_i + sides[1]*2*np.cos(theta)*RIGHT
            mobject.become(
                    Polygon(
                        point_f,
                        point_f + np.array([sides[2]*np.cos(theta), sides[2]*np.sin(theta), 0]),
                        point_f + sides[2]*2*np.cos(theta)*RIGHT,
                        point_f + np.array([sides[2]*np.cos(theta), -1*sides[2]*np.sin(theta), 0])
                        )
                    )



        
        r_1 = Polygon(
                point_0,
                point_01,
                point_1,
                -1*point_01
                )
               
        r_1.add_updater(rhombus_1)

        r_2 = Polygon(
                point_0,
                point_01,
                point_1,
                -1*point_01
                )
        r_2.add_updater(rhombus_2)
        r_3 = Polygon(
                point_0,
                point_01,
                point_1,
                -1*point_01
                )
        r_3.add_updater(rhombus_3)

        v_0 = Dot(point=point_0)

        v_1 = Dot(point=point_1)
        v_1.add_updater(point_m)
        
        v_2 = Dot(point=point_2)
        v_2.add_updater(point_n)
        
        v_3 = Dot(point=point_3)
        v_3.add_updater(point_o)

        a_v = Arrow(point_3, point_3+1.5*RIGHT, buff=0)
        a_v.add_updater(v_arrow)

        self.add(r_1, r_2, r_3, a_v, v_0, v_1, v_2, v_3, tracker)
        
        #tracker.add_updater(lambda mobject, dt: mobject.increment_value(-10*dt))
        #self.wait(2)
        

        #tracker.add_updater(lambda mobject, dt: mobject.increment_value(10*dt))
        #self.wait(2)

        self.play(tracker.animate.set_value(35), run_time=2)
        self.play(tracker.animate.set_value(60), run_time=2)
        self.play(tracker.animate.set_value(35), run_time=2)
        self.play(tracker.animate.set_value(60), run_time=2)




from manim import *

class PointWithTrace(Scene):
	def construct(self):
		dot = Dot()
		traced_path = TracedPath(dot.get_center)
		self.add(traced_path, dot)
		self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
		self.play(dot.animate.shift(2*UP))
		self.play(dot.animate.shift(LEFT))
		self.play(dot.animate.shift(UP))
		self.wait()





class Integrate(Scene):
    def construct(self):
        t = r"""
        \begin{align*}
        a &= b\\
        c &= s
        \end{align*}"""
        
        e = Tex(t)

        lines = e._break_up_by_substrings()
        for line in lines:
            self.add(line)

        equation = MathTex(
                r"a &=b\\ b &=d",
                arg_separator=r'\\'
                )

        self.play(Write(lines[0]))
