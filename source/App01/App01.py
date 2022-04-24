import PySimpleGUI as sg

sg.theme('Dark Brown')

# レイアウト
layout = [[sg.Text('これは PySimpleGUI を使ったサンプルプログラムです． ', font=('System', 14))],
[sg.Button('Quit ', font=('monospace', 12)),sg. Button('OK ', font=('monospace', 12))]]
# ウィンドウ作成
window = sg.Window ('Sample01 ', layout)
# イベントループ
while True:
    event , values = window.read() # イベントの読み取り（イベント待ち）
    print(' イベント:',event ,', 値:',values) # 確認表示
    if event in (None ,'Quit '): # 終了条件（ None: クローズボタン）
        print(' 終了します． ')
        break
# 終了処理
window.close()