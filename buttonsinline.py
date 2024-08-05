from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup


menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kompyuter savodxonligi", callback_data="Komp_Savod"), InlineKeyboardButton(text="Microsoft Office darslari", callback_data="Microsoft_darslarri")],
        [InlineKeyboardButton(text="Kiber-xavfsizlik darslari", callback_data="kiber_xaf"),InlineKeyboardButton(text="Dasturlash", callback_data="Dasturlashsh")],
        [InlineKeyboardButton(text="Chet tillari", callback_data="cet_till"), InlineKeyboardButton(text="Tarmoq qurish (Cisco)", callback_data="Tarmoq_qurish")],
        [InlineKeyboardButton(text="Musiqa yaratish", callback_data="Musiqa_yaratish"), InlineKeyboardButton(text="Frilanserlik darslari", callback_data="Frilanserlik_darslari")],
        [InlineKeyboardButton(text="Grafik dizayn", callback_data="grafik_dizayn"), InlineKeyboardButton(text="Kopirayting/Mobilografiya", callback_data="kopirayting_mobilagrafiya")],
        [InlineKeyboardButton(text="3D modeling", callback_data="3d_modeling"), InlineKeyboardButton(text="Machine Learning (AI)", callback_data="maching_learning")],
        [InlineKeyboardButton(text="Video montaj", callback_data="video_mpontaj"), InlineKeyboardButton(text="1C bugalteriya", callback_data="1c_bugalter")],
        [InlineKeyboardButton(text="Sun'iy intellekt", callback_data="suniy_intelect"), InlineKeyboardButton(text="SMM va marketing", callback_data="smm__va_marketing")],
        [InlineKeyboardButton(text='Admin', url = 'https://t.me/Web_developer_UrDu'), InlineKeyboardButton(text="📊 Statistika", callback_data="/admin")],
    ],
)

Kompyuter_savodxonligi = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kompyuterni 0 dan o'rganish", callback_data="Kompyuterni_0_dan_organish"), InlineKeyboardButton(text="Windows o'rnatish", callback_data="windows_ornatish")],
        [InlineKeyboardButton(text="Windows zaruriy sozlamalari", callback_data="Windows_zarursiy_sozlamalar"), InlineKeyboardButton(text="Linux darslari", callback_data="Linux_darslari")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="ksavod_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Glavni")]
    ],
)

Kompyuterni_0_dan_organish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="0_dan1"), InlineKeyboardButton(text="3-4 dars", callback_data="0_dan2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="0_dan3"), InlineKeyboardButton(text="7-8 dars", callback_data="0_dan4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="0_dan5"), InlineKeyboardButton(text="11-12 dars", callback_data="0_dan6")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="0_dan12")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="0_dan_Orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data='0_dan_Glavni')]
    ],
)



Windows1 = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text="Windows 7 o'rnatish", callback_data="win7"), InlineKeyboardButton(text="Windows 10 o'rnatish", callback_data="win10")],
        [InlineKeyboardButton(text="Windows 11 o'rnatish", callback_data="win11")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="win1_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="win1_glavni")]
    ],
)

Windows7 = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Win7_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Win7_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Win7_3"), InlineKeyboardButton(text="7 dars", callback_data="Win7_4")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="win7_7dars")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="win7_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="win7_glavni")]
    ],
)


Windows10 = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="win10_1"), InlineKeyboardButton(text="3-4 dars", callback_data="win10_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="win10_3"), InlineKeyboardButton(text="7-8 dars", callback_data="win10_4")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="win10_8dars")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="win10_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="win10_glavni")]
    ],
)

Windows11 = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="win11_1")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="win11_2dars")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="win11_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="win11_glavni")]
    ],
)


Windows_zaruriy_sozlamalari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="winzarur_1"), InlineKeyboardButton(text="3-4 dars", callback_data="winzarur_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="winzarur_3"), InlineKeyboardButton(text="7-8 dars", callback_data="winzarur_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="winzarur_5"), InlineKeyboardButton(text="11-12 dars", callback_data="winzarur_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="winzarur_7"), InlineKeyboardButton(text="15 dars", callback_data="winzarur_8")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="win_zarur_15")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="winzarur_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="winzarur_glavni")]
    ],
    
)

Linux_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Linux_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Linux_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Linux_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Linux_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Linux_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Linux_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Linux_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Linux_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Linux_9"), InlineKeyboardButton(text="19 dars", callback_data="Linux_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Linux_dars_19")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Linux_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Linux_glavni")]
    ],
   
)


Microsoft_Office= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Word darslari", callback_data="Word_dars" ), InlineKeyboardButton(text="Excel darslari", callback_data="excele_dars")],
        [InlineKeyboardButton(text="Power Point darslari", callback_data="power_dars")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="microsoft_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="microsoft_glavni")]
    ],

)

Word_darslari = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="word_1"), InlineKeyboardButton(text="3-4 dars", callback_data="word_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="word_3"), InlineKeyboardButton(text="7-8 dars", callback_data="word_4")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Word_hammas")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="word_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="word_glavnii")]
    ],

)


Excel_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Excel 0 dan o'rganish", callback_data="Excele__dan0"), InlineKeyboardButton(text="Excelda formula va fuksiyalar", callback_data="Exele_formulaa")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="excele_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="excele_glavni")]
    ],

)

Excel_0_dan_organish= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Excele0_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Excele0_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Excele0_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Excele0_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Excele0_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Excele0_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Excele0_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Excele0_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Excele0_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Excele0_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Excele0_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Excele0_12")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Excele_0dan_hammas")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Excele0_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Excele0_glavni")]
    ],

)

Excelda_formula_va_fuksiyalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Excele_for_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Excele_for_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Excele_for_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Excele_for_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Excele_for_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Excele_for_6")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Excele_for_for")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Excele_for_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Excele_for_glavni")]
    ],

)

Power_Point_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Power_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Power_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Power_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Power_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Power_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Power_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Power_7"), InlineKeyboardButton(text="15 dars", callback_data="Power_8")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Power_12")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Power_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Power_glavni")]
    ],
)


Kiber_xavfsizlik_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Milliy ta'lim resurslari", callback_data='Kibaer_d_milliy'), InlineKeyboardButton(text="Saud Abdulwahed darslari", callback_data='kiber_d_saud')],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="kiber_d_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="kiber_d_asosi")]
    ],

)

Milliy_talim_resurslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="milliy_1"), InlineKeyboardButton(text="3-4 dars", callback_data="milliy_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="milliy_3"), InlineKeyboardButton(text="7-8 dars", callback_data="milliy_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="milliy_5"), InlineKeyboardButton(text="11-12 dars", callback_data="milliy_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="milliy_7"), InlineKeyboardButton(text="15-16 dars", callback_data="milliy_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="milliy_9"), InlineKeyboardButton(text="19-20 dars", callback_data="milliy_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Milliy_11")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="milliy_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="milliy_glavni")]
    ],

)

Saud_Abdulwahed_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="saud_1"), InlineKeyboardButton(text="3-4 dars", callback_data="saud_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="saud_3"), InlineKeyboardButton(text="7-8 dars", callback_data="saud_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="saud_5"), InlineKeyboardButton(text="11-12 dars", callback_data="saud_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="saud_7"), InlineKeyboardButton(text="15-16 dars", callback_data="saud_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="saud_9"), InlineKeyboardButton(text="19-20 dars", callback_data="saud_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="saud_11"), InlineKeyboardButton(text="23-24 dars", callback_data="saud_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="saud_13"), InlineKeyboardButton(text="27-28 dars", callback_data="saud_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="saud_15"), InlineKeyboardButton(text="31-32 dars", callback_data="saud_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="saud_17"), InlineKeyboardButton(text="35-36 dars", callback_data="saud_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="saud_19"), InlineKeyboardButton(text="39-40 dars", callback_data="saud_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="saud_21"), InlineKeyboardButton(text="43-44 dars", callback_data="saud_22")],
        [InlineKeyboardButton(text="45-46 dars", callback_data="saud_23"), InlineKeyboardButton(text="47-48 dars", callback_data="saud_24")],
        [InlineKeyboardButton(text="49-50 dars", callback_data="saud_25"), InlineKeyboardButton(text="51-52 dars", callback_data="saud_26")],
        [InlineKeyboardButton(text="53-54 dars", callback_data="saud_27"), InlineKeyboardButton(text="55-56 dars", callback_data="saud_28")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="saud_29")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Saud_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Saud_glavni")]
    ],

)





Dasturlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Front-end/Back-end", callback_data="frontenttttt_backendd"), InlineKeyboardButton(text="Android/iOS dasturlash", callback_data="Android_iossss")],
        [InlineKeyboardButton(text="Telegram bot darslari", callback_data="Telegram_botdarlari"), InlineKeyboardButton(text="Ma'lumotlar bazasi", callback_data="Malumotlar_bazasi")],
        [InlineKeyboardButton(text="Scratch darslari", callback_data="Scratch_darslarriri")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="dasturlash_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="dasturlash_glavni")]
    ],

)

#####################################################
Frontend_Backend= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Front-end", callback_data="Frontendddd"), InlineKeyboardButton(text="Back-end", callback_data="Backendddd")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Frontend_Backend_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Frontend_Backend_glavni")]
    ],
   
)

Frontend = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Frontend (intensiv)", callback_data="Frontend_intensiv"), InlineKeyboardButton(text="HTML darslari", callback_data="Htmlll_dars")],
        [InlineKeyboardButton(text="CSS darslari",callback_data="CSSS_darslarii"), InlineKeyboardButton(text="Sass darslari", callback_data="Sassss_darslari")],
        [InlineKeyboardButton(text="Bootstrap darslari", callback_data="Bootstrabb_darslari"), InlineKeyboardButton(text="JavaScript darslari", callback_data="Java_script_darslarrr")],
        [InlineKeyboardButton(text="jQuery darslari", callback_data="JQuery_darslarirrr"), InlineKeyboardButton(text="React JS darslari", callback_data="React_JS_darslari")],
        [InlineKeyboardButton(text="Vue JS darslari", callback_data="Vue_JS_darsss"), InlineKeyboardButton(text="TypeScript darslari", callback_data="TypeScript_darss")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Frontend_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Frontend_glavni")]
    ],

)



Frontend_intensiv = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="f_i_1"), InlineKeyboardButton(text="3-4 dars", callback_data="f_i_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="f_i_3"), InlineKeyboardButton(text="7-8 dars", callback_data="f_i_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="f_i_5"), InlineKeyboardButton(text="11-12 dars", callback_data="f_i_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="f_i_7"), InlineKeyboardButton(text="15-16 dars", callback_data="f_i_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="f_i_9"), InlineKeyboardButton(text="19-20 dars", callback_data="f_i_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="f_i_11"), InlineKeyboardButton(text="23-24 dars", callback_data="f_i_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="f_i_13"), InlineKeyboardButton(text="27-28 dars", callback_data="f_i_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="f_i_15"), InlineKeyboardButton(text="31-32 dars", callback_data="f_i_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="f_i_17"), InlineKeyboardButton(text="35-36 dars", callback_data="f_i_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="f_i_19"), InlineKeyboardButton(text="39-40 dars", callback_data="f_i_20")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="f_i_21")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="f_i_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="f_i_glavni")]
    ],

)

HTML_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="HTMLL_1"), InlineKeyboardButton(text="3-4 dars", callback_data="HTMLL_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="HTMLL_3"), InlineKeyboardButton(text="7-8 dars", callback_data="HTMLL_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="HTMLL_5"), InlineKeyboardButton(text="11 dars", callback_data="HTMLL_6")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="HTML_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="HTMLL_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="HTMLL_glavni")]
    ],
     
)

CSS_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="CSSS_1"), InlineKeyboardButton(text="3-4 dars", callback_data="CSSS_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="CSSS_3"), InlineKeyboardButton(text="7-8 dars", callback_data="CSSS_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="CSSS_5"), InlineKeyboardButton(text="15-16 dars", callback_data="CSSS_6")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="CSSS_7"), InlineKeyboardButton(text="19-20 dars", callback_data="CSSS_8")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="CSSS_9"), InlineKeyboardButton(text="23-24 dars", callback_data="CSSS_10")],
        [InlineKeyboardButton(text="25 dars", callback_data="CSSS_11")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="CSS_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="CSSS_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="CSSS_glavni")]
    ],
   
)

Sass_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1 dars", callback_data="sasss_1")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="SASS_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="sasss_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="sasss_glavni")]
    ],

)

Bootstrap_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Bootrstarb_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Bootrstarb_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Bootrstarb_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Bootrstarb_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Bootrstarb_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Bootrstarb_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Bootrstarb_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Bootrstarb_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Bootrstarb_9")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Bootstrab_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Bootrstarb_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Bootrstarb_glavni")]
    ],

)

JavaScript_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="JavaScript_1"), InlineKeyboardButton(text="3-4 dars", callback_data="JavaScript_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="JavaScript_3"), InlineKeyboardButton(text="7-8 dars", callback_data="JavaScript_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="JavaScript_5"), InlineKeyboardButton(text="11-12 dars", callback_data="JavaScript_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="JavaScript_7"), InlineKeyboardButton(text="15-16 dars", callback_data="JavaScript_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="JavaScript_9"), InlineKeyboardButton(text="19-20 dars", callback_data="JavaScript_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="JavaScript_11"), InlineKeyboardButton(text="23-24 dars", callback_data="JavaScript_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="JavaScript_13"), InlineKeyboardButton(text="27-28 dars", callback_data="JavaScript_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="JavaScript_15"), InlineKeyboardButton(text="31-32 dars", callback_data="JavaScript_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="JavaScript_17"), InlineKeyboardButton(text="35-36 dars", callback_data="JavaScript_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="JavaScript_19"), InlineKeyboardButton(text="39-40 dars", callback_data="JavaScript_20")],
        [InlineKeyboardButton(text="41 dars", callback_data="JavaScript_21")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="JavaScript_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="JavaScript_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="JavaScript_glavni")]
    ],

)

jQuery_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="JQuery_1")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="jQuery_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="JQuery_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="JQuery_glavni")]
    ],
   
)

React_JS_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="React_JS_1"), InlineKeyboardButton(text="3-4 dars", callback_data="React_JS_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="React_JS_3"), InlineKeyboardButton(text="7-8 dars", callback_data="React_JS_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="React_JS_5"), InlineKeyboardButton(text="11-12 dars", callback_data="React_JS_6")],
        [InlineKeyboardButton(text="13 dars", callback_data="React_JS_7")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="React_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="React_JS_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="React_JS_glavni")]
    ],
  
)

Vue_JS_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Vue_JS_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Vue_JS_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Vue_JS_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Vue_JS_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Vue_JS_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Vue_JS_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Vue_JS_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Vue_JS_8")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="VusJS_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Vue_JS_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Vue_JS_glavni")]
    ],
)

TypeScript_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="TypeScript_1"), InlineKeyboardButton(text="3-4 dars", callback_data="TypeScript_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="TypeScript_3"), InlineKeyboardButton(text="7-8 dars", callback_data="TypeScript_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="TypeScript_5"), InlineKeyboardButton(text="11-12 dars", callback_data="TypeScript_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="TypeScript_7"), InlineKeyboardButton(text="15-16 dars", callback_data="TypeScript_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="TypeScript_9"), InlineKeyboardButton(text="19-20 dars", callback_data="TypeScript_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="TypeScript_11")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Type_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="TypeScript_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="TypeScript_glavni")]
    ],
    
)















Backend= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Node JS darslari", callback_data="Node_JS_darslariii"), InlineKeyboardButton(text="Java darslari", callback_data="Java_darslariii")],
        [InlineKeyboardButton(text="Python darslari", callback_data="Python_darslariiiii"), InlineKeyboardButton(text="PHP darslari", callback_data="PHP_darslariii")],
        [InlineKeyboardButton(text="C++ darslari", callback_data="CPLUSPLUS_darslariiiii"), InlineKeyboardButton(text="C# darslari", callback_data="csharpdarslarii")],
        [InlineKeyboardButton(text="Go darslari", callback_data="Go_darslariiii"), InlineKeyboardButton(text="PHP (Yii2 framework)", callback_data="PHP_YII2_darlari")],
        [InlineKeyboardButton(text="Python (Django framework)", callback_data="PythonDjangodarslarii"),],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Backend_orqagaa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Backend_glavniii")]
    ],

)

