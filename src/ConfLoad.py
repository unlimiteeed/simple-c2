import yaml

def LoadConfigFile():
    with open("config/config.yaml") as configuration:
        c = yaml.safe_load(configuration)
        Host = c['Host']['IP-adder']
        Port = c['Host']['Port']
        return Host,Port

