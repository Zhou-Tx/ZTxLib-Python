import os

import CriteriaGenerator
import MapperGenerator
import ModelGenerator
import yaml

current_file = os.path.abspath(__file__)
directory = os.path.dirname(current_file)

with open(os.path.join(directory, 'config.yml'), 'rb') as f:
    config = yaml.safe_load(f)
mysql = config['mysql']
tables = config['tables']
directory = os.path.abspath(config['directory'])


def main():
    for table_name in tables:
        model_name = ''.join([word[0].upper() + word[1:] for word in table_name.split('_')])
        model_path = os.path.join(directory, f"%s.py")
        criteria_path = os.path.join(directory, f"%sCriteria.py")
        mapper_path = os.path.join(directory, f"%sMapper.py")
        ModelGenerator.generate(
            mysql=mysql,
            table_name=table_name,
            model_name=model_name,
            model_path=model_path,
        )
        CriteriaGenerator.generate(
            model_name=model_name,
            model_path=model_path,
            criteria_path=criteria_path,
        )
        MapperGenerator.generate(
            table_name=table_name,
            model_name=model_name,
            mapper_path=mapper_path
        )


if __name__ == '__main__':
    main()