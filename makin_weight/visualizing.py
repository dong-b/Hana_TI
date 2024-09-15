# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm

# # 한글 폰트 설정 (Mac과 Windows에 맞춰서 선택하세요)
# plt.rcParams['font.family'] = 'Malgun Gothic'  # For Windows users
# plt.rcParams['axes.unicode_minus'] = False  # 마이너스 폰트 깨짐 방지

# # CSV 파일 불러오기
# file_path = 'C:\\Users\\james\\3.coding\\new_temporary\\지하철 호선별시간별이용량.csv'
# df_subway = pd.read_csv(file_path, encoding='cp949')

# # 시간대 관련 열만 추출
# time_columns = [col for col in df_subway.columns if '승차인원' in col or '하차인원' in col]

# # '호선명'을 기준으로 시간대별 승차/하차 인원을 합산한 데이터프레임 생성
# df_subway['Total'] = df_subway[time_columns].sum(axis=1)
# df_lineplot = df_subway.set_index('호선명')[time_columns]

# # 데이터 정수형으로 변환
# df_lineplot = df_lineplot.apply(pd.to_numeric, errors='coerce')

# # 꺾은선 그래프 그리기
# plt.figure(figsize=(12, 8))

# for line in df_lineplot.index:
#     plt.plot(df_lineplot.columns, df_lineplot.loc[line], label=line)

# # 그래프 설정
# plt.title('지하철 호선별 시간대별 이용량', fontsize=16)
# plt.xlabel('시간대', fontsize=12)
# plt.ylabel('이용량 (명)', fontsize=12)
# plt.xticks(rotation=45)  # X축 레이블 회전
# plt.legend(loc='upper right', title='호선')

# # 그래프 보여주기
# plt.tight_layout()
# plt.show()







import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정 (Mac과 Windows에 맞춰서 선택하세요)
plt.rcParams['font.family'] = 'Malgun Gothic'  # For Windows users
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 폰트 깨짐 방지

# CSV 파일 불러오기
file_path = 'C:\\Users\\james\\3.coding\\new_temporary\\지하철 호선별시간별이용량.csv'
df_subway = pd.read_csv(file_path, encoding='cp949')

# 승차/하차 합계를 구해서 전체 시간대별로 합산
hourly_columns = [col for col in df_subway.columns if '승차인원' in col or '하차인원' in col]

# 각 시간대의 승차 및 하차 인원을 합산한 열을 추가
for hour in range(4, 25):  # 시간대가 04시부터 24시까지 있는 것으로 가정
    boarding_col = f'{hour:02d}시-{hour+1:02d}시 승차인원'
    alighting_col = f'{hour:02d}시-{hour+1:02d}시 하차인원'
    if boarding_col in df_subway.columns and alighting_col in df_subway.columns:
        df_subway[f'{hour:02d}시 승하차 합계'] = df_subway[boarding_col] + df_subway[alighting_col]

# 필요한 열만 선택하여 새로운 DataFrame 생성
sum_columns = [f'{hour:02d}시 승하차 합계' for hour in range(4, 25) if f'{hour:02d}시 승하차 합계' in df_subway.columns]
df_total = df_subway[['호선명'] + sum_columns]

# '호선명'을 인덱스로 설정
df_total.set_index('호선명', inplace=True)

# 히트맵 그리기 (annot=False로 숫자 제외)
plt.figure(figsize=(16, 10))
sns.heatmap(df_total, cmap='coolwarm', annot=False, linewidths=0.5, cbar_kws={'label': '이용량 (명)'})

# 그래프 설정
plt.title('지하철 호선별 시간대별 승하차 합계 (전체 시간)', fontsize=16)
plt.xlabel('시간대', fontsize=12)
plt.ylabel('호선', fontsize=12)

# 그래프 표시
plt.tight_layout()
plt.show()
