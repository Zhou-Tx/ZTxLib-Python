#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/17
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from abc import ABCMeta
from typing import Generic, TypeVar

_T = TypeVar('_T')


class BaseCriteria(Generic[_T], metaclass=ABCMeta):
    __abstract__ = True

    criteria: list[tuple]

    def __call__(self) -> tuple[str, dict]:
        if len(self.criteria) == 0:
            return str(), dict()
        else:
            args = {
                f"_{index}": item[1]
                for index, item in enumerate(self.criteria)
            }
            where = 'where %s' % ' and '.join([
                '(%s)' % (item[0] % f"%(_{index})s")
                for index, item in enumerate(self.criteria)
            ])
            return where, args

    def _is_null(self, field: str):
        self.criteria.append((f"`{field}` is null",))
        return self

    def _is_not_null(self, field: str):
        self.criteria.append((f"`{field}` is not null",))
        return self

    def _equal_to(self, field: str, value):
        self.criteria.append((f"`{field}` = %s", value))
        return self

    def _not_equal_to(self, field: str, value):
        self.criteria.append((f"`{field}` <> %s", value))
        return self

    def _grater_than(self, field: str, value):
        self.criteria.append((f"`{field}` > %s", value))
        return self

    def _less_than(self, field: str, value):
        self.criteria.append((f"`{field}` > %s", value))
        return self

    def _not_grater_than(self, field: str, value):
        self.criteria.append((f"`{field}` <= %s", value))
        return self

    def _not_less_than(self, field: str, value):
        self.criteria.append((f"`{field}` >= %s", value))
        return self

    def _in(self, field: str, value: tuple):
        self.criteria.append((f"`{field}` in %s", value))
        return self

    def _like(self, field: str, value):
        self.criteria.append((f"`{field}` like %s", value))
        return self

    def _not_like(self, field: str, value):
        self.criteria.append((f"`{field}` not like %s", value))
        return self

    def _regexp(self, field: str, value):
        self.criteria.append((f"`{field}` regexp %s", value))
        return self
