class TestLists:
    def default_list_from_test(self, start=0, end=11):
        return [x for x in range(start, end)]

    def test_positive_numbers(self):
        list_obj = self.default_list_from_test(1, 15)
        assert 5 in list_obj

    def test_last_item(self):
        items = self.default_list_from_test()
        last_item = lambda items: items[len(items) - 1]
        assert last_item(items) == 10

    def test_first_item(self):
        items = self.default_list_from_test()
        first_item = lambda items: items[0]
        assert first_item(items) == 0

    def test_all_items_positive(self):
        items = self.default_list_from_test(start=1, end=9)
        all_is_positive = all(items) >= 0
        assert all_is_positive is True

    def test_is_a_list(self):
        items = self.default_list_from_test()
        assert isinstance(items, list) is True

class TestDict:
    def default_dict_from_test(self):
        person = {
            "name": "Test",
            "last_name": "Python"
        }
        return person

    def test_keys_from_dict(self):
        keys = self.default_dict_from_test().keys()
        keys = tuple(keys)
        assert 'name' in keys
