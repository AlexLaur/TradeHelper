from PySide2 import QtCore, QtGui, QtWidgets


class StackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super(StackedWidget, self).__init__(parent=parent)

        self.m_direction = QtCore.Qt.Horizontal
        self.m_speed = 800
        self.m_animationtype = QtCore.QEasingCurve.InOutQuad
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = True
        self.m_pnow = QtCore.QPoint(0, 0)
        self.m_active = False

    def set_direction(self, direction):
        self.m_direction = direction

    def set_speed(self, speed):
        self.m_speed = speed

    def set_animation(self, animationtype):
        self.m_animationtype = animationtype

    def set_wrap(self, wrap):
        self.m_wrap = wrap

    def slide_in_prev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slide_in_idx(now - 1)

    def slide_in_next(self):
        now = self.currentIndex()
        if self.m_wrap or now < (self.count() - 1):
            self.slide_in_idx(now + 1)

    def slide_in_idx(self, idx):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            return
        self.slide_in_widget(self.widget(idx))

    def slide_in_widget(self, newwidget):
        if self.m_active:
            return

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(newwidget)

        if _now == _next:
            self.m_active = False
            return

        offsetx, offsety = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        if not self.m_direction == QtCore.Qt.Horizontal:
            if _now < _next:
                offsetx, offsety = 0, -offsety
            else:
                offsetx = 0
        else:
            if _now < _next:
                offsetx, offsety = -offsetx, 0
            else:
                offsety = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnow = pnow

        offset = QtCore.QPoint(offsetx, offsety)
        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        anim_group = QtCore.QParallelAnimationGroup(
            self, finished=self.animation_done_slot
        )

        for index, start, end in zip(
            (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QtCore.QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end,
            )
            anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True
        anim_group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    @QtCore.Slot()
    def animation_done_slot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False
