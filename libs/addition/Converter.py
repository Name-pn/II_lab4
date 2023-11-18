# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QImage, QColorSpace, qGray, qRgb
#
#
# class Converter():
#     def __init__(self, n, m, *args, **argv):
#         super().__init__(*args, **argv)
#         self.n = n
#         self.m = m
#
#     def toGray(self, path):
#         image = QImage(path)
#         for x in range(image.height()):
#             for y in range(image.width()):
#                 pixel = image.pixel(x, y)
#                 gray = qGray(pixel)
#                 image.setPixel(x, y, qRgb(gray, gray, gray))
#         return image
#
#     def getImage(self, path):
#         image = self.toGray(path)
#         image = image.scaled(5, 7, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
#         return image
#     def getArray(self, path):
#         image = self.toGray(path)
#         image = image.scaled(5, 7, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
#
#         res = [[0 for i in range(self.m)] for j in range(self.n)]
#         for i in range(self.n):
#             for j in range(self.m):
#                 pixel = image.pixel(j, i)
#                 res[i][j] = qGray(pixel)
#         return res