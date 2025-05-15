
# Load python libraries
import numpy as np
import pandas as pd
import argparse
import json
import pywr
from pywr.core import Model
from pywr.parameters import load_parameter
from pywr.parameters import Parameter

# Handle warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--scenario', help='scenario id used for the training', default='scenario_1')
args = parser.parse_args()
scenario = args.scenario

# A python class that describe the rationing policy when the system storage drops.
class DeliveryFactor(Parameter):

    """
        This python class defines a parameter that reduces deliveries when Little Loch storage
        drops below pre-specified values
    """

    def __init__(self, model):
        super().__init__(model)

        # By default, 100% of the demand is satisfied
        self.delivery_factor = 1

    def value(self, timestep, scenario_index):

        # Maximum storage for the Little Loch Reservoir
        little_loch_max_storage = self.model.nodes['little_loch'].max_volume

        # Current storage for the Little Loch Reservoir
        little_loch_storage = self.model.nodes['little_loch'].volume
        
        if little_loch_storage> 0.5 * little_loch_max_storage:
            self.delivery_factor = 1 # No rationing
        elif 0.25* little_loch_max_storage < little_loch_storage<= 0.50* little_loch_max_storage:
            self.delivery_factor = 0.5 # 50% rationing
        else:
            self.delivery_factor = 0.25 # 75% rationing

        return self.delivery_factor
    
    @classmethod
    def load(cls, model, data):
        return cls(model, **data)
    

# Make the 'DeliveryFactor' parameter known to pywr
DeliveryFactor.register()

model = '../models/model_json/water_town_{}.json'.format(scenario)

# Load the json model file
m = Model.load(model) 
# Run the model
m.run() 
# Move the output into a dataframe
results = m.to_dataframe()
# Take out the first empty row of the dataframe
results.columns = results.columns.get_level_values(0)
results.index.name = 'Date'

# Save the dataframe into a.csv file
results.to_csv('../results/WaterTown_{}.csv'.format(scenario))
print("Water Town script run was successful.")