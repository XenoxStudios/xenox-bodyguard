import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents = nextcord.Intents().all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

logging = True
logschannel = INPUT_LOG_CHANNEL_ID

@bot.slash_command()
async def test(interaction: nextcord.Interaction, user: nextcord.Member):
    await interaction.response.send_message(f"{user.mention}")

@bot.slash_command()
async def kick(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:  # Corrected this line
        await interaction.response.send_message("You are not authorised to run this command.", ephemeral=True)
    else:
        await interaction.response.send_message(f"Kicked {user.mention}", ephemeral=True)  # Corrected this line
        if logging is True:
            log_channel = bot.get_channel(logschannel)
            await log_channel.send(f"{user.mention} Was kicked by {interaction.user.mention} for {reason}")
        await user.kick(reason=reason)

@bot.slash_command()
async def ban(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:  # Corrected this line
        await interaction.response.send_message("You are not authorised to run this command.", ephemeral=True)
    else:
        await interaction.response.send_message(f"Banned {user.mention}", ephemeral=True)  # Corrected this line
        if logging is True:
            log_channel = bot.get_channel(logschannel)
            await log_channel.send(f"{user.mention} Was banned by {interaction.user.mention} for **{reason}**")
        await user.ban(reason=reason)

@bot.slash_command()
async def unban(interaction: nextcord.Interaction, user_id: str, reason: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You are not authorized to run this command.", ephemeral=True)
        return

    try:
        # Check if the provided user_id is a valid integer
        if not user_id.isdigit():
            await interaction.response.send_message("Please provide a valid user ID.", ephemeral=True)
            return

        user = await bot.fetch_user(int(user_id))
        await interaction.guild.unban(user, reason=reason)
        await interaction.response.send_message(f"Unbanned {user.mention}", ephemeral=True)
        
        if logging:
            log_channel = bot.get_channel(logschannel)
            await log_channel.send(f"{user.mention} was unbanned by {interaction.user.mention} for **{reason}**")
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)



bot.run("INPUT_BOT_TOKEN")