Node_JS_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Node_JS_darslariii_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Node_JS_darslariii_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Node_JS_darslariii_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Node_JS_darslariii_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Node_JS_darslariii_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Node_JS_darslariii_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Node_JS_darslariii_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Node_JS_darslariii_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Node_JS_darslariii_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Node_JS_darslariii_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Node_JS_darslariii_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Node_JS_darslariii_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Node_JS_darslariii_13"), InlineKeyboardButton(text="27-28 dars", callback_data="Node_JS_darslariii_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="Node_JS_darslariii_15"), InlineKeyboardButton(text="31-32 dars", callback_data="Node_JS_darslariii_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="Node_JS_darslariii_17"), InlineKeyboardButton(text="35-36 dars", callback_data="Node_JS_darslariii_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="Node_JS_darslariii_19"), InlineKeyboardButton(text="39-40 dars", callback_data="Node_JS_darslariii_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="Node_JS_darslariii_21"), InlineKeyboardButton(text="43-44 dars", callback_data="Node_JS_darslariii_22")],
        [InlineKeyboardButton(text="45-46 dars", callback_data="Node_JS_darslariii_23"), InlineKeyboardButton(text="47-48 dars", callback_data="Node_JS_darslariii_24")],
        [InlineKeyboardButton(text="49-50 dars", callback_data="Node_JS_darslariii_25"), InlineKeyboardButton(text="51-52 dars", callback_data="Node_JS_darslariii_26")],
        [InlineKeyboardButton(text="53-54 dars", callback_data="Node_JS_darslariii_27"), InlineKeyboardButton(text="55-56 dars", callback_data="Node_JS_darslariii_28")],
        [InlineKeyboardButton(text="57-58 dars", callback_data="Node_JS_darslariii_29"), InlineKeyboardButton(text="59-60 dars", callback_data="Node_JS_darslariii_30")],
        [InlineKeyboardButton(text="61-62 dars", callback_data="Node_JS_darslariii_31"), InlineKeyboardButton(text="63-64 dars", callback_data="Node_JS_darslariii_32")],
        [InlineKeyboardButton(text="65-66 dars", callback_data="Node_JS_darslariii_33"), InlineKeyboardButton(text="67-68 dars", callback_data="Node_JS_darslariii_34")],
        [InlineKeyboardButton(text="69-70 dars", callback_data="Node_JS_darslariii_35"), InlineKeyboardButton(text="71-72 dars", callback_data="Node_JS_darslariii_36")],
        [InlineKeyboardButton(text="73-74 dars", callback_data="Node_JS_darslariii_37"), InlineKeyboardButton(text="75-76 dars", callback_data="Node_JS_darslariii_38")],
        [InlineKeyboardButton(text="77-78 dars", callback_data="Node_JS_darslariii_39"), InlineKeyboardButton(text="79-80 dars", callback_data="Node_JS_darslariii_40")],
        [InlineKeyboardButton(text="81-82 dars", callback_data="Node_JS_darslariii_41"), InlineKeyboardButton(text="83-84 dars", callback_data="Node_JS_darslariii_42")],
        [InlineKeyboardButton(text="85-86 dars", callback_data="Node_JS_darslariii_43"), InlineKeyboardButton(text="87-88 dars", callback_data="Node_JS_darslariii_44")],
        [InlineKeyboardButton(text="89-90 dars", callback_data="Node_JS_darslariii_45"), InlineKeyboardButton(text="91-92 dars", callback_data="Node_JS_darslariii_46")],
        [InlineKeyboardButton(text="93-94 dars", callback_data="Node_JS_darslariii_47"), InlineKeyboardButton(text="95-98 dars", callback_data="Node_JS_darslariii_48")],
        [InlineKeyboardButton(text="99-100 dars", callback_data="Node_JS_darslariii_49"), InlineKeyboardButton(text="101-102 dars", callback_data="Node_JS_darslariii_50")],
        [InlineKeyboardButton(text="103-104 dars", callback_data="Node_JS_darslariii_51"), InlineKeyboardButton(text="105-106 dars", callback_data="Node_JS_darslariii_52")],
        [InlineKeyboardButton(text="107-108 dars", callback_data="Node_JS_darslariii_53"), InlineKeyboardButton(text="109-110 dars", callback_data="Node_JS_darslariii_54")],
        [InlineKeyboardButton(text="111-112 dars", callback_data="Node_JS_darslariii_55"), InlineKeyboardButton(text="113 dars", callback_data="Node_JS_darslariii_56")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Node_Js_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Node_JS_darslariii_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Node_JS_darslariii_glavni")]
    ],
  
)

Java_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Java_darsss_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Java_darsss_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Java_darsss_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Java_darsss_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Java_darsss_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Java_darsss_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Java_darsss_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Java_darsss_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Java_darsss_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Java_darsss_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Java_darsss_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Java_darsss_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Java_darsss_13"), InlineKeyboardButton(text="27-28 dars", callback_data="Java_darsss_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="Java_darsss_15"), InlineKeyboardButton(text="31-32 dars", callback_data="Java_darsss_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="Java_darsss_17"), InlineKeyboardButton(text="35-36 dars", callback_data="Java_darsss_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="Java_darsss_19"), InlineKeyboardButton(text="39-40 dars", callback_data="Java_darsss_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="Java_darsss_21"), InlineKeyboardButton(text="43 dars", callback_data="Java_darsss_22")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="JAva_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Java_darsss_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Java_darsss_glavni")]
    ],

)

Python_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Pythonnn_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Pythonnn_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Pythonnn_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Pythonnn_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Pythonnn_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Pythonnn_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Pythonnn_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Pythonnn_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Pythonnn_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Pythonnn_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Pythonnn_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Pythonnn_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Pythonnn_13"), InlineKeyboardButton(text="27-28 dars", callback_data="Pythonnn_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="Pythonnn_15"), InlineKeyboardButton(text="31-32 dars", callback_data="Pythonnn_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="Pythonnn_17"), InlineKeyboardButton(text="35-36 dars", callback_data="Pythonnn_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="Pythonnn_19"), InlineKeyboardButton(text="39-40 dars", callback_data="Pythonnn_20")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Python_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Pythonnn_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Pythonnn_glavni")]
    ],
 
)

PHP_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="PHPP_1"), InlineKeyboardButton(text="3-4 dars", callback_data="PHPP_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="PHPP_3"), InlineKeyboardButton(text="7-8 dars", callback_data="PHPP_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="PHPP_5"), InlineKeyboardButton(text="11-12 dars", callback_data="PHPP_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="PHPP_7"), InlineKeyboardButton(text="15-16 dars", callback_data="PHPP_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="PHPP_9"), InlineKeyboardButton(text="19-20 dars", callback_data="PHPP_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="PHPP_11"), InlineKeyboardButton(text="23-24 dars", callback_data="PHPP_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="PHPP_13"), InlineKeyboardButton(text="27-28 dars", callback_data="PHPP_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="PHPP_15"), InlineKeyboardButton(text="31 dars", callback_data="PHPP_16")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="PHP_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="PHPP_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="PHPP_glavnii")]
    ],

)
CPlusPlus_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="CPulsPUls_1"), InlineKeyboardButton(text="3-4 dars", callback_data="CPulsPUls_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="CPulsPUls_3"), InlineKeyboardButton(text="7-8 dars", callback_data="CPulsPUls_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="CPulsPUls_5"), InlineKeyboardButton(text="11-12 dars", callback_data="CPulsPUls_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="CPulsPUls_7"), InlineKeyboardButton(text="15-16 dars", callback_data="CPulsPUls_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="CPulsPUls_9"), InlineKeyboardButton(text="19-20 dars", callback_data="CPulsPUls_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="CPulsPUls_11"), InlineKeyboardButton(text="23-24 dars", callback_data="CPulsPUls_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="CPulsPUls_13"), InlineKeyboardButton(text="27-28 dars", callback_data="CPulsPUls_14")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Cpu_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="CPulsPUls_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="CPulsPUls_glavni")]
    ],

)

CSharp_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Csharppp_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Csharppp_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Csharppp_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Csharppp_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Csharppp_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Csharppp_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Csharppp_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Csharppp_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Csharppp_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Csharppp_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Csharppp_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Csharppp12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Csharppp_13"), InlineKeyboardButton(text="27-28 dars", callback_data="Csharppp_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="Csharppp_15"), InlineKeyboardButton(text="31-32 dars", callback_data="Csharppp_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="Csharppp_17"), InlineKeyboardButton(text="35-36 dars", callback_data="Csharppp_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="Csharppp_19"), InlineKeyboardButton(text="39-40 dars", callback_data="Csharppp_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="Csharppp_21"), InlineKeyboardButton(text="43 dars", callback_data="Csharppp_22")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="Csharppp_23"), InlineKeyboardButton(text="43-44 dars", callback_data="Csharppp_24")],
        [InlineKeyboardButton(text="45 dars", callback_data="Csharppp_25")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Csharp_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Csharppp_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Csharppp_glavni")]
    ],

)

Go_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Go_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Go_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Go_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Go_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Go_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Go_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Go_7")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Go_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Go_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Go_glavni")]
    ],

)

