import os
import shutil

import CriteriaGenerator
import MapperGenerator
import ModelGenerator
import yaml

current_file = os.path.abspath(__file__)
directory = os.path.dirname(current_file)

with open(os.path.join(directory, 'config.yml'), 'rb') as f:
    config = yaml.safe_load(f)
mysql = config['mysql']
switch = [config['switch'] ^ i == 0 for i in (1, 2, 4)]
tables = config['tables']

directory = os.path.dirname(directory)
base_model = os.path.join(directory, '_BaseModel.py')
base_criteria = os.path.join(directory, '_BaseCriteria.py')
base_mapper = os.path.join(directory, '_BaseMapper.py')

directory = os.path.abspath(config['directory'])
os.makedirs(directory, exist_ok=True)
if not os.path.isdir(directory):
    raise IOError

if switch[0]:
    shutil.copy(base_model, directory)
if switch[1]:
    shutil.copy(base_criteria, directory)
if switch[2]:
    shutil.copy(base_mapper, directory)


def main():
    model_path = os.path.join(directory, f"%s.py")
    criteria_path = os.path.join(directory, f"%sCriteria.py")
    mapper_path = os.path.join(directory, f"%sMapper.py")
    for table_name in tables:
        model_name = ''.join([word[0].upper() + word[1:] for word in table_name.split('_')])
        if switch[0]:
            ModelGenerator.generate(
                mysql=mysql,
                table_name=table_name,
                model_name=model_name,
                model_path=model_path,
            )
        if switch[1]:
            CriteriaGenerator.generate(
                model_name=model_name,
                model_path=model_path,
                criteria_path=criteria_path,
            )
        if switch[2]:
            MapperGenerator.generate(
                table_name=table_name,
                model_name=model_name,
                mapper_path=mapper_path
            )
        with open(os.path.join(directory, '__init__.py'), 'a') as f:
            if switch[0]:
                f.write(f"from .{model_name} import {model_name}\n")
            if switch[1]:
                f.write(f"from .{model_name}Criteria import {model_name}Criteria\n")
            if switch[2]:
                f.write(f"from .{model_name}Mapper import {model_name}Mapper\n")


if __name__ == '__main__':
    main()
