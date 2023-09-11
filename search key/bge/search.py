# %%
import csv
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# %%
model = SentenceTransformer('BAAI/bge-large-zh')
index = faiss.read_index('/home/yaojia/projects/SQL LLM/search key/bge/index.faiss')
index_name = faiss.read_index('/home/yaojia/projects/SQL LLM/search key/bge/index_name.faiss')
df = pd.read_csv('/home/yaojia/projects/SQL LLM/search key/bge/dataframe.csv')

# %%
print(df)

# %%
query = "询所有在特定日期后送电的用户的用户ID、用户名称和送电日期"

# 将查询句子转化为向量
query_embedding = model.encode([query], normalize_embeddings=True)

# %%
# 测试中文名称+中文描述的方法
# 在FAISS索引中搜索最相似的句子
D, I = index.search(query_embedding, 10)

# 打印出最相似的句子和它们的得分
for i, score in zip(I[0], D[0]):
    print(f"键: {df['键名'].iloc[i]}\t类型: {df['类型'].iloc[i]}\t键中文名：{df['中文名称'].iloc[i]}\t描述: {df['中文描述'].iloc[i]}")

# %%
# 测试只编码中文名称的方法
D, I = index_name.search(query_embedding, 50)

# 打印出最相似的句子和它们的得分
for i, score in zip(I[0], D[0]):
    # print(f"Num: {i}\t  Score: {score:.2f}\t键: {df['键名'].iloc[i]}")
    print(f"Num: {i}\t  Score: {score:.2f}")

# %%
