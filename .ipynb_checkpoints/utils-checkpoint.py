import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
def generate_random_sales(min_val, max_val, size):
    """
    Génère un tableau NumPy d'entiers aléatoires entre min_val et max_val
    
    Args:
        min_val (int): Valeur minimale
        max_val (int): Valeur maximale
        size (int): Taille du tableau
    
    Returns:
        np.array: Tableau de valeurs aléatoires
    """
    return np.random.randint(min_val, max_val + 1, size)
