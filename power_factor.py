import math

def calculate_power_values(input_var_1, value_1, input_var_2, value_2, decimal_places=4):
    """
    Calculate power factor, apparent power, active power, reactive power, and angle given any two of them.

    Parameters:
    input_var_1, input_var_2: Variables to be calculated. Can be 's', 'p', 'q', 'pf', 'angle'
    value_1, value_2: Corresponding values of input_var_1 and input_var_2.
    decimal_places: Number of decimal places to round the results to.

    Returns:
    Dictionary with calculated values of 's', 'p', 'q', 'pf', 'angle'
    """
    power_values = {input_var_1: value_1, input_var_2: value_2}

    # Calculate power factor and angle if they are not provided
    if 'pf' not in power_values and 'angle' not in power_values:
        if 's' not in power_values or 'p' not in power_values:
            raise ValueError("Cannot calculate power factor and angle without 's' and 'p' values")

        power_values['pf'] = power_values['p'] / power_values['s']
        power_values['angle'] = math.degrees(math.acos(power_values['pf']))

    # Calculate power factor or angle if one of them is not provided
    elif 'pf' not in power_values:
        power_values['pf'] = math.cos(math.radians(power_values['angle']))
    elif 'angle' not in power_values:
        power_values['angle'] = math.degrees(math.acos(power_values['pf']))

    # Calculate 's', 'p', and 'q' values
    if 's' not in power_values:
        if 'p' in power_values and 'q' in power_values:
            power_values['s'] = math.sqrt(power_values['p']**2 + power_values['q']**2)
        else:
            raise ValueError("Cannot calculate 's' value without 'p' and 'q' values")

    if 'p' not in power_values:
        power_values['p'] = power_values['s'] * power_values['pf']

    if 'q' not in power_values:
        power_values['q'] = math.sqrt(power_values['s']**2 - power_values['p']**2)

    # Round results to the specified number of decimal places
    for key, value in power_values.items():
        if isinstance(value, float):
            power_values[key] = round(value, decimal_places)

    return power_values
