'''

У Дурова отжали ВКонтакте, но он не сдался и создал уже не социальную сеть, а мессенджер - Телеграм. 
Вы наверное знаете, что в Телеграме любой пользователь может выбрать себе username, чтобы его было легче искать. 
Давайте поможем Паше и напишем регулярное выражение, которое будет проверять валидность username.

Что нужно найти:

Если посмотреть на эти скриншоты:

то можно понять, что в username, в котором выполняются следующие условия:

    Используются символы a-z, A-Z, 0-9, _
    Длина от 5 до 32 символов включительно
    Не может начинаться с цифры или _
    Не может заканчиваться на _

На самом деле есть ещё одно условие: username не может содержать в себе __, но на данный момент сделать такое будет трудновато.

Sample Input 1:

hazzus ⇒ tegmilan ⇒ lordvladtheimpalertransylvania ⇒ anxkhn ⇒ cksnb ⇒ tatotan ⇒ plashspeed ⇒ mikesew1320 ⇒ i_am_just_as_cringe ⇒ meertkrts ⇒ megajoy ⇒ hexwrty ⇒ yltned ⇒ origincode ⇒ freedomnesss ⇒ sayakamiki ⇒ mohammedbablasi ⇒ posi_farmer_ranjan ⇒ lesikvip ⇒ th_bst ⇒ aryansamra ⇒ necrowitch ⇒ xxkhanxx ⇒ nome_tg ⇒ aless1010 ⇒ sudo_nautilus ⇒ try2prog ⇒ devonpython ⇒ the_jug ⇒ databankco ⇒ du3ei ⇒ lenni_builder ⇒ aemangar ⇒ uwuth ⇒ hz_lucifer ⇒ kangaroointernational ⇒ scagionare ⇒ mahi747 ⇒ andrey_rucvc ⇒ joker_asd_s ⇒ alk_is_noob ⇒ o_osp_bcf_offi ⇒ haiz_me ⇒ xtremeornob ⇒ skiduchiha ⇒ meizishandev ⇒ nitrovenom ⇒ plankff ⇒ glocktwentyone ⇒ faizbastomi ⇒ antihallobst ⇒ erdils ⇒ helledryn ⇒ kircheiss ⇒ av7m7x ⇒ tarbless

Sample Output 1:

hazzus tegmilan lordvladtheimpalertransylvania anxkhn cksnb tatotan plashspeed mikesew1320 i_am_just_as_cringe meertkrts megajoy hexwrty yltned origincode freedomnesss sayakamiki mohammedbablasi posi_farmer_ranjan lesikvip th_bst aryansamra necrowitch xxkhanxx nome_tg aless1010 sudo_nautilus try2prog devonpython the_jug databankco du3ei lenni_builder aemangar uwuth hz_lucifer kangaroointernational scagionare mahi747 andrey_rucvc joker_asd_s alk_is_noob o_osp_bcf_offi haiz_me xtremeornob skiduchiha meizishandev nitrovenom plankff glocktwentyone faizbastomi antihallobst erdils helledryn kircheiss av7m7x tarbless

Sample Input 2:

i0i#r ⇒ kigd@2 ⇒ taaphli-octoandri ⇒ crypticfrоg ⇒ тест ⇒ suDhAsa010 ⇒ Thematdev ⇒ oo?om09 ⇒ ooo>m11 ⇒ sac<charose ⇒ thekillerbun$ny12341 ⇒ shuse!kagari ⇒ du%eru42 ⇒ hy&perterminal ⇒ su*theta ⇒ adb(reboot)bootloader ⇒ marb=ololo ⇒ theminidev ⇒ a_e_i_o_u_hacker143 ⇒ aldyhk ⇒ bio_chain_2_bot ⇒ miiiiiyt ⇒ bederke ⇒ barry021 ⇒ aikaravinu ⇒ romangraef ⇒ awidok ⇒ mechanarutosucks

Sample Output 2:

suDhAsa010 Thematdev theminidev a_e_i_o_u_hacker143 aldyhk bio_chain_2_bot miiiiiyt bederke barry021 aikaravinu romangraef awidok mechanarutosucks

Sample Input 3:

SpamBot GroupAnonymousBot

Sample Output 3:

SpamBot GroupAnonymousBot

'''

regex = r'(?<!\S)([a-zA-Z0-9_])*(?!\S){5,32}'
