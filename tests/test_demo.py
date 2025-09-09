import pytest
import matplotlib.pyplot as plt

def test_mpl():
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show() 
