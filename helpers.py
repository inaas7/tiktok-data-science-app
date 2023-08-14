# Convert processing code to function
def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges', 'duetInfo', 'textExtra', 'stickersOnItem', 'contents']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    # Create blank dictionary
    flattened_data = {}
    # Loop through each video
    for idx, value in enumerate(data): 
        flattened_data[idx] = {}
        # Loop through each property in each video 
        if isinstance(value, dict):
            for prop_idx, prop_value in value.items():
                # Check if nested
                if prop_idx in nested_values:
                    if prop_idx == 'contents':
                        first_dict = prop_value[0]
                        if isinstance(first_dict, dict):
                            first_key, first_value = next(iter(first_dict.items()))
                            flattened_data[idx][first_key] = first_value
                    elif prop_idx not in skip_values:
                        # Loop through each nested property
                        if isinstance(prop_value, dict):
                            for nested_idx, nested_value in prop_value.items():
                                flattened_data[idx][prop_idx+'_'+nested_idx] = nested_value
                # If it's not nested, add it back to the flattened dictionary
                else: 
                    flattened_data[idx][prop_idx] = prop_value
    
    return flattened_data