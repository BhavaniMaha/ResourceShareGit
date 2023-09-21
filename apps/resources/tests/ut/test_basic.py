from django.test import TestCase


# Create your tests here.

class TestBasicCalculation(TestCase):
    # Unit test
    def test_basic_sum(self):
        # Arrange
        x = 1
        y = 4
        expected_output = 5
        
        # Act
        result = x + y
        
        # Assert
        self.assertEqual(result, expected_output)
       