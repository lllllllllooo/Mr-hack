import telebot,requests,sqlite3,glob
from telebot import types
def en(num):
 num = str(num)
 return num.replace('1','q').replace('2','w').replace('3','e').replace('4','r').replace('5','t').replace('6','y').replace('7','u').replace('8','i').replace('9','o').replace('0','p')
def de(num):
 return num.replace('q','1').replace('w','2').replace('e','3').replace('r','4').replace('t','5').replace('y','6').replace('u','7').replace('i','8').replace('o','9').replace('p','0')
id = '5401818788'
open(f'H/H{id}.txt','w').write('oooo')
token = '5726249899:AAHYdrPEUwnAYJZDhKpSZq_YG1Ac0cQbfTU'
bot = telebot.TeleBot(token)
bot = telebot.TeleBot (token)
def ch(user_id):
   b=0
   a=[]
   f = open("ch.txt", "r")
   for huks in f:
    x = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{huks}&user_id={user_id}")
    
    if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
        pass
    else:
     return huks
def search_card(fam_nos, place):
  conn = sqlite3.connect(f"{place}(skidrow).sqlite")
  cursor = conn.cursor()

  print(fam_nos)
  card = f"'{fam_nos}'" if str(fam_nos)[0] ==("0") else f"{fam_nos}"

  hh=(f"SELECT * FROM PERSON WHERE FAM_NO = {card}")
  cursor.execute(hh)
  rows = cursor.fetchall()
  print(hh)
  column_names = [column[0] for column in cursor.description]
  data = []
  for row in rows:
        
        data_row = {}
        data.append(row)
  cursor.close()
  conn.close()

  return data
def search_person(first_name, father_name, grand_name, birth, place):
    conn = sqlite3.connect(f"{place}(skidrow).sqlite")
    cursor = conn.cursor()
    sql_command = f"SELECT * FROM PERSON WHERE P_FIRST LIKE '{first_name}%' AND P_FATHER LIKE '{father_name}%' AND P_GRAND LIKE '{grand_name}%' AND P_BIRTH LIKE '{birth}%'"
    print(sql_command)
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data_row = {} 
        data.append(row)
    cursor.close()
    conn.close()
    return data
