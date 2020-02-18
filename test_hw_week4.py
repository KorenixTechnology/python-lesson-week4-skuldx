from hw_week4 import hw_week4


def test_condition1(capsys):
    hw_week4('Alice', 12)
    captured = capsys.readouterr()
    expect_output = 'Hi, Alice.\n'
    assert captured.out == expect_output


def test_condition2(capsys):
    hw_week4('Clark', 11)
    captured = capsys.readouterr()
    expect_output = 'You are not Alice, kiddo.\n'
    assert captured.out == expect_output


def test_condition3(capsys):
    hw_week4('Clark', 3000)
    captured = capsys.readouterr()
    expect_output = 'Unlike you, Alice is not an undead, immortal vampire.\n'
    assert captured.out == expect_output


def test_condition4(capsys):
    hw_week4('Clark', 150)
    captured = capsys.readouterr()
    expect_output = 'You are not Alice, grannie.\n'
    assert captured.out == expect_output
