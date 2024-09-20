
create table news_articles (
	id int primary key,
	title TEXT,
	content TEXT
	)
Create extension vector;

CREATE TABLE document_embeddings (
    id int PRIMARY KEY,
    embedding vector(1536) NOT NULL
);
	