PHP_Yii2_framework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="PHPYii_1"), InlineKeyboardButton(text="3-4 dars", callback_data="PHPYii_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="PHPYii_3"), InlineKeyboardButton(text="7-8 dars", callback_data="PHPYii_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="PHPYii_5"), InlineKeyboardButton(text="11-12 dars", callback_data="PHPYii_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="PHPYii_7"), InlineKeyboardButton(text="15-16 dars", callback_data="PHPYii_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="PHPYii_9"), InlineKeyboardButton(text="19-20 dars", callback_data="PHPYii_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="PHPYii_11"), InlineKeyboardButton(text="23-24 dars", callback_data="PHPYii_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="PHPYii_13"), InlineKeyboardButton(text="27-28 dars", callback_data="PHPYii_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="PHPYii_15")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="PHPTII_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="PHPYii_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="PHPYii_glavni")]
    ],

)

Python_Django_framework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="djangoo_1"), InlineKeyboardButton(text="3-4 dars", callback_data="djangoo_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="djangoo_3"), InlineKeyboardButton(text="7-8 dars", callback_data="djangoo_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="djangoo_5"), InlineKeyboardButton(text="11-12 dars", callback_data="djangoo_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="djangoo_7"), InlineKeyboardButton(text="15-16 dars", callback_data="djangoo_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="djangoo_9"), InlineKeyboardButton(text="19-20 dars", callback_data="djangoo_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="djangoo_11"), InlineKeyboardButton(text="23-24 dars", callback_data="djangoo_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="djangoo_13"), InlineKeyboardButton(text="27-28 dars", callback_data="djangoo_14")],
        [InlineKeyboardButton(text="29 dars", callback_data="djangoo_15")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Django_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="djangoo_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="djangoo_glavni")]
    ],
    
)

#####################################################

Android_iOSdasturlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Android",callback_data="Androiddddddd"), InlineKeyboardButton(text="iOS",callback_data="IOSSSS")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="a_o_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu",callback_data="a_o_glavni")]
    ],

)

Android = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Android (Java) darslari", callback_data="Androiddd_Java"), InlineKeyboardButton(text="Kotlin darslari", callback_data="Kotlindarsslari")],
        [InlineKeyboardButton(text="Android Studio darslari", callback_data="Android_studioooo"), InlineKeyboardButton(text="Flutter darslari", callback_data="Flutter_darlariii")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Androiddd_orqa"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Androiddd_glavni")]
    ],
   
)

Android_Java_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="androiddd_1"), InlineKeyboardButton(text="3-4 dars", callback_data="androiddd_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="androiddd_3"), InlineKeyboardButton(text="7-8 dars", callback_data="androiddd_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="androiddd_5"), InlineKeyboardButton(text="11-12 dars", callback_data="androiddd_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="androiddd_7"), InlineKeyboardButton(text="15-16 dars", callback_data="androiddd_8")],
        [InlineKeyboardButton(text="17 dars", callback_data="androiddd_9")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="android_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="androiddd_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="androiddd_glavni")]
    ],

)

Kotlin_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Kotlindarsslari_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Kotlindarsslari_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Kotlindarsslari_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Kotlindarsslari_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Kotlindarsslari_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Kotlindarsslari_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Kotlindarsslari_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Kotlindarsslari_8")],
        [InlineKeyboardButton(text="17 dars", callback_data="Kotlindarsslari_9")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="kotlin_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Kotlindarsslari_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Kotlindarsslari_")]
    ],
  
)

Android_Studio_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="androidstudi_1"), InlineKeyboardButton(text="3-4 dars", callback_data="androidstudi_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="androidstudi_3"), InlineKeyboardButton(text="7-8 dars", callback_data="androidstudi_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="androidstudi_5"), InlineKeyboardButton(text="11-12 dars", callback_data="androidstudi_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="androidstudi_7"), InlineKeyboardButton(text="15-16 dars", callback_data="androidstudi_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="androidstudi_9"), InlineKeyboardButton(text="19-20 dars", callback_data="androidstudi_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="androidstudi_11"), InlineKeyboardButton(text="23-24 dars", callback_data="androidstudi_12")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="a_studio_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="androidstudi_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="androidstudi_glavni")]
    ],

)

Flutter_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="fluter_1"), InlineKeyboardButton(text="3-4 dars", callback_data="fluter_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="fluter_3"), InlineKeyboardButton(text="7-8 dars", callback_data="fluter_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="fluter_5"), InlineKeyboardButton(text="11-12 dars", callback_data="fluter_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="fluter_7"), InlineKeyboardButton(text="15-16 dars", callback_data="fluter_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="fluter_9"), InlineKeyboardButton(text="19-20 dars", callback_data="fluter_10")],
        [InlineKeyboardButton(text="21 dars", callback_data="fluter_11")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="flutter_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="fluter_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="fluter_glavni")]
    ],
    
)





iOS = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Swift darslari", callback_data="swift_darslarrii")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="iosss_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="iosss_glavni")]
    ],
 
)

Swift_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="swift_1"), InlineKeyboardButton(text="3-4 dars", callback_data="swift_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="swift_3"), InlineKeyboardButton(text="7-8 dars", callback_data="swift_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="swift_5"), InlineKeyboardButton(text="11-12 dars", callback_data="swift_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="swift_7"), InlineKeyboardButton(text="15-16 dars", callback_data="swift_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="swift_9"), InlineKeyboardButton(text="19-20 dars", callback_data="swift_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="swift_11"), InlineKeyboardButton(text="23 dars", callback_data="swift_12")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="swift_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="swift_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="swift_glavni")]
    ],
  
)
####################################################
Telegram_bot_darslari= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Sariq Dev", callback_data="Sariq_devvv"), InlineKeyboardButton(text="Botir Ziyatov", callback_data="Botir_ziyatovvv")],
        [InlineKeyboardButton(text="CodeUz", callback_data="codeuzuz"), InlineKeyboardButton(text="Co-Learning Academy", callback_data="colearning_academy")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="tg_orqaag"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="tg_glavni")]
    ],

)

Sariq_Dev = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars",callback_data="sarq_1"), InlineKeyboardButton(text="3-4 dars",callback_data="sarq_2")],
        [InlineKeyboardButton(text="5-6 dars",callback_data="sarq_3"), InlineKeyboardButton(text="7-8 dars",callback_data="sarq_4")],
        [InlineKeyboardButton(text="9-10 dars",callback_data="sarq_5"), InlineKeyboardButton(text="11-12 dars",callback_data="sarq_6")],
        [InlineKeyboardButton(text="13-14 dars",callback_data="sarq_7")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="sariq_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga",callback_data="sarq_orqaag"), InlineKeyboardButton(text="🔝 Asosiy Menyu",callback_data="sarq_glavni")]
    ],

)

Botir_Ziyatov = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="botir_1"), InlineKeyboardButton(text="3-4 dars", callback_data="botir_2")],
        [InlineKeyboardButton(text="5 dars", callback_data="botir_3")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="botir_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="botir_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="botir_glavni")]
    ],

)

CodeUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="code_1"), InlineKeyboardButton(text="3-4 dars", callback_data="code_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="code_3"), InlineKeyboardButton(text="7-8 dars", callback_data="code_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="code_5"), InlineKeyboardButton(text="11-12 dars", callback_data="code_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="code_7"), InlineKeyboardButton(text="15-16 dars", callback_data="code_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="code_9"), InlineKeyboardButton(text="19-20 dars", callback_data="code_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="code_11")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="code_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="code_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="code_glavni")]
    ],

)

Co_Learning_Academy =InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars",callback_data="co_1"), InlineKeyboardButton(text="3 dars", callback_data="co_2")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Co_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="co_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="co_glavni")]
    ],

)

######################################################

Malumotlar_bazasi = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="PostgreSQL", callback_data="postsql_da"), InlineKeyboardButton(text="MySQL", callback_data="mysql_da")],
        [InlineKeyboardButton(text="MongoDB", callback_data="mpngo_da")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="baza_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="baza_glavni")]
    ],

)
PostgreSQL = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="post_1"), InlineKeyboardButton(text="3-4 dars", callback_data="post_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="post_3"), InlineKeyboardButton(text="7-8 dars", callback_data="post_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="post_5"), InlineKeyboardButton(text="11-12 dars", callback_data="post_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="post_7"), InlineKeyboardButton(text="15-16 dars", callback_data="post_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="post_9"), InlineKeyboardButton(text="19-20 dars", callback_data="post_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="post_11"), InlineKeyboardButton(text="23-24 dars", callback_data="post_12")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="post_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="post_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="post_glavni")]
    ],

)

