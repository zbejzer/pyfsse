import pathlib

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QMainWindow, QStackedWidget, QTabWidget

from pyfsse import file_handler
from pyfsse.ui.widgets.tabs import TabContainer
from pyfsse.ui.widgets.welcome import WelcomeView


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Fallout Shelter Save Editor")
        self.resize(1280, 720)

        self.central_stack = QStackedWidget()
        self.setCentralWidget(self.central_stack)

        self.welcome_screen = WelcomeView()
        self.tabs_screen = TabContainer()

        self.central_stack.addWidget(self.welcome_screen)
        self.central_stack.addWidget(self.tabs_screen)

        self._create_menu()

    def _create_menu(self) -> None:
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        open_action = QAction("&Open...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.on_file_open)

        save_action = QAction("&Save...", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.on_file_save)

        save_as_action = QAction("&Save As...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.on_file_save_as)

        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

    def on_file_open(self) -> None:
        file_path_str, _ = QFileDialog.getOpenFileName(
            self, "Open Vault File", "", "Vault Files (*.sav);;All Files (*)"
        )

        if file_path_str:
            path = pathlib.Path(file_path_str)
            data = file_handler.load_vault(path)

            self.tabs_screen.raw_save_data_tab.display_data(data)

            self.central_stack.setCurrentWidget(self.tabs_screen)

    def on_file_save(self) -> None:
        self.central_stack.setCurrentWidget(self.welcome_screen)

    def on_file_save_as(self) -> None:
        self.central_stack.setCurrentWidget(self.welcome_screen)
