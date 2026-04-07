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
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 've_may_bay:1100000'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1950000})
Trả lời trực tiếp

TravelBuddy: Dưới đây là những gợi ý cho chuyến đi của bạn từ Hà Nội đến Phú Quốc trong 2 đêm với ngân sách 5 triệu:

**Chuyến bay:**
- **Hãng:** VietJet Air
- **Giờ khởi hành:** 16:00
- **Giờ đến nơi:** 18:15
- **Giá:** 1,100,000 VND

**Khách sạn:**
- **Tên:** Sunset Palms
  - **Tầm giá:** 1,500,000 VND/đêm
  - **Tại sao chọn nơi này:** Khách sạn có đánh giá 4 sao, cung cấp các tiện ích tốt và gần bãi biển. Rất phù hợp cho việc thư giãn và vui chơi!

**Phân tích ngân sách:**
- **Chi phí vé máy bay:** 1,100,000 VND
- **Chi phí khách sạn (2 đêm):** 3,000,000 VND  (1,500,000 VND x 2 đêm)
- **Tổng chi:** 4,100,000 VND
- **Ngân sách còn lại sau chi tiêu:** 900,000 VND

Bạn vẫn còn 900,000 VND để sử dụng cho ăn uống và tham quan tại Phú Quốc. 

**Gợi ý thêm:**
- Bạn có thể thử các món hải sản tươi ngon tại các nhà hàng ven biển.
- Tham quan các địa điểm nổi tiếng như Vinpearl Land, Bãi Sao hay khám phá hệ sinh thái của Vinpearl Safari.
- Tham gia các hoạt động thể thao biển như lặn ngắm san hô hoặc đi tàu đáy kính.

Nếu bạn đồng ý với kế hoạch này, mình có thể giúp bạn đặt vé máy bay và khách sạn luôn nhé!

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