MySQL = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="mysqlll_1"), InlineKeyboardButton(text="3-4 dars", callback_data="mysqlll_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="mysqlll_3"), InlineKeyboardButton(text="7-8 dars", callback_data="mysqlll_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="mysqlll_5")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="mysql_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="mysqlll_ortga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="mysqlll_glavni")]
    ],

)

MongoDB = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="mongo_1"), InlineKeyboardButton(text="3-4 dars", callback_data="mongo_2")],
        [InlineKeyboardButton(text="5 dars", callback_data="mongo_3")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="mongo_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="mongo_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="mongo_glavni")]
    ],

)

##############################################
Scratch_darslari= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="scr_1"), InlineKeyboardButton(text="3-4 dars", callback_data="scr_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="scr_3"), InlineKeyboardButton(text="7-8 dars", callback_data="scr_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="scr_5")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="scratch_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="scr_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="scr_glavni")]
    ],
)

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
Tillar_11= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Rus tili", callback_data="rus"), InlineKeyboardButton(text="Ingliz tili", callback_data="ingls")],
        [InlineKeyboardButton(text="Arab tili", callback_data="arab_t"), InlineKeyboardButton(text="Xitoy tili", callback_data="xitoy")],
        [InlineKeyboardButton(text="Fransuz tili", callback_data="Fransuz"), InlineKeyboardButton(text="Turk tili", callback_data="Turk")],
        [InlineKeyboardButton(text="Koreys tili", callback_data="Koreys"), InlineKeyboardButton(text="Yapon tili", callback_data="Yapon")],
        [InlineKeyboardButton(text="Nemis tili", callback_data="Nemis"), InlineKeyboardButton(text="Ispan tili", callback_data="Ispan")],
        [InlineKeyboardButton(text="Hind tili", callback_data="Hind")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="till_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="tilll_glavni")]
    ],
)

rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="russ_1"), InlineKeyboardButton(text="3-4 dars", callback_data="russ_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="russ_3"), InlineKeyboardButton(text="7-8 dars", callback_data="russ_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="russ_5"), InlineKeyboardButton(text="11-12 dars", callback_data="russ_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="russ_7"), InlineKeyboardButton(text="15-16 dars", callback_data="russ_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="russ_9"), InlineKeyboardButton(text="19-20 dars", callback_data="russ_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="russ_11"), InlineKeyboardButton(text="23-24 dars", callback_data="russ_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="russ_13"), InlineKeyboardButton(text="27 dars", callback_data="russ_14")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="russ_toliqq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="rus_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="rus_glavni")]
    ],

)



ingls = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="ingls_1"), InlineKeyboardButton(text="3-4 dars", callback_data="ingls_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="ingls_3"), InlineKeyboardButton(text="7-8 dars", callback_data="ingls_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="ingls_5"), InlineKeyboardButton(text="11-12 dars", callback_data="ingls_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="ingls_7"), InlineKeyboardButton(text="15-16 dars", callback_data="ingls_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="ingls_9"), InlineKeyboardButton(text="19-20 dars", callback_data="ingls_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="ingls_11"), InlineKeyboardButton(text="23-24 dars", callback_data="ingls_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="ingls_13"), InlineKeyboardButton(text="27-28 dars", callback_data="ingls_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="ingls_15"), InlineKeyboardButton(text="31-32 dars", callback_data="ingls_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="ingls_17"), InlineKeyboardButton(text="35-36 dars", callback_data="ingls_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="ingls_19"), InlineKeyboardButton(text="39-40 dars", callback_data="ingls_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="ingls_21"), InlineKeyboardButton(text="43-44 dars", callback_data="ingls_22")],
        [InlineKeyboardButton(text="45-46 dars", callback_data="ingls_23"), InlineKeyboardButton(text="47-48 dars", callback_data="ingls_24")],
        [InlineKeyboardButton(text="49-50 dars", callback_data="ingls_25"), InlineKeyboardButton(text="51-52 dars", callback_data="ingls_26")],
        [InlineKeyboardButton(text="53-54 dars", callback_data="ingls_27"), InlineKeyboardButton(text="55-56 dars", callback_data="ingls_28")],
        [InlineKeyboardButton(text="57-58 dars", callback_data="ingls_29"), InlineKeyboardButton(text="59-60 dars", callback_data="ingls_30")],
        [InlineKeyboardButton(text="61-62 dars", callback_data="ingls_31"), InlineKeyboardButton(text="63-64 dars", callback_data="ingls_32")],
        [InlineKeyboardButton(text="65-66 dars", callback_data="ingls_33"), InlineKeyboardButton(text="67-68 dars", callback_data="ingls_34")],
        [InlineKeyboardButton(text="69-70 dars", callback_data="ingls_35"), InlineKeyboardButton(text="71-72 dars", callback_data="ingls_36")],
        [InlineKeyboardButton(text="73-74 dars", callback_data="ingls_37"), InlineKeyboardButton(text="75-76 dars", callback_data="ingls_38")],
        [InlineKeyboardButton(text="77-78 dars", callback_data="ingls_39"), InlineKeyboardButton(text="79-80 dars", callback_data="ingls_40")],
        [InlineKeyboardButton(text="81-82 dars", callback_data="ingls_41"), InlineKeyboardButton(text="83-84 dars", callback_data="ingls_42")],
        [InlineKeyboardButton(text="85-86 dars", callback_data="ingls_43"), InlineKeyboardButton(text="87-88 dars", callback_data="ingls_44")],
        [InlineKeyboardButton(text="89-90 dars", callback_data="ingls_45"), InlineKeyboardButton(text="91-92 dars", callback_data="ingls_46")],
        [InlineKeyboardButton(text="93-94 dars", callback_data="ingls_47"), InlineKeyboardButton(text="95-98 dars", callback_data="ingls_48")],
        [InlineKeyboardButton(text="99-100 dars", callback_data="ingls_49"), InlineKeyboardButton(text="101-102 dars", callback_data="ingls_50")],
        [InlineKeyboardButton(text="103-104 dars", callback_data="ingls_51"), InlineKeyboardButton(text="105-106 dars", callback_data="ingls_52")],
        [InlineKeyboardButton(text="107-108 dars", callback_data="ingls_53"), InlineKeyboardButton(text="109-110 dars", callback_data="ingls_54")],
        [InlineKeyboardButton(text="111-112 dars", callback_data="ingls_55"), InlineKeyboardButton(text="113 dars", callback_data="ingls_56")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="ingls_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="ingls_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="ingls_glavni")]
    ], 
)


arabb_tilii =  InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Arab alifbo darslari", callback_data="arab_alifbo"), InlineKeyboardButton(text="Arab tili gramatikasi", callback_data="arab_gramatika")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="arabb_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="arabb_glavni")]
    ],
)

arab_alifbooo = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="arabb_1"), InlineKeyboardButton(text="3-4 dars", callback_data="arabb_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="arabb_3"), InlineKeyboardButton(text="7-8 dars", callback_data="arabb_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="arabb_5"), InlineKeyboardButton(text="11-12 dars", callback_data="arabb_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="arabb_7"), InlineKeyboardButton(text="15-16 dars", callback_data="arabb_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="arabb_9"), InlineKeyboardButton(text="19-20 dars", callback_data="arabb_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="arabb_11"), InlineKeyboardButton(text="23-24 dars", callback_data="arabb_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="arabb_13"), InlineKeyboardButton(text="27-28 dars", callback_data="arabb_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="arabb_15"), InlineKeyboardButton(text="31-32 dars", callback_data="arabb_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="arabb_17"), InlineKeyboardButton(text="35 dars", callback_data="arabb_18")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="arab_alifbo_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="arabb_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="arabb_1_glavni")]
    ],
)

arab_gramatika = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="arabb_g_1"), InlineKeyboardButton(text="3-4 dars", callback_data="arabb_g_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="arabb_g_3"), InlineKeyboardButton(text="7-8 dars", callback_data="arabb_g_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="arabb_g_5"), InlineKeyboardButton(text="11-12 dars", callback_data="arabb_g_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="arabb_g_7"), InlineKeyboardButton(text="15-16 dars", callback_data="arabb_g_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="arabb_g_9"), InlineKeyboardButton(text="19 dars", callback_data="arabb_g_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="arab_gramatika_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="arabb_g_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="arabb_g_1_glavni")]
    ],
)


