import twitchAPI.type
import twitchAPI.twitch
from twitchAPI.chat import Chat, EventData, ChatCommand

from dotenv import load_dotenv
from pathlib import Path
import os
import asyncio



load_dotenv(Path(__file__).resolve().parents[2] / "config" / ".env")

APP_ID = os.getenv("TWITCH_CLIENT_ID")
APP_KEY = os.getenv("TWITCH_API_KEY")
access_token, refresh_token = os.getenv("TWITCH_ACCESS_TOKEN_NE0N"), os.getenv("TWITCH_REFRESH_TOKEN_NE0N")

TARGET_CHANNEL = "ne0nflyers"

SCOPE = [twitchAPI.type.AuthScope.CHANNEL_READ_SUBSCRIPTIONS]

def update_env(values, file=".env"):
    path = Path(file)
    lines = path.read_text().splitlines()

    for key, value in values.items():
        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}"
                break
        else:
            lines.append(f"{key}={value}")

    path.write_text("\n".join(lines) + "\n")

async def print_subscribers(api):
    async for user in api.get_users(logins=[TARGET_CHANNEL]):
        broadcaster_id = user.id
        break

    subs = await api.get_broadcaster_subscriptions(broadcaster_id)

    print(f"Total subscribers: {subs.total}")

    for sub in subs.data:
        print(f"User: {sub.user_name} | Tier: {sub.tier} | Is gift: {sub.is_gift}")

async def run_bot():
    global access_token, refresh_token

    # Create the api
    api = await twitchAPI.twitch.Twitch(APP_ID, APP_KEY)
    api.get_broadcaster_subscriptions
    
    # Try old token
    try:
        await api.set_user_authentication(access_token, SCOPE, refresh_token)

    # Token failed, refresh
    except twitchAPI.type.TwitchAPIException:
        access_token, refresh_token = await api.refresh_used_token(refresh_token)

        update_env({"TWITCH_ACCESS_TOKEN_NE0N": access_token, "TWITCH_REFRESH_TOKEN_NE0N": refresh_token})

        await api.set_user_authentication(access_token, SCOPE, refresh_token)

    await print_subscribers(api)

asyncio.run(run_bot())