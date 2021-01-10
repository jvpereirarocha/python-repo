class TestStrings:
    def test_last_character(self):
        last_character = lambda text: text[-1]
        assert last_character("Hello") == 'o'

    def test_first_character(self):
        first_character = lambda text: text[0]
        assert first_character("hi") == "h"

    def test_low_text(self):
        low_text = lambda text: text.lower()
        assert low_text("TEST") == "test"

    def test_upper_text(self):
        upper_text = lambda text: text.upper()
        assert upper_text("hello") == "HELLO"
