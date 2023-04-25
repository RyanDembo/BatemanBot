import asyncio
import discord
import os
import wavelink
import random
import logging
from discord import Message

from Config import TOKEN
from Config import SECRET
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.voice_states = True

#Queue = wavelink.BaseQueue()

bot = commands.Bot(command_prefix='!', intents=intents)
voice_client = None
Node_id = None


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.event
async def setup_hook() -> None:
    # Wavelink 2.0 has made connecting Nodes easier... Simply create each Node
    # and pass it to NodePool.connect with the client/bot.
    node: wavelink.Node = wavelink.Node(uri='http://localhost:2333', password=SECRET)
    await wavelink.NodePool.connect(client=bot, nodes=[node])


@bot.event
async def on_wavelink_node_ready(node: wavelink.Node) -> None:
    print(f"Node {node.id} is ready!")


# @bot.event
# async def on_wavelink_track_start(payload: wavelink.TrackEventPayload):
# now playing msg


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # if message.content.startswith(f'<@{bot.user.id}> !roll'):
    #   print("activated roll")
    #    await message.channel.send(get_roll())
    if message.content.startswith(f'<@{bot.user.id}>'):
        print("activated quote")
        await message.channel.send(get_quote())
    await bot.process_commands(message)


@bot.command(name='roll')
async def rolling(ctx):
    print("activated roll")
    await ctx.send(get_roll())


def get_roll():
    quotes = [
        'You got a negative attitude. That\'s what\'s stopping you. ',
        'Yes Allen.',
        'No, Allen.',
        'I don\'t know. I don\'t have anything in common with you. ',
        'Get a goddamn job, Al. ',
        'Not if you want to keep your spleen. ',
        'Another martini, Paul ?',
        'Tell him I\'m at lunch. ',
        'Yes, always tip the stylist 15 percent. ',
        'Just say "no" ',
        'No, don\'t tip the owner of the salon. ',
        'So, what\'s the, uh, topic of discussion ?',
        'I\'m at a loss.',
        'I hope I\'m not being cross-examined here ',
        'Listen, you\'ll have to excuse me. I have a lunch meeting with Cliff Huxtable at Four Seasons in 20 minutes. ',
        'I\'ve gotta return some video tapes. ',
        'I\'m leaving. I\'ve assessed the situation, and I\'m going. '
    ]
    return random.choice(quotes)


