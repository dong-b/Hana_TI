import pandas as pd

df = pd.read_csv('C:\\Users\\james\\3.coding\\processed_data1.csv')

# 시간대, 출발 시군구 코드, 도착 시군구 코드별로 그룹화하고 이동인구의 합을 계산
df_grouped = df.groupby(['시간대', '출발 시군구 코드', '도착 시군구 코드'], as_index=False)['이동인구(합)'].sum()

df_grouped.to_csv('aggregated_data.csv', index=False)

print("데이터가 성공적으로 그룹화되고, 'aggregated_data1.csv'에 저장되었습니다.")



# import pandas as pd

# # CSV 파일 읽기
# df = pd.read_csv('C:\\Users\\james\\3.coding\\processed_data1.csv')

# # 시간대, 출발 시군구 코드, 도착 시군구 코드별로 그룹화하고 이동인구의 합을 계산
# df_grouped = df.groupby([ '출발 시군구 코드', '도착 시군구 코드'], as_index=False)['이동인구(합)'].sum()

# # 결과를 새로운 CSV 파일로 저장
# df_grouped.to_csv('aggregated_data.csv', index=False)

# print("데이터가 성공적으로 그룹화되고, 'aggregated_data1.csv'에 저장되었습니다.")





##############################나이



import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('C:\\Users\\james\\3.coding\\processed_data1.csv')

# 시간대, 출발 시군구 코드, 도착 시군구 코드별로 그룹화하고 이동인구의 합을 계산
df_grouped = df.groupby([ '출발 시군구 코드', '도착 시군구 코드','나이'], as_index=False)['이동인구(합)'].sum()

# 결과를 새로운 CSV 파일로 저장
df_grouped.to_csv('aggregated_data.csv', index=False)

print("데이터가 성공적으로 그룹화되고, 'aggregated_data1.csv'에 저장되었습니다.")