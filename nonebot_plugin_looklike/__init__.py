from nonebot.plugin import on_keyword, PluginMetadata

from .utils import Look


usage: str = """

指令表:
    你看我像

""".strip()


__plugin_meta__ = PluginMetadata(
    name="你看我像",
    description="你看我像人吗?",
    usage=usage,
    type="application",
    homepage="https://github.com/tkgs0/nonebot-plugin-looklike",
    supported_adapters=None
)


look_like = on_keyword({"你看我像"}, priority=99, block=True)

@look_like.handle()
async def _():
    msg = Look.like()
    await look_like.finish(msg)
