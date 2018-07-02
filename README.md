# any url embedder for discord


is there are way to embed any kind of url in discord ? 
like a bot that you can pass any url to and it will embed it in to the discord like nothing happend :)


example of command would be like


.embed "insert_url_here"

.embed https://2018.javazone.no/program/92799046-8f4d-45ef-af0f-20767b8041f9


```python
embed = discord.Embed(title="Javazone", colour=discord.Colour(0x1e240), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```", timestamp=datetime.datetime.utcfromtimestamp(1530528450))

embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
embed.set_author(name="author name", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

embed.add_field(name="🤔", value="some of these properties have certain limits...")
embed.add_field(name="<:thonkang:219069250692841473>", value="these last two", inline=True)
embed.add_field(name="<:thonkang:219069250692841473>", value="are inline fields", inline=True)

await bot.say(embed=embed)
```