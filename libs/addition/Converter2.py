# import numpy as np
# from PIL import Image
# import cv2
# import os
# IMG_DIR = '../learningImage'
# for img in os.listdir(IMG_DIR):
#     img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)
#     img_pil = Image.fromarray(img_array)
#     img_7x5 = np.array(img_pil.resize((7, 5), Image.LANCZOS))
#     data = Image.fromarray(img_7x5)
#     data.save(img)
#     print(img_array)