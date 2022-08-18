from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from initBot import bot, userDB, crsr
import initBot
from moderatorButtons import volunteerVerificationButtons
import handlerVolunteer
import handlerOther









async def volunteer_confirmation(vlnt, rowId):
    if not initBot.stopReceivingRequest[-1]:
        global volunteer_id
        global vlntRowId
        
        initBot.stopReceivingRequest.append(True)
        initBot.stopReceivingRequest.pop(-2)
        
        vlntRowId = rowId
        volunteer_id = vlnt[0]
        volunteer_data = f'''
        Юзернейм: {vlnt[1]}
        Полное имя: {vlnt[2]}
        Город: {vlnt[3]}
        Университет: {vlnt[4]}
        Факультет: {vlnt[5]}
        '''
        
        await bot.send_message(5412832211,
                            f'Добрый день. Поступила новая заявка на верификацию от волонтёра. Его данные:{volunteer_data}',
                            reply_markup=volunteerVerificationButtons)
        


async def volunteer_confirmation_iteration(vlnt, rowId):
    if rowId:
        global volunteer_id
        global vlntRowId
        
        vlntRowId = rowId
        volunteer_id = vlnt[0]
        volunteer_data = f'''
        Юзернейм: {vlnt[1]}
        Полное имя: {vlnt[2]}
        Город: {vlnt[3]}
        Университет: {vlnt[4]}
        Факультет: {vlnt[5]}
        '''
        
        await bot.send_message(5412832211,
                            f'Следующая заявка:{volunteer_data}',
                            reply_markup=volunteerVerificationButtons)
    else:
        initBot.stopReceivingRequest.append(False)
        initBot.stopReceivingRequest.pop(-2)
        vlntRowId = False
        
        
        
        
        
        


async def volunteer_accept(message: types.Message):
    volunteerStatus = crsr.execute("SELECT Confirmed FROM volunteers WHERE TelegramID = {}".format(volunteer_id)).fetchone()[0]
    print(f'Статус: {volunteerStatus}\nRow id: {vlntRowId}')
    if message.from_user.id == 5412832211 and volunteerStatus == 0 and vlntRowId:
        crsr.execute("UPDATE volunteers SET Confirmed = 1 WHERE TelegramID = {}".format(volunteer_id))
        userDB.commit()
        await message.answer('Заявка принята.', reply_markup=ReplyKeyboardRemove())
        await handlerVolunteer.accepted_request_notice(volunteer_id)
        volunteerData = initBot.crsr.execute("SELECT * FROM {}  WHERE rowid = {}".format('volunteers', vlntRowId+1)).fetchone()
        volunteerRowId = initBot.crsr.execute("SELECT rowid FROM {}  WHERE rowid = {}".format('volunteers', vlntRowId+1)).fetchone()
        print(volunteerData, volunteerRowId)
        
        await volunteer_confirmation_iteration(volunteerData, volunteerRowId)
    else:
        await handlerOther.other_messages(message)
    
    

async def volunteer_decline(message: types.Message):
    volunteerStatus = crsr.execute("SELECT Confirmed FROM volunteers WHERE TelegramID = {}".format(volunteer_id)).fetchone()[0]
    if message.from_user.id == 5412832211 and volunteerStatus == 0 and vlntRowId:
        crsr.execute("DELETE FROM volunteers WHERE TelegramID = {}".format(volunteer_id))
        userDB.commit()
        await message.answer('Заявка отклонена.', reply_markup=ReplyKeyboardRemove())
        await handlerVolunteer.declined_request_notice(volunteer_id)
        volunteerData = initBot.crsr.execute("SELECT * FROM {}  WHERE rowid = {}".format('volunteers', vlntRowId+1)).fetchone()
        volunteerRowId = initBot.crsr.execute("SELECT rowid FROM {}  WHERE rowid = {}".format('volunteers', vlntRowId+1)).fetchone()[0]
        await volunteer_confirmation(volunteerData, volunteerRowId)
    else:
        await handlerOther.other_messages(message)
    
def register_moderator_handlers(dp: Dispatcher):
    dp.register_message_handler(volunteer_accept, Text(equals="Принять", ignore_case=True))
    dp.register_message_handler(volunteer_decline, Text(equals="Отклонить", ignore_case=True))