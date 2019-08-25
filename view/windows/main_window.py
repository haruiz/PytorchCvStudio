from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QWidget,QHBoxLayout,QGraphicsDropShadowEffect,QVBoxLayout,QStatusBar,QTabWidget, \
    QLabel
from util import GUIUtilities
from view.widgets import LateralMenu,LateralMenuItemLoc,TopBar,DatasetTabWidget
from .base_main_window import Ui_MainWindow


class MainWindowContainer(QWidget):
    def __init__(self, window: QMainWindow, parent=None):
        super(MainWindowContainer, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(1280,800)
        layout = QVBoxLayout(self)
        layout.addWidget(window)
        layout.setContentsMargins(0,0,6,6)
        self.shadow=QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setColor(QtGui.QColor(138,145,140))
        self.shadow.setOffset(8)
        window.setGraphicsEffect(self.shadow)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tab_widget_manager.tabCloseRequested.connect(lambda index: self.tab_widget_manager.removeTab(index))
        self.lateral_menu=LateralMenu()
        self.setWindowTitle("Pytorch Studio")
        self.resize(1440,900)
        self.lateral_menu.add_item(GUIUtilities.get_icon("data.png"),"Datasets", name="datasets")
        self.lateral_menu.add_item(GUIUtilities.get_icon("experiments.png"),"Experiments", name="experiments")
        self.lateral_menu.add_item(GUIUtilities.get_icon("models.png"),"Models", name="models")
        self.lateral_menu.add_item(GUIUtilities.get_icon("support.png"),"Support", name="support")
        self.lateral_menu.add_item(GUIUtilities.get_icon("config.png"),"Settings",loc=LateralMenuItemLoc.BOTTOM,name="settings")
        self.lateral_menu.add_item(GUIUtilities.get_icon("logout.png"),"Exit",loc=LateralMenuItemLoc.BOTTOM, name="exit")
        self.lateral_menu.item_click_signal.connect(self.item_click_signal_slot)
        self.tab_widget_manager.clear()
        self.frame_lateral_bar.setLayout(QVBoxLayout())
        self.frame_lateral_bar.layout().addWidget(self.lateral_menu)

    def set_current_tab(self, widget: QWidget, title: str):
        pass

    @QtCore.pyqtSlot(str)
    def item_click_signal_slot(self, object_name):
        try:
            self.tab_widget_manager.clear()
            if object_name == "datasets":
                tab_widget = DatasetTabWidget()
                self.tab_widget_manager.addTab(tab_widget, "Datasets")
            elif object_name == "experiments":
                raise NotImplementedError
            elif object_name == "models":
                raise NotImplementedError
            elif object_name == "support":
                raise NotImplementedError
            elif object_name == "exit":
                self.close()
        except Exception as ex:
            print(ex)


