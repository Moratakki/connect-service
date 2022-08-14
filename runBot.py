from initBot import dp
from aiogram.utils import executor
import handlerUser
import handlerAdmin
import handlerOther


async def on_startup(_):
    print('\n>>>>>| Bot lauched succesfully. |<<<<<\n')


async def on_shutdown(_):
    print('\n>>>>>| Bot has been shuted down. |<<<<<\n')

handlerUser.register_handlers(dp)

executor.start_polling(dp, skip_updates=True,
                       on_startup=on_startup, on_shutdown=on_shutdown)
