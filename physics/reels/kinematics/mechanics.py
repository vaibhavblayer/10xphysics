from vmanim import *
from manim import *
from manim_physics import *
import random as rn


class PendulumExample(SpaceScene):
    def construct(self):
        # positions of the pendulum balls
        dot = Dot(point=UP)
        bob_positions = [RIGHT * 1.5 + UP,
                         RIGHT * 1.5 + UP * 2.5,
                         RIGHT * 3 + UP * 2.5]

        pendulum = MultiPendulum(
            *bob_positions,
            pivot_point=UP,
            bob_style={"color": WHITE, "fill_opacity": 1, "radius": 0.15},
        )

        self.make_rigid_body(pendulum.bobs)
        pendulum.start_swinging()

        self.add(pendulum, dot)

        # we will track the movement of the pendulum balls
        for i, bob in enumerate(pendulum.bobs):
            if i == 1:
                self.bring_to_back(TracedPath(
                    bob.get_center, stroke_color=BLUE_D))
            elif i == 2:
                self.bring_to_back(TracedPath(
                    bob.get_center, stroke_color=GREEN_D))
            else:
                self.bring_to_back(TracedPath(
                    bob.get_center, stroke_color=PINK
                ))

        self.wait(60)


class SHM(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        center = Dot()
        axes = ThreeDAxes()
        bob = Dot3D(point=RIGHT*3, radius=0.25)
        radius = Line(center.get_center(), bob.get_center())
        radius.add_updater(lambda m: m.become(
            Line(center.get_center(), bob.get_center())))
        self.add(axes, radius, center, bob)

        theta.set_value(60*DEGREES)
        phi.set_value(60*DEGREES)
        self.play(
            Rotating(
                bob,
                radians=4*PI,
                about_point=ORIGIN
            ),
            run_time=5)

        self.play(
            Rotating(
                bob,
                radians=8*PI,
                about_point=ORIGIN
            ),
            phi.animate.set_value(90*DEGREES),
            theta.animate.set_value(0*DEGREES),
            run_time=10)

        # phi.set_value(90*DEGREES)
        self.play(
            Rotating(
                bob,
                radians=8*PI,
                about_point=ORIGIN
            ),
            run_time=15)


class Dipole(Scene):
    def construct(self):
        p = LabeledDot("+", point=2*(RIGHT+UP))
        n = LabeledDot("-", point=2*(LEFT+DOWN))
        line = Line(n.get_center(), p.get_center())
        c = Dot()
        e = MathTex("\\vec{E}").move_to(4*RIGHT)

        line.add_updater(lambda m: m.become(
            Line(n.get_center(), p.get_center())))

        for i in range(-4, 5, 1):
            field = Arrow(start=3.5*LEFT + i*UP, end=3.5 *
                          RIGHT + i*UP, stroke_width=2)
            self.add(field)

        self.add(line, n, p, c, e)

        for i in range(1, 61):
            self.play(
                Rotating(p,
                         radians=((-1)**i)*PI/2,
                         about_point=ORIGIN
                         ),

                Rotating(
                    n,
                    radians=((-1)**i)*PI/2,
                    about_point=ORIGIN
                ),
                rate_func=rate_functions.ease_in_out_cubic,
                run_time=0.5
            )


class Dipole3D(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        p = LabeledDot("+", point=2*(RIGHT+UP))
        n = LabeledDot("-", point=2*(LEFT+DOWN))
        line = Line(n.get_center(), p.get_center())
        c = Dot()
        e = MathTex("\\vec{E}").move_to(4*RIGHT)

        line.add_updater(lambda m: m.become(
            Line(n.get_center(), p.get_center())))

        for i in range(-4, 5, 1):
            field = Arrow(start=3.5*LEFT + i*UP, end=3.5 *
                          RIGHT + i*UP, stroke_width=2)
            self.add(field)

        self.add(line, n, p, c, e)

        for i in range(1, 61):
            self.play(
                AnimationGroup(
                    Rotating(p,
                             radians=((-1)**i)*PI/2,
                             about_point=ORIGIN
                             ),

                    Rotating(
                        n,
                        radians=((-1)**i)*PI/2,
                        about_point=ORIGIN
                    ),
                    rate_func=rate_functions.ease_in_out_cubic
                ),
                phi.animate.set_value(phi.get_value() + 0.05*i*DEGREES),
                theta.animate.set_value(theta.get_value() - 0.2*i*DEGREES),
                distance_to_origin.animate.set_value(
                    distance_to_origin.get_value()+0.1*np.sin(0.5*i)),
                rate_func=rate_functions.linear,
                run_time=0.5
            )


class ThreeDLightSourcePosition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                2.5 * np.cos(u) * np.cos(v),
                2.5 * np.cos(u) * np.sin(v),
                2.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[PI / 6, PI / 6 + 10*DEGREES],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(
            3*IN)  # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, sphere)


class VectPractice(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        def func(pos):
            dot = np.dot(pos, pos)
            r3 = dot**(3/2)
            if dot == 0:
                return RIGHT
            else:
                return 2*RIGHT/r3 + UP/r3
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 2)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()


class ElectricFieldExample(Scene):
    def construct(self):
        charge1 = Charge(-2, add_glow=True)
        charge2 = Charge(2, add_glow=True)
        line = Line(charge1.get_center(), charge2.get_center())
        line.add_updater(lambda m: m.become(
            Line(charge1.get_center(), charge2.get_center())))

        def rebuild(field):
            """Funkce která přestaví elektrické pole."""
            field.become(ElectricField(charge1, charge2))

        field = ElectricField(charge1, charge2)

        self.add(line, field, charge1, charge2)

        self.play(
            Write(field),
            FadeIn(charge1),
            FadeIn(charge2),
            Write(line)
        )

        field.add_updater(rebuild)

        self.play(
            charge1.animate.shift(LEFT),
            charge2.animate.shift(RIGHT),
            run_time=5,
        )

        self.play(
            Rotating(
                charge1,
                radians=2*PI,
                about_point=ORIGIN
            ),
            Rotating(
                charge2,
                radians=2*PI,
                about_point=ORIGIN
            ),
            run_time=10,
        )

        self.play(
            charge1.animate.move_to(ORIGIN),
            charge2.animate.move_to(ORIGIN),
            run_time=2,
        )

        self.play(
            Unwrite(field),
            FadeOut(charge1),
            FadeOut(charge2),
            Unwrite(line)
        )


class LessWrong(Scene):
    def construct(self):
        n = ValueTracker(3)
        poly = RegularPolygon(n=4, radius=2)
        poly.add_updater(
            lambda m: m.become(
                RegularPolygon(int(n.get_value()), radius=3)
            )
        )

        def text_update(mobject):
            sides = int(n.get_value())
            if sides == 3:
                tex_exp = f"\\textit{{wrong\\_}}"
            else:
                tex_exp = f"\\textit{{less wrong\\_}}"
            mobject.become(
                MathTex(tex_exp).scale(0.25 + 5/sides)
            )

        text = MathTex(f"\\textit{{wrong\\_}}")
        text.add_updater(text_update)

        def pii(mobject):
            sides = int(n.get_value())
            value_pi = sides * np.sin(PI/sides)
            tex_exp = f"\\pi=\\dfrac{{\\textit{{perimeter}}}}{{\\textit{{diameter}}}}={value_pi:.10f}"
            mobject.become(
                MathTex(tex_exp).shift(4.5*DOWN)
            )

        pi = Tex(r"$\pi$")
        pi.add_updater(pii)

        self.add(n, poly, pi, text)

        n.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(60)


class ElectricFieldLine(Scene):
    def construct(self):
        charges = []
        for i in range(0, 17):
            charge = Charge(2, add_glow=True)
            self.add(charge)
            charges.append(charge)

        def rebuild(field):
            field.become(ElectricField(
                *[charges[i] for i in range(0, 17)]
            ))

        field = ElectricField(
            *[charges[i] for i in range(0, 17)]
        )

        self.add(field)

        field.add_updater(rebuild)

        for i in range(0, 9):
            self.play(
                charges[i].animate.shift((4-0.5*i)*RIGHT),
                charges[i+8].animate.shift((4-0.5*i)*LEFT)
            )

        for i in range(0, 8):
            self.play(
                Rotating(
                    charges[i],
                    radians=0.5*PI,
                    about_point=ORIGIN
                ),
                Rotating(
                    charges[i+8],
                    radians=0.5*PI,
                    about_point=ORIGIN
                ),
                run_time=1
            )


class Rain(SpaceScene):
    def construct(self):
        drops = []
        for i in range(50):
            pos_x = rn.randint(-3, 4)
            pos_y = rn.randint(0, 5)
            drop = Dot(pos_x*LEFT + pos_y*UP)*26
            self.add(drop)
            drops.append(drop)

        plane_r = Line(UP, 4*RIGHT+2*DOWN)
        self.add(plane_r)
        self.make_static_body(plane_r)

        plane_l = Line(UP, 4*LEFT+2*DOWN)
        self.add(plane_l)
        self.make_static_body(plane_l)

        for drop in drops:
            self.make_rigid_body(drop)
        self.wait(5)


class VerticalCircle(SpaceScene):
    def construct(self):
        ball = Dot(
            point=2*(2*UP),
            radius=0.2
        )
        ax = Axes()

        path = Line(2*(1.5*LEFT+UP), 2*(RIGHT+DOWN))
        arc = Arc(2, -PI/2, PI/2, arc_center=2*RIGHT)
        plot = ax.plot(lambda x: x**2)

        self.add(ball, plot)
        # self.make_static_body(path, arc)

        # dot = Dot(2*(1.5*LEFT+UP))
        # tp = TracedPath(dot.get_center)

        # self.add(tp)
        # self.play(
        #     dot.animate.shift(2*(RIGHT+DOWN))
        # )
        # self.play(
        #     Rotating(
        #         dot,
        #         radians=PI,
        #         about_point=2*RIGHT
        #     ),
        #     run_time=2
        # )
        # self.make_static_body(tp)
        self.make_static_body(plot)
        self.make_rigid_body(ball)

        self.wait(5)


class MagnetismExampleScene(Scene):
    def construct(self):
        magnet1 = BarMagnet().shift(LEFT * 2.5)
        magnet2 = BarMagnet().shift(RIGHT * 2.5)
        magnet3 = BarMagnet().shift(UP * 2.5)
        magnet4 = BarMagnet().shift(DOWN * 2.5)
        field = MagneticField(magnet1, magnet2, magnet3, magnet4)
        self.add(field, magnet1, magnet3)
        self.play(Write(field))


class Limit(Scene):
    def construct(self):
        n = ValueTracker(0)
        title = Tex(
            r"\[ \lim_{x \to \infty} \left( 1 + \dfrac{1}{x} \right)^x = e \]"
        ).move_to(3*UP).scale(1.2)

        def expn(mobject):
            if int(n.get_value()) != 0:
                x = int(n.get_value())
                N = f"{x:.0e}".split('+')
                P = int(N[1])
                M = N[0].split('e')
                X = int(M[0])

                e = (1 + 1/x)**x

                if x > 1000000:
                    tex_exp = f"\\[\\left( 1 + \\dfrac{{1}}{{{X}\\times 10^{{{P}}}}} \\right)^{{{X}\\times 10^{{{P}}}}}={e:.10f}\\]"
                else:
                    tex_exp = f"\\[\\left( 1 + \\dfrac{{1}}{{{x}}} \\right)^{{{x}}}={e:.10f}\\]"
                mobject.become(
                    Tex(tex_exp).shift(2*DOWN)
                )

        E = Tex(
            r"\[ \left( 1 + \dfrac{1}{1} \right)^1 = 2 \]"
        ).shift(2*DOWN)
        E.add_updater(expn)

        self.add(n, title, E)

        self.play(
            Write(title),
            Write(E)
        )

        for i in range(2, 9):
            n.add_updater(
                lambda mobject, dt: mobject.increment_value(int(f'1e{i}')*dt)
            )
            self.wait(2)

        n.add_updater(lambda mobject, dt: mobject.increment_value(1e10*dt))
        self.wait(5)


class Squares(SpaceScene):

    def construct(self):
        def lower_squares():
            SG = VGroup()
            for i in range(0, 9):
                for j in range(0, 3):
                    if (i not in [6]) and (j in [0, 1]):
                        SG.add(
                            Square().scale(0.5).shift((4-i)*LEFT + j*UP)
                        )

            return SG

        LS = lower_squares()
        self.add(LS)


class ElectricFieldSquare(Scene):
    def construct(self):
        charges = []
        for i in range(0, 16):
            charge = Charge(2, add_glow=False)
            self.add(charge)
            charges.append(charge)

        def rebuild(field):
            field.become(ElectricField(
                *[charges[i] for i in range(0, 16)]
            ))

        field = ElectricField(
            *[charges[i] for i in range(0, 16)]
        )

        self.add(field)

        field.add_updater(rebuild)

        for i in range(0, 2):
            self.play(
                #  2 -> 5
                charges[i+2].animate.shift((1-0.5*i)*RIGHT),
                charges[i+4].animate.shift((1-0.5*i)*LEFT),

                # 6 -> 10
                charges[i+6].animate.shift(RIGHT),
                charges[i+8].animate.shift(RIGHT),
                charges[i+10].animate.shift(RIGHT),

                # 12 -> 16
                charges[i+12].animate.shift(LEFT),
                charges[i+14].animate.shift(LEFT),
                charges[i+16].animate.shift(LEFT),
            )

        for i in range(0, 2):
            self.play(
                #  0 -> 4
                # charges[i+1].animate.shift((1-0.5*i)*RIGHT),
                # charges[i+3].animate.shift((1-0.5*i)*LEFT),

                # 5 -> 10
                charges[i+5].animate.shift((1-0.5*i)*DOWN),
                charges[i+7].animate.shift((2-0.5*i)*DOWN),

                charges[i+9].animate.shift(2*DOWN),

                # 11 -> 16
                charges[i+11].animate.shift((1-0.5*i)*DOWN),
                charges[i+13].animate.shift((2-0.5*i)*DOWN),

                charges[i+15].animate.shift(2*DOWN),
            )

        for i in range(0, 2):
            self.play(
                #  0 -> 4
                # charges[i+1].animate.shift((1-0.5*i)*RIGHT),
                # charges[i+3].animate.shift((1-0.5*i)*LEFT),

                # 5 -> 10
                # charges[i+5].animate.shift((1-0.5*i)*DOWN),
                # charges[i+7].animate.shift((2-0.5*i)*DOWN),
                charges[i+9].animate.shift((1-0.5*i)*LEFT),

                # 11 -> 16
                # charges[i+11].animate.shift((1-0.5*i)*DOWN),
                # charges[i+13].animate.shift((2-0.5*i)*DOWN),
                charges[i+15].animate.shift((1-0.5*i)*RIGHT),
            )

        # for i in range(0, 5):
        #     self.play(
        #         charges[i].animate.shift((2-0.5*i)*RIGHT),
        #         charges[i+4].animate.shift((2-0.5*i)*DOWN + 2*RIGHT),
        #         charges[i+8].animate.shift((2-0.5*i)*(LEFT)),
        #         charges[i+12].animate.shift((2-0.5*i)*DOWN + 2*LEFT)
        #     )

        # for i in range(0, 8):
        #     self.play(
        #         Rotating(
        #             charges[i],
        #             radians=0.5*PI,
        #             about_point=ORIGIN
        #         ),
        #         Rotating(
        #             charges[i+8],
        #             radians=0.5*PI,
        #             about_point=ORIGIN
        #         ),
        #         run_time=1
        #     )


class Collision(SpaceScene):

    def construct(self):
        Circle.set_default(color=WHITE)

        i_line = Line(3.5*LEFT, 3.5*RIGHT).shift(2*DOWN)
        e_line = i_line.copy().shift(5*UP)
        p_i_line = i_line.copy().shift(5*DOWN)

        i_m = Circle().shift(UP)
        e_m = i_m.copy().shift(5*UP)
        p_i_m = i_m.copy().shift(5*DOWN)

        i_t = MathTex(r"\textit{inelastic collision}").next_to(
            i_line, DOWN).scale(0.5)
        e_t = MathTex(r"\textit{elastic collision}").next_to(
            e_line, DOWN).scale(0.5)
        p_i_t = MathTex(r"\textit{perfectly inelastic collision}").next_to(
            p_i_line, DOWN).scale(0.5)

        self.add(i_line, e_line, p_i_line, i_m, e_m, p_i_m, i_t, e_t, p_i_t)

        self.make_static_body(i_line, elasticity=0.9)
        self.make_static_body(e_line)
        self.make_static_body(p_i_line, elasticity=0)

        self.make_rigid_body(i_m, elasticity=0.9)
        self.make_rigid_body(e_m, elasticity=1)
        self.make_rigid_body(p_i_m, elasticity=0)

        self.wait(30)


class Collisions(SpaceScene):

    def construct(self):
        Circle.set_default(color=WHITE)

        COLLISIONS = [
            ['elastic collision', 1],
            ['inelastic collision', 0.98],
            ['perfectly inelastic collision', 0]
        ]

        OBJECTS = VGroup()

        for col in COLLISIONS:
            S = Line(3.5*LEFT, 3.5*RIGHT)
            C = Circle().next_to(S, 8*UP)
            T = MathTex(f'\\textit{{{col[0]}}}').next_to(S, DOWN).scale(0.5)
            self.add(S, C, T)
            OBJECTS.add(
                VGroup(
                    S, C, T
                )
            )

        self.add(OBJECTS.arrange(buff=0.2, direction=DOWN))
        for obj in zip(OBJECTS, COLLISIONS):
            self.make_rigid_body(obj[0][1], elasticity=obj[1][1])
            self.make_static_body(obj[0][0], elasticity=obj[1][1])

        self.wait(30)


class ElectricFieldHexagon(Scene):
    def construct(self):
        charges = []
        for i in range(0, 6):
            charge = Charge(2, add_glow=True)
            self.add(charge)
            charges.append(charge)

        def rebuild(field):
            field.become(ElectricField(
                *[charges[i] for i in range(0, 6)]
            ))

        field = ElectricField(
            *[charges[i] for i in range(0, 6)]
        )

        self.add(field)

        field.add_updater(rebuild)

        for i in range(0, 3):
            self.play(
                charges[i].animate.shift(2*RIGHT),
                charges[i+3].animate.shift(2*LEFT)
            )

        for i in range(0, 3):
            self.play(
                Rotating(
                    charges[i],
                    radians=i*PI/3,
                    about_point=ORIGIN
                ),
                Rotating(
                    charges[i+3],
                    radians=i*PI/3,
                    about_point=ORIGIN
                ),
                run_time=1
            )


class StandingWaveExampleScene(Scene):
    def construct(self):
        title = MathTex(r"\textit{Standing Wave}").move_to(7.5*UP)
        wave1 = StandingWave(1, 8, 2)
        wave2 = StandingWave(2, 8, 4)
        wave3 = StandingWave(3, 8, 3)
        wave4 = StandingWave(4, 8, 2)

        waves = VGroup(wave1, wave2, wave3, wave4)
        dots = VGroup()
        waves.arrange(DOWN, buff=2).move_to(ORIGIN)

        for w in waves:
            g = VGroup()
            g.add(Dot(w.get_left()))
            g.add(Dot(w.get_right()))
            dots.add(g)

        self.add(title, waves, dots)
        for wave in waves:
            wave.start_wave()
        self.wait(30)


# class TestingSubclass(Scene):
#     def construct(self):
#         c = DCircle(3)
#         f = Field().shift(4*UP)

#         self.play(
#             Create(c),
#             Create(f)
#         )

#         self.wait(2)


class Magnetics(Scene):
    def construct(self):
        t = ValueTracker(0)

        field = VGroup()
        for i in range(-4, 5):
            for j in range(-2, 7):
                field.add(MathTex(r"\times").shift(i*RIGHT + j*(UP)))

        charge1 = LabeledDot(label=r"2q", radius=0.35).shift(2*RIGHT + 2*UP)
        charge2 = LabeledDot(label=r"q", radius=0.35).shift(4*RIGHT * 2*UP)

        radius = MathTex(r"r=\dfrac{mv}{Bq}").shift(4*DOWN)
        title = MathTex(r"\textit{charge in a uniform magnetic field}").shift(
            6*DOWN).scale(0.65)

        def charge1mxy(mobject):
            mobject.set_x(2 * np.cos(2*t.get_value()*DEGREES))
            mobject.set_y(2 + 2 * np.sin(2*t.get_value()*DEGREES))

        def charge2mxy(mobject):
            mobject.set_x(4 * np.cos(t.get_value()*DEGREES))
            mobject.set_y(2 + 4 * np.sin(t.get_value()*DEGREES))

        charge1.add_updater(charge1mxy)
        charge2.add_updater(charge2mxy)

        path1 = TracedPath(charge1.get_center)
        path2 = TracedPath(charge2.get_center)

        self.add(t, field, path1, path2, charge1, charge2,
                 radius, title)

        self.play(
            Write(field),
            Write(radius),
            Write(title),
            Write(charge1),
            Write(charge2)
        )

        t.add_updater(
            lambda mobject, dt: mobject.increment_value(100*dt)
        )

        self.wait(30)


class HelicalPath(ThreeDScene):
    def construct(self):
        # phi -> x_axis, theta -> y_axis, gamma -> z_axis
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        t = ValueTracker(0)

        field = Field()
        axes = ThreeDAxes().scale(0.5)
        charge = Dot3D(
            point=axes.coords_to_point(3, 0, 0),
            radius=0.12,
            color=WHITE
        )
        radius = MathTex(r"r=\dfrac{mv_\perp}{Bq}").shift(7*UP)
        title = Title(
            r"$\textit{charge projected in a uniform magnetic field at some angle}$",
            include_underline=False
        ).scale(0.65)

        def charge_mxyz(mobject):
            mobject.set_x(2 * np.cos(5*t.get_value()*DEGREES))
            mobject.set_y(2 * np.sin(5*t.get_value()*DEGREES))
            mobject.set_z(0.01*t.get_value())

        charge.add_updater(charge_mxyz)

        path = TracedPath(charge.get_center)

        self.add(t, field, path, charge,
                 axes)

        self.add_fixed_in_frame_mobjects(radius, title)
        self.play(
            Write(field),
            Write(radius),
            Write(title),
            Write(charge)
        )

        theta.set_value(-90*DEGREES)
        phi.set_value(0*DEGREES)

        t.add_updater(
            lambda mobject, dt: mobject.increment_value(10*dt)
        )

        self.play(
            gamma.animate.set_value(gamma.get_value() - 90*DEGREES),
            run_time=5
        )

        self.play(
            phi.animate.set_value(phi.get_value() + 360*DEGREES),
            rate_func=rate_functions.linear,
            run_time=40
        )

        self.play(
            distance_to_origin.animate.set_value(
                distance_to_origin.get_value() - 5),
            rate_func=rate_functions.linear,
            run_time=5
        )


class HS(ThreeDScene):
    def construct(self):
        hs = HemiSphere(radius=3)
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(hs)


class Planes(ThreeDScene):
    def construct(self):
        # phi -> x_axis, theta -> y_axis, gamma -> z_axis
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        title = Title(
            r"$\textit{Electric flux through a hemisphere}$",
            include_underline=False
        ).scale(0.65).shift(1.25*DOWN)
        flux = MathTex(r"\phi_{\vec{E}} = E\cdot \pi r^2 ").shift(5*DOWN)
        axes = ThreeDAxes()
        cp = CircularPlane().scale(3).set_fill(GRAY_E).shift(IN)
        hs = HemiSphere(radius=3).shift(3*OUT)
        plane = Plane(radius=3).shift(IN).scale(3)
        # charge = Dot3D().scale(1.5).shift(3*OUT)

        def func(pos):
            return pos*IN

        def funcp(pos):
            return pos*OUT

        vf = ArrowVectorField(
            func,
            x_range=[-3.5, 3.5, 0.2],
            y_range=[-3.5, 3.5, 0.2],
            z_range=[4, 4, 0.5],
            three_dimensions=True
        )

        pvf = ArrowVectorField(
            funcp,
            x_range=[-3, 3, 0.1],
            y_range=[-3, 3, 0.1],
            z_range=[-0.5, 0, 0.5],
            three_dimensions=True
        )  # .shift(3*OUT)

        def clipped_vf(vf):
            c_vf = VGroup()
            for f in vf:
                l = np.array([f.get_x(), f.get_y(), f.get_z()])
                n = np.sqrt(np.sum(np.square(l)))
                if n <= 3:
                    c_vf.add(f)

            return c_vf

        cvf = clipped_vf(pvf)

        self.add_fixed_in_frame_mobjects(title, flux)
        self.set_camera_orientation(theta=70 * DEGREES, phi=0 * DEGREES)
        self.add(cp, hs, vf, cvf)

        self.play(
            Write(hs),
            Write(vf),
            Write(cvf),
            Write(cp)
        )

        self.play(
            phi.animate.set_value(phi.get_value() + 150*DEGREES),
            theta.animate.set_value(theta.get_value() + 480*DEGREES),
            rate_func=rate_functions.linear,
            run_time=30
        )


class TestingRTitle(Scene):
    def construct(self):

        title = RTitle(r"$\textit{Hello there}$")
        axes = RAxes()
        self.add(title, axes)

        L1 = r"a &=b \\"
        L2 = r"c &=d + r \\"
        L3 = r"d &=f + 4 + 7 + p"

        tex = MathTex(L1, L2, L3)
        self.play(
            Succession(
                Write(tex[0]),
                Write(tex[1]),
                Write(tex[2])
            )

        )


class WorkEnergyTheorem(Scene):
    def construct(self):
        title = RTitle(r"\textit{Work Energy Theorem}")

        L1 = r"\vec{v} &= \dfrac{\d{\vec{r}}}{\d{t}}"
        L2 = r"\vec{v} \cdot \d{\vec{v}} &= \dfrac{\d{\vec{r}}}{\d{t}} \cdot \d{\vec{v}}"
        L3 = r"v \d{v} &= \vec{a} \cdot \d{\vec{r}}"
        L4 = r"mv \d{v} &= m\vec{a} \cdot \d{\vec{r}}"
        L5 = r"m \int_u^v v \d{v} &= \int_{\vec{r_i}}^{\vec{r_f }}\vec{F} \cdot \d{\vec{r}}"
        L6 = r"\Delta K.E. &= W_\textit{all forces}"

        LL = [L1, L2, L3, L4, L5, L6]
        L = [x + r"\\[3mm]" for x in LL]

        equation = MathTex(*L)
        self.play(
            Succession(
                Write(title),
                Write(equation[0]),
                AnimationGroup(
                    FadeIn(equation[1], shift=DOWN),
                    run_time=2
                ),
                AnimationGroup(
                    FadeIn(equation[2], shift=DOWN),
                    run_time=2
                ),
                AnimationGroup(
                    FadeIn(equation[3], shift=DOWN),
                    run_time=2
                ),
                AnimationGroup(
                    FadeIn(equation[4], shift=DOWN),
                    run_time=2
                ),
                AnimationGroup(
                    FadeIn(equation[5], shift=DOWN),
                    run_time=2
                )
            )

        )
        self.wait(2)


class WorkEnergyTheoremRotation(Scene):
    def construct(self):
        title = RTitle(r"\textit{Work Energy Theorem\\Rotational Motion}")

        L1 = r"\vec{v} &= \dfrac{\d{\vec{r}}}{\d{t}}"
        L2 = r"\vec{v} \cdot \d{\vec{v}} &= \dfrac{\d{\vec{r}}}{\d{t}} \cdot \d{\vec{v}}"
        L3 = r"v \d{v} &= \vec{a} \cdot \d{\vec{r}}"
        L4 = r"mv \d{v} &= m\vec{a} \cdot \d{\vec{r}}"
        L5 = r"m  r\omega r\d{\omega} &= m r\vec{\alpha} \cdot r \d{\vec{\theta}}"
        L6 = r"mr^2 \omega \d{\omega} &= mr^2 \vec{\alpha} \cdot \d{\vec{\theta}}"
        L7 = r"I\int_{\omega_i}^{\omega_f} \omega \d{\omega} &= \int_{\theta_i}^{\theta_f} \vec{\tau} \cdot \d{\vec{\theta}}"
        L8 = r"\Delta \textit{R.K.E.} &= W_\textit{all torques}"

        ref_tex_1 = MathTex(
            r"v&=r\omega\\a &= r\alpha"
        ).shift(3.5*RIGHT).scale(0.75)

        ref_tex_2 = MathTex(
            r"\tau = I\alpha"
        ).shift(3.5*RIGHT + 3*DOWN).scale(0.75)

        LL = [L1, L2, L3, L4, L5, L6, L7, L8]
        L = [x + r"\\[3mm]" for x in LL]

        equation = MathTex(*L)
        self.play(
            Succession(
                Write(title),
                Write(equation[0])
            )
        )

        for e in equation[1:4]:
            self.play(
                FadeIn(e, shift=DOWN),
                run_time=1
            )

        self.play(
            FadeIn(ref_tex_1, shift=LEFT),
            run_time=2
        )

        for e in equation[4:6]:
            self.play(
                FadeIn(e, shift=DOWN),
                run_time=2
            )

        self.play(
            FadeIn(ref_tex_2, shift=LEFT),
            run_time=2
        )

        for e in equation[6:]:
            self.play(
                FadeIn(e, shift=DOWN),
                run_time=2
            )

        self.wait(2)


class Sine3D(ThreeDScene):
    def construct(self):
        t = ValueTracker(0)
        axes = ThreeDAxes(x_range=[-4, 4], x_length=8)
        surface = Surface(
            lambda u, v: np.array([u, np.cos(u), v]),
            u_range=[-PI, PI],
            v_range=[0, 0],
            resolution=24,
        )
        surface.add_updater(
            lambda m: m.become(
                Surface(
                    lambda u, v: np.array([u, 2*np.sin(u), v]),
                    u_range=[-PI, PI],
                    v_range=[0, t.get_value()],
                    resolution=24,
                    checkerboard_colors=[GRAY_D, GRAY_D],
                    stroke_color=GRAY_D,
                )
            )
        )
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(t, axes, surface)
        t.add_updater(
            lambda mobject, dt: mobject.increment_value(dt)
        )

        self.wait(2)


class TestingButton(Scene):
    def construct(self):
        b = ToggleButton(corner_radius=0.8)

        self.add(b)

        for i in range(10):
            self.play(
                b.animate.toggle()
            )
            self.wait(1/(i+1))


class GenSphere(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        t = ValueTracker(0)
        axes = ThreeDAxes().scale(0.5)
        title = RTitle(r"\textit{Sphere}")

        X = r"x &= \cos(\theta)\cdot\sin(\phi)\\"
        Y = r"y &= \sin(\theta)\cdot\sin(\phi)\\"
        Z = r"z &= -\cos(\phi)"
        coords = MathTex(X, Y, Z).shift(5*DOWN)

        surface = Surface(
            lambda u, v: np.array([u, np.cos(u), v]),
            u_range=[-PI, PI],
            v_range=[0, 0],
            resolution=24,
        )

        def func(u, v):
            return 3*np.array([
                np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -np.cos(v)
            ])
        surface.add_updater(
            lambda m: m.become(
                Surface(
                    func,
                    u_range=[0, 2*t.get_value()],
                    v_range=[0, t.get_value()],
                    resolution=24,
                    checkerboard_colors=[GRAY_C, GRAY_C],
                    stroke_color=GRAY_D,
                )
            )
        )
        self.add_fixed_in_frame_mobjects(title, coords)
        self.set_camera_orientation(theta=60 * DEGREES, phi=60 * DEGREES)
        self.add(t, axes, surface)

        def funct(mobject, dt):
            if t.get_value() <= PI:
                mobject.increment_value(0.5*dt)

        t.add_updater(funct)
        self.play(
            theta.animate.set_value(theta.get_value() + 360*DEGREES),
            rate_func=rate_functions.linear,
            run_time=8
        )

        self.wait(1)


class GenSpiral(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        t = ValueTracker(0)
        axes = ThreeDAxes().scale(0.5)
        title = RTitle(r"\textit{Helicoid}")

        X = r"x &= \theta\cdot\cos(\phi)\\"
        Y = r"y &= \theta\cdot\sin(\phi)\\"
        Z = r"z &= \phi"
        coords = MathTex(X, Y, Z).shift(5*DOWN)

        def func(u, v):
            return 2*np.array([
                u*np.cos(v), u*np.sin(v), 0.4*v
            ])

        surface = Surface(
            func,
            u_range=[-PI, PI],
            v_range=[0, 0],
            resolution=24,
        )

        surface.add_updater(
            lambda m: m.become(
                Surface(
                    func,
                    u_range=[0, PI],
                    v_range=[0, t.get_value()],
                    resolution=24,
                    checkerboard_colors=[GRAY_C, GRAY_C],
                    stroke_color=GRAY_C,
                )
            )
        )
        self.add_fixed_in_frame_mobjects(title, coords)
        self.set_camera_orientation(theta=60 * DEGREES, phi=60 * DEGREES)
        self.add(t, axes, surface)

        def funct(mobject, dt):
            if t.get_value() <= 4*PI:
                mobject.increment_value(0.5*dt)

        t.add_updater(funct)
        self.play(
            phi.animate.set_value(phi.get_value() + 20*DEGREES),
            theta.animate.set_value(theta.get_value() + 360*DEGREES),
            zoom.animate.set_value(theta.get_value()*0.4),
            rate_func=rate_functions.linear,
            run_time=30
        )

        self.wait(2)


class GenCylinder(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        t = ValueTracker(0)
        axes = ThreeDAxes().scale(0.5)
        title = RTitle(r"\textit{Cylinder}")

        X = r"x &= \cos(\theta)\\"
        Y = r"y &= \sin(\theta)\\"
        Z = r"z &= \phi"
        coords = MathTex(X, Y, Z).shift(5*DOWN)

        def func(u, v):
            return 2*np.array([
                np.cos(u), np.sin(u), 0.4*v
            ])

        surface = Surface(
            func,
            u_range=[-PI, PI],
            v_range=[0, 0],
            resolution=24,
        )

        surface.add_updater(
            lambda m: m.become(
                Surface(
                    func,
                    u_range=[0, TAU],
                    v_range=[0, t.get_value()],
                    resolution=8,
                    checkerboard_colors=[GRAY_C, GRAY_C],
                    stroke_color=GRAY_C,
                )
            )
        )
        self.add_fixed_in_frame_mobjects(title, coords)
        self.set_camera_orientation(theta=60 * DEGREES, phi=60 * DEGREES)
        self.add(t, axes, surface)

        def funct(mobject, dt):
            if t.get_value() <= 4*PI:
                mobject.increment_value(0.5*dt)

        t.add_updater(funct)
        self.play(
            phi.animate.set_value(phi.get_value() + 20*DEGREES),
            theta.animate.set_value(theta.get_value() + 360*DEGREES),
            zoom.animate.set_value(theta.get_value()*0.4),
            rate_func=rate_functions.linear,
            run_time=5
        )

        # self.wait(2)


class MovePointOnSpiral(ThreeDScene):
    def func(self, u, v):
        return np.array([
            u*np.cos(v), u*np.sin(v), 0.4*v
        ])

    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        t = ValueTracker(0)
        axes_h = ThreeDAxes().scale(0.5)

        title = RTitle(r"\textit{Helicoid}")

        X = r"x &= \theta\cdot\cos(\phi)\\"
        Y = r"y &= \theta\cdot\sin(\phi)\\"
        Z = r"z &= \phi"
        coords = MathTex(X, Y, Z).shift(5*DOWN)

        surface = Surface(
            lambda u, v: axes_h.c2p(*self.func(u, v)),
            u_range=[0, PI],
            v_range=[0, TAU],
            resolution=24,
        )

        def func_p(u, v):
            return np.array([u, v, 0])

        plane = Surface(
            func_p,
            u_range=[0, PI],
            v_range=[0, TAU],
            resolution=24,
        ).shift(7*DOWN + 1.5*LEFT).rotate(90*DEGREES)

        point_on_helix = Dot3D(radius=0.2)
        point_on_plane = Dot3D(radius=0.2)

        def move_point_on_helix(mobject):
            u = t.get_value()
            v = t.get_value()
            mobject.set_x(u*np.cos(v))
            mobject.set_y(u*np.sin(v))
            mobject.set_z(0.4*v)

        def move_point_on_plane(mobject):
            u = t.get_value()
            v = t.get_value()
            mobject.set_x(u)
            mobject.set_y(v)
            mobject.set_z(t.get_value())

        point_on_helix.add_updater(move_point_on_helix)

        self.add_fixed_in_frame_mobjects(title, coords, plane)
        self.set_camera_orientation(theta=60 * DEGREES, phi=60 * DEGREES)
        self.add(t, axes_h, surface,
                 point_on_helix, point_on_plane)

        def funct(mobject, dt):
            if t.get_value() <= 4*PI:
                mobject.increment_value(dt)

        t.add_updater(funct)
        # self.play(
        #     phi.animate.set_value(phi.get_value() + 20*DEGREES),
        #     theta.animate.set_value(theta.get_value() + 360*DEGREES),
        #     zoom.animate.set_value(theta.get_value()*0.4),
        #     rate_func=rate_functions.linear,
        #     run_time=30
        # )

        self.wait(1)


class ElectricFieldArc(Scene):
    def construct(self):
        charges = []
        for i in range(0, 17):
            charge = Charge(2, add_glow=False)
            self.add(charge)
            charges.append(charge)

        def rebuild(field):
            field.become(ElectricField(
                *[charges[i] for i in range(0, 18)]
            ))

        field = ElectricField(
            *[charges[i] for i in range(0, 18)]
        )

        self.add(field)

        field.add_updater(rebuild)

        for i in range(0, 3):
            self.play(
                charges[i].animate.shift(4*RIGHT),
                charges[(i+1)*6].animate.shift(4*RIGHT),
                charges[i].animate.shift(4*RIGHT),
                charges[i].animate.shift(4*RIGHT),
                charges[i].animate.shift(4*RIGHT),
                charges[i].animate.shift(4*LEFT)
            )

        for i in range(0, 8):
            self.play(
                Rotating(
                    charges[i],
                    radians=-5*DEGREES,
                    about_point=ORIGIN
                ),
                Rotating(
                    charges[i+8],
                    radians=5*DEGREES,
                    about_point=ORIGIN
                ),
                run_time=1
            )


class GravitationalFied(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        G = 6.67e-11
        M = 6e27
        R = 6.6e6
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        earth = Sphere()
        def func_field(pos): return -(G*M/(R**2))*pos
        grav_field = ArrowVectorField(
            func_field,
            min_color_scheme_value=2,
            max_color_scheme_value=10,
            colors=colors,
            x_range=[-3.5, 3.5, 0.5],
            y_range=[-3.5, 3.5, 0.5],
            z_range=[-3.5, 3.5, 0.5],
            three_dimensions=True
        )
        self.add(earth, grav_field)
        self.play(
            phi.animate.set_value(
                phi.get_value()+100*DEGREES,
            ),

            run_time=5
        )

#


class Hello(Scene):
    def construct(self):
        title = RTitle(r"\textit{Hello there}")
        self.add(title)
        self.wait(2)

    text = Text("Hello there")
