import logging
from initBot import dp
from aiogram.utils import executor
import handlerApplicant
import handlerVolunteer
import handlerOther


logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('\n>>>>>| Bot lauched succesfully. |<<<<<\n')


async def on_shutdown(_):
    print('\n>>>>>| Bot has been shuted down. |<<<<<\n')

handlerVolunteer.register_volunteer_handlers(dp)
handlerApplicant.register_applicant_handlers(dp)
handlerOther.register_other_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
