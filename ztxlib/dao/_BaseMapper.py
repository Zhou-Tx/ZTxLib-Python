from abc import ABCMeta
from typing import Generic, TypeVar

from ztxlib import aiomysql

from ._BaseCriteria import BaseCriteria

_T = TypeVar('_T')


class BaseMapper(Generic[_T], metaclass=ABCMeta):
    __abstract__ = True
    table_name: str
    mysql: aiomysql.MySQL

    async def insert(self, row: _T) -> int:
        data = {
            attr: row.__getattribute__(attr)
            for attr in dir(row)
            if attr[0] != '_' and row.__getattribute__(attr) is not None
        }
        sql = "insert into %s(%s) values (%s)" % (
            self.table_name,
            ','.join([f"`{field}`" for field in data.keys()]),
            ','.join([f"%({field})s" for field in data.keys()]),
        )
        return await self.mysql.execute(sql, data)

    async def delete(self, criteria: BaseCriteria[_T]) -> int:
        criteria = criteria()
        sql = "delete from %s %s" % (
            self.table_name,
            criteria[0]
        )
        return await self.mysql.execute(sql, criteria[1])

    async def update(self, row: _T, criteria: BaseCriteria[_T]) -> int:
        data = {
            attr: row.__getattribute__(attr)
            for attr in dir(row)
            if attr[0] != '_' and row.__getattribute__(attr) is not None
        }
        if len(data) == 0:
            return 0
        criteria = criteria()
        sql = "update %s set %s %s" % (
            self.table_name,
            ','.join([
                f"{field} = %({field})s"
                for field in data.keys()
            ]),
            criteria[0]
        )
        data.update(criteria[1])
        return await self.mysql.execute(sql, data)

    async def select(self, criteria: BaseCriteria[_T]) -> list[_T]:
        criteria = criteria()
        sql = f"select * from {self.table_name} %s" % criteria[0]
        result = await self.mysql.fetchall(sql, criteria[1])
        return [_T(row) for row in result]

    async def count(self, criteria: BaseCriteria[_T]) -> int:
        criteria = criteria()
        sql = f"select count(*) as count from {self.table_name} %s" % criteria[0]
        result = await self.mysql.fetchone(sql, criteria[1])
        return result['count']
