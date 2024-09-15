import pandas as pd

file_path_stations = 'C:/Users/james/3.coding/new_temporary/상위_30퍼센트_역_7_9시_합계_퇴근.csv'  
file_path_location = 'C:/Users/james/3.coding/new_temporary/loaction_station.CSV' 

df_stations = pd.read_csv(file_path_stations, encoding='utf-8')  # 역 데이터
df_location = pd.read_csv(file_path_location, encoding='cp949')  # 자치구 정보

# 자치구 파일에서 역 정보를 정리 (역이 여러 개 포함된 셀을 나누기)
df_location['해당역(호선)'] = df_location['해당역(호선)'].str.split(', ')
df_location_exploded = df_location.explode('해당역(호선)').reset_index(drop=True)  # 역을 개별로 분리

# 역 이름에서 괄호를 제거하고 비교하기 위한 전처리 (자치구 데이터)
df_location_exploded['해당역'] = df_location_exploded['해당역(호선)'].str.extract(r'(\S+)\(')  # 괄호 앞 부분만 추출

# 역 이름에서도 괄호 제거 (역 데이터)
df_stations['지하철역'] = df_stations['지하철역'].str.replace(r'\(.*\)', '', regex=True)

# 역 파일과 자치구 파일을 역 이름을 기준으로 병합
df_merged = pd.merge(df_stations, df_location_exploded[['해당역', '자치구']], left_on='지하철역', right_on='해당역', how='inner')

# 자치구 열을 추가한 후, 불필요한 열 제거
df_merged = df_merged[['지하철역', '호선명', '7-9시 유입+유출 합계', '자치구']]

df_merged.to_csv('역_자치구_추가_결과.csv', encoding='utf-8-sig', index=False)

print("자치구 정보가 추가된 역 파일이 '역_자치구_추가_결과.csv'로 저장되었습니다.")
