import unittest
import sys
from io import StringIO

class TestAux(unittest.TestCase):

    # Captures functions output
    def capture_output(function, *args):
        captured_output = StringIO()
        sys.stdout = captured_output
        function(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_something(self):
        pass
    
if __name__ == '__main__':
    unittest.main()