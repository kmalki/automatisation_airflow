# **Airflow Automationsation**

Ce repos recense le DAG, ainsi que les scripts Python et jobs Spark lancés dans ce DAG.
Pour le moment, une erreur d'accès à Hive font planter les jobs Spark lors de la tentative d'insertion en base. Une première erreur nous bloquait car le job ne retrouvait pas la base Hive, mais après avoir passé le thrift du metadata store uris Hive, elle s'est résolue et a laissé place à une autre erreur, que nous n'arrivons pas à régler :

`[2020-12-11 15:22:53,690] {bash_operator.py:157} INFO - 	 diagnostics: User class threw exception: org.apache.spark.sql.AnalysisException: org.apache.hadoop.hive.ql.metadata.HiveException: Unable to fetch table spotify_playlists. Invalid method name: 'get_table_req';
`
C'est la seule étape bloquante des jobs Spark et donc du DAG.

Les étapes de récupération de récupération des données brutes de Spotify, à l'écriture dans Hive en passant par la case transformation en parquet sont fonctionnelles.

Les jobs ont été testés sur notre edgenode et sont fonctionnels à 100%.

Le DAG est plannifié tous les jours à 7H00, mais désactivé.
