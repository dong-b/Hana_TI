import pandas as pd

file_path = 'C:\\Users\\james\\3.coding\\combined_output_filtered.csv'
data = pd.read_csv(file_path, encoding='utf-8')

print(data.head())

data = data[['시간대','출발 시군구 코드','도착 시군구 코드','이동인구(합)']]


output_file_path = 'base_data.csv'
data.to_csv(output_file_path, index=False)

print(f'Data saved to {output_file_path}')





# import pandas as pd
# import matplotlib.pyplot as plt


# # CSV 파일을 읽어 데이터프레임으로 변환
# file_path = 'C:\\Users\\james\\3.coding\\combined_output_filtered.csv'
# data = pd.read_csv(file_path, encoding='utf-8')

# print(data.head())

# # 필요한 열만 선택
# data = data[['출발 시군구 코드','도착 시군구 코드','이동인구(합)']]


# output_file_path = 'base_data.csv'
# data.to_csv(output_file_path, index=False)

# print(f'Data saved to {output_file_path}')




#####################나이
import pandas as pd
import matplotlib.pyplot as plt


# CSV 파일을 읽어 데이터프레임으로 변환
file_path = 'C:\\Users\\james\\3.coding\\combined_output.csv'
data = pd.read_csv(file_path, encoding='utf-8')

print(data.head())

# 필요한 열만 선택
data = data[['출발 시군구 코드','도착 시군구 코드','나이','이동인구(합)']]


output_file_path = 'base_data.csv'
data.to_csv(output_file_path, index=False)

print(f'Data saved to {output_file_path}')