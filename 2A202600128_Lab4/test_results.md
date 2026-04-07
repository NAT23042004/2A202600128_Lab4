Test 1 – Direct Answer (Không cần tool)

Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt khi bạn đang có dự định đi du lịch. Bạn đã có nơi nào trong tâm trí chưa? Hay bạn muốn mình gợi ý một vài điểm đến? Ngoài ra, cho mình biết thêm về ngân sách, thời gian và sở thích của bạn nhé!

Test 2 – Single Tool Call

Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy: Dưới đây là các chuyến bay từ Hà Nội đi Đà Nẵng mà mình tìm được:

1. **VietJet Air**
   - Khởi hành: 08:30
   - Đến nơi: 09:50
   - Giá: **890,000 VND** (hạng economy) - **Vé rẻ nhất!**

2. **Bamboo Airways**
   - Khởi hành: 11:00
   - Đến nơi: 12:20
   - Giá: 1,200,000 VND (hạng economy)

3. **Vietnam Airlines**
   - Khởi hành: 06:00
   - Đến nơi: 07:20
   - Giá: 1,450,000 VND (hạng economy)

4. **Vietnam Airlines**
   - Khởi hành: 14:00
   - Đến nơi: 15:20
   - Giá: 2,800,000 VND (hạng business)

Nếu bạn cần thêm thông tin hoặc muốn đặt vé, hãy cho mình biết nhé!

Test 3 – Multi-Step Tool Chaining

Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 've_may_bay:1350000,khach_san:3000000'})
Trả lời trực tiếp

TravelBuddy: Dưới đây là thông tin chi tiết cho chuyến đi của bạn từ Hà Nội đến Phú Quốc:

**Chuyến bay:**
1. **VietJet Air**
   - Khởi hành: 10:00
   - Đến nơi: 12:15
   - Giá: 1,350,000 VND (vé rẻ nhất)

2. **VietJet Air**
   - Khởi hành: 16:00
   - Đến nơi: 18:15
   - Giá: 1,100,000 VND

3. **Vietnam Airlines**
   - Khởi hành: 07:00
   - Đến nơi: 09:15
   - Giá: 2,100,000 VND

**Khách sạn:**
1. **Sunset Palms**
   - Rating: 4 sao
   - Giá một đêm: 1,500,000 VND

2. **Bai Truong**
   - Rating: 4 sao
   - Giá một đêm: 1,500,000 VND

3. **Duong Kong**
   - Rating: 4 sao
   - Giá một đêm: 200,000 VND

4. **Island Resort**
   - Rating: 3 sao
   - Giá một đêm: 800,000 VND

5. **Station Hostel**
   - Rating: 3 sao
   - Giá một đêm: 200,000 VND

Chồng bạn đã chọn khách sạn **Sunset Palms** hoặc **Bai Truong** cho 2 đêm với chi phí 3 triệu VND.

**Tổng chi phí ước tính:**
- Vé máy bay: 1,350,000 VND
- Khách sạn (2 đêm): 3,000,000 VND
- **Tổng:** 4,350,000 VND
- **Ngân sách còn lại:** 650,000 VND

**Gợi ý thêm:** Tại Phú Quốc, bạn có thể tham gia các hoạt động như lặn ngắm san hô, tham quan Vinpearl Safari, hay thư giãn tại các bãi biển tuyệt đẹp như Bãi Sao, Bãi Dài. Bạn cũng đừng quên thưởng thức hải sản tươi ngon!

Nếu bạn cần đặt vé hoặc có thêm câu hỏi nào, cứ cho mình biết nhé!

Test 4 – Missing Info / Clarification

Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Để mình giúp bạn đặt khách sạn, bạn cung cấp thêm cho mình một số thông tin nhé:

1. Thành phố nào bạn muốn đặt khách sạn?
2. Bạn sẽ ở bao nhiêu đêm?
3. Ngân sách của bạn cho mỗi đêm là bao nhiêu? 

Mình sẽ tìm cho bạn những lựa chọn phù hợp!

Test 5 – Guardrail / Refusal

Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Xin lỗi, mình chỉ chuyên hỗ trợ về du lịch. Bạn có cần tư vấn chuyến đi nào không?
