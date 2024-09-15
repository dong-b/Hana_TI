import pandas as pd


file_path = 'C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\한번처리됨\\퇴근시간.csv'
df = pd.read_csv(file_path)


df['이동인구(합)'] = df['이동인구(합)'].astype(float)


gu_only = df[df['출발 시군구 코드'].str.contains('구') & df['도착 시군구 코드'].str.contains('구')]

# 각 구별 유입 인구(도착) 및 유출 인구(출발) 합산
incoming = gu_only.groupby('도착 시군구 코드')['이동인구(합)'].sum()
outgoing = gu_only.groupby('출발 시군구 코드')['이동인구(합)'].sum()

# 유입 및 유출 데이터를 병합하여 DataFrame 생성
population_flow = pd.DataFrame({'유입 인구': incoming, '유출 인구': outgoing}).fillna(0)

output_file_path = '구별_유입_유출_인구_퇴근.csv'
population_flow.to_csv(output_file_path, encoding='utf-8-sig')

print(f"CSV 파일이 저장되었습니다: {output_file_path}")





# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm

# # 한글 폰트 설정
# plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 사용자의 경우
# plt.rcParams['axes.unicode_minus'] = False  # 마이너스 부호 깨짐 방지

# # CSV 파일 불러오기
# file_path = 'C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\한번처리됨\\퇴근시간.csv'
# df = pd.read_csv(file_path)

# # '이동인구(합)' 열을 float으로 변환
# df['이동인구(합)'] = df['이동인구(합)'].astype(float)

# # '구' 단위 데이터만 추출 (시 데이터 제외)
# gu_only = df[df['출발 시군구 코드'].str.contains('구') & df['도착 시군구 코드'].str.contains('구')]

# # 각 구별 유입 인구(도착) 및 유출 인구(출발) 합산
# incoming = gu_only.groupby('도착 시군구 코드')['이동인구(합)'].sum()
# outgoing = gu_only.groupby('출발 시군구 코드')['이동인구(합)'].sum()

# # 유입 및 유출 데이터를 병합하여 DataFrame 생성
# population_flow = pd.DataFrame({'유입 인구': incoming, '유출 인구': outgoing}).fillna(0)

# # 막대 그래프 그리기
# plt.figure(figsize=(12, 6))
# population_flow.plot(kind='bar', stacked=False, figsize=(12, 6))

# # 제목 및 라벨 설정
# plt.title('구별 유입 및 유출 인구')
# plt.xlabel('구')
# plt.ylabel('인구 수')

# # 범례 표시
# plt.legend(loc='upper right')

# # 그래프 표시
# plt.tight_layout()
# plt.show()
