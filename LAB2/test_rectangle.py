from pytest import raises
from rectangle import Rectangle

# Valid variables
recx1y2w1h4a4p10 = Rectangle(x=1,y=2,width=1, height=4) # xy both positive | Area 4 Perimeter 10
recx2y3w4h1a4p10 = Rectangle(x=2,y=3,width=4, height=1) # xy both positive | Area 4 Perimeter 10
recxn1y2w2h2a4p8 = Rectangle(x=-1,y=2,width=2, height=2) # x negative y positive | Area 4 Perimeter 8 | Squer 
recx1yn3w3h3a9p12 = Rectangle(x=1,y=-3,width=3, height=3) # x positive y negative | Area 9 Perimeter 12 | Squer
recxn3yn3w1h5a10p12 = Rectangle(x=-3,y=-3,width=1, height=5) # xy both negative | Area 5 Perimeter 12

def test_init_x_pos_valid():
    assert recx1y2w1h4a4p10.x == 1

def test_init_x_neg_valid():
    assert recxn1y2w2h2a4p8.x == -1

def test_init_x_bool_error():
    with raises(TypeError):
         Rectangle(x=True,y=2,width=1, height=4)

def test_init_x_str_error():
    with raises(TypeError):
         Rectangle(x="word",y=2,width=1, height=4)

def test_init_y_pos_valid():
    assert recx1y2w1h4a4p10.y == 2

def test_init_y_neg_valid():
    assert recx1yn3w3h3a9p12.y == -3

def test_init_y_bool_error():
    with raises(TypeError):
         Rectangle(x=2 ,y=False,width=1, height=4)

def test_init_y_str_error():
    with raises(TypeError):
         Rectangle(x=2,y="word",width=1, height=4)

def test_init_width_valid():
    assert recx1y2w1h4a4p10.width == 1

def test_init_width_bool_error():
    with raises(TypeError):
         Rectangle(x=1,y=2,width=False, height=4)

def test_init_width_str_error():
    with raises(TypeError):
         Rectangle(x=1,y=2,width="word", height=4)

def test_init_width_no_neg_error():
    with raises(ValueError):
         Rectangle(x=1,y=2,width=-1, height=4)

def test_init_width_no_zero_error():
    with raises(ValueError):
         Rectangle(x=1,y=2,width=0, height=4)

def test_init_height_valid():
    assert recx1y2w1h4a4p10.height == 4

def test_init_height_bool_error():
    with raises(TypeError):
         Rectangle(x=1,y=2,width=1, height=True)

def test_init_height_str_error():
    with raises(TypeError):
         Rectangle(x=1,y=2,width=1, height="word")

def test_init_height_no_neg_error():
    with raises(ValueError):
         Rectangle(x=1,y=2,width=1, height=-1)

def test_init_height_no_zero_error():
    with raises(ValueError):
         Rectangle(x=1,y=2,width=1, height=0)

def test_repr_valid():
    rectangl = (recx1y2w1h4a4p10, recx2y3w4h1a4p10, recxn1y2w2h2a4p8, recx1yn3w3h3a9p12, recxn3yn3w1h5a10p12)
    exp_repr = (
        "x=1.0 y=2.0, height:4.0, width:1.0",
        "x=2.0 y=3.0, height:1.0, width:4.0",
        "x=-1.0 y=2.0, height:2.0, width:2.0",
        "x=1.0 y=-3.0, height:3.0, width:3.0",
        "x=-3.0 y=-3.0, height:5.0, width:1.0"
    )

    for rec, exp_rep in zip(rectangl,exp_repr):
        assert repr(rec) == exp_rep

def test_str_valid():
    rectangl = (recx1y2w1h4a4p10, recx2y3w4h1a4p10, recxn1y2w2h2a4p8, recx1yn3w3h3a9p12, recxn3yn3w1h5a10p12)
    exp_strings = (
        "A Rectangle with height 4.0 and width 1.0 and a centerposition at (1.0, 2.0)",
        "A Rectangle with height 1.0 and width 4.0 and a centerposition at (2.0, 3.0)",
        "A Rectangle with height 2.0 and width 2.0 and a centerposition at (-1.0, 2.0)",
        "A Rectangle with height 3.0 and width 3.0 and a centerposition at (1.0, -3.0)",
        "A Rectangle with height 5.0 and width 1.0 and a centerposition at (-3.0, -3.0)"
    )

    for rec, exp_str in zip(rectangl,exp_strings):
        assert str(rec) == exp_str

