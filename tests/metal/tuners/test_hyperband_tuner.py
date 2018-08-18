import unittest

from metal.tuners.hyperband_tuner import HyperbandTuner


class HyperbandTunerModelTunerTest(unittest.TestCase):
    def test_hyperband_schedule_correctness(self):
        # Test the default schedule that is generated by the hyperband tuner
        # (which at the moment is budget=200, eta=3)
        hyperband_tuner = HyperbandTuner(
            None,
            hyperband_epochs_budget=200,
            hyperband_proportion_discard=3,
            seed=123,
        )
        expected_schedule = [
            [(9, 2), (3, 8), (1, 26)],
            [(3, 8), (1, 26)],
            [(3, 26)],
        ]

        self.assertEqual(hyperband_tuner.hyperband_schedule, expected_schedule)

    def test_hyperband_paper_schedule_correctness(self):
        # Generate the schedule in the hyperband paper
        # (https://arxiv.org/pdf/1603.06560.pdf)
        hyperband_tuner = HyperbandTuner(
            None,
            hyperband_epochs_budget=1701,
            hyperband_proportion_discard=3,
            seed=123,
        )

        # This should generate the exact schedule in the paper.
        expected_schedule = [
            [(81, 1), (27, 3), (9, 9), (3, 27), (1, 81)],
            [(27, 3), (9, 9), (3, 27), (1, 81)],
            [(9, 9), (3, 27), (1, 81)],
            [(6, 27), (2, 81)],
            [(5, 81)],
        ]

        self.assertEqual(hyperband_tuner.hyperband_schedule, expected_schedule)


if __name__ == "__main__":
    unittest.main()
