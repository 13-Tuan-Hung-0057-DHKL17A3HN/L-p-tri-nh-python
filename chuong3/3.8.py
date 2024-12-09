import numpy as np

# Bước 1: Đọc dữ liệu từ tập tin heights.txt và positions.txt
with open('heights.txt', 'r') as f:
    heights = [float(line.strip()) for line in f]

with open('positions.txt', 'r') as f:
    positions = [line.strip() for line in f]

# a) Tạo numpy array np_positions từ list positions
np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

# b) Tạo numpy array np_heights từ list heights
np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

# Bước 2: Tính chiều cao trung bình của các GK
gk_heights = np_heights[np_positions == 'GK']
mean_gk_height = np.mean(gk_heights)
print("\nChiều cao trung bình của các GK:", mean_gk_height)

# Bước 3: Tính chiều cao trung bình của những vị trí khác (Không phải GK)
other_heights = np_heights[np_positions != 'GK']
mean_other_height = np.mean(other_heights)
print("Chiều cao trung bình của các vị trí khác:", mean_other_height)

# Bước 4: Tạo mảng dữ liệu có cấu trúc tự định nghĩa players
players_dtype = np.dtype([('position', 'U5'), ('height', 'float')])
players = np.empty(len(np_positions), dtype=players_dtype)
players['position'] = np_positions
players['height'] = np_heights

# Bước 5: Sắp mảng players theo height
sorted_players = np.sort(players, order='height')

# Vị trí có chiều cao cao nhất và chiều cao thấp nhất
highest_player = sorted_players[-1]
lowest_player = sorted_players[0]

print("\nVị trí có chiều cao cao nhất:", highest_player['position'], "với chiều cao:", highest_player['height'])
print("Vị trí có chiều cao thấp nhất:", lowest_player['position'], "với chiều cao:", lowest_player['height'])