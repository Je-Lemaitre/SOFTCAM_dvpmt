from PySide6.QtWidgets import QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QFont, QImage, QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SvgWidget(QWidget):
    def __init__(self, svg_path, parent=None):
        super().__init__(parent)
        self.renderer = QSvgRenderer(svg_path)
        self.setMinimumSize(200, 200)  # Set a minimum size for the widget

    def paintEvent(self, event):
        painter = QPainter(self)
        size = self.size()

        # Calculate the aspect ratio preserving size
        aspect_ratio = self.renderer.defaultSize().width() / self.renderer.defaultSize().height()
        if size.width() / size.height() > aspect_ratio:
            width = size.height() * aspect_ratio
            height = size.height()
        else:
            width = size.width()
            height = size.width() / aspect_ratio

        # Center the SVG within the widget
        x = (size.width() - width) / 2
        y = (size.height() - height) / 2

        # Draw the SVG
        self.renderer.render(painter, QRectF(x, y, width, height))


    
    # def resizeEvent(self, event):
    #     width, height = self.get_width_height()
    #     # Adjust fontsize based on the canvas size
    #     new_fontsize = min(width, height) // 15
    #     self.plot_expression(self.latex_expression, fontsize=new_fontsize)
    #     super().resizeEvent(event)

def create_image(img_path : str) :
    label = QLabel()
    label.setAlignment(Qt.AlignCenter)

    # Load the image
    image = QImage(img_path)

    # Convert QImage to QPixmap and set it to the label
    pixmap = QPixmap.fromImage(image)
    label.setPixmap(pixmap)

    # Enable scaling
    label.setScaledContents(True)

    return label

def create_latex(latex_expression : str, scale = 1):
    figure = Figure()
    canvas = FigureCanvas(figure)
    figure.clear()
    text = figure.suptitle(
        latex_expression,
        x=0.5,
        y=0.5,
        horizontalalignment='center',
        verticalalignment='center'
    )
    canvas.draw()

    (x0, y0), (x1, y1) = text.get_window_extent().get_points()
    w = x1 - x0
    h = y1 - y0

    figure.set_size_inches(w / 80, h / 80)

    canvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    return canvas