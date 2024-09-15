# import pandas as pd

# # 기존 CSV 파일 읽기
# input_file = 'C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\number_getting_inout.csv'  # 실제 파일 이름으로 변경하세요
# df = pd.read_csv(input_file, encoding='cp949')  # 필요에 따라 인코딩 변경

# # 연월이 202406인 데이터만 필터링
# filtered_df = df[df['사용월'] == 202406]

# # 새로운 CSV 파일로 저장
# output_file = 'filtered_output_202406.csv'
# filtered_df.to_csv(output_file, index=False, encoding='cp949')  # 필요에 따라 인코딩 변경

# print(f'Filtered data saved to {output_file}')



import pandas as pd

# 기존 CSV 파일 읽기
input_file = 'C:\\Users\\james\\3.coding\\filtered_output_202406.csv'  # 필터링된 데이터 파일 이름
df = pd.read_csv(input_file, encoding='cp949')  # 필요에 따라 인코딩 변경
df = df.drop(columns=['사용월', '지하철역'])
# 호선별로 승차 및 하차 인원을 합산
summed_df = df.groupby('호선명').sum().reset_index()

# 결과를 새로운 CSV 파일로 저장
output_file = 'summed_output_202406.csv'
summed_df.to_csv(output_file, index=False, encoding='cp949')  # 필요에 따라 인코딩 변경

print(f'Summed data saved to {output_file}')
