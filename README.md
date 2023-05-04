# Better Python Lists

Makes lists in Python better, by adding some useful methods.

## Installation

`pip install better-python-lists`

## Basic Usage

### Compact

The `compact` method is inspired by
[Ruby's `Array.compact`](https://ruby-doc.org/core-3.0.0/Array.html#method-i-compact).
It removes all `None` elements from the List, returning a copy of the List.

```py
from better_python_lists import List

my_list = List([1, None, 2, 3, 4, None, None, 5])
compact_list = my_list.compact()
print(compact_list)
# => [1, 2, 3, 4, 5]
```

You can also perform in-place compacting using the `compacted` method:

```py
print(my_list)  # => [1, None, 2, 3, 4, None, None, 5]
my_list.compacted()
print(my_list)  # => [1, 2, 3, 4, 5]
```

If you want to filter out more than just `None`, you can pass in an optional filter list:

```py
another_list = List([1, "None", 2, None, 3, "N/A"])
another_list.compacted(filter_list=[None, "None", "N/A"])
print(another_list)  # => [1, 2, 3]
```
