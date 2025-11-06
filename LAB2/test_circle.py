from pytest import raises
from circle import Circle
import math

# Valid variables
cirx0y0r1a3p6 = Circle(x=0, y=0, radius=1)
cirx3y6r1a3p6 = Circle(x=3, y=6, radius=1)
cirxn1yn3r3a28p18 = Circle(x=-1, y=-3, radius=3)

def test_init_x_pos_valid():
    assert cirx3y6r1a3p6.x == 3

def test_init_x_neg_valid():
    assert cirxn1yn3r3a28p18.x == -1

def test_init_x_bool_error():
    with raises(TypeError):
         Circle(x=True, y=0, radius=1)

def test_init_x_str_error():
    with raises(TypeError):
         Circle(x="word", y=0, radius=1)

def test_init_y_pos_valid():
    assert cirx3y6r1a3p6.y == 6

def test_init_y_neg_valid():
    assert cirxn1yn3r3a28p18.y == -3

def test_init_y_bool_error():
    with raises(TypeError):
         Circle(x=0, y=False, radius=1)

def test_init_y_str_error():
    with raises(TypeError):
         Circle(x=0, y="word", radius=1)

def test_init_radius_valid():
    assert cirxn1yn3r3a28p18.radius == 3

def test_init_radius_bool_error():
    with raises(TypeError):
         Circle(x=0, y=0, radius=True)

def test_init_radius_str_error():
    with raises(TypeError):
         Circle(x=0, y=0, radius="word")

def test_init_radius_no_neg_error():
    with raises(ValueError):
         Circle(x=0, y=0, radius=-2)

def test_init_radius_no_zero_error():
    with raises(ValueError):
         Circle(x=0, y=0, radius=0)

def test_repr_valid():
    cirk_l = (cirx0y0r1a3p6, cirx3y6r1a3p6, cirxn1yn3r3a28p18)
    exp_repr = (
        "x=0.0 y=0.0 radius:1.0",
        "x=3.0 y=6.0 radius:1.0",
        "x=-1.0 y=-3.0 radius:3.0"
    )

    for cir, exp_rep in zip(cirk_l,exp_repr):
        assert repr(cir) == exp_rep

def test_str_valid():
    cirk_l = (cirx0y0r1a3p6, cirx3y6r1a3p6, cirxn1yn3r3a28p18)
    exp_strings = (
        "A Circle with radius 1.0 and a centerposition at (0.0, 0.0)",
        "A Circle with radius 1.0 and a centerposition at (3.0, 6.0)",
        "A Circle with radius 3.0 and a centerposition at (-1.0, -3.0)"
    )

    for cir, exp_str in zip(cirk_l,exp_strings):
        assert str(cir) == exp_str

def test_position_valid():
    assert cirxn1yn3r3a28p18.position() == (-1.0,-3.0)

def test_is_unitcircle():
    assert cirx0y0r1a3p6.is_unitcircle() == True

def test_translate_valid():
    cirk_l = cirk_l = (cirx0y0r1a3p6, cirx3y6r1a3p6, cirxn1yn3r3a28p18)
    exp_results = ((2,2),(5,8),(1,-1))
    
    for cir, exp_res in zip(cirk_l,exp_results):
        assert cir.translate(2,2) == exp_res

def test_translate_x_bool_error():
    with raises(TypeError):
         cirx0y0r1a3p6.translate(True, 1)

def test_translate_x_str_error():
    with raises(TypeError):
         cirx0y0r1a3p6.translate("word", 1)

def test_translate_y_bool_error():
    with raises(TypeError):
         cirx0y0r1a3p6.translate(1, True)

def test_translate_y_str_error():
    with raises(TypeError):
         cirx0y0r1a3p6.translate(1, "word")

def test_area_valid():
    assert cirxn1yn3r3a28p18.area == math.pi * 9

def test_area_readonly_error():
    with raises(AttributeError):
         cirxn1yn3r3a28p18.area = 2

def test_perimeter_valid():
    assert cirxn1yn3r3a28p18.perimeter == math.pi * 6

def test_perimeter_readonly_error():
    with raises(AttributeError):
         cirxn1yn3r3a28p18.perimeter = 2

def test_eq_valid():
    assert  cirx0y0r1a3p6 == cirx3y6r1a3p6

def test_lt_valid():
    assert cirx3y6r1a3p6 < cirxn1yn3r3a28p18

def test_lt_str_error():
    with raises(TypeError):
         cirx3y6r1a3p6 < "word"

def test_lt_bool_error():
    with raises(TypeError):
         cirx3y6r1a3p6 < True

def test_le_valid():
    assert cirx3y6r1a3p6 <= cirxn1yn3r3a28p18

def test_le_equal_valid():
    assert cirx3y6r1a3p6 <= cirx0y0r1a3p6

def test_le_str_error():
    with raises(TypeError):
         cirx3y6r1a3p6 <= "word"

def test_le_bool_error():
    with raises(TypeError):
         cirx3y6r1a3p6 <= True

def test_gt_valid():
    assert cirxn1yn3r3a28p18 > cirx0y0r1a3p6

def test_gt_str_error():
    with raises(TypeError):
         cirxn1yn3r3a28p18 > "word"

def test_gt_bool_error():
    with raises(TypeError):
         cirxn1yn3r3a28p18 > True

def test_ge_valid():
    assert cirxn1yn3r3a28p18 >= cirx3y6r1a3p6

def test_ge_equal_valid():
    assert cirx0y0r1a3p6 >= cirx3y6r1a3p6

def test_ge_str_error():
    with raises(TypeError):
         cirxn1yn3r3a28p18 >= "word"

def test_ge_bool_error():
    with raises(TypeError):
         cirxn1yn3r3a28p18 >= True