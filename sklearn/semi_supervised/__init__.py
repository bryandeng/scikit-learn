"""
The :mod:`sklearn.semi_supervised` module implements semi-supervised learning
algorithms. These algorithms utilized small amounts of labeled data and large
amounts of unlabeled data for classification tasks. This module includes Label
Propagation and Smoothness Maximization.
"""

from .label_propagation import LabelPropagation, LabelSpreading
from .smoothness_maximization import SmoothnessMaximization

__all__ = ['LabelPropagation', 'LabelSpreading',
           'SmoothnessMaximization']
