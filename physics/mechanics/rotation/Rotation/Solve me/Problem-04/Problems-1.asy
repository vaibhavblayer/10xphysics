if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
defaultfilename="Problems-1";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

size(6cm,0);
draw((3,0) -- (0,0) -- (3,4));
draw(arc((0,0), (2,0), (3,4)), arrow=Arrow(HookHead), red);
draw(arc((0,0), (2,0), (3,4), direction=CW), arrow=Arrow(HookHead), blue);
dot((0,0)); dot((2,0)); dot((3,4)); dot((4,0));
draw(circle((0,0), 1.5), blue + linewidth(2.5 pt));
draw(unitcircle);
draw((2,1) -- arc((2,1), 2, 30, 90) -- cycle);
