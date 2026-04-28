import json

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QPlainTextEdit, QTabWidget, QVBoxLayout, QWidget

from pyfsse.types import JsonData


class TabContainer(QTabWidget):
    def __init__(self) -> None:
        super().__init__()
        self.dwellers_tab = DwellersTab()
        self.inventory_tab = InventoryTab()
        self.vault_tab = VaultTab()
        self.raw_save_data_tab = RawSaveDataTab()

        self.addTab(self.dwellers_tab, "Dwellers")
        self.addTab(self.inventory_tab, "Inventory")
        self.addTab(self.vault_tab, "Vault")
        self.addTab(self.raw_save_data_tab, "Raw Save Data")


class DwellersTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout(self)

        content = QLabel("Placeholder for Tab 1: Dwellers")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(content)


class InventoryTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout(self)

        content = QLabel("Placeholder for Tab 2: Inventory")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(content)


class VaultTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout(self)

        content = QLabel("Placeholder for Tab 3: Vault")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(content)


class RawSaveDataTab(QPlainTextEdit):
    def __init__(self) -> None:
        super().__init__()

        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        font = QFont("Courier New")
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.setFont(font)

    def display_data(self, data: JsonData) -> None:
        try:
            formatted_json = json.dumps(data, indent=4, sort_keys=False, default=str)
            self.setPlainText(formatted_json)
        except (TypeError, ValueError) as e:
            self.setPlainText(f"Error formatting JSON: {e}")
