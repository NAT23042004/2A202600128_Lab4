"""
Shared pytest fixtures and configuration for Lab4 Agent tests
"""

import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

# Add src directory to Python path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path.parent))

# Load environment variables
load_dotenv()


@pytest.fixture(scope="session")
def api_key_available():
    """Check if OpenAI API key is available"""
    return bool(os.getenv("OPENAI_API_KEY"))


@pytest.fixture
def sample_flight_search():
    """Sample flight search parameters"""
    return {"origin": "Hà Nội", "destination": "Đà Nẵng"}


@pytest.fixture
def sample_hotel_search():
    """Sample hotel search parameters"""
    return {"city": "Đà Nẵng", "max_price": 1_500_000}


@pytest.fixture
def sample_budget_calculation():
    """Sample budget calculation parameters"""
    return {"total_budget": 10_000_000, "expenses": "ve_may_bay:1000000,khach_san:2000000"}


@pytest.fixture
def all_cities():
    """List of all available cities in the database"""
    return ["Hà Nội", "Đà Nẵng", "Phú Quốc", "Hồ Chí Minh"]


@pytest.fixture
def all_routes():
    """List of all available flight routes"""
    return [
        ("Hà Nội", "Đà Nẵng"),
        ("Đà Nẵng", "Hà Nội"),
        ("Hà Nội", "Phú Quốc"),
        ("Hồ Chí Minh", "Đà Nẵng"),
        ("Hồ Chí Minh", "Hà Nội"),
        ("Hồ Chí Minh", "Phú Quốc"),
    ]


@pytest.fixture
def hotel_cities():
    """List of cities with hotel information"""
    return ["Đà Nẵng", "Phú Quốc", "Hồ Chí Minh"]
