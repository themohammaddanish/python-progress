import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import argparse

def plot_equation(equation, x_range):
  x_sym = sp.symbols('x')
  y_sym = sp.sympify(equation)
  x = np.linspace(x_range[0], x_range[1], 400)
  y = [float(y_sym.subs(x_sym, val).evalf()) for val in x]
  
  plt.plot(x, y, label=equation)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Graph of the equation')
  plt.legend()
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Plot an equation over a specified range.")
  parser.add_argument('equation', type=str, help="The equation to plot, e.g., 'x**2 + 2*x + 1'")
  parser.add_argument('x_min', type=float, help="The minimum value of x")
  parser.add_argument('x_max', type=float, help="The maximum value of x")
  
  args = parser.parse_args(args=['x**4 ', '-10', '10'])
  
  equation = args.equation
  x_min = args.x_min
  x_max = args.x_max
  
  x_range = (x_min, x_max)
  plot_equation(equation, x_range)