@bot.message_handler(commands = ['start'])
def phone(message):
 kl = ch(message.from_user.id)
 if kl == None:
  if glob.glob(f'H/H{message.from_user.id}.txt'):
   u = open('pay.txt').read()
   key = types.InlineKeyboardMarkup()
   key.row_width = 2
   hUkS = de(open(f'H/H{message.from_user.id}.txt').read())
    
   a1 = types.InlineKeyboardButton(text="- اربيل 🛰️",callback_data='erbil;')
   a2 = types.InlineKeyboardButton(text="- الانبار 🛰️",callback_data="al-anbar;")
   a3 = types.InlineKeyboardButton(text="- النجف 🛰️",callback_data="najaf;")
   a4= types.InlineKeyboardButton(text="- بابل 🛰️",callback_data="babylon;")
   a5 = types.InlineKeyboardButton(text="- البصرة 🛰️",callback_data="basra;")
   a6 = types.InlineKeyboardButton(text="- دهوك 🛰️",callback_data="duhok;")
   a7 = types.InlineKeyboardButton(text="- ديالى 🛰️",callback_data='diyala;')
   a8 = types.InlineKeyboardButton(text="- ذي قار 🛰️",callback_data='dhiqar;')
   a9 = types.InlineKeyboardButton(text="- سليمانية🛰️",callback_data='sulaymaniyah;')
   a10 = types.InlineKeyboardButton(text="- صلاح الدين 🛰️",callback_data='salah-aldeen;')
   a11 = types.InlineKeyboardButton(text="- القادسية 🛰️",callback_data="qadisiya;")
   a12 = types.InlineKeyboardButton(text="- كربلاء 🛰️",callback_data="karbalaa;")
   a13 = types.InlineKeyboardButton(text="- كركوك 🛰️",callback_data="kirkuk;")
   a14 = types.InlineKeyboardButton(text="- المثنى 🛰️",callback_data="muthana;")
   a15 = types.InlineKeyboardButton(text="- ميسان 🛰️",callback_data="mesan;")
   a16 = types.InlineKeyboardButton(text="- نينوى 🛰️",callback_data="nineveh;")
   a17 = types.InlineKeyboardButton(text="- واسط 🛰️",callback_data="wasit;")
   a18 = types.InlineKeyboardButton(text="- بغداد 🛰️",callback_data="baghdad;")
   ah= types.InlineKeyboardButton(text=f"- محاولاتك ({hUkS}) .",callback_data="nothing")
   key.add(a1,a2,a3,a4,a5,a18,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,ah)
   if str(message.from_user.id)== id:
      hk = types.InlineKeyboardMarkup()
      hk.row_width =2
      ooi = open("pay.txt", "r")
      o = len(ooi.readlines())
      btn4 =types.InlineKeyboardButton(text="- اضافة محاولات .",callback_data="m7a")
      btn5 = types.InlineKeyboardButton(text="- مسح محاولات .",callback_data="delm7a")
      bt = types.InlineKeyboardButton(text=f"- ارسال القنوات الاجبارية .",callback_data='aj')
      btn = types.InlineKeyboardButton(text=f"- مسح قناة اجباري .",callback_data='delqn')
      btn1 = types.InlineKeyboardButton(text=f"- تفعيل قناة اجباري",callback_data='qn')
      btn3 = types.InlineKeyboardButton(text=f"- عدد المفعلين {o} .",callback_data='nothing')
      btn2 = types.InlineKeyboardButton(text="- ارسل التخزين .",callback_data="t5")
      hk.add(bt,btn2,btn,btn1,btn4,btn5,btn3)
      bot.reply_to(message,'- اهلا بك ايه المطور .',reply_markup=hk)
      bot.reply_to(message,'- اختر احد المحافظات واتبع التعليمات .',reply_markup=key)  
   elif str(message.from_user.id) in u:
      bot.reply_to(message,'- اختر احد المحافظات واتبع التعليمات .',reply_markup=key)
   else:
           keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True)
           button_phone = types.KeyboardButton (text = "ارسال ", request_contact = True)
           keyboard.add (button_phone)
           
           bot.send_message (message.chat.id, '''• مرحبا بك في البوت
  
  • يجب ان نتحقق من انك لست روبوت 💯
 
 - اضغط على الزر ادناه لكي اتحقق ذلك ...''', reply_markup = keyboard)
  else:
   bot.reply_to(message,'- تم اعطائك محاولتين محاولات للمزيد  راسل المطور @pf_vxv')
   open(f'H/H{message.from_user.id}.txt','w').write('w')
 else:bot.reply_to(message,f'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

    ‼️| اشترك ثم ارسل /start''')
@bot.callback_query_handler(func=lambda m:True)
def qu(call):
     kl = ch(call.from_user.id)
     if kl == None:
      if glob.glob(f'H/H{call.from_user.id}.txt'):
       if int(de(open(f'H/H{call.from_user.id}.txt','r').read())) >= 1:
        u = open('pay.txt').read()
        if str(call.message.chat.id) in u or str(call.message.chat.id) == id:
         
         if ';' in call.data:
          place = call.data.split(';')[0]
          h = bot.send_message(call.message.chat.id,'''يرجى كتابة الاسم الثلاثي مع او بدون المواليد مع دمج الاسم المركب او كتابة اول اسم😎''')
          bot.register_next_step_handler(h,huks, place)
         if ':' in call.data:
            hU= de(open(f'H/H{call.from_user.id}.txt').read())
            hUKs = en(int(hU)-1)
            open(f'H/H{call.from_user.id}.txt','w').write(f'{hUKs}')
            print(hUKs)
            bot.send_message(call.message.chat.id,'انتظر ...')
            place, fam_no = call.data.split(":")
            if fam_no == '':bot.reply_to(call.message,'لاتحاول وي عمك (:.')
            else:
             card_info = search_card(fam_no, place)
             message = """"""
             for row in card_info:
                 if place =='baghdad':
                  
                  h=row[2].replace("\x84", "")
                  u = row[3].replace("\x84", "")
                  ks=row[4].replace("\x84", "")
                  results = f"- الاسم : {h} {u} {ks}\n- مواليد : {row[6]}\n- رقم التموينيه : {row[1]}"
                  bot.send_message(call.message.chat.id, results)
                 else:
                  h=row[3].replace("\x84", "")
                  u = row[4].replace("\x84", "")
                  ks=row[5].replace("\x84", "")
                  results = f"- الاسم : {h} {u} {ks}\n- مواليد : {row[7]}\n- رقم التموينيه : {row[1]}"
                  bot.send_message(call.message.chat.id, results)

         if call.data == 'delqn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,delqna)
         if call.data == 'qn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,qna)
         if call.data =='delm7a':
          h=bot.send_message(call.message.chat.id,'- ارسل ايديه مع المحاولات الآن \n مثل : 123456:5.')
          bot.register_next_step_handler(h,delm7a)
         if call.data == 'tf':
            g= bot.send_message(call.message.chat.id,'- ارسل الايدي الي تريد تفعله .')
            bot.register_next_step_handler(g,hukss)
         if call.data == 'm7a':
          h=bot.send_message(call.message.chat.id,'- ارسل ايديه مع المحاولات الآن \n مثل : 123456:5.')
          bot.register_next_step_handler(h,m7a)
         if call.data == 'aj':
          bot.send_document(call.message.chat.id, open('ch.txt','rb'))
         if call.data == 't5':
            bot.send_document(call.message.chat.id, open('pay.txt','rb'))
        else:
         bot.answer_callback_query(call.id, f"- لازم تتحقق .", show_alert=True)
       else:bot.answer_callback_query(call.id,'- خلصوا محاولاتك راسل المطور او انتظره يجدد المحاولات \nالمطور : @pf_vxv', show_alert=True)
      else:bot.reply_to(call.message,'- ارسل /start وسيتم اعطائك محاولات .')
     else:bot.reply_to(call.message,f'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

    ‼️| اشترك ثم ارسل /start''')
