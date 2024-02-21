from manim import *
class AxesTemplate(Scene):
    def construct(self):
        graph = Axes(
            x_range=[-1,11,11],
            y_range=[-6,6,6],
         	x_length=6,
            y_length=6,
            axis_config={"include_tip":False,
                        }
        )
        plot = graph.plot(lambda x: 3*np.sin(x) / np.e ** 2 * x)

        t = ValueTracker(0.1)
        def circ():
       	    position = graph.input_to_graph_point(x=t.get_value(), graph=plot)
       	    position_i = graph.input_to_graph_point(x=t.get_value()-0.1, graph=plot)
       	    position_f = graph.input_to_graph_point(x=t.get_value()+0.1, graph=plot)
            circle = Circle.from_three_points(position_i, position, position_f, color=WHITE)
            dot = Dot(circle.get_center()).scale(0.5)
            group = VGroup(circle, dot)
            return group
        
        c = always_redraw(circ)
        self.add(graph, plot, t, c)
        self.play(t.animate.set_value(11), run_time=10, rate_func=rate_functions.linear)




class CodeH(Scene):
    def construct(self):
        c = open('tikz-1.tex', 'r')
        code = Code(code=c, language='tex')
        self.add(code)
