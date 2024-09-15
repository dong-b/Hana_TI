import pandas as pd


file_path = 'C:\\Users\\james\\3.coding\\new_temporary\\number_getting_inout.csv' 
df = pd.read_csv(file_path, encoding='cp949')

station_column = '지하철역'
line_column = '호선명'
date_column = '사용월'

df_filtered = df[df[date_column] == 202406].copy() 

df_filtered['7-9시 유입+유출 합계'] = (
    df_filtered['17시-18시 승차인원'] + df_filtered['17시-18시 하차인원'] +
    df_filtered['18시-19시 승차인원'] + df_filtered['18시-19시 하차인원']
)

df_grouped = df_filtered.groupby([station_column, line_column], as_index=False).agg({'7-9시 유입+유출 합계': 'sum'})

df_sorted = df_grouped.sort_values(by='7-9시 유입+유출 합계', ascending=False)

top_30_threshold = int(len(df_sorted) * 0.3) 
top_30_stations = df_sorted.head(top_30_threshold)

top_30_stations.to_csv('상위_30퍼센트_역_7_9시_합계_202406.csv', encoding='utf-8-sig', index=False)

print("Top 30% stations for 7-9 AM in 202406 have been saved to '상위_30퍼센트_역_7_9시_합계_202406.csv'.")
