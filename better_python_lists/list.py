from __future__ import annotations


class List(list):
    def compact(self, filter_list: list = [None]) -> List:
        """
        Removes None elements from the List (by default), returning a new List.

        Parameters
        ----------
        filter_list : list, optional
            Elements to remove from the List

        Returns
        -------
        A copy of the original List object, with None values removed
        """
        return List(e for e in self if e not in filter_list)

    def compacted(self, filter_list: list = [None]) -> None:
        """
        Removes None elements from the List (by default) performing in-place
        filtering.

        Parameters
        ----------
        filter_list : list, optional
            Elements to remove from the List

        Returns
        -------
        None
        """
        self[:] = self.compact(filter_list=filter_list)

    def flatten(self) -> List:
        """
        Flattens an arbitrarily nested list into a single-level one, returning
        this as a copy.

        Returns
        -------
        A flattened copy of the original List object.
        """
        return List(
            [
                subelement
                for element in self
                for subelement in (
                    List(element).flatten()
                    if isinstance(element, (list, tuple))
                    else [element]
                )
            ]
        )

    def flattened(self) -> None:
        """
        Flattens an arbitrarily nested list into a single-level one, performing
        in-place replacement.

        Returns
        -------
        None
        """
        self[:] = self.flatten()
