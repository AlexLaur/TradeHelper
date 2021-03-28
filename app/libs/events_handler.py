from PySide2 import QtCore


class EventHandler(QtCore.QObject):
    sig_ticker_choosen = QtCore.Signal(str)
    sig_ticker_added_favorite = QtCore.Signal(dict)
    sig_ticker_removed_favorite = QtCore.Signal(dict)
    sig_ticker_data_fetched = QtCore.Signal(object)
    sig_ticker_infos_fetched = QtCore.Signal(dict)
    sig_ticker_articles_fetched = QtCore.Signal(dict)

    sig_thread_pre = QtCore.Signal()
    sig_thread_post = QtCore.Signal()
    sig_thread_failed = QtCore.Signal()
    sig_thread_result = QtCore.Signal(object)

    sig_indicator_switched = QtCore.Signal(object, bool)
    sig_indicator_enabled = QtCore.Signal(object, bool)
    sig_indicator_disabled = QtCore.Signal(object, bool)
    sig_indicator_settings_clicked = QtCore.Signal(object)
    sig_indicator_settings_validated = QtCore.Signal(object)
    sig_indicator_settings_canceled = QtCore.Signal(object)
    sig_indicator_settings_reseted = QtCore.Signal(object)

    sig_action_triggered = QtCore.Signal(str, dict)

    sig_favorite_created = QtCore.Signal(str)
    sig_favorite_loaded = QtCore.Signal(list)
    sig_favorite_saved = QtCore.Signal(list)
    sig_favorite_added = QtCore.Signal(dict)
    sig_favorite_removed = QtCore.Signal(dict)
    sig_favorite_clicked = QtCore.Signal(str)

    sig_graph_clicked = QtCore.Signal(list, object)

    sig_articles = QtCore.Signal(dict)
