class TestMath:
    def test_sum(self):
        sum_numbers = lambda a, b: a + b
        assert sum_numbers(2, 5) == 7

    def test_mult(self):
        mult_numbers = lambda a, b: a * b
        assert mult_numbers(3, 5) == 15

    def test_sub(self):
        sub_numbers = lambda a, b: a - b
        assert sub_numbers(4, 2) == 2

    def test_div(self):
        div_numbers = lambda a, b: a / b
        assert div_numbers(10, 4) == 2.5

    def test_sub_more_than_zero(self):
        positive_sub_numbers = lambda a, b: 0 if a - b < 0 else a - b
        assert positive_sub_numbers(1, 3) == 0
        assert positive_sub_numbers(2, 2) == 0
        assert positive_sub_numbers(4, 1) == 3

    def test_integer_div(self):
        integer_div = lambda a, b: a // b
        assert integer_div(5, 2) == 2
