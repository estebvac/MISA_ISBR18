import ants
import os
import random


def mask_image(im):
    return (im > 0).astype('float32')


def create_ROIs(path: str, extension: str = '.nii.gz'):
    """
    This ROI generator follows the structure FILE/FILE+extension
    and generates a ROI file with the name   FILE/FILE+_ROI+extension
    Parameters
    ----------
    path        Images Path

    Returns     Generated ROI images
    -------

    """

    for scan_id in os.listdir(path):
        print('Creating ROI for: ', scan_id)
        scan = ants.image_read(os.path.join(path, scan_id, scan_id + extension))
        brainmask = ants.image_clone(scan).apply(mask_image)
        brainmask.to_filename(os.path.join(path, scan_id, scan_id + '_ROI' + extension))

    return


def create_training_validation_sets(options: dict):
    """
    Generate the input dictionaries for training and validation
    Parameters
    ----------
    options : Define the paths for the training and validation sets to be used
    must contain the following:
                options['training_path']
                options['test_path']
                options['val_split']
                options['test_path']

    Returns
    -------
    input_dictionary : Contains all the paths of files to feed the network.
                input_dictionary['input_train_data']
                input_dictionary['input_train_labels']....

    """
    #validation_scans = os.listdir(options['test_path'])
    #random.shuffle(validation_scans)

    # load training / validation data
    #t_d = int(len(validation_scans) * (1 - options['val_split']))
    #validation_data = validation_scans[:t_d]
    #test_data = validation_scans[t_d:]
    train_scans = os.listdir(options['training_path'])
    validation_data = os.listdir(options['val_path'])
    test_data = os.listdir(options['test_path'])

    input_dictionary = {}


    input_dictionary['input_train_data'] = {scan: [os.path.join(options['training_path'], scan,
                                                                scan + '_norm.nii.gz')] for scan in train_scans}

    input_dictionary['input_train_labels'] = {scan: [os.path.join(options['training_path'], scan,
                                                                  scan + '_seg.nii.gz')] for scan in train_scans}

    input_dictionary['input_train_rois'] = {scan: [os.path.join(options['training_path'], scan,
                                                                scan + '_ROI.nii.gz')] for scan in train_scans}

    input_dictionary['input_val_data'] = {scan: [os.path.join(options['val_path'], scan,
                                                              scan + '_norm.nii.gz')] for scan in validation_data}

    input_dictionary['input_val_labels'] = {scan: [os.path.join(options['val_path'], scan,
                                                                scan + '_seg.nii.gz')] for scan in validation_data}

    input_dictionary['input_val_rois'] = {scan: [os.path.join(options['val_path'], scan,
                                                              scan + '_ROI.nii.gz')] for scan in validation_data}

    input_dictionary['input_test_data'] = {scan: [os.path.join(options['test_path'], scan,
                                                               scan + '_norm.nii.gz')] for scan in test_data}

    input_dictionary['input_test_labels'] = {scan: [os.path.join(options['test_path'], scan,
                                                                 scan + '_seg.nii.gz')] for scan in test_data}

    input_dictionary['input_test_rois'] = {scan: [os.path.join(options['test_path'], scan,
                                                               scan + '_ROI.nii.gz')] for scan in test_data}

    return input_dictionary
