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

        Parameters
        ----------
        filter_list : list, optional
            Elements to remove from the List

        Returns
        -------
        None
        """
        self[:] = [e for e in self if e not in filter_list]
