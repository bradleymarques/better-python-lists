from better_python_lists import List


class TestCompact:
    def test_compact_returns_a_list_object(self):
        list_1 = List([1, 2, 3])
        list_2 = list_1.compact()
        assert list_2.__class__ == List

    def test_compact_returns_a_copy_of_the_list_and_not_the_original(self):
        list_1 = List([1, 2, 3])
        list_2 = list_1.compact()
        assert id(list_1) != id(list_2)

    def test_compact_does_not_alter_the_list_if_there_are_no_none_values(self):
        list_1 = List([1, 2, 3])
        list_2 = list_1.compact()
        assert list_2 == List([1, 2, 3])

    def test_compact_removes_none_values_by_default(self):
        list_1 = List([None, 1, None, 2, None, None, 3, None])
        list_2 = list_1.compact()
        assert list_1 == List([None, 1, None, 2, None, None, 3, None])
        assert list_2 == List([1, 2, 3])

    def test_compact_removes_any_elements_passed_in_as_optional_filters(self):
        list_1 = List([None, 1, "None", 2, 0, "", 3, None])
        list_2 = list_1.compact()
        list_3 = list_1.compact(filter_list=[None, "None", "none", "", 0])

        assert list_2 == List([1, "None", 2, 0, "", 3])
        assert list_3 == List([1, 2, 3])

    def test_compacted_returns_none(self):
        list_1 = List([1, 2, 3])
        result = list_1.compacted()
        assert result == None
        assert list_1.__class__ == List

    def test_compacted_does_not_alter_the_list_if_it_does_not_contain_none_elements(
        self,
    ):
        list_1 = List([1, 2, 3])
        list_1.compacted()
        assert list_1 == List([1, 2, 3])

    def test_compacted_removes_none_elements_from_the_original_list(self):
        list_1 = List([None, 1, None, 2, 3, None, None, None])
        list_1.compacted()
        assert list_1 == List([1, 2, 3])

    def test_compacted_removes_any_elements_passed_in_as_optional_filters(self):
        list_1 = List([None, 1, "None", 2, 0, "", 3, None])
        list_1.compacted()
        assert list_1 == List([1, "None", 2, 0, "", 3])
        list_1.compacted(filter_list=["None", "", 0])
        assert list_1 == List([1, 2, 3])
