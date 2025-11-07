from numbers import Number

def validate_measure(measure):
    if type(measure) == bool:
        raise TypeError(f"A measure should be a int or float {measure} is a {type(measure)}")
    if not isinstance(measure, Number):
        raise TypeError(f"A measure should be a int or float {measure} is a {type(measure)}")
    if measure <= 0:
        raise ValueError(f"A measure should be a positive {measure} is a not")
    
def validate_class(check_class):
    if isinstance(check_class,(str, bool, Number)):
        raise TypeError(f"Can only compare shapes")
    if check_class.area == None:
        raise TypeError(f"Can't compare classes without area")
    if check_class.perimeter == None:
        raise TypeError(f"Can't compare classes without perimeter")
    
def validate_xy(xy):
    if type(xy) == bool:
        raise TypeError(f"{xy} should be int or float. Not {type(xy)}")
    if not isinstance(xy, Number):
        raise TypeError(f"{xy} should be int or float. Not {type(xy)}")
    
def validate_cube(size_mesure, other_mesure):
    if not isinstance(other_mesure, Number):
        raise TypeError(f"A measure should be a int or float {other_mesure} is a {type(other_mesure)}")
    if size_mesure != other_mesure:
        raise ValueError(f"A cube can't change just one mesure. Try changing size instead")