import pandas as pd

# 시군구 코드와 구 이름을 포함한 파일 읽기
mapping_df = pd.read_csv('C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\Guo_code.csv')  # 이 파일은 시도, 시군구, name, full name 정보를 포함

# 이동인구 데이터를 포함한 파일 읽기
data_df = pd.read_csv('C:\\Users\\james\\3.coding\\aggregated_data.csv')

# 출발 시군구 코드와 도착 시군구 코드를 구 이름으로 대체
data_df = data_df.merge(mapping_df[['시군구', 'name']], left_on='출발 시군구 코드', right_on='시군구', how='left')
data_df = data_df.drop(columns=['출발 시군구 코드', '시군구'])
data_df = data_df.rename(columns={'name': '출발 시군구 코드'})

data_df = data_df.merge(mapping_df[['시군구', 'name']], left_on='도착 시군구 코드', right_on='시군구', how='left')
data_df = data_df.drop(columns=['도착 시군구 코드', '시군구'])
data_df = data_df.rename(columns={'name': '도착 시군구 코드'})


data_df.to_csv('final_data_with_names.csv', index=False)

print("시군구 코드가 구 이름으로 대체되었으며, 결과가 'final_data_with_names1.csv'에 저장되었습니다.")
