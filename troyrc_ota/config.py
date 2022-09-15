import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="troyrc_ota",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="troyrc_ota_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from troyrc_ota.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export troyrc_ota_KEY=value
export troyrc_ota_KEY="@int 42"
export troyrc_ota_KEY="@jinja {{ this.db.uri }}"
export troyrc_ota_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
troyrc_ota_ENV=production troyrc_ota run
```

Read more on https://dynaconf.com
"""
