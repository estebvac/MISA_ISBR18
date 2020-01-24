# Patch-Based Segmentation of Brain MRI Images Using Deep Learning #

This repository contains the source code corresponding to the patch-based segmentation of MRI images using convolutional neural networks (CNN). A pipeline is proposed for the segmentation of Cerebro Spinal Fluid (CSF), Gray Matter (GM) and White Matter (WM). Results are measured by means of the Dice coefficient (DSC), Average Volumetric Difference and Hausdorff distance. Best average DSCs were $0.920 \pm 0.015$, $0.943 \pm 0.008$ and $0.937 \pm 0.015$ for CSF, GM and GM, respectively. 

### Requirements ###
* ANTSPy
* SimpleITK
* Pytorch
* Numpy 
* Matplotlib

### Colab Excecution ###
The present source runs embeeded in Colab using the online GPU Architecture. It is possible to run the project usng the jupyter notebook or running it directly from [Colab Link](https://colab.research.google.com/drive/1WFb6zV8AtY7p2Hh_l89n2j_vFi_7gwTl).



### Results ###

| CASE    | CSF      | GM       | WM       |
|---------|----------|----------|----------|
| IBSR_11 | 0.912701 | 0.926566 | 0.925557 |
| IBSR_13 | 0.902323 | 0.926438 | 0.899622 |
| IBSR_17 | 0.939298 | 0.927427 | 0.902453 |
| IBSR_14 | 0.920844 | 0.941384 | 0.926799 |
| IBSR_12 | 0.875420 | 0.920959 | 0.922149 |


