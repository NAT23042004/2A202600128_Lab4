# 🧳 TravelBuddy - AI Travel Planning Agent

**TravelBuddy** is an intelligent Vietnamese travel planning assistant built with LangChain and LangGraph. It helps users find flights, book hotels, and plan their trips within budget using an AI agent powered by GPT-4o-mini.

This is a production-ready implementation of an agentic AI system that demonstrates advanced concepts in multi-tool orchestration, state management, and conversational AI in Vietnamese.

## ✨ Features

- **✈️ Flight Search**: Find flights between major Vietnamese cities with dynamic pricing
- **🏨 Hotel Recommendations**: Browse hotels with budget filtering and star ratings
- **💰 Budget Planning**: Calculate trip costs and provide comprehensive financial recommendations
- **🤖 Multi-step Tool Chaining**: Seamlessly orchestrate complex travel planning queries
- **🇻🇳 Vietnamese-First**: All interactions in Vietnamese with natural, conversational responses  
- **🎯 Intelligent Decision Making**: Agent automatically determines which tools to use and when

## �🚀 Quick Start

### Prerequisites

- Python 3.12+
- OpenAI API key (set in `.env` file)

### Installation

1. **Clone and navigate to the project**
```bash
cd /home/natus/VinAI_ThucChien/assignments/lab4_agent
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 🚀 Running the Application

The agent can be run in multiple ways with the new package structure. Ensure the virtual environment is activated first:

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 🧪 Option 1: Run Tests (Recommended for verification)
```bash
# From project root
pytest test/ -v
```

### 🌐 Option 2: Interactive Web UI (Streamlit)
```bash
# Option A: Using Python module syntax
python3 -m streamlit run src/app/app.py

# Option B: Using PYTHONPATH
export PYTHONPATH=/path/to/lab4_agent:$PYTHONPATH
streamlit run src/app/app.py
```
- Opens at `http://localhost:8501`
- Real-time streaming responses
- Visual tool usage badges
- Conversation history maintained

### 📝 Option 3: Interactive Demo Script
```bash
# Option A: Using Python module syntax
python3 -m src.demo

# Option B: Using PYTHONPATH  
export PYTHONPATH=/path/to/lab4_agent:$PYTHONPATH
python3 src/demo.py
```
- Pre-configured demonstration queries
- Automated showcase of agent capabilities
- All interactions logged to `logs/demo.log`


## 📁 Project Structure

```
lab4_agent/
├── src/                        # Main source package
│   ├── __init__.py
│   ├── agent/
│   │   ├── __init__.py
│   │   └── agent.py            # LangGraph agent orchestration
│   ├── tools/
│   │   ├── __init__.py
│   │   └── tools.py            # Tool implementations (flights, hotels, budget)
│   ├── app/
│   │   ├── __init__.py
│   │   └── app.py              # Streamlit web UI
│   ├── prompt/
│   │   ├── __init__.py
│   │   └── system_prompt.txt   # Agent system prompt & instructions
│   └── demo.py                 # Interactive demo script
│
├── test/                       # Test suite (33 tests, all passing)
│   ├── __init__.py
│   ├── test_agent.py           # Agent graph tests
│   ├── test_tools.py           # Tool implementation tests
│   ├── test_api.py             # API tests
│   └── conftest.py             # Pytest configuration
│
├── requirements.txt            # Python dependencies
├── conftest.py                 # Root pytest config (sets PYTHONPATH)
├── .env                        # Environment variables (create this)
├── logs/                       # Application logs directory
└── README.md
```

## 🔧 Technology Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | OpenAI GPT-4o-mini |
| **Agent Framework** | LangChain + LangGraph |
| **Web UI** | Streamlit |
| **Logging** | Loguru |
| **Testing** | Pytest (33 tests) |
| **Language** | Vietnamese (primary) |

## 📚 Available Tools

### 1. **search_flights(origin, destination)**

Searches for available flights between two Vietnamese cities. Returns comprehensive flight details including airline, departure/arrival times, prices, and cabin class.

**Parameters:**
- `origin` (str): Departure city
- `destination` (str): Arrival city

**Returns:**
- List of flight options with:
  - Airline name
  - Departure and arrival times
  - Price in Vietnamese Dong (VND)
  - Cabin class (economy, business)

**Example:**
```python
search_flights("Hà Nội", "Phú Quốc")
```

**Supported Routes:**
- Hà Nội ↔ Đà Nẵng, Phú Quốc, Hồ Chí Minh
- Hồ Chí Minh ↔ Đà Nẵng, Phú Quốc, Hà Nội
- Đà Nẵng ↔ Hà Nội, Hồ Chí Minh, Phú Quốc
- Phú Quốc ↔ Hà Nội, Hồ Chí Minh, Đà Nẵng

