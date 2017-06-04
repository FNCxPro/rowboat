from holster.enum import Enum

from rowboat.types import Model, SlottedModel, Field, DictField, text, raw, rule_matcher

CooldownMode = Enum(
    'GUILD',
    'CHANNEL',
    'USER',
)


class PluginConfigObj(object):
    client = None


class PluginsConfig(Model):
    def __init__(self, inst, obj):
        self.client = None
        self.load_into(inst, obj)

    @classmethod
    def parse(cls, obj, *args, **kwargs):
        inst = PluginConfigObj()
        cls(inst, obj)
        return inst


class CommandOverrideConfig(SlottedModel):
    disabled = Field(bool, default=False)
    level = Field(int)


class CommandsConfig(SlottedModel):
    prefix = Field(str, default='')
    mention = Field(bool, default=False)
    overrides = Field(raw)

    def get_command_override(self, command):
        return rule_matcher(command, self.overrides or [])
    
class TagConfig(SlottedModel):
    embed = Field(bool, default=False)
    title = Field(str, default='')
    description = Field(str, default='')
    message = Field(str, default='')

class GuildConfig(SlottedModel):
    nickname = Field(text)
    commands = Field(CommandsConfig, default=None, create=False)
    levels = DictField(int, int)
    plugins = Field(PluginsConfig.parse)
    tags = DictField(TagConfig)
