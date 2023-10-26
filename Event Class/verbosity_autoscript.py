import unittest

# Import your test module here
from event_unittest import TestEventClass  

if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEventClass)

    # Create a TextTestRunner with the '-v' option
    runner = unittest.TextTestRunner(verbosity=2)

    # Run the tests with verbosity
    result = runner.run(suite)

    # Exit with an appropriate exit code based on test results
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