---

### 2. **search_hotels(city, max_price_per_night)**

Finds hotels in a city filtered by budget, sorted by star rating (highest first).

**Parameters:**
- `city` (str): Destination city
- `max_price_per_night` (int): Maximum budget per night in VND

**Returns:**
- List of hotels with:
  - Hotel name
  - Star rating
  - Price per night in VND
  - Available rooms

**Example:**
```python
search_hotels("Phú Quốc", 1_500_000)  # Budget: 1.5M VND/night
```

**Supported Cities:**
- Hà Nội
- Đà Nẵng
- Phú Quốc
- Hồ Chí Minh

---

### 3. **calculate_budget(total_budget, expenses)**

Calculates remaining budget after expenses and provides a detailed breakdown.

**Parameters:**
- `total_budget` (int): Total budget in VND
- `expenses` (str): Comma-separated breakdown as `category:amount` pairs

**Returns:**
- Dictionary with:
  - Total budget
  - Total expenses
  - Remaining budget
  - Expense breakdown

**Example:**
```python
calculate_budget(5_000_000, "ve_may_bay:890_000,khach_san:650_000")
```

**Common Expense Categories:**
- `ve_may_bay` - Flight tickets
- `khach_san` - Hotel accommodation
- `an_uong` - Food and drinks
- `hoat_dong` - Activities
- `di_chuyen` - Transportation

## 🧪 Testing

### Run All Tests
```bash
# Make sure you're in the virtual environment first
source venv/bin/activate

# Run all tests
pytest test/ -v
```

### Run Specific Test Class
```bash
pytest test/test_tools.py::TestSearchFlights -v
pytest test/test_agent.py::TestAgentGraph -v
```

### Test Coverage
- **Agent Tests**: 11 tests (graph compilation, state management, tool integration)
- **Tool Tests**: 22 tests (flights, hotels, budget calculations, error handling)
- **Total**: 33 tests, all passing ✅

### Common Test Issues

**Issue: "ModuleNotFoundError: No module named 'langchain_core'"**
```bash
# This happens when running pytest outside the virtual environment
# Solution: Activate the virtual environment first
source venv/bin/activate
pytest test/ -v
```

**Issue: Tests won't run in VS Code**
1. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Select "Python: Select Interpreter"
3. Choose the one in `./venv/bin/python`
4. Now run tests with Ctrl+Shift+D

## 🐛 Troubleshooting

### "ModuleNotFoundError" (langchain_core, langchain_openai, etc.)

**Problem:** Running `pytest -v` gives import errors

**Root Cause:** Dependencies are not installed in your active Python environment

**Solution:** Use the virtual environment:
```bash
# Create virtual environment (if not exists)
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Now run tests
pytest test/ -v
```

**To verify you're in the virtual environment:**
- Your terminal prompt should show `(venv)` prefix
- Run: `which python` → should show a path containing `venv/bin/python`

### "OpenAI API Key not found"
```bash
# Create .env file in project root
echo "OPENAI_API_KEY=your_actual_key_here" > .env
```

### Tests failing sporadically
```bash
# Run with more verbose output
pytest test/ -vv --tb=long

# Run specific test file
pytest test/test_tools.py -v

# Run with output capture disabled
pytest test/ -v -s
```

### Streamlit app not loading
```bash
# Ensure port 8501 is free or use different port
# Using Python module syntax
python3 -m streamlit run src/app/app.py --server.port 8502

# Or with PYTHONPATH
export PYTHONPATH=$(pwd):$PYTHONPATH
streamlit run src/app/app.py --server.port 8502
```

### ImportError when running scripts directly
```bash
# Problem: "ModuleNotFoundError: No module named 'src'"
# Solution: Set PYTHONPATH before running

# Option 1: Set PYTHONPATH (recommended)
export PYTHONPATH=$(pwd):$PYTHONPATH
python3 src/demo.py

# Option 2: Use Python module syntax
python3 -m src.demo

# Option 3: Run from project root with -m flag
python3 -m pytest test/ -v
```

### Agent not calling tools
1. Verify system prompt is loaded:
```bash
export PYTHONPATH=$(pwd):$PYTHONPATH
python3 -c "from src.agent.agent import SYSTEM_PROMPT; print(SYSTEM_PROMPT[:100])"
```
2. Check `tools_list` in `src/agent/agent.py` contains all your tools
3. Verify tools are bound: `llm_with_tools = llm.bind_tools(tools_list)`
4. Review logs (`logs/demo.log` or `logs/app.log`) for detailed execution

### Budget calculation seems wrong
- Verify expense format: `category1:amount1,category2:amount2`
- All amounts should be in VND
- Check that amounts match tool results



