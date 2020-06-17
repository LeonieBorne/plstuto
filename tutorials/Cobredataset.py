# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:38:39 2020

@author: Sara
"""
import nilearn as nilearn
from nilearn import datasets
dataset = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
atlas_filename = dataset.maps
labels = dataset.labels
cobre=nilearn.datasets.fetch_cobre(n_subjects=10, data_dir=None, url=None, verbose=1)
print(sorted(list(cobre.keys()))) 
print(cobre.desc_phenotypic)
import pandas as pd  
labels = pd.DataFrame(cobre.phenotypic)

from nilearn.input_data import NiftiLabelsMasker
masker = NiftiLabelsMasker(labels_img=atlas_filename, standardize=True,memory='nilearn_cache', verbose=5)
time_series = masker.fit_transform(fmri_filenames, confounds=cobre.confounds)
from nilearn.connectome import ConnectivityMeasure
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]

# Plot the correlation matrix
import numpy as np
from nilearn import plotting
# Make a large figure
# Mask the main diagonal for visualization:
np.fill_diagonal(correlation_matrix, 0)
# The labels we have start with the background (0), hence we skip the
# first label
# matrices are ordered for block-like representation
plotting.plot_matrix(correlation_matrix, figure=(10, 8), labels=labels[1:],vmax=0.8, vmin=-0.8, reorder=True)
#excluding confounders
time_series = masker.fit_transform(fmri_filenames)
# Note how we did not specify confounds above. This is bad!

correlation_matrix = correlation_measure.fit_transform([time_series])[0]

# Mask the main diagonal for visualization:
np.fill_diagonal(correlation_matrix, 0)

plotting.plot_matrix(correlation_matrix, figure=(10, 8), labels=labels[1:],
                     vmax=0.8, vmin=-0.8, title='No confounds', reorder=True)

plotting.show()

########## 
#signal cleanining
nilearn.signal.clean(time_series, sessions=None, detrend=True, standardize='zscore', confounds=cobre.confounds, low_pass=None, high_pass=None, t_r=2.5, ensure_finite=False)
