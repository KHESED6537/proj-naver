import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터프레임 생성 (실제 사용 시 df2에 해당하는 실제 데이터 사용)
data = {
    "USD": [1.1, 1.2, 1.3, 1.4, 1.5],
    "EUR": [1.3, 1.4, 1.5, 1.6, 1.7]
}
df2 = pd.DataFrame(data)

# 시각화
# 차트의 크기를 가로7인치, 세로4인치로 설정합니다.
# @param3 - 차트에 그리드를 표시합니다.
df2.plot(figsize=(7, 4), title="네이버환율정보", grid=True)

# 차트를 보여주기 위한 명령
# 일부 환경에서는 없어도 시각화를 처리해주지만 일관된 결과를 위해서
# 명시적으로 호출하는 것이 좋습니다.
plt.show()