from scipy.ndimage import gaussian_filter
from scipy import misc
import numpy as np
import pandas as pd

__all__ = ['rand_array', 'smooth_image','my_mat_solve','my_choice']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a,sigma=1):
	return gaussian_filter(a,sigma=sigma)

def my_mat_solve(A,b):
	return A.inv()*b

def my_choice():
	d = {'col1': [1, 2], 'col2': [3, 4]}
	df = pd.DataFrame(data=d)
	return df