def get_quote() -> str:
    rolls = [
        'Jesus, McDermott, what does that have to do with anything ?',
        'Not a menorah. You spin a dreidel. ',
        'Cool it with the anti-Semitic remarks. ',
        '''
My name is Patrick Bateman. 
I'm 27 years old.         
I believe in taking care of myself,         
in a balanced diet, in a rigorous exercise routine.         
ln the morning, if my face is a little puffy,         
I'll put on an icepack while doing my stomach crunches.         
I can do a thousand now.         
After I remove the icepack, I use a deeppore cleanser lotion.         
In the shower, I use a water-activated gel cleanser.         
Then a honey-almond bodyscrub.         
And on the face, an exfoliating gelscrub.         
Then I apply an herb mint facial masque,         
which leave on forteen minutes while I prepare the rest of my routine.         
I always use an aftershave lotion with little or no alcohol,         
because alcohol dries your face out and makes you look older.         
Then moisturizer, then an anti-aging eye balm,         
followed by a final moisturizing protective lotion. 
        ''',
        'I simply am not there.',
        'I occasionally box with Ricky at the Harvard Club. Anyone else ?',
        'Just say "no" ',
        'Don\'t wear that outfit again',
        '''I'm trying to listen to the new Robert Palmer tape, 
but Evelyn, my supposed fiance, keeps buzzing in my ear. ''',
        'No. I can\'t take the time off work.',
        'Because I want to fit in.',
        '''I'm on the verge of tears by the time we arrive at Espace, 
since I'm positive we won't have a decent table. 
But we do, and relief washes over me in an awesome wave. ''',
        '''Well, we have to end apartheid, for one, 
slow down the nuclear arms race, stop terrorism and world hunger. 
We have to provide food and shelter for the homeless... 
and oppose racial discrimination and promote civil rights, 
while also promoting equal rights for women. 
We have to encourage a return... 
to traditional moral values. 
Most importantly, 
we have to promote general social concern... 
and less materialism in young people. ''',
        'I have a lunch meeting at Hubert\'s in 20 minutes with Ronald Harrison. '
        '''I need those sheets cleaned by this afternoon. 
Listen, I can't understand you ! This is crazy ! You're a fool. 
I can't cope with this stupid "bitchee" ! Understand ?''',
        '''You know, Courtney, you should take some more lithium or have a Diet Coke.
Some caffeine might get you out of this slump.''',
        'Your compliment was sufficient, Luis. ',
        'New card. What do you think ? ',
        'That\'s bone. And the lettering is something called Silian Rail. ',
        'Let\'s see Paul Allen\'s card. ',
        'Look at that subtle off-white coloring. The tasteful thickness of it. Oh, my God. It even has a watermark. ',
        'Get a goddamn job, Al. ',
        'Why don\'t you get a job ? If you\'re so hungry, why don\'t you get a job ? ',
        'You got a negative attitude. That\'s what\'s stopping you. ',
        'I think my mask of sanity is about to slip. ',
        'Hey, Hamilton. Have a holly, jolly Christmas. ',
        'Hey, I\'m a child of divorce. Give me a break. ',
        'I see they\'ve omitted the pork loin with lime Jell-O.',
        'Is that Ivana Trump ? ',
        'I like to dissect girls. Did you know I\'m utterly insane ',
        'Another martini, Paul ?',
        '''You like Huey Lewis and the News ? 
They're early work was a little too new wave for my taste. 
But when Sports came out in '83, 
I think they really came into their own, commercially and artistically. 
The whole album has a clear, crisp sound, 
and a new sheen of consummate professionalism... 
that really gives the songs a big boost. 
He's been compared to Elvis Costello, 
but I think Huey has a far more bitter, cynical sense of humor. ''',
        '''In '87, Huey released this-- 
Fore, their most accomplished album. 
I think their undisputed masterpiece is "Hip To Be Square." 
The song's so catchy, most people probably don't listen to the lyrics. 
But they should, because it's not just about... 
the pleasures of conformity and the importance of trends. 
It's also a personal statement about the band itself. Hey, Paul !''',
        '''There is a moment of sheer panic... 
when I realize that Paul's apartment overlooks the park... 
and is obviously more expensive than mine. ''',
        'He was part of that whole Yale thing.',
        '''Well, I think for one that he was probably a closet homosexual... 
who did a lot of cocaine. 
That "Yale thing." ''',
        'Listen, you\'ll have to excuse me. I have a lunch meeting with Cliff Huxtable at Four Seasons in 20 minutes. ',
        'Don\'t just stare at it. Eat it. ',
        'Is that all you ever have to contribute, Van Patten ? "What about fucking dinner" ? ',
        'I\'ve gotta return some video tapes. ',
        'We\'d gone to a new musical... called Oh, Africa, Brave Africa. It was a laugh riot. ',
        'Duct tape. I need it for, uh, taping something. ',
        '''Did you know... 
that Whitney Houston's debut LP...      
called simply Whitney Houston... 
had four number-one singles on it ? ''',
        'I\'m in touch with humanity. '
    ]
    return random.choice(rolls)


def format_duration(duration_ms):
    """Returns formatted string of song time with input of milliseconds
    bool at the end returns if hours are included
    """
    duration_ms = int(duration_ms)
    seconds, milliseconds = divmod(duration_ms, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}", True
    else:
        return f"{minutes:02d}:{seconds:02d}", False


@bot.command()
async def play(ctx: commands.Context, *, search: str, ) -> None:
    """Simple play command."""
    author = ctx.message.author
    voice_state = author.voice

    if not voice_state or not voice_state.channel:
        await ctx.send("Get in the Voice Channel")
    if not ctx.voice_client:
        # makes new player when joining voice
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    else:
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild.id)

        if player is None:
            vc: wavelink.Player = ctx.voice_client
        else:
            vc: wavelink.Player = player

    vc.autoplay = True
    # get track
    track = await wavelink.YouTubeTrack.search(search, return_first=True)
    if not track:
        await ctx.send("Could not find song")

    # await vc.queue.put_wait(track)

    if vc.current and vc.is_playing():
        await vc.queue.put_wait(track)
        await ctx.send(f"Adding {track.title} to queue!")

    else:
        # await ctx.send("Playing track now!")
        try:
            await vc.play(track, replace=False, populate=True)
        except Exception as e:
            await ctx.send('something went wrong')
            logging.exception("An exception occurred: %s", str(e))
            return

        durationStr, isHours = format_duration(track.length)
        if isHours:
            mbed = discord.Embed(title=f"Now Playing... {track.title}", url=track.uri,
                                 description=f"[0:00:0 / {durationStr}]")
        else:
            mbed = discord.Embed(title=f"Now Playing... {track.title}", url=track.uri,
                                 description=f"[0:00 / {durationStr}]")
        await ctx.send(embed=mbed)


