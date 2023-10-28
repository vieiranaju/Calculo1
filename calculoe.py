
from sympy import symbols, Lambda, sin, cos

x = symbols("x")
f = Lambda(x, (x-1)/(x**2-1))
f

f(0)

f(0.5)

f(0.6)

f(1)

f(0.999999)

f(1.001)

f(1.5)

from pylab import *

def calcula_f(x):
  return (x-1)/(x**2-1)

x = arange(0.1,2,0.01)

y = calcula_f(x)

plot(x,y)
xlabel("Variavel Independente X")
ylabel("Função Y = (x-1)/(x^2 - 1)")
grid(True)
title("Visão geometrica do Conceito de limite")
axhline(y=0, color = 'k')
axvline(x=0, color = 'k')

import math
import sympy

from sympy import symbols, Lambda

t = symbols("t")
h = Lambda(t, (pow((t**2 + 9),1/2 )- 3) / (t**2))
h

h(1)

h(0.001)
from sympy import pi, sin

w = symbols("w")
m = Lambda(w, (sin(pi/w)))
m

from pylab import *
import math
import numpy

def calcula_f(w):
  return sin(pi/w)

w = arange(-10,10,0.01)
m = calcula_f(w)

plot(w, m)
xlabel("Variavel Independente X")
ylabel("Função Y = (x-1)/(x^2 - 1)")
grid(True)
title("Visão geometrica do Conceito de limite")
axhline(y=0, color = 'k')
axvline(x=0, color = 'k')

from sympy import oo, limit, Symbol

x = Symbol('x')

limit((1+1/x)**x, x, oo) # (1+1/x)**x com x tendendo ao oo

from sympy.plotting import plot
from sympy import E
import matplotlib.pyplot as plt

def move_sympy_plot_to_axes(sympy_plot, plt_ax):
  backend = sympy_plot.backend(sympy_plot)
  backend.ax = plt_ax
  backend._process_series(backend.parent._series, plt_ax, backend.parent)
  backend.ax.spines['right'].set_color('none')
  backend.ax.spines['bottom'].set_position('zero')
  backend.ax.spines['top'].set_color('none')
  plt.close(backend.fig)

fig, ax = plt.subplots(figsize=(8,6))
p1 = plot((1 + 1/x)**x, (x,0,50), show = False,
          label =r'$\left(1+\frac{1}{x} \right)^x$')
p2 = plot(E, (x,0,50), show=False, label='Numero de Euler')
move_sympy_plot_to_axes(p1, ax)
move_sympy_plot_to_axes(p2, ax)
ax.get_lines()[1].set(color = 'red', linestyle='--')
ax.set_ylim(0,3)
ax.legend(loc= 'lower right')

plt.show()

f = 1/x

plot(f, (x, -10, 10), ylim=(-10,10))

limit(f, x, 0, dir='+')

limit(f, x, 0, dir='-')

limit(f, x, -oo), limit(f, x, oo)

limit(f, x, 0)

from sympy import sin, exp

limit((x**2 - 1)/(x - 1), x, 1) # (x**2 - 1)/(x - 1) com x tendendo a 1

#se 'f' for ua função polinomial ou racional e 'a' estiver no dominio de 'f', então
# lim f(x) = f(a)
#     x->a

b = (x**2 - 1)/(x - 1)
plot(b,(x, -10, 10))

b1 = x + 1
plot(b1, (x, -10, 10))

g = sin(x)/x
plot(g,(x, -30, 30))

u = sin(x)**2/x
plot(u,(x, -30, 30))

limit(g, x, 0)

limit(g, x, oo)

limit(u, x, 0)

limit(u, x, oo)

h = symbols('h')
limit(((3 + h)**2 - 9)/h, h, 0)