xitoyy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="xitoy_1"), InlineKeyboardButton(text="3-4 dars", callback_data="xitoy_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="xitoy_3"), InlineKeyboardButton(text="7-8 dars", callback_data="xitoy_4")],
        [InlineKeyboardButton(text="9 dars", callback_data="xitoy_5")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="xitoy_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="xitoy_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="xitoy_1_glavni")]
    ],
)


fransuz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="fransuzz_1"), InlineKeyboardButton(text="3-4 dars", callback_data="fransuzz_1")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="fransuzz_1"), InlineKeyboardButton(text="7-8 dars", callback_data="fransuzz_1")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="fransuzz_1")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="fransuzz_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="fransuzz_1_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="fransuzz_11_glavni")]
    ],
)



turkk =  InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ulug'bek Madg'oziyev darslari", callback_data="turk_ulug"), InlineKeyboardButton(text="Turk tilidan dialoglar (amaliyot)", callback_data="turk_dialog")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="turk_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="turk_glavni")]
    ],
)


uluggg = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="ulug_1"), InlineKeyboardButton(text="3-4 dars", callback_data="ulug_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="ulug_3"), InlineKeyboardButton(text="7-8 dars", callback_data="ulug_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="ulug_5"), InlineKeyboardButton(text="11-12 dars", callback_data="ulug_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="ulug_7"), InlineKeyboardButton(text="15-16 dars", callback_data="ulug_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="ulug_9"), InlineKeyboardButton(text="19 dars", callback_data="ulug_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="ulug_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="ulug_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="ulug_1_glavni")]
    ],
)
 
turk_diagnoz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="turk_d_1"), InlineKeyboardButton(text="3-4 dars", callback_data="turk_d_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="turk_d_3")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="turk_d_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="turk_d_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="turk_d_1_glavni")]
    ],
)

koerss  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="koers_1"), InlineKeyboardButton(text="3-4 dars", callback_data="koers_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="koers_3"), InlineKeyboardButton(text="7-8 dars", callback_data="koers_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="koers_5"), InlineKeyboardButton(text="11-12 dars", callback_data="koers_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="koers_7"), InlineKeyboardButton(text="15-16 dars", callback_data="koers_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="koers_9"), InlineKeyboardButton(text="19-20 dars", callback_data="koers_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="koers_11"), InlineKeyboardButton(text="23 dars", callback_data="koers_12")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="akoers_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="koers_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="akoers_1_glavni")]
    ],
)

yaponn =InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="yapon_1"), InlineKeyboardButton(text="3-4 dars", callback_data="yapon_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="yapon_3"), InlineKeyboardButton(text="7-8 dars", callback_data="yapon_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="yapon_5")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="yapon_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="yapon_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="yapon_1_glavni")]
    ],
)

nemiss = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="nems_1"), InlineKeyboardButton(text="3-4 dars", callback_data="nems_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="nems_3"), InlineKeyboardButton(text="7-8 dars", callback_data="nems_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="nems_5"), InlineKeyboardButton(text="11-12 dars", callback_data="nems_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="nems_7"), InlineKeyboardButton(text="15-16 dars", callback_data="nems_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="nems_9"), InlineKeyboardButton(text="19-20 dars", callback_data="nems_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="nems_11"), InlineKeyboardButton(text="23-24 dars", callback_data="nems_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="nems_13"), InlineKeyboardButton(text="27-28 dars", callback_data="nems_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="nems_15"), InlineKeyboardButton(text="31-32 dars", callback_data="nems_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="nems_17"), InlineKeyboardButton(text="35-36 dars", callback_data="nems_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="nems_19"), InlineKeyboardButton(text="39-40 dars", callback_data="nems_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="nems_21"), InlineKeyboardButton(text="43-44 dars", callback_data="nems_22")],
        [InlineKeyboardButton(text="45-46 dars", callback_data="nems_23"), InlineKeyboardButton(text="47-48 dars", callback_data="nems_24")],
        [InlineKeyboardButton(text="49-50 dars", callback_data="nems_25"), InlineKeyboardButton(text="51-52 dars", callback_data="nems_26")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="inems_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="nems_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="nems_1_glavni")]
    ], 
)

ispan = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="ispan_1"), InlineKeyboardButton(text="3-4 dars", callback_data="ispan_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="ispan_3"), InlineKeyboardButton(text="7-8 dars", callback_data="ispan_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="ispan_5")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="ispan_11toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="ispan_11orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="ispan_1_glavni")]
    ], 
)

Hind = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Hind_1")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Hind1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Hindorqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Hind_glavni")]
    ], 
)




Tarmoq_qurish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="tarmoq_1"), InlineKeyboardButton(text="3-4 dars", callback_data="tarmoq_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="tarmoq_3"), InlineKeyboardButton(text="7-8 dars", callback_data="tarmoq_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="tarmoq_5"), InlineKeyboardButton(text="11-12 dars", callback_data="tarmoq_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="tarmoq_7"), InlineKeyboardButton(text="15-16 dars", callback_data="tarmoq_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="tarmoq_9"), InlineKeyboardButton(text="19-20 dars", callback_data="tarmoq_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="tarmoq_11")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="tarmoq_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="tarmoq_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="tarmoq_1_glavni")]
    ], 
)



Musiqa_yaratish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="FL studio", callback_data="FL_studio")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="fl_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="fl_glavni")]
    ], 
)


FL_studio= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="ftstudio_1"), InlineKeyboardButton(text="3-4 dars", callback_data="ftstudio_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="ftstudio_3"), InlineKeyboardButton(text="7-8 dars", callback_data="ftstudio_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="ftstudio_5"), InlineKeyboardButton(text="11-12 dars", callback_data="ftstudio_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="ftstudio_7"), InlineKeyboardButton(text="15-16 dars", callback_data="ftstudio_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="ftstudio_9"), InlineKeyboardButton(text="19 dars", callback_data="ftstudio_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="ftstudio_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="ftstudio_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="ftstudio_1_glavni")]
    ], 
)

Frilanserlik_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Frilanserlik__1"), InlineKeyboardButton(text="3-4 dars", callback_data="Frilanserlik__2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Frilanserlik__3"), InlineKeyboardButton(text="7-8 dars", callback_data="Frilanserlik__4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Frilanserlik__5"), InlineKeyboardButton(text="11-12 dars", callback_data="Frilanserlik__6")],
        [InlineKeyboardButton(text="13 dars", callback_data="Frilanserlik__7")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Frilanserlik__1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Frilanserlik__11orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Frilanserlik__1_glavni")]
    ], 
)









grafik_dizayn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Adobe Photoshop", callback_data="adoble_photoshop"), InlineKeyboardButton(text="Adobe Illustrator", callback_data="Adoble_Illustrator")],
        [InlineKeyboardButton(text="Adobe XD", callback_data="Adoble_XD"), InlineKeyboardButton(text="Figma", callback_data="Figma")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="grafikd_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="grafik_glavni")]
    ], 
)

Adoble_Photo = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="adoble_Ptoto_1"), InlineKeyboardButton(text="3-4 dars", callback_data="adoble_Ptoto_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="adoble_Ptoto_3"), InlineKeyboardButton(text="7-8 dars", callback_data="adoble_Ptoto_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="adoble_Ptoto_5"), InlineKeyboardButton(text="11-12 dars", callback_data="adoble_Ptoto_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="adoble_Ptoto_7"), InlineKeyboardButton(text="15-16 dars", callback_data="adoble_Ptoto_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="adoble_Ptoto_9"), InlineKeyboardButton(text="19-20 dars", callback_data="adoble_Ptoto_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="adoble_Ptoto_11"), InlineKeyboardButton(text="23-24 dars", callback_data="adoble_Ptoto_12")],
        [InlineKeyboardButton(text="25 dars", callback_data="adoble_Ptoto_13")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="adoble_Ptoto_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="adoble_Ptoto_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="adoble_Ptoto_glavni")]
    ], 
)

Adoble_Illustrator = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Adoble_Illustrator_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Adoble_Illustrator_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Adoble_Illustrator_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Adoble_Illustrator_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Adoble_Illustrator_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Adoble_Illustrator_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Adoble_Illustrator_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Adoble_Illustrator_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Adoble_Illustrator_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Adoble_Illustrator_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Adoble_Illustrator_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Adoble_Illustrator_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Adoble_Illustrator_13")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Adoble_Illustrator_1_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Adoble_Illustrator_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Adoble_Illustrator_1_glavni")]
    ], 
)

Adoble_XD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Adoble_xd_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Adoble_xd_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Adoble_xd_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Adoble_xd_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Adoble_xd_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Adoble_xd_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Adoble_xd_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Adoble_xd_8")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Adoble_xd_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Adoble_xd_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Adoble_xd_1_glavni")]
    ], 
)

