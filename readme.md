# **Airflow Automationsation**

Ce repos recense le DAG, ainsi que les scripts Python et jobs Spark lancés dans ce DAG.
Pour le moment, une erreur d'accès à Hive font planter les jobs Spark lors de la tentative d'insertion en base.

`[2020-12-11 15:22:53,690] {bash_operator.py:157} INFO - 	 diagnostics: User class threw exception: org.apache.spark.sql.AnalysisException: org.apache.hadoop.hive.ql.metadata.HiveException: Unable to fetch table spotify_playlists. Invalid method name: 'get_table_req';
`

Les jobs ont été testé sur notre edgenode et sont fonctionnels.

Le DAG est plannifié tous les jours à 7H00, mais désactivé.