import os

def convert_metric(value, from_unit, to_unit):
    """Convert metric units."""
    conversion_factors = {
        ('km', 'mi'): float(os.getenv("KM_TO_MI", 0.621371)),
        ('km/h', 'mph'): float(os.getenv("KMH_TO_MPH", 0.621371)),
        ('kg', 'lb'): float(os.getenv("KG_TO_LB", 2.20462))
    }

    conversion_key = (from_unit, to_unit)
    if conversion_key in conversion_factors:
        return value * conversion_factors[conversion_key]
    else:
        raise ValueError("Conversion not supported")
