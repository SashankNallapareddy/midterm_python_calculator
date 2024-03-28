import os
import conversions

def test_convert_metric_km_to_mi():
    value = 10
    from_unit = 'km'
    to_unit = 'mi'
    expected_result = value * float(os.getenv("KM_TO_MI", 0.621371))
    assert conversions.convert_metric(value, from_unit, to_unit) == expected_result

def test_convert_metric_km_to_mph():
    value = 100
    from_unit = 'km/h'
    to_unit = 'mph'
    expected_result = value * float(os.getenv("KMH_TO_MPH", 0.621371))
    assert conversions.convert_metric(value, from_unit, to_unit) == expected_result

def test_convert_metric_kg_to_lb():
    value = 50
    from_unit = 'kg'
    to_unit = 'lb'
    expected_result = value * float(os.getenv("KG_TO_LB", 2.20462))
    assert conversions.convert_metric(value, from_unit, to_unit) == expected_result

def test_convert_metric_invalid_conversion():
    value = 10
    from_unit = 'km'
    to_unit = 'cm'
    try:
        conversions.convert_metric(value, from_unit, to_unit)
        assert False, "Expected ValueError"
    except ValueError:
        assert True