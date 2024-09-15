import pandas as pd
import numpy as np
from scipy import stats

# 데이터 읽기
df = pd.read_csv('C:\\Users\\james\\3.coding\\base_data.csv')

# 1. '*' 처리된 이동인구 합을 0으로 지정
df['이동인구(합)'] = df['이동인구(합)'].replace('*', 0).astype(float)

# # 2. z-점수 방법을 이용한 이상값 탐지
# z_scores = np.abs(stats.zscore(df['이동인구(합)']))
# threshold = 3  

# # 3. 이동평균을 이용한 노이즈 처리
# window_size = 3  
# df['이동평균'] = df['이동인구(합)'].rolling(window=window_size, min_periods=1, center=True).mean()

# # 이상값을 이동평균으로 대체
# df.loc[z_scores > threshold, '이동인구(합)'] = df['이동평균']

# # 4. 이동평균 열 제거 
# df = df.drop(columns=['이동평균'])

# 5. 새로운 파일로 저장
df.to_csv('processed_data1.csv', index=False)

print("전처리 완료. 결과가 'processed_data1.csv'에 저장되었습니다.")
