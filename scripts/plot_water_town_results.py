

import os 
import argparse
import pandas as pd
import matplotlib.pyplot as plt


# 3. Parse the argument passed to the SFWSM_ClimateStressTest.py script
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--scenario', help='scenario id used for the training', default='scenario_1')
args = parser.parse_args()
scenario = args.scenario

# Read the SOLUTION file for the picked scenario
solution = pd.read_csv('../results/WaterTown_{}.csv'.format(scenario), index_col='Date',
                       parse_dates=True)

# List of variable to be plotted
variables = (
    ('LITTLE_LOCH_STORAGE', 'AF'),
    ('WATER_TOWN_DELIVERIES', 'AFD'),
    ('RIVER_OUTLET', 'AFD')
)

# Check whether there is an output file availalbe for the picked scenario
if os.path.isfile('../results/WaterTown_{}.csv'.format(scenario)):
    run_available = True
    results = pd.read_csv('../results/WaterTown_{}.csv'.format(scenario), index_col='Date',
                       parse_dates=True)
else:
    run_available = False

# Plot the figure
fig, axes = plt.subplots(3,1, figsize=(12,10))

for (var, unit), ax in zip(variables, axes.ravel()):
    ax.plot(solution[var], color='black', label='solution')

    if run_available == True:
        ax.plot(results[var], color='red', linestyle='--', label='your simulation')

    ax.grid()
    ax.set_ylabel(unit, fontsize=12)
    ax.set_title(var, fontsize=12)

plt.legend(fontsize=12)
plt.tight_layout()
fig.savefig('../figures/verification_{}.png'.format(scenario), dpi=130)
plt.show()