### Example 1: Simple Flight Search
```
User: "Tìm chuyến bay từ Hà Nội đến Phú Quốc vào ngày mai"

Agent:
  [🔍 Calls: search_flights("Hà Nội", "Phú Quốc")]
  
  "Dạ, em tìm được các chuyến bay từ Hà Nội đến Phú Quốc:

  ✈️ **Vietnam Airlines**
     🕖 Khởi hành 07:00 → Đến 09:15
     💰 2,100,000 VND (Hạng V)

  ✈️ **VietJet Air** (Rẻ nhất! 🎉)
     🕖 Khởi hành 10:00 → Đến 12:15
     💰 1,350,000 VND (Hạng V)

  ✈️ **Bamboo Airways**
     🕖 Khởi hành 14:30 → Đến 16:45
     💰 1,600,000 VND (Hạng V)
     
  Chuyến nào em thích nhất?"
```

### Example 2: Hotel Search with Budget
```
User: "Giúp em tìm khách sạn ở Đà Nẵng, ngân sách dưới 2 triệu một đêm"

Agent:
  [🔍 Calls: search_hotels("Đà Nẵng", 2_000_000)]
  
  "Dạ em có các khách sạn phù hợp ở Đà Nẵng:

  🏨 **Riviel Danang** ⭐⭐⭐⭐⭐
      💰 1,850,000 VND/đêm
      🏊 Có hồ bơi, view biển

  🏨 **Sandy Beach Hotel** ⭐⭐⭐⭐
      💰 1,500,000 VND/đêm
      🍽️ Bao gồm ăn sáng

  🏨 **Coastland Central** ⭐⭐⭐⭐
      💰 1,200,000 VND/đêm
      📍 Gần trung tâm thành phố
      
  Em thích loại nào?"
```

### Example 3: Complete Trip Planning (Multi-step)
```
User: "Em muốn từ Hà Nội đi Phú Quốc 3 ngày 2 đêm, ngân sách 10 triệu. Tư vấn giúp em!"

Agent:
  [Step 1: 🔍 Searching flights...]
  [Step 2: 🔍 Searching hotels...]
  [Step 3: 💰 Calculating budget...]
  
  "Dạ em có gợi ý hoàn hảo cho chuyến đi Phú Quốc của em:

  **✈️ CHUYẾN BAY:** VietJet Air
      🕖 Hà Nội 10:00 → Phú Quốc 12:15
      💰 1,350,000 VND (rẻ nhất!)

  **🏨 KHÁCH SẠN:** Sandy Beach Resort ⭐⭐⭐⭐⭐
      💰 2,000,000 VND/đêm × 2 = 4,000,000 VND

  **💳 TỔNG CHI PHÍ:**
      ✈️ Vé máy bay:     1,350,000 VND
      🏨 Khách sạn:      4,000,000 VND
      ─────────────────────────────
      💰 Tổng:           5,350,000 VND
      
      📊 Ngân sách còn lại: 4,650,000 VND ✅

  **💡 GỢI Ý:**
      - Dành ~2 triệu cho ăn uống
      - Dành ~1.5 triệu cho hoạt động (lặn, tour...)
      - Còn lại cho các phụ phí"
```

### Example 4: Off-Topic Rejection
```
User: "Giải giúp em bài tập lập trình Python về linked list"

Agent:
  "Xin lỗi bạn, em chỉ chuyên hỗ trợ về du lịch thôi. 
   Bạn có cần tư vấn chuyến đi nào không? 
   Em sẽ giúp bạn tìm vé máy bay, khách sạn, và kế hoạch du lịch tốt nhất! 🌍✈️"
```

## 📝 Usage Examples

### Via Web UI (Recommended)
1. Run `streamlit run app.py`
2. Type your travel planning query in Vietnamese
3. View results with tool badges showing which tools were used
4. Logs saved to `logs/app.log`

### Via Demo Script
```bash
python demo.py
```
Demonstrations include:
- Flight search queries
- Hotel browsing
- Complete trip planning scenarios
- Budget calculations



## 📋 Available Response Modes

### Chat Interface (app.py)
- Real-time streaming responses
- Tool usage tracking with visual badges
- Conversation history
- Responsive Streamlit UI

### Demo Mode (demo.py)
- Pre-configured test queries
- Automated demonstrations
- Logging of all interactions
- Perfect for showcasing capabilities

### CLI Mode (agent.py)
- Interactive terminal-based chat
- Direct agent communication
- Detailed logging output
- Manual query testing

## 🔍 Logging

Logs are stored in multiple locations:
- **App logs**: `logs/app.log` (when running Streamlit)
- **Demo logs**: `logs/demo.log` (when running demo.py)

All logs include:
- Timestamps
- Log levels (DEBUG, INFO, WARNING, ERROR)
- Function names and line numbers
- Tool invocation details
