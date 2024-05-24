from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 6
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 12
        assert result == expected

    def test_divide(self):
        # arrange
        a = 8
        b = 4
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 2
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 9
        b = 0
        cal = Calculator()

        # act and assert
        try:
            cal.divide(a, b)
        except ZeroDivisionError as e:
            assert str(e) == "Division by zero error"
