import tensorflow_decision_forests as tfdf

import os
import numpy as np
import pandas as pd
import tensorflow as tf
import math

dataset_df = pd.read_csv("penguins.csv")
dataset_df.head(3)


