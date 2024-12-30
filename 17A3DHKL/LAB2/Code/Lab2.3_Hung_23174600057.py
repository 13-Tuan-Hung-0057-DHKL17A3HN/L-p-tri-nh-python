# Đọc dữ liệu từ tập tin efficiency.txt và shifts.txt
with open("efficiency.txt", "r") as file:
    efficiency = [float(line.strip()) for line in file]

with open("shifts.txt", "r") as file:
    shifts = [line.strip() for line in file]

print("Dữ liệu hiệu suất:", efficiency)
print("Dữ liệu ca làm việc:", shifts)

import numpy as np

# Tạo numpy array từ shifts
np_shifts = np.array(shifts)
print("Numpy array np_shifts:", np_shifts)
print("Kiểu dữ liệu của np_shifts:", np_shifts.dtype)

# Tạo numpy array từ efficiency
np_efficiency = np.array(efficiency)
print("Numpy array np_efficiency:", np_efficiency)
print("Kiểu dữ liệu của np_efficiency:", np_efficiency.dtype)
# Lọc các nhân viên làm việc vào ca 'Morning'
morning_efficiency = np_efficiency[np_shifts == 'Morning']

# Tính hiệu suất trung bình
avg_morning_efficiency = np.mean(morning_efficiency)
print(f"Hiệu suất trung bình của ca 'Morning': {avg_morning_efficiency:.2f}")
# Lọc các nhân viên không làm việc vào ca 'Morning'
other_efficiency = np_efficiency[np_shifts != 'Morning']

# Tính hiệu suất trung bình
avg_other_efficiency = np.mean(other_efficiency)
print(f"Hiệu suất trung bình của các ca khác (không phải 'Morning'): {avg_other_efficiency:.2f}")
