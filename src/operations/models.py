from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey

metadata = MetaData()


question = Table(
    "question",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("answer1", String, nullable=False),
    Column("answer2", String, nullable=False),
    Column("answer3", String, nullable=False),
    Column("answer4", String, nullable=False),
    Column("answer5", String, nullable=False)
)

research = Table(
    "research",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("total_question", Integer, nullable=False),
    Column("start_date", TIMESTAMP, default=datetime.utcnow),
    Column("finish_date", TIMESTAMP, default=datetime.utcnow),
    Column("question_id", Integer, ForeignKey(question.c.id))
)
