# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division


__version__ = '0.2.0.dev0'


from allel.constants import *
from allel.model import GenotypeArray, HaplotypeArray, PositionIndex, \
    LabelIndex
from allel.util import windowed_count, windowed_density
