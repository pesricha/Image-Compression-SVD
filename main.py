# Load image.png as an array

import numpy as np
import matplotlib.pyplot as plt
import cv2

# open image
img = cv2.imread('image.png')
print(np.shape(img))

# get svd of image
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]

Ur, Sr, Vr = np.linalg.svd(red_channel, full_matrices=False)
Ug, Sg, Vg = np.linalg.svd(green_channel, full_matrices=False)
Ub, Sb, Vb = np.linalg.svd(blue_channel, full_matrices=False)

# Function to reconstruct image with k singular values
def reconstruct_image(k):
    R = np.dot(Ur[:, :k], np.dot(np.diag(Sr[:k]), Vr[:k, :]))
    G = np.dot(Ug[:, :k], np.dot(np.diag(Sg[:k]), Vg[:k, :]))
    B = np.dot(Ub[:, :k], np.dot(np.diag(Sb[:k]), Vb[:k, :]))
    return np.stack([R, G, B], axis=2).astype('uint8')

# Reconstruct and plot images with different values of k
k_values = [10, 50, 100, 200]
fig, axes = plt.subplots(1, len(k_values), figsize=(15, 5))

for i, k in enumerate(k_values):
    compressed_image = reconstruct_image(k)
    axes[i].imshow(compressed_image)
    axes[i].set_title(f'k = {k}')
    axes[i].axis('off')

plt.show()