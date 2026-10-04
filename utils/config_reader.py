import configparser 

def get_config():
    parser = configparser.ConfigParser()
    parser.read('config.ini')

    return parser ["API_SETTINGS"]