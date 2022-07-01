dist=384400000000 # 月までの距離(mm)
thickness=1 #紙の厚さ(mm)
count=0 #折り曲げた回数

while thickness < dist:
    thickness=thickness*2 #厚みを2倍にする
    count=count+1 #回数を1増やす
    #状況を出力
    print(count,'回折り曲げた','厚み:',thickness)

#while文を抜けたら結果を出力
print(count,'回で月に到達しました。')
