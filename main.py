import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def get_service_implementiation(service_name, default=None):
    try:
        class_name = config["SERVICES"].get(service_name, default)
        module = __import__("services")
        class_ = getattr(module, class_name)
        return class_()
    except (AttributeError, ImportError) as e:
        print(e)
        return None

service_a_instance = get_service_implementiation("ServiceA")
service_b_instance = get_service_implementiation("ServiceB")

print(service_a_instance.execute())
print(service_b_instance.run())

