from utils.utils import *

input_train_data = {'IBSR_01': [r'C:\MISAPROJ\Training_Set\IBSR_01\IBSR_01_norm.nii.gz']}
input_train_labels = {'IBSR_01': [r'C:\MISAPROJ\Training_Set\IBSR_01\IBSR_01_seg.nii.gz']}
input_train_rois = {'IBSR_01': [r'C:\MISAPROJ\Training_Set\IBSR_01\IBSR_01_ROI.nii.gz']}
patch_size = (32, 32, 32)
sampling_step = (16, 16, 16)
normalize = True

training_dataset = MRI_DataPatchLoader(input_data=input_train_data,
                                       labels=input_train_labels,
                                       rois=input_train_rois,
                                       patch_size=patch_size,
                                       sampling_step=sampling_step,
                                       normalize=normalize,
                                       sampling_type='mask',
                                       resample_csf=1
                                       )
inf = training_dataset[400]
inf