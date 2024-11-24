from main import add


def test_add():
    """testing out add function"""
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    print("hello")


def test_add2():
    """testing out add function"""
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    assert add(1, 2) == 3


if __name__ == "__main__":
    test_add()
