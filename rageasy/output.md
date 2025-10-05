

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy>
(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy>python -m graphrag.prompt_tune --config ./settings.yaml --root ./ --no-entity-types --language Chinese --output ./prompts-ch
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\graphrag\prompt_tune\__main__.py:126: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()


INFO: Reading settings from settings.yaml


Loading Input (InputFileType.text).
INFO: Generating domain...

INFO: Generated domain: Domain: Fictional narrative / Animated media

INFO: Generating persona...

INFO: Generating community report ranking description...

INFO: Generating entity relationship examples...

INFO: Generating entity extraction prompt...

INFO: Generating entity summarization prompt...

INFO: Generating community reporter role...

INFO: Generating community summarization prompt...

INFO: Writing prompts to prompts-ch

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy>python -m graphrag.index --root ./
🚀 Reading settings from settings.yaml
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
🚀 create_base_text_units
                                 id        chunk                          chunk_id                        document_ids  n_tokens
0  8dbd1064152be7725b60725b36c34c80  灰太狼是小灰灰的爸爸。  8dbd1064152be7725b60725b36c34c80  [05ee4c187aa5f6f8bb045d4b7aeea22d]        19
🚀 create_base_extracted_entities
                                        entity_graph
0  <graphml xmlns="http://graphml.graphdrawing.or...
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\datashaper\engine\verbs\convert.py:65: FutureWarning: errors='ignore' is deprecated and will raise in a future    
version. Use to_numeric without passing `errors` and catch exceptions explicitly instead
  column_numeric = cast(pd.Series, pd.to_numeric(column, errors="ignore"))
🚀 create_final_covariates
                                     id human_readable_id covariate_type  ...                      text_unit_id                        document_ids n_tokens
0  4d5db4ef-c2de-49f4-84d7-f137281ea7f1                 1          claim  ...  8dbd1064152be7725b60725b36c34c80  [05ee4c187aa5f6f8bb045d4b7aeea22d]       19

[1 rows x 16 columns]
🚀 create_summarized_entities
                                        entity_graph
0  <graphml xmlns="http://graphml.graphdrawing.or...
🚀 join_text_units_to_covariate_ids
                       text_unit_id                           covariate_ids                                id
0  8dbd1064152be7725b60725b36c34c80  [4d5db4ef-c2de-49f4-84d7-f137281ea7f1]  8dbd1064152be7725b60725b36c34c80
🚀 create_base_entity_graph
   level                                    clustered_graph
0      0  <graphml xmlns="http://graphml.graphdrawing.or...
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
🚀 create_final_entities
                                 id name    type  ... graph_embedding                       text_unit_ids                              description_embedding
0  b45241d70f0e43fca764df95b2b81f77  灰太狼  PERSON  ...            None  [8dbd1064152be7725b60725b36c34c80]  [-0.3825605511665344, -2.7085249423980713, -0....
1  4119fd06010c494caa07f439b333f4c5  小灰灰  PERSON  ...            None  [8dbd1064152be7725b60725b36c34c80]  [0.5238127708435059, 2.8067445755004883, -1.61...

[2 rows x 8 columns]
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\datashaper\engine\verbs\convert.py:72: FutureWarning: errors='ignore' is deprecated and will raise in a future    
version. Use to_datetime without passing `errors` and catch exceptions explicitly instead
  datetime_column = pd.to_datetime(column, errors="ignore")
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\datashaper\engine\verbs\convert.py:72: UserWarning: Could not infer format, so each element will be parsed        
individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.
  datetime_column = pd.to_datetime(column, errors="ignore")
🚀 create_final_nodes
   level title    type                       description                         source_id  ... size  graph_embedding                 top_level_node_id  x  y
0      0   灰太狼  PERSON  灰太狼是小灰灰的父亲，一个动画角色，以试图抓羊而闻名，但始终失败  8dbd1064152be7725b60725b36c34c80  ...    1             None
b45241d70f0e43fca764df95b2b81f77  0  0
1      0   小灰灰  PERSON      小灰灰是灰太狼的儿子，性格天真善良，与父亲灰太狼关系亲密  8dbd1064152be7725b60725b36c34c80  ...    1             None
4119fd06010c494caa07f439b333f4c5  0  0

[2 rows x 14 columns]
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
🚀 create_final_communities
  id        title  level raw_community                    relationship_ids                       text_unit_ids
0  0  Community 0      0             0    [8dbd1064152be7725b60725b36c34c80]
🚀 join_text_units_to_entity_ids
                      text_unit_ids                                         entity_ids                                id
0  8dbd1064152be7725b60725b36c34c80  [b45241d70f0e43fca764df95b2b81f77, 4119fd06010...  8dbd1064152be7725b60725b36c34c80
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\numpy\core\fromnumeric.py:59: FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future   
version. Please use 'DataFrame.transpose' instead.
  return bound(*args, **kwds)
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\datashaper\engine\verbs\convert.py:65: FutureWarning: errors='ignore' is deprecated and will raise in a future    
version. Use to_numeric without passing `errors` and catch exceptions explicitly instead
  column_numeric = cast(pd.Series, pd.to_numeric(column, errors="ignore"))
🚀 create_final_relationships
  source target  weight         description                       text_unit_ids                                id human_readable_id  source_degree  target_degree  rank     
0    灰太狼    小灰灰     1.0  灰太狼是小灰灰的父亲，两人是父子关系  [8dbd1064152be7725b60725b36c34c80]  d3835bf3dda84ead99deadbeac5d0d7d                 0              1  
1     2
🚀 join_text_units_to_relationship_ids
                                 id                    relationship_ids
0  8dbd1064152be7725b60725b36c34c80
🚀 create_final_community_reports
  community                                       full_content  ...                                  full_content_json                                    id
0         0  # 灰太狼与小灰灰父子关系社区\n\n该社区围绕小灰灰及其父亲灰太狼的亲子关系构建。核心实体...  ...  {\n    "title": "灰太狼与小灰灰父子关系社区",\n    "summary... 
9b210165-002e-4d97-bdc7-9cc97125d398

[1 rows x 10 columns]
🚀 create_final_text_units
                                 id         text  ...                    relationship_ids                           covariate_ids
0  8dbd1064152be7725b60725b36c34c80  灰太狼是小灰灰的爸爸。  ...    [4d5db4ef-c2de-49f4-84d7-f137281ea7f1]

[1 rows x 7 columns]
C:\Users\zooos\.conda\envs\graphrag-env\Lib\site-packages\datashaper\engine\verbs\convert.py:72: FutureWarning: errors='ignore' is deprecated and will raise in a future    
version. Use to_datetime without passing `errors` and catch exceptions explicitly instead
  datetime_column = pd.to_datetime(column, errors="ignore")
🚀 create_base_documents
                                 id                          text_units  raw_content  title
0  05ee4c187aa5f6f8bb045d4b7aeea22d  [8dbd1064152be7725b60725b36c34c80]  灰太狼是小灰灰的爸爸。  1.txt
🚀 create_final_documents
                                 id                       text_unit_ids  raw_content  title
0  05ee4c187aa5f6f8bb045d4b7aeea22d  [8dbd1064152be7725b60725b36c34c80]  灰太狼是小灰灰的爸爸。  1.txt
⠇ GraphRAG Indexer
├── create_base_text_units
├── create_base_extracted_entities
├── create_final_covariates
├── create_summarized_entities
├── join_text_units_to_covariate_ids
├── create_base_entity_graph
├── create_final_entities
├── create_final_nodes
├── create_final_communities
├── join_text_units_to_entity_ids
├── create_final_relationships
├── join_text_units_to_relationship_ids
├── create_final_community_reports
├── create_final_text_units
├── create_base_documents
└── create_final_documents
🚀 All workflows completed successfully.

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy>cd utils   

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy\utils>python main.py        
D:\zyt\git_ln\GraphragTest\rageasy\utils\main.py:43: SyntaxWarning: invalid escape sequence '\z'
  INPUT_DIR = "D:\zyt\git_ln\GraphragTest/rageasy/inputs/artifacts"
2025-10-05 13:09:56,093 - __main__ - INFO - 在端口 8012 上启动服务器
INFO:     Started server process [20424]
INFO:     Waiting for application startup.
INFO - LLM和嵌入器设置完成
2025-10-05 13:10:06,874 - __main__ - INFO - 正在加载上下文数据
[2025-10-05T05:10:07Z WARN  lance::dataset] No existing dataset at D:\zyt\git_ln\GraphragTest\rageasy\inputs\artifacts\lancedb\entity_description_embeddings.lance, it will be created
INFO - LLM和嵌入器设置完成
2025-10-05 13:10:06,874 - __main__ - INFO - 正在加载上下文数据
[2025-10-05T05:10:07Z WARN  lance::dataset] No existing dataset at D:\zyt\git_ln\GraphragTest\rageasy\inputs\artifacts\lancedb\entity_description_embeddings.lance, it will be created
2025-10-05 13:10:07,391 - __main__ - INFO - 声明记录数: 1
2025-10-05 13:10:07,391 - __main__ - INFO - 上下文数据加载完成
2025-10-05 13:10:07,392 - __main__ - INFO - 正在设置搜索引擎
2025-10-05 13:10:07,392 - __main__ - INFO - 搜索引擎设置完成
2025-10-05 13:10:07,392 - __main__ - INFO - 初始化完成
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8012 (Press CTRL+C to quit)
2025-10-05 13:15:11,600 - __main__ - INFO - 收到聊天完成请求: model='graphrag-global-search:latest' messages=[Message(role='user', content='这个故事的首要主题是什么?记住请使
用中文进行回答，不要用英文。')] temperature=0.7 top_p=1.0 n=1 stream=False stop=None max_tokens=None presence_penalty=0 frequency_penalty=0 logit_bias=None user=None
2025-10-05 13:15:11,647 - __main__ - INFO - 处理提示: 这个故事的首要主题是什么?记住请使用中文进行回答，不要用英文。
2025-10-05 13:15:11,648 - graphrag.query.context_builder.community_context - INFO - Computing community weights...
2025-10-05 13:15:15,456 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-05 13:15:15,504 - graphrag.query.structured_search.global_search.search - INFO - Map response: {
    "points": [
        {
            "description": "这个故事的首要主题是灰太狼与小灰灰之间的父子关系，该关系构 成了整个社区结构的基础，并围绕家庭纽带展开。小灰灰作为核心成员，被描述为天真善良，且与 父亲灰太狼关系亲密，体现了以亲情为核心的叙事重点 [Data: Reports (0)]",
            "score": 100
        }
    ]
}
2025-10-05 13:15:15,811 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-05 13:15:18,034 - __main__ - INFO - 格式化的搜索结果:
 这个故事的首要主题是灰太狼与小灰灰之间的父子关系。这种亲情纽带不仅是角色互动的核心，也构成了整个社区结构的基础。叙事围绕家庭关系展开，强调了亲情在个体成长与社会联结中的重要 作用 [Data: Reports (0)]。

小灰灰被描绘为天真善良的角色，他与父亲灰太狼之间亲密的关系进一步凸显了家庭温暖与情感依 赖的主题。这种父子关系不仅塑造了角色的行为动机，也影响着他们在社群中的定位与互动方式。 因此，故事通过这一核心关系传递出对家庭价值的肯定与弘扬 [Data: Reports (0)]。
2025-10-05 13:15:18,035 - __main__ - INFO - 发送响应:

id='chatcmpl-dbc320d9c7724fcfaec6b00864330db2' object='chat.completion' created=1759641318 model='graphrag-global-search:latest' choices=[ChatCompletionResponseChoice(index=0, message=Message(role='assistant', content='这个故事的首要主题是灰太狼与小灰灰之间的父子关系。这种亲情纽带不仅是角色互动的核心，也构成了整个社区结构的基础。叙事围绕家庭关系 展开，强调了亲情在个体成长与社会联结中的重要作用 [Data: Reports (0)]。\n\n小灰灰被描绘 为天真善良的角色，他与父亲灰太狼之间亲密的关系进一步凸显了家庭温暖与情感依赖的主题。这 种父子关系不仅塑造了角色的行为动机，也影响着他们在社群中的定位与互动方式。因此，故事通 过这一核心关系传递出对家庭价值的肯定与弘扬 [Data: Reports (0)]。'), finish_reason='stop')] usage=Usage(prompt_tokens=1, completion_tokens=8, total_tokens=9) system_fingerprint=None
INFO:     127.0.0.1:49660 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-10-05 13:16:22,493 - __main__ - INFO - 收到聊天完成请求: model='graphrag-local-search:latest' messages=[Message(role='user', content='灰太狼是谁，他的主要关系是什么?记住请使用中文进行回答，不要用英文。')] temperature=0.7 top_p=1.0 n=1 stream=False stop=None max_tokens=None presence_penalty=0 frequency_penalty=0 logit_bias=None user=None     
2025-10-05 13:16:22,494 - __main__ - INFO - 处理提示: 灰太狼是谁，他的主要关系是什么?记住请使用中文进行回答，不要用英文。
2025-10-05 13:16:22,612 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/embeddings "HTTP/1.1 200 OK"
2025-10-05 13:16:22,831 - graphrag.query.context_builder.community_context - WARNING - Warning: No community records added when building community context.
2025-10-05 13:16:22,838 - graphrag.query.structured_search.local_search.search - INFO - GENERATE ANSWER: 1759641382.4945211. QUERY: 灰太狼是谁，他的主要关系是什么?记住请使用 中文进行回答，不要用英文。
2025-10-05 13:16:23,101 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-05 13:16:27,986 - __main__ - INFO - 格式化的搜索结果:
 灰太狼是一个著名的动画角色，出自中国动画《喜羊羊与灰太狼》。他是一只狼，以试图捕捉羊村的羊而闻名，但其计划总是以失败告终。这一形象深入人心，常被用来象征坚持不懈却屡战屡败的 角色。在家庭关系方面，灰太狼是小灰灰的父亲，展现出作为父亲的责任感和温情一面，尽管他在 捕猎方面的努力常常显得滑稽可笑。

根据所提供的数据，灰太狼的主要关系是与他的儿子小灰灰之间的父子关系。这种关系在数据中被 明确指出：“灰太狼是小灰灰的父亲，两人是父子关系” [Data: Relationships (0); Entities (0, 1); Sources (0)]。小灰灰性格天真善良，与父亲关系亲密，这为灰太狼这一角色增添了更多情感层次，使其不仅仅是一个反派角色，更是一位有家庭责任感的父亲。

综上所述，灰太狼不仅因其反复失败的抓羊行动而广为人知，也因他与小灰灰之间的亲情关系而受 到观众喜爱。这些信息均来自提供的数据记录，包括实体描述、关系说明以及文本来源的支持 [Data: Entities (0); Relationships (0); Sources (0)]。
2025-10-05 13:16:27,991 - __main__ - INFO - 发送响应:

id='chatcmpl-149466444e5f4b0cad60a03c44d900e8' object='chat.completion' created=1759641387 model='graphrag-local-search:latest' choices=[ChatCompletionResponseChoice(index=0, message=Message(role='assistant', content='灰太狼是一个著名的动画角色，出自中国动画《 喜羊羊与灰太狼》。他是一只狼，以试图捕捉羊村的羊而闻名，但其计划总是以失败告终。这一形 象深入人心，常被用来象征坚持不懈却屡战屡败的角色。在家庭关系方面，灰太狼是小灰灰的父亲 ，展现出作为父亲的责任感和温情一面，尽管他在捕猎方面的努力常常显得滑稽可笑。\n\n根据所 提供的数据，灰太狼的主要关系是与他的儿子小灰灰之间的父子关系。这种关系在数据中被明确指 出：“灰太狼是小灰灰的父亲，两人是父子关系” [Data: Relationships (0); Entities (0, 1); Sources (0)]。小灰灰性格天真善良，与父亲关系亲密，这为灰太狼这一角色增添了更多情感层次，使其不仅仅是一个反派角色，更是一位有家庭责任感的父亲。\n\n综上所述，灰太狼不仅因其反复 失败的抓羊行动而广为人知，也因他与小灰灰之间的亲情关系而受到观众喜爱。这些信息均来自提 供的数据记录，包括实体描述、关系说明以及文本来源的支持 [Data: Entities (0); Relationships (0); Sources (0)]。'), finish_reason='stop')] usage=Usage(prompt_tokens=1, completion_tokens=18, total_tokens=19) system_fingerprint=None
INFO:     127.0.0.1:55184 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-10-05 13:16:47,411 - __main__ - INFO - 收到聊天完成请求: model='full-model:latest' messages=[Message(role='user', content='灰太狼是谁，他的主要关系是什么?记住请使用中文 进行回答，不要用英文。')] temperature=0.7 top_p=1.0 n=1 stream=False stop=None max_tokens=None presence_penalty=0 frequency_penalty=0 logit_bias=None user=None
2025-10-05 13:16:47,412 - __main__ - INFO - 处理提示: 灰太狼是谁，他的主要关系是什么?记住请使用中文进行回答，不要用英文。
2025-10-05 13:16:47,516 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/embeddings "HTTP/1.1 200 OK"
2025-10-05 13:16:47,552 - graphrag.query.context_builder.community_context - WARNING - Warning: No community records added when building community context.
2025-10-05 13:16:47,561 - graphrag.query.structured_search.local_search.search - INFO - GENERATE ANSWER: 1759641407.4128873. QUERY: 灰太狼是谁，他的主要关系是什么?记住请使用 中文进行回答，不要用英文。
2025-10-05 13:16:47,925 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-05 13:16:57,229 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-05 13:16:57,231 - graphrag.query.structured_search.global_search.search - INFO - Map response: {
    "points": [
        {
            "description": "灰太狼是小灰灰的父亲，与小灰灰构成明确的父子关系。这一关系 是当前社区中唯一具体的关系连接，并构成了该社区结构的基础 [Data: Relationships (0)]",   
            "score": 95
        },
        {
            "description": "灰太狼作为小灰灰的父亲，在一个以家庭纽带为核心的社区中扮演 重要角色。他与儿子小灰灰的关系被描述为亲密，且小灰灰的性格特征（天真善良）可能受到其父 亲的影响 [Data: Entities (1)]",
            "score": 85
        }
    ]
}
2025-10-05 13:16:57,609 - httpx - INFO - HTTP Request: POST http://localhost:3000/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-05 13:17:00,428 - __main__ - INFO - 格式化的搜索结果:
 #综合搜索结果:

##本地检索结果:
灰太狼是一个著名的动画角色，出自中国动画《喜羊羊与灰太狼》。他被描绘为一只总是试图捕捉 羊群的狼，但其计划屡屡失败，成为该系列的主要反派角色之一。尽管他以“抓羊”为己任，但在家 庭生活中，他展现出作为父亲的一面，具有一定的温情色彩。

根据提供的资料，灰太狼最主要的关系是与他的儿子小灰灰之间的父子关系。小灰灰性格天真善良 ，与父亲灰太狼关系亲密。灰太狼作为父亲，在动画中有时表现出严厉，但也不乏对儿子的关爱与 包容。这一父子关系在数据中有明确描述，并被列为重要人际关系 [Data: Entities (0, 1); Relationships (0); Sources (0)]。

此外，目前的数据集中未提及其他与灰太狼相关的人物或社会关系，也没有涉及他在狼族家庭或其 他社会角色中的位置。因此，基于现有信息，灰太狼的核心身份是小灰灰的父亲，其主要关系即为 与儿子的亲子纽带。

##全局检索结果:
灰太狼是小灰灰的父亲，两人之间存在明确的父子关系。这一关系构成了当前社区结构中唯一具体 的关系连接，并作为该社区组织的基础 [Data: Relationships (0)]。灰太狼在以家庭纽带为核心 的社区中扮演着重要角色，其与儿子小灰灰的互动体现出亲密的家庭联系。

此外，灰太狼与小灰灰的亲子关系不仅限于血缘层面，还可能对小灰灰的性格发展产生影响。资料 显示，小灰灰具有天真善良的性格特征，这种特质可能受到父亲灰太狼的熏陶或家庭教育的影响 [Data: Entities (1)]。因此，灰太狼不仅是家庭中的家长角色，也可能在情感和道德引导方面发挥 重要作用。


2025-10-05 13:17:00,429 - __main__ - INFO - 发送响应:

id='chatcmpl-816b1b927e7649c999446b28b25e6e35' object='chat.completion' created=1759641ated=1759641420 model='full-model:latest' choices=[ChatCompletionResponseChoice(atated=1759641420 modelated=1759641420 model='full-model:latestated=1759641420 model='full-model:latest' choices=[ChatCompletionResponseChoice(index=0, message=Message(role='assistanated=1759641420 model='full-model:latest' choices=[ChatCompletionResponseChoice(index=0, message=Message(role='assistant', content='#综合搜索结果:\n\n##本地检索结果:\n灰太狼是一个著名的动画角色，出自中国动画《喜羊羊与灰太狼》。他被描绘为一只总是试图捕捉羊群的狼，但其计划屡屡失败，成为该系列的主要反派角色之一。尽管他以“抓羊”为己任，但在家庭生活中，他展现出作为父亲的一面，具有一定的温情色彩。\n\n根据提供的资料，灰太狼最主要的关系是与他的儿子小灰灰之间的父子关系。小灰灰性格天真善良，与父亲灰太狼关系亲密。灰太狼作为父亲，在动画中有时表现出严厉，但也不乏对儿子的关爱与包容。这一父子关系在数据中有明确描述，并被列为重要人际关系 [Data: Entities (0, 1); Relationships (0); Sources (0)]。\n\n此外，目 前的数据集中未提及其他与灰太狼相关的人物或社会关系，也没有涉及他在狼族家庭或其他社会角色中的位置。因此，基于现有信息，灰太狼的核心身份是小灰灰的父亲，其主要关系即为与儿子的亲子纽带。\n\n##全局检索结果:\n灰太狼是小灰灰的父亲，两人之间存在明确的父子关系。这一关系构成了当前社区结构中唯一具体的关系连接，并作为该社区组织的基础 [Data: Relationships (0)]。灰太狼在以家庭纽带为核心的社区中扮演着重要角色，其与儿子小灰灰的互动体现出亲密的家庭联系。\n\n此外，灰太狼与小灰灰的亲子关系不仅限于血缘层面，还可能对小灰灰的性格发展产生影响。资料显示，小灰灰具有天真善良的性格特征，这种特质可能受到父亲灰太狼的熏陶或家庭教育的影响 [Data: Entities (1)]。因此，灰太狼不仅是家庭中的家长角色，也可能在情感和道德引导方面发挥重要作用。\n\n'), finish_reason='stop')] usage=Usage(prompt_tokens=1, completion_tokens=22, total_tokens=23) system_fingerprint=None
INFO:     127.0.0.1:55217 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
2025-10-05 13:18:45,637 - __main__ - INFO - 正在关闭...
INFO:     Application shutdown complete.
INFO:     Finished server process [20424]

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy\utils>^A

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy\utils>

