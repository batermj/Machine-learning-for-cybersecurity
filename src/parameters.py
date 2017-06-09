# -*- coding: utf-8 -*-

import os

dir_name = os.path.dirname

# ----------- SPAM -----------
TRAINING_DATA_FOR_SPAM = os.path.join(dir_name(dir_name(__file__)),
                                      'datasets',
                                      'cs_problems',
                                      'spam',
                                      'training.spambase.data.txt')

# ----------- PHISHING -----------
TRAINING_DATA_FOR_PHISHING = os.path.join(dir_name(dir_name(__file__)),
                                          'datasets',
                                          'cs_problems',
                                          'phishing',
                                          'training.phishing.data.txt')

# ----------- TRACKWARE -----------
TRACKWARE_SAMPLES_FILE = os.path.join(dir_name(dir_name(__file__)),
                                      'datasets',
                                      'cs_problems',
                                      'trackware',
                                      'trackware_samples.txt')
ALL_SAMPLES_FOR_TRACKWARE = os.path.join(dir_name(dir_name(__file__)),
                                         'datasets',
                                         'cs_problems',
                                         'trackware',
                                         'all_samples.txt')
GENERATED_SAMPLES_FILE_FOR_TRACKWARE = os.path.join(
    dir_name(dir_name(__file__)),
    'datasets',
    'cs_problems',
    'trackware',
    'generated_samples.txt')
