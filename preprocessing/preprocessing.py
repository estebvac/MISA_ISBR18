import SimpleITK as sitk
import os
import ants

def histogram_matching(fixed, moving):
    """

    Parameters
    ----------
    fixed:      Base image to match all the MRI volumes
    moving      Image to mach

    Returns
    -------
    The histogram matched image result.
    """
    matcher = sitk.HistogramMatchingImageFilter()
    if (fixed.GetPixelID() in (sitk.sitkUInt8, sitk.sitkInt8)):
        matcher.SetNumberOfHistogramLevels(128)
    else:
        matcher.SetNumberOfHistogramLevels(1024)
    matcher.SetNumberOfMatchPoints(7)
    #matcher.ThresholdAtMeanIntensityOn()
    moving = matcher.Execute(moving, fixed)
    return moving


def normalize_images(path: str, base_path: str,extension: str = '.nii.gz'):
    """
    This ROI generator follows the structure FILE/FILE+extension
    and generates a ROI file with the name   FILE/FILE+_norm+extension
    Parameters
    ----------
    path        Images Path

    Returns     Generated ROI images
    -------

    """
    fixed_itk = sitk.ReadImage(base_path)

    for scan_id in os.listdir(path):
        print('Normalizing image : ', scan_id)
        moving_itk = sitk.ReadImage(os.path.join(path, scan_id, scan_id + extension))
        moving_matched_itk = histogram_matching(fixed_itk, moving_itk)
        sitk.WriteImage(moving_matched_itk,os.path.join(path, scan_id, scan_id + '_norm' + extension))
    return


def bias_field_correction(path: str,extension: str = '.nii.gz'):
    """
    This ROI generator follows the structure FILE/FILE+extension
    and generates a ROI file with the name   FILE/FILE+_norm+extension
    Parameters
    ----------
    path        Images Path

    Returns     Generated ROI images
    -------

    """
    for scan_id in os.listdir(path):
        print('Bias Field correction : ', scan_id)
        image = ants.image_read(os.path.join(path, scan_id, scan_id + extension))
        image_n4 = ants.n4_bias_field_correction(image)
        ants.image_write(image_n4,os.path.join(path, scan_id, scan_id + extension))
    return