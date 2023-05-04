from better_python_lists import List


class TestFlatten:
    def test_flatten_returns_a_copy_of_the_list_object(self):
        list_1: List = List([1, 2, 3])
        list_2: List = list_1.flatten()
        assert list_2.__class__ == List
        assert id(list_1) != id(list_2)

    def test_flatten_returns_the_same_list_if_it_was_already_flat(self):
        list_1: List = List([1, 2, 3])
        list_2: List = list_1.flatten()
        assert list_2 == List([1, 2, 3])

    def test_flatten_returns_an_empty_list_if_the_input_is_empty(self):
        list_1: List = List([])
        list_2: List = list_1.flatten()
        assert list_2 == List([])

    def test_flatten_flattens_a_list_with_double_nesting(self):
        the_list: List = List([["a"], ["b"]])
        assert the_list.flatten() == List(["a", "b"])

    def test_flatten_flattens_a_list_of_multiple_different_levels_of_nesting(self):
        the_list: List = List([["a"], "b", 5, [6, 7, [8, 9, [10]]]])
        assert the_list.flatten() == List(["a", "b", 5, 6, 7, 8, 9, 10])

    def test_flatten_ignores_empty_elements(self):
        the_list: List = List([[[]], [[], []], [[], [[], []]]])
        assert the_list.flatten() == List([])

    def test_flatten_does_not_break_dictionaries_apart(self):
        the_list: List = List([{"a": 1}, {"b": 2}, [3, 4, [5], {"c": 6, "d": 7}]])
        assert the_list.flatten() == [{"a": 1}, {"b": 2}, 3, 4, 5, {"c": 6, "d": 7}]

    def test_flattened_modifies_the_original_list_and_returns_none(self):
        the_list: List = List([1, [2, [3]]])
        result = the_list.flattened()
        assert result is None
        assert the_list == List([1, 2, 3])
