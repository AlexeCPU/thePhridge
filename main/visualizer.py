from PySide2 import QtCore, QtWidgets, QtOpenGL
import sys

try:
    from OpenGL.GL import *
except ImportError:
    app = QtWidgets.QApplication(sys.argv)
    messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "OpenGL sample",
                                       "PyOpenGL must be installed to run this example.",
                                       QtWidgets.QMessageBox.Close)
    messageBox.setDetailedText("Run:\npip install PyOpenGL PyOpenGL_accelerate")
    messageBox.exec_()
    sys.exit(1)


class GLWidget(QtOpenGL.QGLWidget):
    x_rotation_changed = QtCore.Signal(int)
    y_rotation_changed = QtCore.Signal(int)
    z_rotation_changed = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.shape1 = None
        self.x_rot_speed = 0
        self.x_shape_rot = 0
        self.y_rot_speed = 0
        self.y_shape_rot = 0
        self.z_rot_speed = 0
        self.z_shape_rot = 0

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.advance)
        timer.start(20)

    def initializeGL(self):
        """Set up the rendering context, define display lists etc."""
        glEnable(GL_DEPTH_TEST)
        self.shape1 = self.make_shape()
        glEnable(GL_NORMALIZE)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        """draw the scene:"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        self.draw_shape(self.shape1, -1.0, -1.0, 0.0,
            (self.x_shape_rot, self.y_shape_rot, self.z_shape_rot))
        glPopMatrix()

    def resizeGL(self, width, height):
        """setup viewport, projection etc."""
        side = min(width, height)
        if side < 0:
            return

        glViewport(int((width - side) / 2), int((height - side) / 2), side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.2, +1.2, -1.2, 1.2, 6.0, 70.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -20.0)

    def free_resources(self):
        """Helper to clean up resources."""
        self.makeCurrent()
        glDeleteLists(self.shape1, 1)

    # slots
    def set_x_rot_speed(self, speed):
        self.x_rot_speed = speed
        self.updateGL()

    def set_y_rot_speed(self, speed):
        self.y_rot_speed = speed
        self.updateGL()

    def set_z_rot_speed(self, speed):
        self.z_rot_speed = speed
        self.updateGL()

    def advance(self):
        """Used in timer to actually rotate the shape."""
        self.x_shape_rot += self.x_rot_speed
        self.x_shape_rot %= 360
        self.y_shape_rot += self.y_rot_speed
        self.y_shape_rot %= 360
        self.z_shape_rot += self.z_rot_speed
        self.z_shape_rot %= 360
        self.updateGL()

    def make_shape(self):
        """Helper to create the shape and return list of resources."""
        list = glGenLists(1)
        glNewList(list, GL_COMPILE)

        glNormal3d(0.0, 0.0, 0.0)

        # Vertices
        a = ( 1, -1, -1),
        b = ( 1,  1, -1),
        c = (-1,  1, -1),
        d = (-1, -1, -1),
        e = ( 1, -1,  1),
        f = ( 1,  1,  1),
        g = (-1, -1,  1),
        h = (-1,  1,  1)

        edges = [
            (a, b), (a, d), (a, e),
            (c, b), (c, d), (c, h),
            (g, d), (g, e), (g, h),
            (f, b), (f, e), (f, h)
        ]

        glBegin(GL_LINES)
        for edge in edges:
            glVertex3fv(edge[0])
            glVertex3fv(edge[1])
        glEnd()

        glEndList()

        return list

    def draw_shape(self, shape, dx, dy, dz, rotation):
        """Helper to translate, rotate and draw the shape."""
        glPushMatrix()
        glTranslated(dx, dy, dz)
        glRotated(rotation[0], 1.0, 0.0, 0.0)
        glRotated(rotation[1], 0.0, 1.0, 0.0)
        glRotated(rotation[2], 0.0, 0.0, 1.0)
        glCallList(shape)
        glPopMatrix()