# https://docs.python.org/3/library/unittest.html

from solver import *
import unittest

class TestSolver(unittest.TestCase):
  def test_init(self):
    s1 = Solver([1, 2])
    self.assertEqual(s1.data, [1, 2])
    self.assertIsNone(s1.cnt)

    s2 = Solver()
    self.assertIsNone(s2.data)
    self.assertIsNone(s2.cnt)


  def test_set_cnt(self):
    s1 = Solver([1, 2, 3])
    s1.set_cnt()
    self.assertEqual(s1.cnt[1:4], [1, 1, 1])
    self.assertEqual(sum(s1.cnt), 3)

    s2 = Solver([])
    s2.set_cnt()
    self.assertEqual(s2.cnt, [0] * (DESIRED_SUM + 1))

    s3 = Solver([0] * 100 + [12] * 100)
    s3.set_cnt()
    self.assertEqual([100] + ((DESIRED_SUM - 1) * [0]) + [100], s3.cnt)

  def change_order_of_pairs(self, l):
    result = []
    for x, y in l:
      result.append((min(x, y), max(x, y))) # tutaj wpycham pary jako tuple a nie jako listy

    return result

  def is_the_same_result(self, r1, r2):
    r1 = self.change_order_of_pairs(r1)
    r2 = self.change_order_of_pairs(r2)
    return sorted(r1) == sorted(r2)

  def test_set_result(self):
    s1 = Solver([1, 2, 3])
    s1.set_result()
    self.is_the_same_result(s1.result, [])

    s2 = Solver([1, 11, 2, 10])
    s2.set_result()
    self.is_the_same_result(s2.result, [[11, 1], [2, 10]])


if __name__ == '__main__':
    unittest.main()