@bot.command()
async def playlist(ctx: commands.Context, *, search: str, ) -> None:
    """///////Under construction////////
                """
    author = ctx.message.author
    voice_state = author.voice

    if not voice_state or not voice_state.channel:
        await ctx.send("Get in the Voice Channel")
    if not ctx.voice_client:
        # makes new player when joining voice
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    else:
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild.id)

        if player is None:
            vc: wavelink.Player = ctx.voice_client
        else:
            vc: wavelink.Player = player

    vc.autoplay = True
    q = vc.queue
    # get tracks from playlist
    yt_playlist = await wavelink.YouTubePlaylist.search(search)
    tracks = yt_playlist.tracks
    random.shuffle(tracks)
    if not tracks:
        await ctx.send("Could not find playlist")
        return

    if vc.current and vc.is_playing():
        q.extend(tracks, atomic=False)
        await ctx.send(f"Adding playlist {yt_playlist.name} to queue!")
        return

    else:

        # populate queue
        q.extend(tracks, atomic=False)
        track = q.pop()
        await vc.play(track, populate=True, replace=False)

        durationStr, isHours = format_duration(track.length)
        if isHours:
            mbed = discord.Embed(title=f"Now Playing... {track.title}", url=track.uri,
                                 description=f"[0:00:0 / {durationStr}]")
        else:
            mbed = discord.Embed(title=f"Now Playing... {track.title}", url=track.uri,
                                 description=f"[0:00 / {durationStr}]")
        await ctx.send(embed=mbed)


@bot.command()
async def stop(ctx: commands.Context) -> None:
    """stops the song playing and empties the queue"""

    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)

    if player:
        await player.stop()
        q = player.queue
        q.reset()

    else:
        await ctx.send("There is no connected player")


@bot.command()
async def skip(ctx: commands.Context) -> Message | None:
    """skips current song
            """
    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)

    if player:
        q = player.queue
        if q.is_empty:
            return await player.stop()
        else:
            if player.current:
                await ctx.send(f"skipped {player.current.title}")
            # await player.stop()
            #print(q)

            await player.play(q.get(), populate=True, replace=True)
            return await ctx.send(f"now playing {player.current.title}")

    else:
        return await ctx.send("There is no connected player")


@bot.command()
async def st(ctx: commands.Context) -> None:
    """stop command
               """
    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)

    if player:
        try:
            await player.stop()
        except:
            await ctx.send('Somthing went wrong')

    else:
        await ctx.send('No connected player')


@bot.command()
async def q(ctx: commands.Context) -> None:
    """Displays contents of the queue
        """
    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)

    if player:
        q = player.queue
        if q.is_empty:
            await ctx.send("The queue is empty")
        else:

            queue_str = "\n".join([f"{i + 1}. {track.title}" for i, track in enumerate(q, start=0) if i < 5])
            await ctx.send(f"Queue:\n{queue_str}")
    else:
        await ctx.send("There is no connected player")


@bot.command()
async def np(ctx: commands.Context) -> None:
    """Now playing command
        """
    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)
    if not player:
        await ctx.send("There is no connected player")
    if not player.current:
        await ctx.send("There is no Song playing")
    else:
        curtime, temp = format_duration(player.position)
        endtime, isHours = format_duration(player.current.length)

        await ctx.send(f"Now Playing {player.current.title} \n [{curtime} / {endtime}] \n {player.current.uri}")


@bot.command()
async def pause(ctx: commands.Context) -> None:
    """Pause command
           """
    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)

    try:
        await player.pause()
    except:
        await ctx.send('Somthing went wrong')


@bot.command()
async def resume(ctx: commands.Context, ) -> None:
    """Resumes playing from paused state
           """
    node = wavelink.NodePool.get_node()
    player = node.get_player(ctx.guild.id)
    try:
        await player.resume()
    except:
        await ctx.send('Somthing went wrong')


@bot.command()
async def disc(ctx: commands.Context) -> None:
    """Simple disconnect command.

    This command assumes there is a currently connected Player.
    """
    vc: wavelink.Player = ctx.voice_client
    await vc.disconnect()


# bot.run(os.getenv('DISCORD_TOKEN'))
bot.run(TOKEN)
