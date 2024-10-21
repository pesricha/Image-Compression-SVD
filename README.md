# Image Compression Using SVD

For details, refer to [Image_Compression_Using_SVD.pdf](./Image_Compression_Using_SVD.pdf) which is in the repo root.

## Overview

This project compresses an image using Singular Value Decomposition (SVD) for each individual color channel (Red, Green, and Blue). We aim to retain 99% of the energy of the image by keeping only the most significant singular values. The energy is calculated using the following formula:

### Energy Calculation

The total energy $E$ is defined as:

$$
E = \sum_{i=1}^{n} (\sigma_i)^2
$$

For the first $k$ singular values:

$$
E_k = \sum_{i=1}^{k} (\sigma_i)^2
$$

We ensure that $E_k \geq 0.99E$ to retain 99% of the energy. The number of singular values required for each channel to capture 99% of the energy is as follows:

- Red channel ($k_R$): 276 singular values
- Green channel ($k_G$): 176 singular values
- Blue channel ($k_B$): 292 singular values

## SVD Decomposition

We perform SVD on each channel of the image, resulting in the following matrices for each channel:

- $U_{l \times l}$ where $l = 2000$
- $S_{w \times w}$ where $w = 1968$
- $V^T_{w \times w}$

## Dimensionality Reduction

To reduce the image size while preserving 99% of the energy, we truncate the matrices as follows:

- $U_{l \times k}$
- $S_{k \times k}$
- $V^T_{k \times w}$

Where $k$ is the number of singular values retained for each channel ($k_R$, $k_G$, and $k_B$).

## Image Reconstruction

After truncating the matrices, we reconstruct the compressed image by multiplying the matrices for each channel:

$$
\text{Reconstructed Channel} = U_{l \times k} \cdot S_{k \times k} \cdot V^T_{k \times w}
$$

This process is repeated for the Red, Green, and Blue channels to obtain the final compressed image.

## How to Run

1. Ensure you have the necessary dependencies installed.
2. Run the main script to perform the SVD, compress the image, and reconstruct it.
3. The output will be saved as a compressed image file in the output folder.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- PIL (Python Imaging Library)
