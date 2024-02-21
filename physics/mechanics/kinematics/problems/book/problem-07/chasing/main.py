from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        cat = Dot().shift(2*UP)
        dog = Dot()
        value = ValueTracker(0)

        def get_unit_vector(u, v):
            v_f = v.get_center()
            u_f = u.get_center()
            unit_vector = (v_f-u_f)/(np.linalg.norm(v_f-u_f))
            return unit_vector

        v_cat = Arrow(cat.get_center(), cat.get_center())
        v_dog = Arrow(dog.get_center(), dog.get_center())
        v_cat.add_updater(lambda m: m.become(Arrow(cat.get_center(), cat.get_center() + RIGHT, buff=0)))
        v_dog.add_updater(
                lambda m: m.become(
                    Arrow(
                        dog.get_center(), 
                        dog.get_center() + get_unit_vector(dog, cat),
                        buff=0
                        )
                    )
                )
        cat.add_updater(lambda x: x.set_x(value.get_value()-2))
        v=1.05
        dog.add_updater(
                lambda x: x.set_x(
                    -2 + v*(get_unit_vector(dog, cat)[0]*(value.get_value()))
                    )
                )
        dog.add_updater(
                lambda y: y.set_y(
                    -2 + v*(get_unit_vector(dog, cat)[1]*value.get_value())
                    )
                )

        trace_dog = TracedPath(dog.get_center)
        trace_cat = TracedPath(cat.get_center)
        self.add(v_cat, v_dog, cat, dog, value, trace_dog, trace_cat)
        value.add_updater(lambda m, dt: m.increment_value(dt))
        self.wait(5)





