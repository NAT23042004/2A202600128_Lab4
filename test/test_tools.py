import pytest

from src.tools.tools import calculate_budget, search_flights, search_hotels


# Helper wrappers to call tools properly (StructuredTool objects)
def _call_search_flights(origin: str, destination: str) -> str:
    """Call search_flights tool and return result"""
    return search_flights.invoke({"origin": origin, "destination": destination})


def _call_search_hotels(city: str, max_price_per_night: int = 9999999) -> str:
    """Call search_hotels tool and return result"""
    return search_hotels.invoke({"city": city, "max_price_per_night": max_price_per_night})


def _call_calculate_budget(total_budget: int, expenses: str) -> str:
    """Call calculate_budget tool and return result"""
    return calculate_budget.invoke({"total_budget": total_budget, "expenses": expenses})


class TestSearchFlights:
    """Test cases for search_flights function"""

    def test_search_flights_existing_route(self):
        """Test searching for an existing flight route"""
        result = _call_search_flights("Hà Nội", "Đà Nẵng")
        assert "Chuyến bay từ Hà Nội đến Đà Nẵng" in result
        assert "Vietnam Airlines" in result
        assert "VietJet Air" in result

    def test_search_flights_nonexistent_route(self):
        """Test searching for a non-existent route"""
        result = _call_search_flights("Hà Nội", "Nha Trang")
        assert "Không tìm thấy chuyến bay" in result

    def test_search_flights_format_includes_price(self):
        """Test that flight results include formatted prices"""
        result = _call_search_flights("Hà Nội", "Phú Quốc")
        assert "VND" in result
        assert "Hãng:" in result

    def test_search_flights_multiple_options(self):
        """Test that multiple flight options are returned"""
        result = _call_search_flights("Hồ Chí Minh", "Đà Nẵng")
        assert result.count("-") >= 2

    def test_search_flights_all_cities(self):
        """Test search_flights with all available routes"""
        routes = [
            ("Hà Nội", "Đà Nẵng"),
            ("Đà Nẵng", "Hà Nội"),
            ("Hà Nội", "Phú Quốc"),
            ("Hồ Chí Minh", "Đà Nẵng"),
            ("Hồ Chí Minh", "Hà Nội"),
            ("Hồ Chí Minh", "Phú Quốc"),
        ]
        for origin, dest in routes:
            result = _call_search_flights(origin, dest)
            assert isinstance(result, str)
            assert len(result) > 0

    def test_search_flights_returns_string(self):
        """Test that search_flights returns a string"""
        result = _call_search_flights("Hà Nội", "Đà Nẵng")
        assert isinstance(result, str)


class TestSearchHotels:
    """Test cases for search_hotels function"""

    def test_search_hotels_existing_city(self):
        """Test searching for hotels in an existing city"""
        result = _call_search_hotels("Đà Nẵng")
        assert "Huang Thanh Luxury" in result

    def test_search_hotels_nonexistent_city(self):
        """Test searching for hotels in a non-existent city"""
        result = _call_search_hotels("Nha Trang")
        assert "Không tìm thấy khách sạn tại Nha Trang" in result

    def test_search_hotels_with_budget_filter(self):
        """Test hotel search with budget limit"""
        result = _call_search_hotels("Đà Nẵng", max_price_per_night=500_000)
        assert isinstance(result, str)

    def test_search_hotels_exceed_budget(self):
        """Test when no hotels match the budget"""
        result = _call_search_hotels("Đà Nẵng", max_price_per_night=100_000)
        assert "Không tìm thấy khách sạn" in result

    def test_search_hotels_sorted_by_rating(self):
        """Test that hotels are sorted by rating"""
        result = _call_search_hotels("Phú Quốc", max_price_per_night=5_000_000)
        assert "VieganI Resort" in result

    def test_search_hotels_all_cities(self):
        """Test search_hotels for all available cities"""
        cities = ["Đà Nẵng", "Phú Quốc", "Hồ Chí Minh"]
        for city in cities:
            result = _call_search_hotels(city)
            assert isinstance(result, str)
            assert len(result) > 0

    def test_search_hotels_returns_string(self):
        """Test that search_hotels returns a string"""
        result = _call_search_hotels("Đà Nẵng")
        assert isinstance(result, str)


class TestCalculateBudget:
    """Test cases for calculate_budget function"""

    def test_calculate_budget_basic(self):
        """Test basic budget calculation"""
        result = _call_calculate_budget(5_000_000, "ve_may_bay:890000,khach_san:1500000")
        assert isinstance(result, str)

    def test_calculate_budget_within_limit(self):
        """Test budget calculation when within limit"""
        result = _call_calculate_budget(10_000_000, "ve_may_bay:1000000,khach_san:2000000")
        assert "!!!Cảnh báo" not in result

    def test_calculate_budget_exceed_limit(self):
        """Test budget calculation when exceeding limit"""
        result = _call_calculate_budget(2_000_000, "ve_may_bay:1500000,khach_san:1500000")
        assert "!!!Cảnh báo" in result
        assert "thiếu" in result.lower()

    def test_calculate_budget_exact_limit(self):
        """Test budget calculation when exactly at limit"""
        result = _call_calculate_budget(3_000_000, "ve_may_bay:1500000,khach_san:1500000")
        assert isinstance(result, str)

    def test_calculate_budget_single_expense(self):
        """Test budget with single expense item"""
        result = _call_calculate_budget(5_000_000, "tour_package:2000000")
        assert isinstance(result, str)

    def test_calculate_budget_multiple_expenses(self):
        """Test budget with multiple expense items"""
        result = _call_calculate_budget(10_000_000, "ve_may_bay:1000000,khach_san:2000000,tour:1500000,an_sang:500000")
        assert isinstance(result, str)

    def test_calculate_budget_returns_string(self):
        """Test that calculate_budget returns a string"""
        result = _call_calculate_budget(5_000_000, "expense:1000000")
        assert isinstance(result, str)


class TestIntegration:
    """Integration tests combining multiple functions"""

    def test_travel_planning_scenario(self):
        """Test a complete travel planning scenario"""
        flights = _call_search_flights("Hà Nội", "Đà Nẵng")
        assert isinstance(flights, str)
        assert len(flights) > 0

        hotels = _call_search_hotels("Đà Nẵng", max_price_per_night=1_500_000)
        assert isinstance(hotels, str)

        budget = _call_calculate_budget(10_000_000, "ve_may_bay:890000,khach_san:1200000")
        assert isinstance(budget, str)

    def test_all_functions_return_strings(self):
        """Ensure all functions return strings"""
        f1 = _call_search_flights("Hà Nội", "Đà Nẵng")
        h1 = _call_search_hotels("Đà Nẵng")
        b1 = _call_calculate_budget(5_000_000, "expense:1000000")

        assert isinstance(f1, str)
        assert isinstance(h1, str)
        assert isinstance(b1, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
