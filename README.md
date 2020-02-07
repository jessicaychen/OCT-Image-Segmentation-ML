# OCT-Image-Segmentation-ML
Optical coherence tomography (OCT) image segmentation with a Convolutional Neural Network. Long work in progress...

## Goal:

(a) Input image | (b) Ground truth  | (c) Segmentation prediction - tbd
--------------- | ----------------- | ---------------------------------
![Input image](images/cSLO52-input.jpg) | ![Ground truth](images/cSLO52-groundtruth.jpg)


## Process: 

1. Manual segmentation (Adobe Photoshop)
2. Masking and converting masks to grayscale (Python)
3. Pre-processing input and ground truth sets (Python)
4. CNN - building, testing, training, validation
5. Run on different subgroup images
6. Skeletonize binary images (ImageJ)
7. Extract data - # of junctions, lengths, area (ImageJ)
8. Statistical analysis with SPSS
