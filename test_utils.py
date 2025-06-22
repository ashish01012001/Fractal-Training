import pytest
from utils import area_of_circle


def test_area_of_circle():
    """Test the area_of_circle function."""
    # Test with radius 0
    assert area_of_circle(0) == 0.0
    
    # Test with radius 1
    assert area_of_circle(1) == 3.14
    
    # Test with radius 2
    assert area_of_circle(2) == 12.56
    
    # Test with radius 10
    assert area_of_circle(10) == 314.0
    
    # Test with a negative radius (should still return a positive area)
    assert area_of_circle(-5) == 78.5