import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def setup_plots():
    fig_init, ax_init = plt.subplots()
    fig_def, ax_def = plt.subplots()
    ax_init.set_title('Initialramme')
    ax_def.set_title('Deformert ramme') 
    ax_init.axes.set_aspect('equal')
    ax_def.axes.set_aspect('equal')
    return fig_init, ax_init, fig_def, ax_def

def plot_structure(ax, punkt, elem, numbers, index_start):
    # This is a translation of the original function written by Josef Kiendl in Matlab
    # It has been slightly modified in order to be used in TMR4176

    # This function plots the beam structure defined by nodes and elements
    # The bool (0 or 1) 'numbers' decides if node and element numbers are plotted or not

    # Change input to the correct format
    nodes = np.array(punkt[:, 0:2], copy = 1, dtype = int)
    el_nod = np.array(elem[:, 0:2], copy = 1, dtype=int) + 1

    # Start plotting part
    for iel in range(0, el_nod.shape[0]):
        # Plot element
        ax.plot([nodes[el_nod[iel, 0] - 1, 0], nodes[el_nod[iel, 1] - 1, 0]],
                [nodes[el_nod[iel, 0] - 1, 1], nodes[el_nod[iel, 1] - 1, 1]], '-k', linewidth = 2)

        if numbers == 1:
            # Plot element numbers. These are not plotted in the midpoint to
            # avoid number superposition when elements cross in the middle
            ax.text(nodes[el_nod[iel, 0] - 1, 0] + ( nodes[el_nod[iel, 1] - 1, 0] - nodes[el_nod[iel, 0] - 1, 0] ) / 2.5,
                    nodes[el_nod[iel, 0] - 1, 1] + ( nodes[el_nod[iel, 1] - 1, 1] - nodes[el_nod[iel, 0] - 1, 1] ) / 2.5,
                    str(iel + index_start), color = 'blue', fontsize = 16)

    if numbers == 1:
        # Plot node number
        for inod in range(0, nodes.shape[0]):
            ax.text(nodes[inod, 0], nodes[inod, 1], str(inod + index_start), color = 'red', fontsize = 16)


def format_data(knutepunkter, elementer): #formaterer lister så det kan tolkes riktig av plot_structure

    # Extract node coordinates from knutepunkter list
    kp_koordinater = np.array([[node[1], node[2]] for node in knutepunkter])
    
    # Extract element node indices from elementer list
    elementer_kp = np.array([[int(node[1]), int(node[2])] for node in elementer])
    
    return kp_koordinater, elementer_kp

