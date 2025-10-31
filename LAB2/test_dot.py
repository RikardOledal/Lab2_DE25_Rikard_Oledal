from pytest import raises
from dot import Dot

# Valid variables
dotx1y2 = Dot(x=1,y=2) # both positive
dotx2y3 = Dot(x=2,y=3) # both positive
dotxn1y2 = Dot(x=-1,y=2) # x negative y positive
dotx1yn3 = Dot(x=1,y=-3) # x positive y negative
dotxn3yn3 = Dot(x=-3,y=-3) # both negative

def test_init_x_pos_valid():
    assert dotx1y2.x == 1

def test_init_x_neg_valid():
    assert dotxn1y2.x == -1

def test_init_y_pos_valid():
    assert dotx1y2.y == 2

def test_init_y_neg_valid():
    assert dotx1yn3.y == -3

def test_init_bool_x_error():
    with raises(TypeError):
         Dot(x=True,y=2)

def test_init_bool_y_error():
    with raises(TypeError):
         Dot(x=2 ,y=False)

def test_init_str_x_error():
    with raises(TypeError):
         Dot(x="word",y=2)

def test_init_str_y_error():
    with raises(TypeError):
         Dot(x=2,y="word")

def test_repr_valid():
    dots = (dotx1y2,dotx1yn3,dotxn1y2,dotxn3yn3)
    exp_repr = (
        "x=1.0 y=2.0",
        "x=1.0 y=-3.0",
        "x=-1.0 y=2.0",
        "x=-3.0 y=-3.0"        
    )

    for dot, exp_rep in zip(dots,exp_repr):
        assert repr(dot) == exp_rep

def test_str_valid():
    dots = (dotx1y2,dotx1yn3,dotxn1y2,dotxn3yn3)
    exp_strings = (
        "A dot with position (1.0, 2.0)",
        "A dot with position (1.0, -3.0)",
        "A dot with position (-1.0, 2.0)",
        "A dot with position (-3.0, -3.0)",
    )

    for dot, exp_str in zip(dots,exp_strings):
        assert str(dot) == exp_str

def test_position_valid():
    assert dotx1y2.position() == (1.0,2.0)

def test_translate_valid():
    dots = (dotx1y2,dotx1yn3,dotxn1y2,dotxn3yn3)
    exp_results = (
        (3,4),
        (3,-1),
        (1,4),
        (-1,-1)
    )

    for dot, exp_res in zip(dots,exp_results):
        assert dot.translate(2,2) == exp_res

def test_translate_bool_x_error():
    with raises(TypeError):
         Dot(x=False,y=2)

def test_translate_bool_y_error():
    with raises(TypeError):
         Dot(x=2 ,y=True)

def test_translate_str_x_error():
    with raises(TypeError):
         Dot(x="word",y=2)

def test_translate_str_y_error():
    with raises(TypeError):
         Dot(x=2,y="word")