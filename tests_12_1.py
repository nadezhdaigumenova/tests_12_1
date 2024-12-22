import classRun
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = classRun.Runner('Nadya')
        for i in  range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = classRun.Runner('Vlad')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = classRun.Runner('Shura')
        runner_4 = classRun.Runner('Vova')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

    if __name__ == '__main__':
        unittest.main()




