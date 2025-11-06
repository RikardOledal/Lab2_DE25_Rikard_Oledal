from pytest import raises
from cube import Cube
from rectangle import Rectangle

# Valid variables
cubx1y2z3s1w1h1d1a6p12v1= Cube(x=1,y=2,z=3,size=1)
cubx2y3z4w1h1d1a6p12v1 = Cube(x=2,y=3,z=4,size=1)
cubxn1y2zn4s2w2h2d2a24p24v8 = Cube(x=-1,y=2,z=-4,size=2)
cubx1yn3z4s3w3h3d3a54p36v27 = Cube(x=1,y=-3,z=4,size=3)
cubxn3yn5z12s5w5h5d5a150p60v125 = Cube(x=-3,y=-3,z=12,size=5)

def test_init_x_pos_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.x == 1

def test_init_x_neg_valid():
    assert cubxn1y2zn4s2w2h2d2a24p24v8.x == -1

def test_init_x_bool_error():
    with raises(TypeError):
         Cube(x=True, y=2, z=2, size=2)

def test_init_x_str_error():
    with raises(TypeError):
         Cube(x="word", y=2, z=2, size=2)

def test_init_y_pos_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.y == 2

def test_init_y_neg_valid():
    assert cubx1yn3z4s3w3h3d3a54p36v27.y == -3

def test_init_y_bool_error():
    with raises(TypeError):
         Cube(x=2, y=False, z=2, size=2)

def test_init_y_str_error():
    with raises(TypeError):
         Cube(x=2, y="word", z=2, size=2)

def test_init_z_pos_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.z == 3

def test_init_z_neg_valid():
    assert cubxn1y2zn4s2w2h2d2a24p24v8.z == -4

def test_init_z_bool_error():
    with raises(TypeError):
         Cube(x=2, y=2, z=True, size=2)

def test_init_z_str_error():
    with raises(TypeError):
         Cube(x=2, y=2, z="word", size=2)

def test_init_size_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.size == 1

def test_init_size_bool_error():
    with raises(TypeError):
         Cube(x=2, y=2, z=2, size=True)

def test_init_size_str_error():
    with raises(TypeError):
         Cube(x=2, y=2, z=2, size="word")

def test_init_size_no_neg_error():
    with raises(ValueError):
         Cube(x=2, y=2, z=2, size=-1)

def test_init_size_no_zero_error():
    with raises(ValueError):
         Cube(x=2, y=2, z=2, size=0)

def test_init_width_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.width == 1

def test_init_height_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.height == 1

def test_init_depth_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.depth == 1

def test_init_rectangle_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.rectangle == Rectangle(x=1, y=2, width=1, height=1)

def test_repr_valid():
    cube_l = (cubx1y2z3s1w1h1d1a6p12v1, cubx2y3z4w1h1d1a6p12v1, cubxn1y2zn4s2w2h2d2a24p24v8, cubx1yn3z4s3w3h3d3a54p36v27, cubxn3yn5z12s5w5h5d5a150p60v125)
    exp_result = (
        "x=1.0 y=2.0 z=3.0, height:1.0, width:1.0, depth:1.0",
        "x=2.0 y=3.0 z=4.0, height:1.0, width:1.0, depth:1.0",
        "x=-1.0 y=2.0 z=-4.0, height:2.0, width:2.0, depth:2.0",
        "x=1.0 y=-3.0 z=4.0, height:3.0, width:3.0, depth:3.0",
        "x=-3.0 y=-3.0 z=12.0, height:5.0, width:5.0, depth:5.0"
    )

    for cub, exp_res in zip(cube_l,exp_result):
        assert repr(cub) == exp_res

def test_str_valid():
    cube_l = (cubx1y2z3s1w1h1d1a6p12v1, cubx2y3z4w1h1d1a6p12v1, cubxn1y2zn4s2w2h2d2a24p24v8, cubx1yn3z4s3w3h3d3a54p36v27, cubxn3yn5z12s5w5h5d5a150p60v125)
    exp_result = (
        "A Cube with height, width and depth of 1.0 and a centerposition at (1.0, 2.0, 3.0)",
        "A Cube with height, width and depth of 1.0 and a centerposition at (2.0, 3.0, 4.0)",
        "A Cube with height, width and depth of 2.0 and a centerposition at (-1.0, 2.0, -4.0)",
        "A Cube with height, width and depth of 3.0 and a centerposition at (1.0, -3.0, 4.0)",
        "A Cube with height, width and depth of 5.0 and a centerposition at (-3.0, -3.0, 12.0)"
    )

    for cub, exp_res in zip(cube_l,exp_result):
        assert str(cub) == exp_res

def test_position_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.position() == (1.0,2.0,3.0)

def test_translate_valid():
    cube_l = (cubx1y2z3s1w1h1d1a6p12v1, cubx2y3z4w1h1d1a6p12v1, cubxn1y2zn4s2w2h2d2a24p24v8, cubx1yn3z4s3w3h3d3a54p36v27, cubxn3yn5z12s5w5h5d5a150p60v125)
    exp_result = ((3,4,5),(4,5,6),(1,4,-2),(3,-1,6),(-1,-1,14))

    for cub, exp_res in zip(cube_l,exp_result):
        assert cub.translate(2,2,2) == exp_res

def test_translate_x_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1.translate(True, 1, 1)

def test_translate_x_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1.translate("word", 1, 1)

def test_translate_y_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1.translate(1, True, 1)

def test_translate_y_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1.translate(1, "word", 1)

def test_translate_z_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1.translate(1, 1, True)

def test_translate_z_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1.translate(1, 1, "word")

def test_area_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.area == 6

def test_area_readonly_error():
    with raises(AttributeError):
         cubx1y2z3s1w1h1d1a6p12v1.area = 2

def test_perimeter_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.perimeter == 12

def test_perimeter_readonly_error():
    with raises(AttributeError):
         cubx1y2z3s1w1h1d1a6p12v1.perimeter = 2

def test_volume_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1.volume == 1

def test_volume_readonly_error():
    with raises(AttributeError):
         cubx1y2z3s1w1h1d1a6p12v1.volume = 2

def test_eq_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1 == cubx2y3z4w1h1d1a6p12v1

def test_lt_valid():
    assert cubxn1y2zn4s2w2h2d2a24p24v8 < cubx1yn3z4s3w3h3d3a54p36v27

def test_lt_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 < "word"

def test_lt_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 < True

def test_le_valid():
    assert cubxn1y2zn4s2w2h2d2a24p24v8 <= cubx1yn3z4s3w3h3d3a54p36v27

def test_le_equal_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1 <= cubx1y2z3s1w1h1d1a6p12v1

def test_le_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 <= "word"

def test_le_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 <= True

def test_gt_valid():
    assert cubx1yn3z4s3w3h3d3a54p36v27 > cubxn1y2zn4s2w2h2d2a24p24v8

def test_gt_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 > "word"

def test_gt_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 > True

def test_ge_area_valid():
    assert cubx1yn3z4s3w3h3d3a54p36v27 >= cubxn1y2zn4s2w2h2d2a24p24v8

def test_ge_equal_valid():
    assert cubx1y2z3s1w1h1d1a6p12v1 >= cubx1y2z3s1w1h1d1a6p12v1

def test_ge_str_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 >= "word"

def test_ge_bool_error():
    with raises(TypeError):
         cubx1y2z3s1w1h1d1a6p12v1 >= True