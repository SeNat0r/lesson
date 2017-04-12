import unittest
import time
import os

# class TestIO(unittest.TestCase):
#     def setUp(self):
#         """Выполняется при инициализации тестов"""
#         self.filename = '{}_test.txt.tmp'.format(time.time())
#
#     def tearDown(self):
#         """Выполняется при завершении теста"""
#         os.remove(self.filename)
#
#     def test_write(self):
#         with open(self.filename, 'w') as f:
#             f.write('1234')
#
#         with open(self.filename, 'r') as f:
#             self.assertEqual(f.read(), '123')

from battleships import Ship, Field


class TestBattleShips(unittest.TestCase):
    def test_create_coords(self):
        ship = Ship(4, 0, 0)

        self.assertListEqual(list(ship.coords()), [(0, 0), (0, 1), (0, 2), (0, 3)], 'Координаты не выерные')

    # def test_check_pos(self):
    #     ship = Ship(1, 0, 0)
    #     field = Field(10, 10)
    #
    #     status = field.add_ship(ship)
    #
    #     self.assertTrue(status, 'Корабль не добавлен')
    #
    #     ship2 = Ship(2, 1, 1)
    #     status = field.add_ship(ship2)
    #
    #     self.assertFalse(status, 'Почему-то добавился в поле')

    def test_shoot(self):
        ship = Ship(4, 1, 2, 1)

        field = Field(10, 10)

        field.add_ship(ship)
        state, points = field.attack(0, 0)

        self.assertEqual(state, Field.SHOT_MISSED, 'Мы не хотели')

        state, points = field.attack(1, 2)

        self.assertEqual(state, Field.SHOT_INJURED, 'Что-то пошло не так')





if __name__ == '__main__':
    unittest.main()
