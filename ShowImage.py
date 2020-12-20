#===============================================================================
# インポートモジュール
#===============================================================================
import cv2
import matplotlib.pyplot as plt

#===============================================================================
# 主処理
#===============================================================================

#neko.jpgを読み込んで、imgオブジェクトに入れる
img = cv2.imread("neko.jpg")

#imgオブジェクトをmatlotlibを用いて表示する
plt.imshow(img)
plt.show()
