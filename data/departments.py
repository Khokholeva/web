import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Departments(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'departments'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer,
                              sqlalchemy.ForeignKey("users.id"))
    chief_relate = orm.relation('User')
    members = sqlalchemy.Column(sqlalchemy.String,
                                nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)

    # а что привязывать к работе?

    def __repr__(self):
        return "<Department> {} {}".format(self.id, self.title)
