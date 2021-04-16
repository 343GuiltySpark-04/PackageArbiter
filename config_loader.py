import confuse


class LoadConfig:
    config = confuse.Configuration('PackageArbiter', __name__)

    config.set_file("/etc/packageArbiter/config.yaml")
