from numbers import Number

def validate_measure(measure):
    if type(measure) == bool:
        raise TypeError(f"A measure should be a int or float {measure} is a {type(measure)}")
    if not isinstance(measure, Number):
        raise TypeError(f"A measure should be a int or float {measure} is a {type(measure)}")
    if measure <= 0:
        raise ValueError(f"A measure should be a positive {measure} is a not")
    
def validate_class(class1, class2):
    if not type(class1) == type(class2):
        raise TypeError(f"Can't compare different classes")