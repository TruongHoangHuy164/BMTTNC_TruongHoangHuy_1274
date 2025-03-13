import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),
            "key": self.ui.plainTextEdit_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_2.setPlainText(data["encrypted_message"])  # Fixed to setPlainText
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # Corrected the message box icon
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)  # Printing the exception object directly
            
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_2.toPlainText(),
            "key": self.ui.plainTextEdit_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])  # Fixed to setPlainText
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # Corrected the message box icon
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)  # Printing the exception object directly


if __name__ == "__main__":  # This block should be outside the class definition
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
