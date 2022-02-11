from unittest import TestCase

from iterator import IterableObject, shell_sort, _filter


class Tests(TestCase):

    def setUp(self) -> None:
        self.__iterObj = IterableObject()
        self.__iterObj.add("Iulia")
        self.__iterObj.add("Oana")
        self.__iterObj.add("Razvan")

    def test_iterable(self):

        for obj in self.__iterObj:
            self.assertIn(obj, ['Iulia', 'Oana', 'Razvan'])

        self.assertEqual(self.__iterObj[0], 'Iulia')
        self.assertEqual(self.__iterObj[1], 'Oana')
        self.assertEqual(self.__iterObj[2], 'Razvan')

        self.__iterObj[2] = 'Ioana'
        self.assertEqual(self.__iterObj[0], 'Iulia')
        self.assertEqual(self.__iterObj[1], 'Oana')
        self.assertEqual(self.__iterObj[2], 'Ioana')

        del self.__iterObj[0]
        del self.__iterObj[0]
        del self.__iterObj[0]

        self.assertEqual(len(self.__iterObj), 0)

    @staticmethod
    def sort_key_0(a, b):
        return a[len(a) - 2] < b[len(b) - 2]

    def test_sort(self):
        shell_sort(self.__iterObj, self.sort_key_0)
        self.assertEqual(self.__iterObj[0], 'Razvan')
        self.assertEqual(self.__iterObj[1], 'Iulia')
        self.assertEqual(self.__iterObj[2], 'Oana')

    @staticmethod
    def _condition(v):
        return v.lower() != 'razvan'

    def test_filter(self):
        _filter(self.__iterObj, self._condition)
        self.assertEqual(self.__iterObj[0], 'Iulia')
        self.assertEqual(self.__iterObj[1], 'Oana')