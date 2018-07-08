from configman import (
    RequiredConfig,
    ConfigurationManager,
    Namespace,
)


class DBConfig(RequiredConfig):
    required_config = Namespace()
    required_config.add_option(
        name='url',
        default='localhost:9200',
        doc='Specify the database url address'
    )


class LoggerConfig(RequiredConfig):
    required_config = Namespace()
    required_config.add_option(
        name='level',
        default='INFO',
        doc='Logging level'
    )
    required_config.add_option(
        name='format',
        default='%(levelname) -10s %(asctime)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s',
        doc='Logging level'
    )


class ServerConfig(RequiredConfig):
    required_config = Namespace()
    required_config.add_option(
        name='hostport',
        default='[::]:9090',
        doc='Specify the host and port to listen to'
    )
    required_config.add_option(
        name='max_workers',
        default=1,
        doc='Specify the max number of gRPC server workers'
    )


class Config(RequiredConfig):
    required_config = Namespace()
    required_config.server = ServerConfig.get_required_config()
    required_config.log = LoggerConfig.get_required_config()
    required_config.db = DBConfig.get_required_config()


def get_config_manager(definition_source=None, config_dict=None):
    cm_args = {
        'definition_source': [definition_source.get_required_config()],
    }
    if config_dict is not None:
        cm_args.update({'values_source_list': [config_dict]})

    return ConfigurationManager(**cm_args)


def parse_config(config_dict):
    cm = get_config_manager(definition_source=Config, config_dict=config_dict)
    return cm.get_config()
