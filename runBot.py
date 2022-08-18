import logging
import initBot
from aiogram.utils import executor
import handlerApplicant
import handlerVolunteer
import handlerOther
import userModerating


logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('\n>>>>>| Bot lauched succesfully. |<<<<<\n')


async def on_shutdown(_):
    print('\n>>>>>| Bot has been shuted down. |<<<<<\n')

handlerVolunteer.register_volunteer_handlers(initBot.dp)
handlerApplicant.register_applicant_handlers(initBot.dp)
userModerating.register_moderator_handlers(initBot.dp)
handlerOther.register_other_handlers(initBot.dp)

if __name__ == "__main__":
    executor.start_polling(initBot.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
