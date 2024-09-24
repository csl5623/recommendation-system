drop table IF EXISTS news_articles;
create table news_articles (
	id serial primary key,
	title TEXT,
	content TEXT
	);


drop table IF EXISTS  news_embeddings;
CREATE TABLE news_embeddings (
    id int PRIMARY KEY,
    embedding vector(1536) NOT NULL
);

CREATE INDEX ON news_embeddings USING hnsw (embedding vector_cosine_ops);