def delm7a(message):
 id = (message.text).split(':')[0]
 m= int((message.text).split(':')[1])
 hy=int(de(open(f'H/H{id}.txt','r').read()))
 if m<=hy:
  m7=hy-m
 else:
  m7 = m-hy
 m7 = en(m7)
 print(m7);print(de(m7))
 open(f'H/H{id}.txt','w').write(m7)
def m7a(message):
 id = (message.text).split(':')[0]
 m7 = en((message.text).split(':')[1])
 print(m7)
 open(f'H/H{id}.txt','w').write(m7)
 bot.reply_to(message,f'- تم اضافة {(message.text).split(":")[1]} محاولة الى {id} بنجاح .')
def delqna(message):
 f = open("ch.txt", "r").read()
 HU=(f.replace(f'\n{message.text}',''))
 open('ch.txt','w').write(HU)
 bot.reply_to(message,f'تم حذف القناة {message.text} بنجاح .')
def qna(message):
 open('ch.txt','a').write(f'\n{message.text}')
 bot.reply_to(message,f'تم اضافة القناة {message.text} بنجاح .')
def hukss(message):
 bot.reply_to(message,'انتظر من فضلك ...')
 open('pay.txt','a').write(f'{message.text}\n')
 bot.send_message(message.chat.id,f'- تم التفعيل بنجاح ل{message.text}')
def huks(message, place):
 bot.reply_to(message,'انتظر  ...')
 n=message.text
 h = 0
 try :HUKs = n.split(' ')[3]
 except:HUKs = ''
 u = search_person(n.split(' ')[0],n.split(' ')[1],n.split(' ')[2],HUKs,place)
 for person in u:
     h+=1
     if place == 'baghdad':
      V=person[11]
      
     
      name = person[2] + " " + person[3] + " " +  person[4]
      print(person)
      all = f"""الاسم : {name}
 المواليد : {person[6]}
 رقم التموينية : {person[1]}
 محل الولادة : {V}
 
             """
      fam_no = person[1]
      markup = telebot.types.InlineKeyboardMarkup()
      btn_get_info = telebot.types.InlineKeyboardButton("جلب عائلة الشخص", callback_data=f"{place}:{fam_no}")
      markup.add(btn_get_info)
      bot.send_message(message.chat.id, all, reply_markup=markup)
     
     else:
      V=person[22]
      name = person[3] + " " + person[4] + " " +  person[5]
      print(person)
      all = f"""الاسم : {name}
 المواليد : {person[7]}
 رقم التموينية : {person[1]}
 محل الولادة : {V}
 
             """
      fam_no = person[1]
      markup = telebot.types.InlineKeyboardMarkup()
      btn_get_info = telebot.types.InlineKeyboardButton("جلب عائلة الشخص", callback_data=f"{place}:{fam_no}")
      markup.add(btn_get_info)
      bot.send_message(message.chat.id, all, reply_markup=markup)
 if h == 0:bot.reply_to(message,'- حبيبي تأكد من معلوماتك او من المواليد  للمساعدة : @pf_vxv')
 else:bot.send_message(message.chat.id,"- تم البحث في كل القاعدة .")  
 print(h)  
@bot.message_handler(func=lambda message: message.chat.type == 'private',content_types=['contact'])
def forward(message):
     uu=str(message.from_user.id)
     rp = open(f"pay.txt").read()
     if str(uu) in rp:
         print('')
     else:
         print(message.contact)
         if message.contact.user_id == message.from_user.id:
          bot.reply_to(message,'- ارسل /start .')
          rp=open("pay.txt","a").write(f"{message.from_user.id}\n")
          requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=- New one
 - رقمة : {message.contact.phone_number}
 - اسمة : {message.chat.first_name}
 - يوزرة : @{message.from_user.username}
 - ايدية : {message.from_user.id}
 - المبرمج : @pf_vxv''')
          
         else:bot.reply_to(message,'لاتحاول تتلاعب مع عمك xD .\n ارسل /start من جديد (:')
@bot.message_handler(func=lambda m: True)
def h(message):bot.reply_to(message,'- ارسل /start .')
bot.infinity_polling()
