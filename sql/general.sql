UNLOAD ('select column from table')
TO 's3://<location>'
WITH CREDENTIALS AS 'aws_access_key_id=<aws_access_key_id>;
aws_secret_access_key=<aws_secret_access_key>'
PARQUET
