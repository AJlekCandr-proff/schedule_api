from dishka import Provider, Scope, provide

from sсhedule_api.application.config import Config


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_config(self, config: Config) -> Config:
        return config
