import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_shipping_rate(method: str, distance: int) -> float:
    
    if not isinstance(distance, (int, float)):
        raise TypeError("Khoảng cách phải là một số (int hoặc float).")
    
    if distance <= 0:
        raise ValueError("Khoảng cách vận chuyển bắt buộc phải lớn hơn 0.")
        
    valid_methods = {"standard", "express", "next_day"}
    if method not in valid_methods:
        raise ValueError(f"Phương thức vận chuyển '{method}' không hợp lệ. Chỉ chấp nhận: {valid_methods}")

    logger.info(f"Đang tính phí giao hàng cho phương thức '{method}' với khoảng cách {distance} km")
    
    if method == "standard":
        base_rate = 15000.0
    elif method == "express":
        base_rate = 30000.0
    else:  
        base_rate = 50000.0
        
    if distance >= 20:
        base_rate += 10000.0
        
    return base_rate

def calculate_final_shipping(weight: float, distance: int, method: str) -> float:
    
    if not isinstance(weight, (int, float)):
        raise TypeError("Trọng lượng hàng hóa phải là một số (int hoặc float).")
        
    if weight <= 0:
        raise ValueError("Trọng lượng hàng hóa bắt buộc phải lớn hơn 0.")
        
    base_rate = get_shipping_rate(method, distance)
    
    total_cost = base_rate + (weight * 2000.0)
    
    logger.info(f"Kết quả: Tổng phí vận chuyển = {total_cost:,.0f} VNĐ")
    return total_cost

if __name__ == "__main__":
    try:
        calculate_final_shipping(3.5, 25, "express")
    except Exception as e:
        logger.error(f"Lỗi: {e}")
        
    try:
        calculate_final_shipping(2.0, -5, "standard")
    except Exception as e:
        logger.error(f"Lỗi: {e}") 