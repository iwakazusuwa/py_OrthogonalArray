import pandas as pd

#=============================================
# CSVを読み込む
#=============================================
levels_df = pd.read_csv("levels.csv")

#=============================================
# 各列ごとにユニーク値（非NA）を水準として抽出
#=============================================
factor_levels = {}
for col in levels_df.columns:
    unique_levels = levels_df[col].dropna().unique().tolist()
    factor_levels[col] = unique_levels

#=============================================
# 因子ごとにユニークな水準リストを作る
#=============================================
factor_levels = {}
for col in levels_df.columns:
    factor_levels[col] = levels_df[col].dropna().unique().tolist()
    print(factor_levels[col])

#=============================================
# L9直交表の水準番号（0始まり）
#=============================================
orthogonal_index = [
    [0, 0, 0, 0], 
    [0, 1, 1, 1], 
    [0, 2, 2, 2], 
    [1, 0, 1, 2], 
    [1, 1, 2, 0], 
    [1, 2, 0, 1], 
    [2, 0, 2, 1], 
    [2, 1, 0, 2], 
    [2, 2, 1, 0],
]
##=============================================
# 直交表を作る順番を決める
#=============================================
# 必ず factor_levels の全列を使う
selected_factors = list(factor_levels.keys()) 

#=============================================
# 水準リストも順番を合わせる
#=============================================
selected_levels = [factor_levels[f] for f in selected_factors]
#=============================================
# L9のインデックスを水準値に変換しながら直交表を作成
#=============================================
data_OA = []
for row in orthogonal_index:
    entry = [selected_levels[i][row[i]] for i in range(len(selected_factors))]
    data_OA.append(entry)

# DataFrame化（列名も元の因子名のまま）
df_OA = pd.DataFrame(data_OA, columns=selected_factors)

#=============================================
# コンジョイント分析用に行列入れ替えます
#=============================================
df_OA = df_OA.T
#=============================================
#保存
#=============================================
df_OA.to_csv("直交表.csv", index=True, encoding="utf-8-sig")
df_OA
