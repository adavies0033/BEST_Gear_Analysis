###################################
###################################
# Typical internal-gear arrangement
# Involute Tooth Spur Gear Pair

# Version: V 0.1

# Ref. 
# https://khkgears.net/new/gear_knowledge/abcs_of_gears-b/basic_gear_terminology_calculation.html
# https://www.taylorfrancis.com/books/edit/10.1201/9781315368122/dudley-handbook-practical-gear-design-manufacture-stephen-radzevich

###################################
###################################

import matplotlib.pyplot as plt
import numpy as np
import yaml

#####################
# Parse Yaml Params #
#####################

# Path to the YAML file
yaml_file_path = 'Spur/param.yml'

# Read and parse the YAML file
with open(yaml_file_path, 'r') as file:
    params = yaml.safe_load(file)

# Print parsed parameters to verify



#####################
#   Calculations    #
#####################

C = (params['D'] - params['d']) / 2         # Center Dist. (mm)
params['C'] = C

z2 = int(params['u'] * params['z1']  + 1)   # Teeth Gear (for internal gear)
params['z2'] = z2

m = params['d'] / params['z1']              # Module (mm) pinion
params['m'] = m

b = 8 * m                                   # Face width (mm)
params['b'] = b

P = 1 / m                               # Diametral Pitch (mm) pinion
params['P'] = P

ht = 2.25/params['P']                   # WHole Depth (mm)
params['ht'] = ht




for key, value in params.items():
    print(f"{key}: {value}")