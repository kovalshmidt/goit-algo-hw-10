import random
import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2


a = 0
b = 2


def monte_carlo_integration(f, a, b, num_points):
    y_max = max(f(np.linspace(a, b, 1000)))

    x_random = [random.uniform(a, b) for _ in range(num_points)]
    y_random = [random.uniform(0, y_max) for _ in range(num_points)]

    points_under_curve = 0
    for x, y in zip(x_random, y_random):
        if y <= f(x):
            points_under_curve += 1

    area_rectangle = (b - a) * y_max

    integral_estimate = (points_under_curve / num_points) * area_rectangle
    return integral_estimate


num_points = 10_000_000

# Monte-Carlo approach
monte_carlo_result = monte_carlo_integration(f, a, b, num_points)
print(f"Solution with Monte-Carlo approach: {monte_carlo_result}")

# Quad approach
quad_result, error = spi.quad(f, a, b)
print(f"Solution with quad approach: {quad_result} ± {error}")