figmmma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="figmaa_1"), InlineKeyboardButton(text="3-4 dars", callback_data="figmaa_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="figmaa_3"), InlineKeyboardButton(text="7-8 dars", callback_data="figmaa_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="figmaa_5"), InlineKeyboardButton(text="11-12 dars", callback_data="figmaa_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="figmaa_7"), InlineKeyboardButton(text="15-16 dars", callback_data="figmaa_8")],
        [InlineKeyboardButton(text="17 dars", callback_data="figmaa_9")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="figmaa_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="figmaa_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="figmaa_1_glavni")]
    ], 
)




kopirayting_mobilagrafiya = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kopirayting", callback_data="Kopirayting_mobila"), InlineKeyboardButton(text="Mobilografiya", callback_data="Mobilografiya_kopir")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="kop_mobil_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="kop_mobil_glavni")]
    ], 
) 

Kopirayting_mobila = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kopirayting darslari", callback_data="Kopirayting_darslari")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="kopirayt_mobil_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="kopirayt_mobil__glavni")]
    ], 
) 

Kopirayting_darslari  = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Kopirayting_dars_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Kopirayting_dars_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Kopirayting_dars_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Kopirayting_dars_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Kopirayting_dars_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Kopirayting_dars_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Kopirayting_dars_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Kopirayting_dars_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Kopirayting_dars_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Kopirayting_dars_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Kopirayting_dars_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Kopirayting_dars_1_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Kopirayting_dars_1glavni")]
    ], 
) 


Mobilografiya_kopiraytsa = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="mobil_1"), InlineKeyboardButton(text="3-4 dars", callback_data="mobil_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="mobil_3"), InlineKeyboardButton(text="7-8 dars", callback_data="mobil_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="mobil_5"), InlineKeyboardButton(text="11-12 dars", callback_data="mobil_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="mobil_7"), InlineKeyboardButton(text="15-16 dars", callback_data="mobil_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="mobil_9"), InlineKeyboardButton(text="19-20 dars", callback_data="mobil_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="mobil_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="mobil_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="mobil_1_glavni")]
    ], 
) 



d_modeling =  InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="3Ds Max", callback_data="DsMax"), InlineKeyboardButton(text="AutoCAD", callback_data="AutoCAD")],
        [InlineKeyboardButton(text="Blender", callback_data="Blender"), InlineKeyboardButton(text="CorelDRAW", callback_data="CorelDRAW")],
        [InlineKeyboardButton(text="SolidWorks", callback_data="SolidWorks"), InlineKeyboardButton(text="Compass 3D", callback_data="Compass3d")],
        [InlineKeyboardButton(text="Revit darslari", callback_data="Revit_darslari")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="modeling_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="modeling_glavni")]
    ], 
) 

DsMax = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="DsMax_1"), InlineKeyboardButton(text="3-4 dars", callback_data="DsMax_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="DsMax_3"), InlineKeyboardButton(text="7-8 dars", callback_data="DsMax_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="DsMax_5"), InlineKeyboardButton(text="11-12 dars", callback_data="DsMax_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="DsMax_7"), InlineKeyboardButton(text="15-16 dars", callback_data="DsMax_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="DsMax_9"), InlineKeyboardButton(text="19-20 dars", callback_data="DsMax_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="DsMax_11"), InlineKeyboardButton(text="23-24 dars", callback_data="DsMax_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="DsMax_13"), InlineKeyboardButton(text="27-28 dars", callback_data="DsMax_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="DsMax_15"), InlineKeyboardButton(text="31-32 dars", callback_data="DsMax_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="DsMax_17"), InlineKeyboardButton(text="35-36 dars", callback_data="DsMax_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="DsMax_19"), InlineKeyboardButton(text="39-40 dars", callback_data="DsMax_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="DsMax_21"), InlineKeyboardButton(text="43-44 dars", callback_data="DsMax_22")],
        [InlineKeyboardButton(text="45-46 dars", callback_data="DsMax_23"), InlineKeyboardButton(text="47-48 dars", callback_data="DsMax_24")],
        [InlineKeyboardButton(text="49-50 dars", callback_data="DsMax_25"), InlineKeyboardButton(text="51-52 dars", callback_data="DsMax_26")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="DsMax_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="DsMax_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="DsMax_1_glavni")]
    ], 
)


AutoCAD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="AutoCAD_1"), InlineKeyboardButton(text="3-4 dars", callback_data="AutoCAD_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="AutoCAD_3"), InlineKeyboardButton(text="7-8 dars", callback_data="AutoCAD_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="AutoCAD_5"), InlineKeyboardButton(text="11-12 dars", callback_data="AutoCAD_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="AutoCAD_7"), InlineKeyboardButton(text="15-16 dars", callback_data="AutoCAD_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="AutoCAD_9"), InlineKeyboardButton(text="19-20 dars", callback_data="AutoCAD_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="AutoCAD_11"), InlineKeyboardButton(text="23-24 dars", callback_data="AutoCAD_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="AutoCAD_13"), InlineKeyboardButton(text="27-28 dars", callback_data="AutoCAD_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="AutoCAD_15"), InlineKeyboardButton(text="31-32 dars", callback_data="AutoCAD_16")],
        [InlineKeyboardButton(text="33 dars", callback_data="AutoCAD_17")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="AutoCAD_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="AutoCAD_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="AutoCAD_1_glavni")]
    ], 
)
    

Blender = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Blender_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Blender_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Blender_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Blender_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Blender_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Blender_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Blender_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Blender_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Blender_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Blender_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Blender_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Blender_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Blender_13"), InlineKeyboardButton(text="27 dars", callback_data="Blender_14")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Blender_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Blender_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Blender_1glavni")]
    ], 
)

CorelDRAW = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="CorelDRAW_1"), InlineKeyboardButton(text="3-4 dars", callback_data="CorelDRAW_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="CorelDRAW_3"), InlineKeyboardButton(text="7-8 dars", callback_data="CorelDRAW_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="CorelDRAW_5"), InlineKeyboardButton(text="11-12 dars", callback_data="CorelDRAW_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="CorelDRAW_7"), InlineKeyboardButton(text="15-16 dars", callback_data="CorelDRAW_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="CorelDRAW_9"), InlineKeyboardButton(text="19-20 dars", callback_data="CorelDRAW_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="CorelDRAW_11"), InlineKeyboardButton(text="23-24 dars", callback_data="CorelDRAW_12")],
        [InlineKeyboardButton(text="25 dars", callback_data="CorelDRAW_13")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="CorelDRAW_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="CorelDRAW_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="CorelDRAW_1glavni")]
    ], 
)

SolidWorks= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="SolidWorks_1"), InlineKeyboardButton(text="3-4 dars", callback_data="SolidWorks_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="SolidWorks_3"), InlineKeyboardButton(text="7 dars", callback_data="SolidWorks_4")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="SolidWorks_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="SolidWorks_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="SolidWorks_1glavni")]
    ], 
)

Compass3d= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Compass3d_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Compass3d_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Compass3d_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Compass3d_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Compass3d_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Compass3d_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Compass3d_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Compass3d_8")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Compass3d_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Compass3d_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Compass3d_1glavni")]
    ], 
)

