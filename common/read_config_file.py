import yaml
import os


config_file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'config.yaml'
)


def get_config(*args):
    f = open(r'{}'.format(config_file_path))
    y = yaml.load(f, Loader=yaml.FullLoader)
    # print(args)
    length = len(args)
    for i in range(length):
        y = y.get(args[i])
    return y


if __name__ == '__main__':
    print(get_config('host', 'host_test'))