import math
import matplotlib.pyplot as plt
import numpy as np


def rot(point, angle):     #angulo en radianes
    m = np.matrix([[math.cos(angle), -math.sin(angle)],
                   [math.sin(angle), math.cos(angle)]])

    return (m*(point.transpose())).transpose()


def circle(center, radius):
    return plt.Circle(center, radius)


class Pendulo:

    def __init__(self, largo, r_rueda, ang_pendulo, masa):
        # variables
        self.L = largo
        self.R = r_rueda
        self.ang_pend = ang_pendulo # angulo respecto a la vertical
        self.mass = masa

        # wheel plot
        self.wheel = plt.Circle((0,0),  radius=self.R, edgecolor='k', facecolor='w')
        self.wheel_dir = np.matrix([self.R, 0])
        self.wheel_dir_plot = plt.Line2D([0, self.wheel_dir.item(0)], [0, self.wheel_dir.item(1)], linewidth=2,
                                         color='r')
        # floor plot
        self.floor = plt.Line2D([-2*self.L, 2*self.L], [-self.R, -self.R], linewidth=2, color='b')
        # figure
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def config_draw(self):
        self.ax.add_patch(self.wheel)
        self.ax.add_line(self.wheel_dir_plot)
        self.ax.add_line(self.floor)
        self.ax.axis([-self.L-2, self.L+2, -self.L-2, self.L+2])
        self.ax.set_aspect(1)
        plt.show(block=False)
        plt.ion()

    def draw(self):
        self.ax.clear()
        self.ax.add_patch(self.wheel)
        self.ax.add_line(self.wheel_dir_plot)
        self.ax.add_line(self.floor)
        self.ax.axis([-self.L - 2, self.L + 2, -self.L - 2, self.L + 2])
        self.ax.set_aspect(1)
        plt.show(block=False)
        plt.pause(0.001);


    def set_wheel_dir(self, ang):
        self.wheel_dir = rot(self.wheel_dir, ang)
        self.wheel_dir_plot = plt.Line2D([0, self.wheel_dir.item(0)], [0, self.wheel_dir.item(1)], linewidth=2,
                                         color='r')

    def rot(self, point, angle):  # ángulo en radianes
        m = np.matrix([[math.cos(angle), -math.sin(angle)],
                       [math.sin(angle), math.cos(angle)]])

        return (m * (point.transpose())).transpose()


Pend = Pendulo(10, 2, 0, 2)
Pend.config_draw()

for angulo in np.arange(100):
    Pend.set_wheel_dir(2*math.pi/100)
    Pend.draw()

plt.show()

'''
a = np.matrix([1, 0])

b = rot(a, math.pi)

print(a)
print(b)

fig = plt.figure(1)
ax = fig.add_subplot(111)

x = 0
y = 0

wheel = circle((x, y), 1)

lx = a.item(0)
ly = a.item(1)

line = plt.Line2D([x, lx],[y, ly], linewidth=2, color='r')

lx2 = b.item(0)
ly2 = b.item(1)

line2 = plt.Line2D([x, lx2],[y, ly2], linewidth=2, color='g')

ax.add_patch(wheel)
ax.add_line(line)
ax.add_line(line2)

ax.axis([-2, 2, -2, 2])
ax.set_aspect(1)


plt.show()
'''

''' test'''
'''
x = np.linspace(0, 10 * np.pi, 100)
y = np.sin(x)


fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
line1, = ax2.plot(x, y, 'b-')

for phase in np.linspace(0, 10 * np.pi, 100):
    line1.set_ydata(np.sin(np.sin(x) * x + phase))
    fig2.canvas.draw()

plt.ioff()
'''