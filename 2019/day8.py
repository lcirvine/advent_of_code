import pandas as pd
import numpy as np


with open('day8_input.txt', 'r') as f:
    data = f.read()

# PART ONE
width = 25
height = 6
pix_per_layer = width * height
data_in_layers = [data[i: i + pix_per_layer] for i in range(0, len(data), pix_per_layer)]
layer_dict = {}
layer_counter = 0
for layer in data_in_layers:
    layer_dict[layer_counter] = layer.count(str(0))
    layer_counter += 1

min_zero_layer = min(layer_dict, key=layer_dict.get)
print(data_in_layers[min_zero_layer].count(str(1)) * data_in_layers[min_zero_layer].count(str(2)))

# PART TWO
df_data = []
for layer in data_in_layers:
    layer_list = []
    for digit in layer:
        layer_list.append(int(digit))
    df_data.append(layer_list)

pt_2_list = []
df = pd.DataFrame(df_data)
df = df.replace(2, np.nan)
for col in df.columns:
    pt_2_list.append(int(df.loc[df[col].first_valid_index(), col]))
answ = [pt_2_list[i : i + width] for i in range(0, len(pt_2_list), width)]
df_answ = pd.DataFrame(answ)

print(df_answ)

