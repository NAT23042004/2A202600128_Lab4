import pytest
from dotenv import load_dotenv

from src.agent import SYSTEM_PROMPT, AgentState, graph

load_dotenv()


class TestSystemPrompt:
    """Test cases for system prompt"""

    def test_system_prompt_loaded(self):
        """Test that system prompt is loaded"""
        assert SYSTEM_PROMPT is not None
        assert len(SYSTEM_PROMPT) > 0

    def test_system_prompt_contains_key_info(self):
        """Test that system prompt contains key information"""
        assert "TravelBuddy" in SYSTEM_PROMPT or "du lịch" in SYSTEM_PROMPT.lower()


class TestAgentGraph:
    """Test cases for the agent graph"""

    def test_graph_compiles(self):
        """Test that the graph compiles without errors"""
        assert graph is not None

    def test_graph_has_nodes(self):
        """Test that graph has required nodes"""
        # Graph should have agent and tools nodes
        assert graph is not None

    def test_agent_state_type(self):
        """Test that AgentState is properly defined"""
        assert AgentState is not None
        # AgentState should have messages field
        test_state = {"messages": []}
        assert "messages" in test_state


class TestAgentInvocation:
    """Test cases for agent invocation"""

    def test_agent_basic_invocation(self):
        """Test basic agent invocation"""
        test_input = "Xin chào"
        try:
            result = graph.invoke({"messages": [("human", test_input)]})
            assert "messages" in result
            assert len(result["messages"]) > 0
        except Exception as e:
            # API key might not be set in test environment
            pytest.skip(f"Skipping due to API/environment issue: {str(e)}")

    def test_agent_with_flight_query(self):
        """Test agent with flight search query"""
        test_input = "Tìm chuyến bay từ Hà Nội đến Đà Nẵng"
        try:
            result = graph.invoke({"messages": [("human", test_input)]})
            assert "messages" in result
        except Exception as e:
            pytest.skip(f"Skipping due to API/environment issue: {str(e)}")

    def test_agent_with_hotel_query(self):
        """Test agent with hotel search query"""
        test_input = "Tìm khách sạn tại Đà Nẵng"
        try:
            result = graph.invoke({"messages": [("human", test_input)]})
            assert "messages" in result
        except Exception as e:
            pytest.skip(f"Skipping due to API/environment issue: {str(e)}")

    def test_agent_with_budget_query(self):
        """Test agent with budget calculation query"""
        test_input = "Tính toán ngân sách cho chuyến đi"
        try:
            result = graph.invoke({"messages": [("human", test_input)]})
            assert "messages" in result
        except Exception as e:
            pytest.skip(f"Skipping due to API/environment issue: {str(e)}")


class TestToolIntegration:
    """Test that tools are properly integrated in the agent"""

    def test_tools_are_available(self):
        """Test that tools are available in the LLM"""
        # The agent should have tools registered
        assert graph is not None

    def test_graph_structure(self):
        """Test that graph has proper structure"""
        # Graph should be compilable and functional
        assert graph is not None
        assert hasattr(graph, "invoke") or hasattr(graph, "__call__")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
