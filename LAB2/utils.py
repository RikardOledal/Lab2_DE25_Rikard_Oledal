from numbers import Number

def validate_measure(measure):
    if not isinstance(measure, Number):
        raise TypeError(f"A measure should be a int or float {measure} is a {type(measure)}")
    if measure <= 0:
        raise ValueError(f"A measure should be a positive {measure} is a not")