def test_position_valid():
    assert recx1y2w1h4a4p10.position() == (1.0,2.0)

def test_translate_valid():
    rectangl = (recx1y2w1h4a4p10, recx2y3w4h1a4p10, recxn1y2w2h2a4p8, recx1yn3w3h3a9p12, recxn3yn3w1h5a10p12)
    exp_results = ((3,4),(4,5),(1,4),(3,-1),(-1,-1))

    for rec, exp_res in zip(rectangl,exp_results):
        assert rec.translate(2,2) == exp_res

def test_translate_x_bool_error():
    with raises(TypeError):
         recx1y2w1h4a4p10.translate(True, 1)

def test_translate_x_str_error():
    with raises(TypeError):
         recx1y2w1h4a4p10.translate("word", 1)

def test_translate_y_bool_error():
    with raises(TypeError):
         recx1y2w1h4a4p10.translate(1, True)

def test_translate_y_str_error():
    with raises(TypeError):
         recx1y2w1h4a4p10.translate(1, "word")

def test_area_valid():
    rectangl = (recx1y2w1h4a4p10, recx2y3w4h1a4p10, recxn1y2w2h2a4p8, recx1yn3w3h3a9p12, recxn3yn3w1h5a10p12)
    exp_results = (4.0,4.0,4.0,9.0,5.0)

    for rec, exp_res in zip(rectangl,exp_results):
        assert rec.area == exp_res

def test_area_readonly_error():
    with raises(AttributeError):
         recx1y2w1h4a4p10.area = 2

def test_perimeter_valid():
    rectangl = (recx1y2w1h4a4p10, recx2y3w4h1a4p10, recxn1y2w2h2a4p8, recx1yn3w3h3a9p12, recxn3yn3w1h5a10p12)
    exp_results = (10.0,10.0,8.0,12.0,12.0)

    for rec, exp_res in zip(rectangl,exp_results):
        assert rec.perimeter == exp_res

def test_perimeter_readonly_error():
    with raises(AttributeError):
         recx1y2w1h4a4p10.perimeter = 2

def test_eq_valid():
    assert recx1y2w1h4a4p10 == recx2y3w4h1a4p10

def test_lt_area_valid(): # Lesser area == True
    assert recxn1y2w2h2a4p8 < recx1yn3w3h3a9p12

def test_lt_perimeter_valid(): # Same area but lesser perimeter == True
    assert recxn1y2w2h2a4p8 < recx2y3w4h1a4p10

def test_lt_str_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 < "word"

def test_lt_bool_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 < True

def test_le_area_valid(): # Lesser area == True
    assert recxn1y2w2h2a4p8 <= recx1yn3w3h3a9p12

def test_le_perimeter_valid(): # Same area but lesser perimeter == True
    assert recxn1y2w2h2a4p8 <= recx2y3w4h1a4p10

def test_le_equal_valid(): # Same area and perimeter == True
    assert recx1y2w1h4a4p10 <= recx1y2w1h4a4p10

def test_le_str_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 <= "word"

def test_le_bool_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 <= True

def test_gt_area_valid(): # Greater area == True
    assert recx1yn3w3h3a9p12 > recxn1y2w2h2a4p8

def test_gt_perimeter_valid(): # Same area but greater perimeter == True
    assert recx2y3w4h1a4p10 > recxn1y2w2h2a4p8

def test_gt_str_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 > "word"

def test_gt_bool_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 > True

def test_ge_area_valid(): # Greater area == True
    assert recx1yn3w3h3a9p12 >= recxn1y2w2h2a4p8

def test_ge_perimeter_valid(): # Same area but greater perimeter == True
    assert recx2y3w4h1a4p10 >= recxn1y2w2h2a4p8

def test_ge_equal_valid(): # Same area and perimeter == True
    assert recx1y2w1h4a4p10 >= recx1y2w1h4a4p10

def test_ge_str_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 >= "word"

def test_ge_bool_error():
    with raises(TypeError):
         recx1y2w1h4a4p10 >= True

def test_is_squer_valid():
    assert recxn1y2w2h2a4p8.is_squer()