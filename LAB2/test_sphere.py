from pytest import raises
from sphere import Sphere
from circle import Circle
import math

# Valid variables
sphx0y0z0r1a3p6 = Sphere(x=0, y=0, z=0, radius=1)
sphx3y6z9r1a3p6 = Sphere(x=3, y=6, z=9, radius=1)
sphxn1yn3zn5r3a28p18 = Sphere(x=-1, y=-3, z=-5, radius=3)

def test_init_x_pos_valid():
    assert sphx3y6z9r1a3p6.x == 3

def test_init_x_neg_valid():
    assert sphxn1yn3zn5r3a28p18.x == -1

def test_init_x_bool_error():
    with raises(TypeError):
         Sphere(x=True, y=0, radius=1)

def test_init_x_str_error():
    with raises(TypeError):
         Sphere(x="word", y=0, radius=1)

def test_init_y_pos_valid():
    assert sphx3y6z9r1a3p6.y == 6

def test_init_y_neg_valid():
    assert sphxn1yn3zn5r3a28p18.y == -3

def test_init_y_bool_error():
    with raises(TypeError):
         Sphere(x=0, y=False, radius=1)

def test_init_y_str_error():
    with raises(TypeError):
         Sphere(x=0, y="word", radius=1)

def test_init_z_pos_valid():
    assert sphx3y6z9r1a3p6.z == 9

def test_init_z_neg_valid():
    assert sphxn1yn3zn5r3a28p18.z == -5

def test_init_z_bool_error():
    with raises(TypeError):
         Sphere(z=True, y=0, radius=1)

def test_init_z_str_error():
    with raises(TypeError):
         Sphere(z="word", y=0, radius=1)


def test_init_radius_valid():
    assert sphxn1yn3zn5r3a28p18.radius == 3

def test_init_radius_bool_error():
    with raises(TypeError):
         Sphere(x=0, y=0, radius=True)

def test_init_radius_str_error():
    with raises(TypeError):
         Sphere(x=0, y=0, radius="word")

def test_init_radius_no_neg_error():
    with raises(ValueError):
         Sphere(x=0, y=0, radius=-2)

def test_init_radius_no_zero_error():
    with raises(ValueError):
         Sphere(x=0, y=0, radius=0)

def test_init_circle_valid():
    assert sphx0y0z0r1a3p6.circle == Circle(x=0, y=0, radius=1)

def test_repr_valid():
    sph_l = (sphx0y0z0r1a3p6, sphx3y6z9r1a3p6, sphxn1yn3zn5r3a28p18)
    exp_result = (
        "x=0.0 y=0.0 z=0.0, radius:1.0",
        "x=3.0 y=6.0 z=9.0, radius:1.0",
        "x=-1.0 y=-3.0 z=-5.0, radius:3.0"
    )

    for sph, exp_res in zip(sph_l,exp_result):
        assert repr(sph) == exp_res

def test_str_valid():
    sph_l = (sphx0y0z0r1a3p6, sphx3y6z9r1a3p6, sphxn1yn3zn5r3a28p18)
    exp_result = (
        "A Sphere with radius 1.0 and a centerposition at (0.0, 0.0, 0.0)",
        "A Sphere with radius 1.0 and a centerposition at (3.0, 6.0, 9.0)",
        "A Sphere with radius 3.0 and a centerposition at (-1.0, -3.0, -5.0)"
    )
    for sph, exp_res in zip(sph_l,exp_result):
        assert str(sph) == exp_res

def test_position_valid():
    assert sphxn1yn3zn5r3a28p18.position() == (-1.0,-3.0,-5.0)

def test_is_unitsphere():
    assert sphx0y0z0r1a3p6.is_unitsphere() == True

def test_translate_valid():
    cirk_l = cirk_l = (sphx0y0z0r1a3p6, sphx3y6z9r1a3p6, sphxn1yn3zn5r3a28p18)
    exp_results = ((2,2,2),(5,8,11),(1,-1,-3))
    
    for cir, exp_res in zip(cirk_l,exp_results):
        assert cir.translate(2,2,2) == exp_res

def test_translate_x_bool_error():
    with raises(TypeError):
         sphx0y0z0r1a3p6.translate(True, 1, 1)

def test_translate_x_str_error():
    with raises(TypeError):
         sphx0y0z0r1a3p6.translate("word", 1, 1)

def test_translate_y_bool_error():
    with raises(TypeError):
         sphx0y0z0r1a3p6.translate(1, True, 1)

def test_translate_y_str_error():
    with raises(TypeError):
         sphx0y0z0r1a3p6.translate(1, "word", 1)

def test_translate_z_bool_error():
    with raises(TypeError):
         sphx0y0z0r1a3p6.translate(1, 1, True)

def test_translate_z_str_error():
    with raises(TypeError):
         sphx0y0z0r1a3p6.translate(1, 1, "word")

def test_area_valid():
    assert sphxn1yn3zn5r3a28p18.area == math.pi * 36

def test_area_readonly_error():
    with raises(AttributeError):
         sphxn1yn3zn5r3a28p18.area = 2

def test_perimeter_valid():
    assert sphxn1yn3zn5r3a28p18.perimeter == math.pi * 6

def test_perimeter_readonly_error():
    with raises(AttributeError):
         sphxn1yn3zn5r3a28p18.perimeter = 2

def test_eq_valid():
    assert  sphx0y0z0r1a3p6 == sphx3y6z9r1a3p6

def test_lt_valid():
    assert sphx3y6z9r1a3p6 < sphxn1yn3zn5r3a28p18

def test_lt_str_error():
    with raises(TypeError):
         sphx3y6z9r1a3p6 < "word"

def test_lt_bool_error():
    with raises(TypeError):
         sphx3y6z9r1a3p6 < True

def test_le_valid():
    assert sphx3y6z9r1a3p6 <= sphxn1yn3zn5r3a28p18

def test_le_equal_valid():
    assert sphx3y6z9r1a3p6 <= sphx0y0z0r1a3p6

def test_le_str_error():
    with raises(TypeError):
         sphx3y6z9r1a3p6 <= "word"

def test_le_bool_error():
    with raises(TypeError):
         sphx3y6z9r1a3p6 <= True

def test_gt_valid():
    assert sphxn1yn3zn5r3a28p18 > sphx0y0z0r1a3p6

def test_gt_str_error():
    with raises(TypeError):
         sphxn1yn3zn5r3a28p18 > "word"

def test_gt_bool_error():
    with raises(TypeError):
         sphxn1yn3zn5r3a28p18 > True

def test_ge_valid():
    assert sphxn1yn3zn5r3a28p18 >= sphx3y6z9r1a3p6

def test_ge_equal_valid():
    assert sphx0y0z0r1a3p6 >= sphx3y6z9r1a3p6

def test_ge_str_error():
    with raises(TypeError):
         sphxn1yn3zn5r3a28p18 >= "word"

def test_ge_bool_error():
    with raises(TypeError):
         sphxn1yn3zn5r3a28p18 >= True