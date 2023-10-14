import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.title = "TESTING"
        self.setWindowTitle(self.title)

        # Create a button
        button = QPushButton('Click me!')

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add the button to the layout
        layout.addWidget(button)

        # Set the layout for the window
        self.setLayout(layout)
        #add label
        label = QLabel("Hello World")
        layout.addWidget(label)
        

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = MyWindow()

    # Show the window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())
