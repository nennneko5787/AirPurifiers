import asyncio
import os

import dotenv
import discord
from discord.ext import commands

dotenv.load_dotenv()

bot = commands.Bot("ap#")


@bot.command(
    name="seijou", aliases=["s"], description="ボイスチャンネルの空気を清浄します。"
)
async def airPurifierCommand(
    ctx: commands.Context, channel: discord.VoiceChannel = None
):
    if not channel:
        if ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        else:
            channel = bot.get_channel(1252411440892215307)

    voiceClient: discord.VoiceClient = ctx.voice_client
    if not voiceClient:
        voiceClient: discord.VoiceClient = await channel.connect(self_deaf=True)

        loop = asyncio.get_event_loop()

        def after(e: Exception):
            asyncio.run_coroutine_threadsafe(voiceClient.disconnect(), loop=loop)

        voiceClient.play(
            discord.FFmpegPCMAudio("./Air_Purifier01-mp3/Air_Purifier01-01(Mid).mp3"),
            after=after,
        )
    else:
        voiceClient.source = discord.FFmpegPCMAudio(
            "./Air_Purifier01-mp3/Air_Purifier01-01(Mid).mp3"
        )


@bot.command(name="poweroff", aliases=["po"], description="スイッチオフ")
async def powerOffCommand(ctx: commands.Context):
    if not ctx.voice_client:
        return
    voiceClient: discord.VoiceClient = ctx.voice_client
    voiceClient.source = discord.FFmpegPCMAudio(
        "./Air_Purifier01-mp3/Air_Purifier01-07(Beep).mp3"
    )


bot.run(os.getenv("discord"))
