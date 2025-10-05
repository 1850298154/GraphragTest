Microsoft Windows [版本 10.0.22621.1105]
(c) Microsoft Corporation。保留所有权利。

D:\zyt\git_ln\GraphragTest>D:/Anaconda3/Scripts/activate

(base) D:\zyt\git_ln\GraphragTest>conda activate graphrag-env

(graphrag-env) D:\zyt\git_ln\GraphragTest>cd rageasy

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy>cd utils

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy\utils>python neo4jTest.py
D:\zyt\git_ln\GraphragTest\rageasy\utils\neo4jTest.py:52: SyntaxWarning: invalid escape sequence '\z'
  GRAPHRAG_FOLDER="D:\zyt\git_ln\GraphragTest/rageasy/inputs/artifacts"

create constraint document_id if not exists for (d:__Document__) require d.id is unique

create constraint chunk_id if not exists for (c:__Chunk__) require c.id is unique

create constraint entity_id if not exists for (e:__Entity__) require e.id is unique

create constraint entity_title if not exists for (e:__Entity__) require e.name is unique

create constraint entity_id if not exists for (c:__Community__) require c.community is unique

create constraint entity_title if not exists for (e:__Covariate__) require e.title is unique

create constraint related_id if not exists for ()-[rel:RELATED]->() require rel.id is unique
SummaryCounters{properties_set: 2, contains_updates: True, contains_system_updates: False}
1 rows in 1.9868199825286865 s.
返回的结果： 1
                                 id         text  ...                    relationship_ids                           covariate_ids
0  8dbd1064152be7725b60725b36c34c80  灰太狼是小灰灰的爸爸。  ...  [d3835bf3dda84ead99deadbeac5d0d7d]  [4d5db4ef-c2de-49f4-84d7-f137281ea7f1]

[1 rows x 7 columns]
SummaryCounters{properties_set: 2, contains_updates: True, contains_system_updates: False}
1 rows in 0.6095092296600342 s.
  name    type  ...                              description_embedding                       text_unit_ids
0  灰太狼  PERSON  ...  [-0.3825605511665344, -2.7085249423980713, -0....  [8dbd1064152be7725b60725b36c34c80]
1  小灰灰  PERSON  ...  [0.5238127708435059, 2.8067445755004883, -1.61...  [8dbd1064152be7725b60725b36c34c80]

[2 rows x 7 columns]
SummaryCounters{labels_added: 2, relationships_created: 2, nodes_created: 2, properties_set: 16, contains_updates: True, contains_system_updates: False}
2 rows in 0.8811826705932617 s.
  source target                                id  ...  human_readable_id         description                       text_unit_ids
0    灰太狼    小灰灰  d3835bf3dda84ead99deadbeac5d0d7d  ...                  0  灰太狼是小灰灰的父亲，两人是父子关系  [8dbd1064152be7725b60725b36c34c80]

[1 rows x 8 columns]
SummaryCounters{relationships_created: 1, properties_set: 6, contains_updates: True, contains_system_updates: False}
1 rows in 0.5375323295593262 s.
                                     id  ...                                       full_content
0  9b210165-002e-4d97-bdc7-9cc97125d398  ...  # 灰太狼与小灰灰父子关系社区\n\n该社区围绕小灰灰及其父亲灰太狼的亲子关系构建。核心实体...

[1 rows x 9 columns]
SummaryCounters{labels_added: 3, relationships_created: 2, nodes_created: 3, properties_set: 14, contains_updates: True, contains_system_updates: False}
1 rows in 0.3353426456451416 s.
  id  level        title                       text_unit_ids                    relationship_ids
0  0      0  Community 0  [8dbd1064152be7725b60725b36c34c80]  [d3835bf3dda84ead99deadbeac5d0d7d]
SummaryCounters{relationships_created: 3, properties_set: 1, contains_updates: True, contains_system_updates: False}
1 rows in 0.42505335807800293 s.
                                     id human_readable_id  ...                        document_ids n_tokens
0  4d5db4ef-c2de-49f4-84d7-f137281ea7f1                 1  ...  [05ee4c187aa5f6f8bb045d4b7aeea22d]       19

[1 rows x 16 columns]
SummaryCounters{labels_added: 1, relationships_created: 1, nodes_created: 1, properties_set: 12, contains_updates: True, contains_system_updates: False}
1 rows in 0.20915699005126953 s.

(graphrag-env) D:\zyt\git_ln\GraphragTest\rageasy\utils>