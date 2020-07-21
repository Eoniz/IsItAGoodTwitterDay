from os.path import join

import yaml

from itagtd.infrastructure.entity.configuration import Secrets, Public


class Configuration:
    secrets: Secrets = None
    public: Public = None

    def __init__(
            self, *,
            root: str = None,
            public_path: str = None,
            secrets_path: str = None
    ):
        if public_path is None:
            public_path = "public_dev.yml"

        if secrets_path is None:
            secrets_path = "secrets_dev.yml"

        with open(join(root, public_path)) as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)

            self.public = Public(**(doc or {}))

        with open(join(root, secrets_path)) as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)

            self.secrets = Secrets(**(doc or {}))
