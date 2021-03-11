from PySide2 import QtCore


class EventHandler(QtCore.QObject):
    sig_ticker_choosen = QtCore.Signal(str)
    sig_ticker_infos_fetched = QtCore.Signal(object)

    sig_thread_pre = QtCore.Signal()
    sig_thread_post = QtCore.Signal()
    sig_thread_failed = QtCore.Signal()

    sig_indicator_switched = QtCore.Signal(object, bool)

    sig_indicator_enable = QtCore.Signal(object, bool)
    sig_indicator_disable = QtCore.Signal(object, bool)

    sig_action_triggered = QtCore.Signal(str)
