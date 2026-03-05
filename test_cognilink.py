# test_cognilink.py
"""
Tests for CogniLink module.
"""

import unittest
from cognilink import CogniLink

class TestCogniLink(unittest.TestCase):
    """Test cases for CogniLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CogniLink()
        self.assertIsInstance(instance, CogniLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CogniLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
