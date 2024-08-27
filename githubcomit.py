import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn  
from sklearn import datasets



def get_all_sklearn_datasets():
    dataset_loaders = [
        datasets.load_iris,
        datasets.load_digits,
        datasets.load_wine,
        datasets.load_breast_cancer,
        datasets.load_diabetes,
        datasets.load_linnerud,
        datasets.fetch_california_housing,
        datasets.fetch_covtype,
        datasets.fetch_kddcup99,
        datasets.fetch_olivetti_faces,
        datasets.fetch_20newsgroups,
        datasets.fetch_lfw_people,
        datasets.fetch_rcv1,
    ]
    
    all_datasets = {}
    for loader in dataset_loaders:
        try:
            dataset_name = loader.__name__.split('_')[-1]
            all_datasets[dataset_name] = loader()
        except Exception as e:
            print(f"Error loading {loader.__name__}: {str(e)}")
    
    return all_datasets

# Usage
datasets = get_all_sklearn_datasets()
for name, data in datasets.items():
    print(f"Dataset: {name}")
    print(f"  Features shape: {data.data.shape}")
    print(f"  Target shape: {data.target.shape}")
    print()