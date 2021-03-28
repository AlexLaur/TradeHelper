import pyqtgraph as pg
from PySide2 import QtCore, QtWidgets


class ROIManager(QtCore.QObject):
    def __init__(self, parent=None):
        super(ROIManager, self).__init__(parent)

        # Constants
        self.current_tool = None
        self._graph = self.parent().wgt_graph.graph

        # Signals
        self.parent().wgt_graph.signals.sig_graph_clicked.connect(
            self._on_roi_add_requested
        )

    def drawer(self, graph, event):
        """Drawer over the graph"""
        # Test
        vb = graph.vb
        mousePoint = vb.mapSceneToView(event.pos())
        print(mousePoint)
        # End test

        if self.current_tool:
            self.current_tool(graph=graph)  # Exec the current tool
        self.unset_tool()

    def bounded_line_drawer(self, graph, **kwargs):
        """Draw a bounded line

        :param graph: The graph on whch to draw
        :type graph: pg.PlotItem
        """
        roi = pg.LineSegmentROI(([50, 50], [150, 50]), removable=True)
        graph.addItem(roi)
        roi.sigRemoveRequested.connect(self._on_roi_remove_requested)

    def set_tool(self, **kwargs):
        """Set the current tool. kwargs may have a tool which corresponds to
        the method to call inside this module.

        :return: The current tool
        :rtype: method if found, None instead
        """
        self.current_tool = getattr(self, kwargs.get("tool", None), None)
        return self.current_tool

    def unset_tool(self):
        """Unset the current tool"""
        self.current_tool = None

    def remove_roi(self, roi):
        """Remove the given roi

        :param roi: The roi to remove
        :type roi: pg.ROI
        """
        print(roi.parent())

    @QtCore.Slot(list, object)
    def _on_roi_add_requested(self, objects, event):
        """Called on a draw requested"""
        if objects:
            self.drawer(graph=objects[0], event=event)

    @QtCore.Slot(object)
    def _on_roi_remove_requested(self, roi):
        """Called on a request for ROI deletion

        :param roi: The roi to remove
        :type roi: pg.ROI
        """
        self.remove_roi(roi=roi)
