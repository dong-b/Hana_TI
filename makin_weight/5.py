import pandas as pd

file_path_stations = 'C:\\Users\\james\\3.coding\\new_temporary\\역_자치구_추가_결과_퇴근.csv'  # 역 데이터 파일
file_path_top_30_gu = 'C:\\Users\\james\\3.coding\\new_temporary\\상위_30퍼센트_구_퇴근.csv'  # 상위 30% 구 파일

df_stations = pd.read_csv(file_path_stations, encoding='utf-8')
df_top_30_gu = pd.read_csv(file_path_top_30_gu, encoding='utf-8')

# 열 이름 확인 (중간 확인을 위해 출력)
print(df_stations.columns)
print(df_top_30_gu.columns)

# 자치구가 상위 30% 구에 속하는 역들만 필터링
top_30_gu_names = df_top_30_gu['Unnamed: 0'].unique()  # 상위 30% 구 목록
df_filtered = df_stations[df_stations['자치구'].isin(top_30_gu_names)]

# 호선별 역 개수를 계산
df_grouped = df_filtered.groupby('호선명').size().reset_index(name='역개수')

# 호선별로 정렬
df_grouped_sorted = df_grouped.sort_values(by='역개수', ascending=False)

# 호선별 역 리스트 출력
for index, row in df_grouped_sorted.iterrows():
    print(f"호선: {row['호선명']}, 역 개수: {row['역개수']}")

