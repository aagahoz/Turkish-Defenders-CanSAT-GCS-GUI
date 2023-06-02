import sys
import vtk
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class VTKWidget(QVTKRenderWindowInteractor):
    def __init__(self, parent=None):
        super().__init__(parent)
        renderer = vtk.vtkRenderer()
        self.GetRenderWindow().AddRenderer(renderer)

        reader = vtk.vtkOBJReader()
        reader.SetFileName("DigerDosyalar/model1.obj")
        reader.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(reader.GetOutput())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        renderer.AddActor(actor)

        renderer.SetBackground(0.2, 0.3, 0.4)
        

        self.Initialize()
        self.Start()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_B:
            self.GetRenderWindow().GetRenderers().GetFirstRenderer().GetActiveCamera().Azimuth(10)
        elif key == Qt.Key_N:
            self.GetRenderWindow().GetRenderers().GetFirstRenderer().GetActiveCamera().Azimuth(-10)
        elif key == Qt.Key_A:
            self.GetRenderWindow().GetRenderers().GetFirstRenderer().GetActiveCamera().Roll(-10)
        elif key == Qt.Key_D:
            self.GetRenderWindow().GetRenderers().GetFirstRenderer().GetActiveCamera().Roll(10)
        elif key == Qt.Key_W:
            self.GetRenderWindow().GetRenderers().GetFirstRenderer().GetActiveCamera().Elevation(-10)
        elif key == Qt.Key_S:
            self.GetRenderWindow().GetRenderers().GetFirstRenderer().GetActiveCamera().Elevation(10)

        self.GetRenderWindow().Render()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        vtk_widget = VTKWidget()
        layout.addWidget(vtk_widget)
        self.setCentralWidget(central_widget)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
