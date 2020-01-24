import ants
from models.models import Unet

options = {}

# training data path
options['training_path'] = '/content/data/dataset/Training_Set'
# Test data path
options['test_path'] = '/content/data/dataset/Validation_Set'
# Validation split
options['val_split']  = 0.5


# Define the Unet model
# 2 input channels (FLAIR and T1)
# 2 output classes (healthy and wmh) (we ignore other pathologies)
model = Unet(input_size=1, output_size=4)

options = {}
# some training options
options['gpu_use'] = True
options['num_epochs'] = 10
options['model_name'] = 'unet_tissue_segmentation'
options['save_path'] = '/content/models'




