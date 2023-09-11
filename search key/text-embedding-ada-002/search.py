# %%
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# %%
# 定义模型
embeddings = OpenAIEmbeddings(
    model_kwargs = {"model_name": "text-embedding-ada-002"},
    openai_api_key='',
    openai_api_base='https://openai.api2d.net/v1'
)

# %%
db = FAISS.load_local("index", embeddings)

# %%
# 搜索
query = "Find out which power plant has the largest total generator capacity."
results = db.similarity_search_with_score(query, k=5)
for result in results:
    print(result[0], result[1])
# 把问题+搜索结果写入result.txt文件中
with open('result.txt', 'a') as f:
    f.write(query)
    f.write('\n')
    for result in results:
        f.write(result[0].page_content)
        f.write(': ')
        f.write(str(result[1]))
        f.write('\n')
    f.write('------------------')
    f.write('\n')

# %%
