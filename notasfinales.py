import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout)

class NotasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Nota Final")
        self.setGeometry(300, 200, 400, 350)

        # --- Widgets ---
        self.lbl_nombre = QLabel("Nombre del estudiante:")
        self.txt_nombre = QLineEdit()

        self.lbl_parcial1 = QLabel("Nota Parcial 1 (0-10):")
        self.txt_parcial1 = QLineEdit()

        self.lbl_parcial2 = QLabel("Nota Parcial 2 (0-10):")
        self.txt_parcial2 = QLineEdit()

        self.lbl_trabajo = QLabel("Nota Trabajo Final (0-10):")
        self.txt_trabajo = QLineEdit()

        self.btn_calcular = QPushButton("Calcular Nota Final")
        self.btn_limpiar = QPushButton("Limpiar")

        self.lbl_resultado = QLabel("Nota Final: -")
        self.lbl_estado = QLabel("Estado: -")

        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_nombre)
        layout.addWidget(self.txt_nombre)
        layout.addWidget(self.lbl_parcial1)
        layout.addWidget(self.txt_parcial1)
        layout.addWidget(self.lbl_parcial2)
        layout.addWidget(self.txt_parcial2)
        layout.addWidget(self.lbl_trabajo)
        layout.addWidget(self.txt_trabajo)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.btn_calcular)
        botones_layout.addWidget(self.btn_limpiar)
        layout.addLayout(botones_layout)

        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.lbl_estado)

        self.setLayout(layout)

        # --- Conexión de botones ---
        self.btn_calcular.clicked.connect(self.calcular_nota)
        self.btn_limpiar.clicked.connect(self.limpiar)

    def calcular_nota(self):
        """Calcula la nota final y estado del estudiante"""
        nombre = self.txt_nombre.text().strip()
        try:
            p1 = float(self.txt_parcial1.text())
            p2 = float(self.txt_parcial2.text())
            tf = float(self.txt_trabajo.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese valores numéricos válidos en las notas")
            return

        if not nombre or not (0 <= p1 <= 10) or not (0 <= p2 <= 10) or not (0 <= tf <= 10):
            QMessageBox.warning(self, "Error", "Complete todos los campos y verifique las notas (0-10)")
            return

        # Ponderaciones (ejemplo): Parcial1 30%, Parcial2 30%, Trabajo 40%
        nota_final = (p1 * 0.3) + (p2 * 0.3) + (tf * 0.4)
        estado = "Aprobado" if nota_final >= 6 else "Reprobado"

        self.lbl_resultado.setText(f"Nota Final: {nota_final:.2f}")
        self.lbl_estado.setText(f"Estado: {estado}")

        QMessageBox.information(self, "Resultado", f"Estudiante: {nombre}\nNota Final: {nota_final:.2f}\nEstado: {estado}")

    def limpiar(self):
        """Limpia campos y resultados"""
        self.txt_nombre.clear()
        self.txt_parcial1.clear()
        self.txt_parcial2.clear()
        self.txt_trabajo.clear()
        self.lbl_resultado.setText("Nota Final: -")
        self.lbl_estado.setText("Estado: -")
        QMessageBox.information(self, "Limpieza", "Campos limpiados")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = NotasApp()
    ventana.show()
    sys.exit(app.exec_())
