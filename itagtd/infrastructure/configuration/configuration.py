from os.path import join
from typing import Optional

import yaml
from pydantic import BaseModel

from itagtd.infrastructure.entity.configuration import Secrets, Public


class Configuration(BaseModel):
    secrets: Secrets = None
    public: Public = None
    project_root: str = None

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

            public = Public(**(doc or {}))

        with open(join(root, secrets_path)) as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)

            secrets = Secrets(**(doc or {}))

        super().__init__(
            project_root=root,
            secrets=secrets,
            public=public
        )


_configuration: Optional[Configuration] = None


def init_configuration(
        *,
        root: str = None,
        public_path: str = None,
        secrets_path: str = None
) -> Configuration:
    global _configuration
    _configuration = Configuration(
        root=root,
        public_path=public_path,
        secrets_path=secrets_path
    )

    return _configuration


def get_configuration() -> Configuration:
    global _configuration

    if not _configuration:
        raise ValueError("Configuration is not setted yet !")

    return _configuration
