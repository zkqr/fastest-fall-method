from classes import *

x1, x2 = symbols('x1, x2')
l = Symbol('l')

a, b, c, d, e = 1, 2, -2, 8, -18

x0 = Point(1, 1)

func = a * x1 ** 2 + b * x2 ** 2 + c * x1 * x2 + d * x1 + e * x2

diff_func = Point(2 * a * x1 + c * x2 + d, 2 * b * x2 + c * x1 + e)


def function(x1, x2):
    return a * x1 ** 2 + b * x2 ** 2 + c * x1 * x2 + d * x1 + e * x2


count = 0
e = 10 ** -5
epsilon_point = Point(e, e)

while True:
    count += 1

    diff_func_x0 = Point(diff_func.x.subs({x1: x0.x, x2: x0.y}), diff_func.y.subs({x1: x0.x, x2: x0.y}))

    if diff_func_x0.absolute() < epsilon_point:
        print("Количество итераций:", count)
        print("(x1, x2) =", x0.round_point())
        print("F(x1, x2) =", float(func.subs({x1: x0.round_point().x, x2: x0.round_point().y})))

        x = np.linspace(-20, 200, 40)
        y = np.linspace(-20, 200, 40)

        X, Y = np.meshgrid(x, y)
        Z = function(X, Y)

        fig = plt.figure(figsize=(10, 8))
        ax = plt.axes(projection='3d')

        xmin = x0.round_point().x
        ymin = x0.round_point().y
        point_z = function(xmin, ymin)

        ax.scatter(xmin, ymin, point_z, color='red', s=100)

        surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)

        ax.set_title('F(x1, x2)', fontsize=30)
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_zlabel('z', fontsize=12)

        ax.view_init(elev=15, azim=170)

        plt.show()

        sys.exit()

    expected_next_point = Point(x0.x - diff_func_x0.x * l, x0.y - diff_func_x0.y * l)


    def differ(expr):
        expr = expand(expr)
        return float(-expr.coeff(l)) / float(2 * expr.coeff(l ** 2))


    labda_exp = func.subs({x1: expected_next_point.x, x2: expected_next_point.y})
    lamda = differ(labda_exp)
    next_iteration_point = Point((x0.x + lamda * (-diff_func_x0.x.evalf())).evalf(),
                                 (x0.y + lamda * (-diff_func_x0.y.evalf())).evalf())

    x0 = next_iteration_point
