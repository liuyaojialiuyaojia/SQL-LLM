# %%
import csv
import pandas as pd
import faiss
import numpy as np

# %%
data = []

# 打开并读取文件
with open('/home/yaojia/projects/SQL LLM/search key/bge/keys.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 处理每一行
for line in lines:
    line = line.strip()  # 去掉每行两边的空白字符
    if line:  # 如果行不为空
        parts = line.split('\t')  # 以制表符进行分割
        if len(parts) == 4:  # 如果分割后的部分数量正确
            data.append(parts)
        else:
            print(f'数据有误：{parts}')

# 将数据转换为DataFrame
df = pd.DataFrame(data, columns=['键名', '类型', '中文名称', '中文描述'])

# %%
print(df)

# %%
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('BAAI/bge-large-zh')

# %%
# 将中文名称和中文描述拼接起来
df['text'] = df['中文名称'] + df['中文描述']
print(df['text'])

# %%
# 用模型将文本转化为向量
embeddings = model.encode(df['text'].tolist(), normalize_embeddings=True)

# %%
# 构建FAISS索引
d = embeddings.shape[1]
index = faiss.IndexFlatIP(d)
index.add(embeddings)

# %%
# 保存索引到文件
faiss.write_index(index, '../bge/index.faiss')
df.to_csv('../bge/dataframe.csv', index=False, encoding='utf-8')

# %%
index = faiss.read_index('../bge/index.faiss')

# %%
# 要搜索的句子
query = "电压等级"

# 将查询句子转化为向量
query_embedding = model.encode([query], normalize_embeddings=True)

# 在FAISS索引中搜索最相似的句子
D, I = index.search(query_embedding, 5)

# 打印出最相似的句子和它们的得分
for i, score in zip(I[0], D[0]):
    print(f"Num: {i}\t  Score: {score:.2f}\tText: {df['text'].iloc[i]}")

# %%
# 只编码中文名称
embeddings_name = model.encode(df['中文名称'].tolist(), normalize_embeddings=True)
d_name = embeddings_name.shape[1]
index_name = faiss.IndexFlatL2(d_name)
index_name.add(embeddings_name)

faiss.write_index(index_name, '/home/yaojia/projects/SQL LLM/search key/bge/index_name_test.faiss')

# %%
