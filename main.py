# import numpy as np
import cv2

height_constant = 4320
width_interver = [5760, 7680, 5760, 5760, 5760]
start_x = 0
start_y = 0
file_name = 0
# print(sum(width_interver))

original_img = cv2.imread("gdo.png")
resized_img = cv2.resize(original_img, (30720, 4320))
print(resized_img.shape)

for i in width_interver:
  crop_img = resized_img[start_y:start_y + height_constant, start_x:start_x + i]
  cv2.imwrite('resutls/screen' + str(file_name) + '.png', crop_img)
  file_name = file_name + 1
  start_x = start_x + i