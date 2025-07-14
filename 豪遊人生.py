import keyboard
import time
import random

#初期設定


professinal_list = [0,0,0]
player_name = []
masu = [0,0,0]
player_money = []
player_shoku = []
player_kyuuryou = []
lim_masu = 50
player_num = 0
roulette_gamble = 0
hantei_fate = -1


event =["","朝から並んでパチンコだ！","今日は7月7日！パチンコだ！","","サマージャンボ宝くじ",
"今日は宝くじが当たりそうだ","カジノをかじってみる","","近くに新しいパチンコ屋がオープン！","流行のカフェに行く。",
"新人研修お疲れ。パチンコ行こう！","好きな作家の新作を見つける。","天気がいいからパチンコ","賞与が出た。今夜は飲みだ！","宝くじ買ってみた！",
"お金を増やそう！宝くじだ！","今日は運がいい。宝くじを買おう！","近所の犬にほえられる。","パチンコでひと遊び！","",
"風邪をひいた…。","友達とパチンコに行く。","仕事頑張った。賞与ゲット！","海外といったらカジノです。","図書館で読書",
"パチンコ屋で涼もう！","先輩に誘われてカジノ","","カジノは大人の嗜みです。","宝くじで一発当ててやる！",
"カジノで豪遊＾＾","宝くじ！宝くじ！宝くじ！","話題の新作映画を見た。","友達と夢の国に行く。","アコムをのぞいてみる",
"初めての♪アコム♪","新台入荷！パチンコ！","オンラインカジノで荒稼ぎ＾＾","会社を休みたい","宝くじで大逆転！",
"上手に料理を作れた。","","パチンコでストレス発散～","上司に怒られる…パチンコ！","上司に褒められる。宝くじ！",
"定時退社！パチンコ！","宝くじで夢を買おう！","","友達と飲み会 ↑","カジノ楽しい～～"]




#------------------------------------------------------------------------#
#def

#1.職業決め
def 労働人生():
    global hantei_fate
    global player_money
    global player_name
    global player_kyuuryou
    global player_shoku

    if hantei_fate == -1:
        work = {"公務員":200000,"エンジニア":220000,"底辺youtuber":150000,"石油王":800000,
                "サッカー選手":400000,"営業マン":250000,"ニート":80000,"アイドル":180000,"タイミー":100000,"医者":600000}
        work_list = list(work.keys())

        players = {}

        for i in range(1, 4):
            job = random.choice(work_list) 
            players[f"player{i}"] = {"money": 50000, "job": job}

        for name, info in players.items():
            job = info["job"]
            salary = work.get(job)
            info["money"] += salary
            print(f"{name}（{job}）は給料{salary}円をもらい、現在の所持金は{info['money']}円です。")
            player_name.append(name)
            player_money.append(info["money"])
            player_kyuuryou.append(salary)
            player_shoku.append(job)
    hantei_fate = 0




#パチンコ_確率
def pachi_result():
    global player_money
    global player_num
    price_pachi=40000
    number = random.randint(1,10)
    print(f"出た数字:{number}")
    
    if 1<=number<7:
        player_money[player_num] -= price_pachi
        print("ざんねん！4万円失う")
    elif 7<=number<=10:
        player_money[player_num] += price_pachi
        print("アタリ！4万円もらう")

        
#カジノ_確率
def casino_result():
    global player_money
    global player_num
    price_ca1=100000
    price_ca2=300000
    number = random.randint(1,10)
    print(f"出た数字:{number}")
    
    if 1<=number<8:
        player_money[player_num] -= price_ca1
        print("ざんねん！10万円失う")
    elif  8<=number<=10:
        player_money[player_num] += price_ca2
        print("あたり！30万円もらう")



#宝クジ　確立
def takara_result():
    global player_money
    global player_num
    number = random.randint(1,10)
    price_takara = 200000
    price_takara2 = 1000000
    print(f"出た数字:{number}")

    if 1<=number<9:
        player_money[player_num] -=price_takara
        print("ハズレ！20万円失う")

    elif number==10:

        player_money[player_num] += price_takara2
        print("１等！100万円獲得！")



#ボーナス
def syouyo_result():
    global player_kyuuryou
    global player_num
    global player_money
    player_money[player_num] += player_kyuuryou[player_num]*3



#2.ルーレット
def roulette():
    return random.randint(1,10)





#3.移動
def masu_ido():
    global player_num
    global masu
    global hantei_fate
    global event
    global player_money
    global player_name
    global player_kyuuryou
    global player_shoku
    
    
    if hantei_fate == 0:
        roulettes = roulette()
        masu[player_num] += roulettes
        time.sleep(1)
        #すべてゴールについたら
        if masu[0] > 50 and masu[1] > 50 and masu[2] > 50:
            hantei_fate = 1
            for i in range(len(player_name)):
                print("\n")
                print(f"{player_name[i]}：{player_money[i]}")
            return
        #プレイヤー"n"がゴールについたら
        if masu[player_num] > 50:
            print(f"Player{player_num+1}：{player_shoku[player_num]}\n{masu[player_num]}マス\n")
            print("ゴールしたので5万円貰う")
            player_money[player_num] += 50000
            print(f"現在の所持金は{player_money[player_num]}です\n\n\n")
            player_num += 1

            if player_num == 3:
                player_num = 0
            return
            
        #通常処理
        print(f"Player{player_num+1}：{player_shoku[player_num]}\n{masu[player_num]}マス\n")
        event_masu = event[masu[player_num]]
        print(event_masu)

        #からのマスもあるため
        if event_masu =="":
            pass
        else:        
            money(event_masu)

        print(f"現在の所持金は{player_money[player_num]}です\n\n\n")
        
        player_num += 1

        if player_num == 3:
            player_num = 0
        
        return event_masu



#4.単語検知
def money(event_masu):
    global player_money
    global event
    global player_num
    global masu
    if "パチンコ" in event_masu:
        pachi_result()
    elif "カジノ" in event_masu:
        casino_result()
    elif "宝" in event_masu:
        takara_result()
    elif "賞与" in event_masu:
        syouyo_result()
    elif "アコム" in event_masu:
        if player_money[player_num] <= 0:
            player_money[player_num] = 100000
    return player_money[player_num]


#-------------------------------------------------------------------------------#


#ゲーム文

print("人生ゲーム始まるよ\n職業決めてね")



keyboard.on_press_key("ctrl",lambda _: masu_ido()) #ます移動
keyboard.on_press_key("shift",lambda _: 労働人生()) #職業決め（最初に実行）

keyboard.wait()
