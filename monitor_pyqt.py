import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ChatBot')
        self.setGeometry(100, 100, 400, 400)

        # Layout
        layout = QVBoxLayout()

        # Text display
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        # Input field
        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        # Send button
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        # Widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def send_message(self):
        message = self.input_field.text()
        self.text_display.append(f"User: {message}")

        # Here you'd usually call your chatbot logic or API to get the response.
        # For demonstration, a simple echo bot is used.
        response = self.get_bot_response(message)
        self.text_display.append(f"Bot: {response}")

        self.input_field.clear()

    def get_bot_response(self, message):
        # Replace this function with your actual chatbot logic or API call
        return f"Echo: {message}"


def run_app():
    app = QApplication(sys.argv)
    window = ChatBotWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