Revit_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Revit_darslari_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Revit_darslari_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Revit_darslari_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Revit_darslari_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Revit_darslari_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Revit_darslari_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Revit_darslari_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Revit_darslari_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Revit_darslari_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Revit_darslari_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="Revit_darslari_11"), InlineKeyboardButton(text="23-24 dars", callback_data="Revit_darslari_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="Revit_darslari_13"), InlineKeyboardButton(text="27-28 dars", callback_data="Revit_darslari_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="Revit_darslari_15"), InlineKeyboardButton(text="31-32 dars", callback_data="Revit_darslari_16")],
        [InlineKeyboardButton(text="33-34 dars", callback_data="Revit_darslari_17"), InlineKeyboardButton(text="35-36 dars", callback_data="Revit_darslari_18")],
        [InlineKeyboardButton(text="37-38 dars", callback_data="Revit_darslari_19"), InlineKeyboardButton(text="39-40 dars", callback_data="Revit_darslari_20")],
        [InlineKeyboardButton(text="41-42 dars", callback_data="Revit_darslari_21"), InlineKeyboardButton(text="43-44 dars", callback_data="Revit_darslari_22")],
        [InlineKeyboardButton(text="45-46 dars", callback_data="Revit_darslari_23"), InlineKeyboardButton(text="47-48 dars", callback_data="Revit_darslari_24")],
        [InlineKeyboardButton(text="49-50 dars", callback_data="Revit_darslari_25"), InlineKeyboardButton(text="51-52 dars", callback_data="Revit_darslari_26")],
        [InlineKeyboardButton(text="53-54 dars", callback_data="Revit_darslari_27"), InlineKeyboardButton(text="55-56 dars", callback_data="Revit_darslari_28")],
        [InlineKeyboardButton(text="57-58 dars", callback_data="Revit_darslari_29"), InlineKeyboardButton(text="59-60 dars", callback_data="Revit_darslari_30")],
        [InlineKeyboardButton(text="61-62 dars", callback_data="Revit_darslari_31"), InlineKeyboardButton(text="63-64 dars", callback_data="Revit_darslari_32")],
        [InlineKeyboardButton(text="65-66 dars", callback_data="Revit_darslari_33"), InlineKeyboardButton(text="67-68 dars", callback_data="Revit_darslari_34")],
        [InlineKeyboardButton(text="69-70 dars", callback_data="Revit_darslari_35"), InlineKeyboardButton(text="71-72 dars", callback_data="Revit_darslari_36")],
        [InlineKeyboardButton(text="73-74 dars", callback_data="Revit_darslari_37"), InlineKeyboardButton(text="75-76 dars", callback_data="Revit_darslari_38")],
        [InlineKeyboardButton(text="77 dars", callback_data="Revit_darslari_39")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Revit_darslari_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Revit_darslari_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Revit_darslari_1_glavni")]
    ], 
)

maching_learning = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="maching_learning_1"), InlineKeyboardButton(text="3-4 dars", callback_data="maching_learning_2")],
        [InlineKeyboardButton(text="5 dars", callback_data="maching_learning_3")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="maching_learning_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="maching_learning_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="maching_learning_1glavni")]
    ], 
)


video_montaj = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Premiere Pro", callback_data="Premiere_Pro"), InlineKeyboardButton(text="After Effects", callback_data="After_Effects")],
        [InlineKeyboardButton(text="Filmora", callback_data="Filmora")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="video_montajorqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="video_montaj1glavni")]
    ], 
)


Premiere_Pro= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Premiere_Pro_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Premiere_Pro_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Premiere_Pro_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Premiere_Pro_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Premiere_Pro_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Premiere_Pro_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="Premiere_Pro_7"), InlineKeyboardButton(text="15-16 dars", callback_data="Premiere_Pro_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="Premiere_Pro_9"), InlineKeyboardButton(text="19-20 dars", callback_data="Premiere_Pro_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Premiere_Pro_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Premiere_Pro_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Premiere_Pro_1_glavni")]
    ], 
)

After_Effects = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="After_Effects_1"), InlineKeyboardButton(text="3-4 dars", callback_data="After_Effects_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="After_Effects_3"), InlineKeyboardButton(text="7-8 dars", callback_data="After_Effects_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="After_Effects_5"), InlineKeyboardButton(text="11 dars", callback_data="After_Effects_6")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="After_Effects_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="After_Effects_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="After_Effects_1_glavni")]
    ], 
)

Filmora = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Filmora_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Filmora_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Filmora_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Filmora_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="Filmora_5"), InlineKeyboardButton(text="11-12 dars", callback_data="Filmora_6")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Filmora_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Filmora_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Filmora_1_glavni")]
    ], 
)



bugalteriya = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="bugalteriya_1"), InlineKeyboardButton(text="3-4 dars", callback_data="bugalteriya_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="bugalteriya_3"), InlineKeyboardButton(text="7-8 dars", callback_data="bugalteriya_4")],
        [InlineKeyboardButton(text="9 dars", callback_data="bugalteriya_5")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="bugalteriya_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="bugalteriya_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="bugalteriya_1_glavni")]
    ], 
) 




suniy_intelect = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="suniy_intelect_1"), InlineKeyboardButton(text="3-4 dars", callback_data="suniy_intelect_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="suniy_intelect_3"), InlineKeyboardButton(text="7-8 dars", callback_data="suniy_intelect_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="suniy_intelect_5"), InlineKeyboardButton(text="11-12 dars", callback_data="suniy_intelect_6")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="suniy_intelect_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="suniy_intelect_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="suniy_intelect_1_glavni")]
    ], 
) 
 
smm__va_marketing =InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="SMM (tg,insta,fb)", callback_data="SMM_tg_inst_fb"), InlineKeyboardButton(text="Google Ads darslari", callback_data="Google_Ads_darslari")],
        [InlineKeyboardButton(text="SMM (Facebook) darslari", callback_data="SMM_Facebook_darslari"), InlineKeyboardButton(text="SMM (Instagram) darslari", callback_data="SMMInstagramdarslari")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="smm__va_marketingsorqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="smm__va_marketing_glavni")]
    ], 
) 

SMM_tg_inst_fb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="SMM_tg_inst_fb_1"), InlineKeyboardButton(text="3-4 dars", callback_data="SMM_tg_inst_fb_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="SMM_tg_inst_fb_3"), InlineKeyboardButton(text="7-8 dars", callback_data="SMM_tg_inst_fb_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="SMM_tg_inst_fb_5"), InlineKeyboardButton(text="11-12 dars", callback_data="SMM_tg_inst_fb_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="SMM_tg_inst_fb_7"), InlineKeyboardButton(text="15-16 dars", callback_data="SMM_tg_inst_fb_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="SMM_tg_inst_fb_9"), InlineKeyboardButton(text="19-20 dars", callback_data="SMM_tg_inst_fb_10")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="SMM_tg_inst_fb_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="SMM_tg_inst_fb_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="SMM_tg_inst_fb_1glavni")]
    ], 
)


Google_Ads_darslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="Google_Ads_darslari_1"), InlineKeyboardButton(text="3-4 dars", callback_data="Google_Ads_darslari_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="Google_Ads_darslari_3"), InlineKeyboardButton(text="7-8 dars", callback_data="Google_Ads_darslari_4")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="Google_Ads_darslari__toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="Google_Ads_darslari_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="Google_Ads_darslari_1_glavni")]
    ], 
)

SMM_Facebook_darslari=  InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="SMM_Facebook_darslari_1"), InlineKeyboardButton(text="3-4 dars", callback_data="SMM_Facebook_darslari_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="SMM_Facebook_darslari_3"), InlineKeyboardButton(text="7-8 dars", callback_data="SMM_Facebook_darslari_4")],
        [InlineKeyboardButton(text="9-10 dars", callback_data="SMM_Facebook_darslari_5"), InlineKeyboardButton(text="11-12 dars", callback_data="SMM_Facebook_darslari_6")],
        [InlineKeyboardButton(text="13-14 dars", callback_data="SMM_Facebook_darslari_7"), InlineKeyboardButton(text="15-16 dars", callback_data="SMM_Facebook_darslari_8")],
        [InlineKeyboardButton(text="17-18 dars", callback_data="SMM_Facebook_darslari_9"), InlineKeyboardButton(text="19-20 dars", callback_data="SMM_Facebook_darslari_10")],
        [InlineKeyboardButton(text="21-22 dars", callback_data="SMM_Facebook_darslari_11"), InlineKeyboardButton(text="23-24 dars", callback_data="SMM_Facebook_darslari_12")],
        [InlineKeyboardButton(text="25-26 dars", callback_data="SMM_Facebook_darslari_13"), InlineKeyboardButton(text="27-28 dars", callback_data="SMM_Facebook_darslari_14")],
        [InlineKeyboardButton(text="29-30 dars", callback_data="SMM_Facebook_darslari_15"), InlineKeyboardButton(text="31-32 dars", callback_data="SMM_Facebook_darslari_16")],
        [InlineKeyboardButton(text="33 dars", callback_data="SMM_Facebook_darslari_17")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="SMM_Facebook_darslari_1_toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="SMM_Facebook_darslari_1orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="SMM_Facebook_darslari_1_glavni")]
    ], 
)

SMMInstagramdarslari = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-2 dars", callback_data="SMMInstagramdarslari_1"), InlineKeyboardButton(text="3-4 dars", callback_data="SMMInstagramdarslari_2")],
        [InlineKeyboardButton(text="5-6 dars", callback_data="SMMInstagramdarslari_3"), InlineKeyboardButton(text="7-8 dars", callback_data="SMMInstagramdarslari_4")],
        [InlineKeyboardButton(text="To'liq darslik!", callback_data="SMMInstagramdarslari_1toliq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="SMMInstagramdarslari_1_orqaga"), InlineKeyboardButton(text="🔝 Asosiy Menyu", callback_data="SMMInstagramdarslari_1_glavni")]
    ], 
)