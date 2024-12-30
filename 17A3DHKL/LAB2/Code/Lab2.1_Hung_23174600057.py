import numpy as np

# Tạo mảng nhiệt độ ngẫu nhiên (15°C đến 35°C) cho 30 ngày
temperature = np.round(np.random.uniform(15, 35, size=30), 2)

# Hiển thị nhiệt độ
print("Nhiệt độ hàng ngày trong tháng:", temperature)

# Tính nhiệt độ trung bình
average_temp = np.mean(temperature)
print(f"Nhiệt độ trung bình trong tháng: {average_temp:.2f}°C")

# Nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperature)
min_temp = np.min(temperature)
max_day = np.argmax(temperature) + 1  # Ngày có nhiệt độ cao nhất
min_day = np.argmin(temperature) + 1  # Ngày có nhiệt độ thấp nhất

print(f"Nhiệt độ cao nhất: {max_temp}°C vào ngày {max_day}")
print(f"Nhiệt độ thấp nhất: {min_temp}°C vào ngày {min_day}")

# Chênh lệch nhiệt độ giữa các ngày
temp_diff = np.abs(np.diff(temperature)) #Tính hiệu số giữa nhiệt độ của ngày hiện tại và ngày trước đó, tạo thành một mảng mới chứa sự chênh lệch nhiệt độ.
max_diff = np.max(temp_diff)
max_diff_day = np.argmax(temp_diff) + 1 #tính chênh lệch giữa ngày hiện tại và ngày trước đó, nên ngày có sự chênh lệch lớn nhất là ngày tiếp theo.

print(f"Ngày có sự biến đổi nhiệt độ cao nhất là ngày {max_diff_day} với chênh lệch {max_diff:.2f}°C")

# Ngày có nhiệt độ cao hơn 20°C
days_above_20 = np.where(temperature > 20)[0] + 1
print("Các ngày có nhiệt độ trên 20°C:", days_above_20)

# Nhiệt độ của ngày 5, 10, 15, 20, 25
specific_days = [5, 10, 15, 20, 25]
specific_temps = temperature[np.array(specific_days) - 1]
print("Nhiệt độ của các ngày 5, 10, 15, 20, 25:", specific_temps)

# Nhiệt độ các ngày trên trung bình
days_above_avg = np.where(temperature > average_temp)[0] + 1
print("Các ngày có nhiệt độ trên trung bình:", days_above_avg)

# Nhiệt độ của các ngày chẵn
even_days = np.arange(1, 31, 2)
even_temps = temperature[even_days - 1]
print("Nhiệt độ các ngày chẵn:", even_temps)

# Nhiệt độ của các ngày lẻ
odd_days = np.arange(2, 31, 2)
odd_temps = temperature[odd_days - 1]
print("Nhiệt độ các ngày lẻ:", odd_temps)
