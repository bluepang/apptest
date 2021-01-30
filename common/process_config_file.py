import yaml
import os


config_file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'conf/config.yaml'
)


def get_config(*args):
    f = open(r'{}'.format(config_file_path))
    y = yaml.load(f, Loader=yaml.FullLoader)
    # print(args)
    length = len(args)
    for i in range(length):
        y = y.get(args[i])
    return y


def set_config(dict):
    with open(config_file_path, 'r') as f:
        result = f.read()

    result_dict = yaml.load(result, Loader=yaml.FullLoader)
    for k, v in dict.items():
        result_dict[k] = v

    with open(config_file_path, 'w') as f:
        yaml.dump(result_dict, f)


if __name__ == '__main__':
    print(get_config('host', 'host_test'))