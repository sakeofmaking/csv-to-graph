"""
Graph Voltage

Description: Graph voltage from CH1, CH2, CH4

Author: Nic La
Last modified: May 2022
"""


import csv
import matplotlib.pyplot as plt


def open_csv():
    """Open CSV file and x_values, y1_values, y2_values, y3_values"""
    # Initialize variables
    date_file = 'input.CSV'
    raw = []
    x_values, y1_values, y2_values, y3_values = [], [], [], []

    # Open csv
    with open(date_file) as in_file:
        reader = csv.reader(in_file, delimiter=',')
        for row in reader:
            raw.append(row)
    
    # Assign first row to header
    x_header, y1_header, y2_header, y3_header = raw[0]
    
    # Assign remaining rows to x, y1, y2, y3
    for line in raw[1:]:
        x_values.append((float(line[0]) - 1) / 10)
        y1_values.append(float(line[1]))
        y2_values.append(float(line[2]))
        y3_values.append(float(line[3]))
    
    return x_header, y1_header, y2_header, y3_header, x_values, y1_values, y2_values, y3_values


def plot_data(x_header, y1_header, y2_header, y3_header, x_values, y1_values, y2_values, y3_values):
    """Plot x, y1, y2, y3"""
    # Plot scatter
    # plt.figure()
    # plt.scatter(x_values, y1_values, c='red', edgecolors='none', s=10, label=y1_header)
    # plt.scatter(x_values, y2_values, c='green', edgecolors='none', s=10, label=y2_header)
    # plt.scatter(x_values, y3_values, c='blue', edgecolors='none', s=10, label=y3_header)

    # Plot line
    plt.figure()
    # plt.plot(x_values, y1_values, c='red', label=y1_header)
    plt.plot(x_values, y2_values, c='green', label=y2_header)
    # plt.plot(x_values, y3_values, c='blue', label=y3_header)

    # Set chart title and label axis
    plt.title("Voltage Over Time", fontsize=24)
    plt.xlabel("Time (s)", fontsize=14)
    plt.ylabel("Voltage (V)", fontsize=14)
    plt.legend()

    # Set range for each axis
    # plt.axis([0, 1000, 23.4, 23.6])

    # plt.savefig('plot.png', bbox_inches='tight')  # bbox_inches trims excess white space
    plt.show()


if __name__ == "__main__":
    x_header, y1_header, y2_header, y3_header, x_values, y1_values, y2_values, y3_values = open_csv()
    plot_data(x_header, y1_header, y2_header, y3_header, x_values, y1_values, y2_values, y3_values)
