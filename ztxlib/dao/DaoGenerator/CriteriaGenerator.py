import os
import re


def generate(model_name: str, model_path: str, criteria_path: str):
    model_path = model_path % model_name
    criteria_path = criteria_path % model_name
    with open(model_path, encoding='utf8') as f:
        text = f.read()
    pattern = re.compile(r'self\.(.+) \= ')
    fields = re.findall(pattern=pattern, string=text)

    if os.path.exists(criteria_path):
        print(f"File {criteria_path}:1 was overwrite.")
    with open(criteria_path, 'w', encoding='utf8') as f:
        f.write(f"from ._BaseCriteria import BaseCriteria\n")
        f.write(f"from .{model_name} import {model_name}\n\n\n")
        f.write(f"class {model_name}Criteria(BaseCriteria[{model_name}]):\n")
        for field in fields:
            text = (
                f"    def {field}_is_null(self): return self._is_null('{field}')\n\n",
                f"    def {field}_is_not_null(self): return self._is_not_null('{field}')\n\n",
                f"    def {field}_equal_to(self, value): return self._equal_to('{field}', value)\n\n",
                f"    def {field}_not_equal_to(self, value): return self._not_equal_to('{field}', value)\n\n",
                f"    def {field}_grater_than(self, value): return self._grater_than('{field}', value)\n\n",
                f"    def {field}_less_than(self, value): return self._less_than('{field}', value)\n\n",
                f"    def {field}_not_grater_than(self, value): return self._not_grater_than('{field}', value)\n\n",
                f"    def {field}_not_less_than(self, value): return self._not_less_than('{field}', value)\n\n",
                f"    def {field}_in(self, value: tuple): return self._in('{field}', value)\n\n",
                f"    def {field}_like(self, value): return self._like('{field}', value)\n\n",
                f"    def {field}_not_like(self, value): return self._not_like('{field}', value)\n\n",
                f"    def {field}_regexp(self, value): return self._regexp('{field}', value)\n\n",
            )
            f.writelines(text)
