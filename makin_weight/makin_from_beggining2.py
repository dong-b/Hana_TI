import pandas as pd

# CSV 파일 불러오기
file_path = 'C:\\Users\\james\\3.coding\\new_temporary\\구별_유입_유출_인구_퇴근.csv' 
df = pd.read_csv(file_path, encoding='utf-8')

df['유입+유출 합계'] = df['유입 인구'] + df['유출 인구']

df_sorted = df.sort_values(by='유입+유출 합계', ascending=False)

# 상위 30% 구 추출
top_30_threshold = int(len(df_sorted) * 0.3)  
top_30_gu = df_sorted.head(top_30_threshold)

print(top_30_gu)

top_30_gu.to_csv('상위_30퍼센트_구_퇴근.csv', encoding='utf-8-sig', index=False)
