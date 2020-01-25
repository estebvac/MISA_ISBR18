# Patch-Based Segmentation of Brain MRI Images Using Deep Learning #

This repository contains the source code corresponding to the patch-based segmentation of MRI images using convolutional neural networks (CNN). A pipeline is proposed for the segmentation of Cerebro Spinal Fluid (CSF), Gray Matter (GM) and White Matter (WM). Results are measured by means of the Dice coefficient (DSC), Average Volumetric Difference and Hausdorff distance. Best average DSCs were $0.920 \pm 0.015$, $0.943 \pm 0.008$ and $0.937 \pm 0.015$ for CSF, GM and GM, respectively. 

### Requirements ###
* ANTSPy == 0.1.7
* SimpleITK == 1.2.4
* Pytorch == 1.4
* patsy>=0.4.0
* patsy>=0.4.0
* pandas>=0.19  
* scipy>=0.18
* statsmodels 
* six 
* python-dateutil>=2.6.1
* pytz>=2017.2
* Matplotlib

### Colab Excecution ###
The present source runs embeeded in Colab using the online GPU Architecture. It is possible to run the project usng the jupyter notebook or running it directly from [Colab Link](https://colab.research.google.com/drive/1WFb6zV8AtY7p2Hh_l89n2j_vFi_7gwTl).

## Dataset ##
A copy of the Dataset with the organization used for this project can be found in the [Google Drive Link](https://drive.google.com/open?id=17oE6nDh-AtxfjGwZ9xYvOB7Tx_fv0Gi_).

### Results ###

| CASE    | CSF      | GM       | WM       |
|---------|----------|----------|----------|
| IBSR_11 | 0.912701 | 0.926566 | 0.925557 |
| IBSR_13 | 0.902323 | 0.926438 | 0.899622 |
| IBSR_17 | 0.939298 | 0.927427 | 0.902453 |
| IBSR_14 | 0.920844 | 0.941384 | 0.926799 |
| IBSR_12 | 0.875420 | 0.920959 | 0.922149 |


