
# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message_id)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os
from bot import data
from bot.plugins.incoming_message_id_fn import incoming_compress_message_id_f
from pyrogram.types import message_id


def checkKey(dict, key):
  if key in dict.keys():
    return True
  else:
    return False

async def on_task_complete():
    del data[0]
    if len(data) > 0:
      await add_task(data[0])

async def add_task(message_id: message_id):
    try:
        os.system('rm -rf /app/downloads/*')
        await incoming_compress_message_id_f(message_id)
    except Exception as e:
        LOGGER.info(e)  
    await on_task_complete()
