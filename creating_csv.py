import pandas as pd
import glob
import os


base_path = r'C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\moving\\'
output_file = 'combined_output.csv'

# 경로 내의 모든 CSV 파일 가져오기
all_files = glob.glob(os.path.join(base_path, "*.csv"))


combined_df = pd.DataFrame()

# 모든 CSV 파일을 읽어서 하나의 데이터프레임으로 합치기
for file in all_files:
    # 시간대 추출 
    time_index = os.path.basename(file).split('.')[0]

    df = pd.read_csv(file, encoding='cp949')  

    # 시간대 열 추가
    df['시간대'] = time_index

    # 필요없는 열 제거 (성별, 나이, 평균이동시간)
    df = df.drop(columns=['성별', '나이', '평균 이동 시간(분)'])

    # 데이터프레임을 결합
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# 결과를 새로운 CSV 파일로 저장
combined_df.to_csv(output_file, index=False)

print(f'All files have been successfully combined into {output_file}')







# #################출근시간


# import pandas as pd
# import glob
# import os

# # 기본 경로 설정
# base_path = r'C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\moving\\'
# output_file = 'combined_output_filtered.csv'

# # 07, 08, 09 시간대에 해당하는 CSV 파일만 가져오기
# target_files = [os.path.join(base_path, f"{hour:02}.csv") for hour in range(17, 20)]

# # 빈 데이터프레임 생성
# combined_df = pd.DataFrame()

# # 07, 08, 09 시간대에 해당하는 파일만 처리
# for file in target_files:
#     # CSV 파일 읽기
#     df = pd.read_csv(file, encoding='cp949')  # encoding 옵션은 필요에 따라 변경

#     # 시간대 열 추가
#     time_index = os.path.basename(file).split('.')[0]
#     df['시간대'] = time_index

#     # 필요없는 열 제거 (성별, 나이, 평균 이동 시간)
#     df = df.drop(columns=['성별', '나이', '평균 이동 시간(분)'])

#     # 데이터프레임을 결합
#     combined_df = pd.concat([combined_df, df], ignore_index=True)

# # 결과를 새로운 CSV 파일로 저장
# combined_df.to_csv(output_file, index=False)

# print(f'07시, 08시, 09시 시간대의 데이터가 {output_file} 파일로 성공적으로 결합되었습니다.')








########################나이
import pandas as pd
import glob
import os

# 기본 경로 설정
base_path = r'C:\\Users\\james\\3.coding\\sparkle\\Hana_TI\\data\\moving\\'
output_file = 'combined_output.csv'

# 경로 내의 모든 CSV 파일 가져오기
all_files = glob.glob(os.path.join(base_path, "*.csv"))

# 빈 데이터프레임 생성
combined_df = pd.DataFrame()

# 모든 CSV 파일을 읽어서 하나의 데이터프레임으로 합치기
for file in all_files:
    # 시간대 추출 (파일명에서 시간대 추출: 00.csv -> 00)
    time_index = os.path.basename(file).split('.')[0]

    # CSV 파일 읽기
    df = pd.read_csv(file, encoding='cp949')  # encoding 옵션은 필요에 따라 변경

    # 시간대 열 추가
    df['시간대'] = time_index

    # 필요없는 열 제거 (성별, 나이, 평균이동시간)
    df = df.drop(columns=['성별', '평균 이동 시간(분)'])

    # 데이터프레임을 결합
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# 결과를 새로운 CSV 파일로 저장
combined_df.to_csv(output_file, index=False)

print(f'All files have been successfully combined into {output_file}')
