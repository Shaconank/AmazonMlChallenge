entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'maximum_weight_recommendation': {'gram',
        'kilogram',
        'microgram',
        'milligram',
        'ounce',
        'pound',
        'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre',
        'cubic foot',
        'cubic inch',
        'cup',
        'decilitre',
        'fluid ounce',
        'gallon',
        'imperial gallon',
        'litre',
        'microlitre',
        'millilitre',
        'pint',
        'quart'}
}

allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}

collated_units = {
    'width': {
        'ft', 'centimeter', 'foot-unit', 'milli-meter', 'metre', 'meter', 'inch', 'in', 'milli-metre', 'met-re', '"', 'centi-metre', 'mm', 'cm', 'met-er', 'foot', 'millimetre', "'", 'centimetre', 'yard', 'millimeter', 'feet', 'centi-meter', 'inches', 'm', 'yd', 'yards'
        }, 
    'depth': {
        'ft', 'centimeter', 'foot-unit', 'milli-meter', 'metre', 'meter', 'inch', 'in', 'milli-metre', 'met-re', '"', 'centi-metre', 'mm', 'cm', 'met-er', 'foot', 'millimetre', "'", 'centimetre', 'yard', 'millimeter', 'feet', 'centi-meter', 'inches', 'm', 'yd', 'yards'
        }, 
    'height': {
        'ft', 'centimeter', 'foot-unit', 'milli-meter', 'metre', 'meter', 'inch', 'in', 'milli-metre', 'met-re', '"', 'centi-metre', 'mm', 'cm', 'met-er', 'foot', 'millimetre', "'", 'centimetre', 'yard', 'millimeter', 'feet', 'centi-meter', 'inches', 'm', 'yd', 'yards'
        }, 
    'item_weight': {
        't', 'kilogram', 'oz', 'mg', 'metric ton', 'lb', 'grams', 'tonne', 'lbm', 'milli-gram', 'µg', 'ton', 'tonnes', 'pounds', 'g', 'kilograms', 'lbs', 'ounces', 'kilo-gram', 'metric tonne', 'gm', 'tons', 'milligram', 'ounce', 'microgram', '#', 'gram', 'pound', 'kg', 'micro-gram'
        }, 
    'maximum_weight_recommendation': {
        't', 'kilogram', 'oz', 'mg', 'metric ton', 'lb', 'grams', 'tonne', 'lbm', 'milli-gram', 'µg', 'ton', 'tonnes', 'pounds', 'g', 'kilograms', 'lbs', 'ounces', 'kilo-gram', 'metric tonne', 'gm', 'tons', 'milligram', 'ounce', 'microgram', '#', 'gram', 'pound', 'kg', 'micro-gram'
        }, 
    'voltage': {
        'milli-volt', 'volt', 'V', 'kilo-volt', 'kilovolt', 'kV', 'volts', 'millivolt', 'mV'
    }, 
    'wattage': {
        'kilo-watt', 'kilowatt', 'kW', 'watts', 'watt', 'W'
    }, 
    'item_volume': {
        'imp gal', 'cubic foot', 'liters', 'cL', 'mL', 'micro-liter', 'liter', 'deci-litre', 'imperial gallons', 'in³', 'quarts', 'gal', 'gallon', 'microlitre', 'centilitre', 'cubic inches', 'imperial gallon', 'decilitre', 'centi-litre', 'L', 'cup', 'qt', 'gallons', 'dL', 'fl. oz.', 'ft^3', 'C', 'micro-litre', 'milli-litre', 'fluid ounce', 'centiliter', 'US gallon', 'microliter', 'millilitre', 'litres', 'deciliter', 'pints', 'deci-liter', 'ft³', 'cubic inch', 'in^3', 'cups', 'fluid ounces', 'milli-liter', 'pint', 'µL', 'cubic feet', 'fl oz', 'milliliter', 'litre', 'centi-liter', 'pt', 'quart'
        }
}
