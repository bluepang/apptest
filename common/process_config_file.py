import yaml
import os


class Config(object):
    def __init__(self):
        self.config_file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
            'conf/config.yaml'
        )

    def __get_config(self, *args):
        f = open(r'{}'.format(self.config_file_path))
        y = yaml.load(f, Loader=yaml.FullLoader)
        length = len(args)
        for i in range(length):
            y = y.get(args[i])
        return y

    def get_platform(self):
        return self.__get_config('device_platform')

    def get_serial(self):
        return self.__get_config('device_serial')

    def get_wda_name(self):
        return self.__get_config('wda_app_name')

    def get_target_name(self):
        return self.__get_config('target_app_name')

    def get_target_url(self):
        return self.__get_config('target_app_url')

    def set_config(self, dict):
        with open(self.config_file_path, 'r') as f:
            result = f.read()

        result_dict = yaml.load(result, Loader=yaml.FullLoader)
        for k, v in dict.items():
            if v:
                result_dict[k] = v

        with open(self.config_file_path, 'w') as f:
            yaml.dump(result_dict, f)


if __name__ == '__main__':
    pass