import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.sidebar.title('レイアウトを整える')

# #sidebarを付け加えると左側にインタラクティブなウィジェットを追加し、結果を画面に表示。
# textoption = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', textoption , 'です'

# condition = st.sidebar.slider('あなたの調子は？',0,100,50)
# 'コンディション：', condition

#カラム数に応じたレイアウト作成
# left_column, right_column = st.beta_columns(2)
# butt = left_column.button('右カラムに文字を表示')
# if butt:
#     right_column.write('ここは右カラムです')

# #エクスパンダ= FAQで使用されるレイアウト
# ex = st.beta_expander('かやちゃんってだれ？？',expanded=True)
# ex.write('庚申塚の女です。')
# ex1 = st.beta_expander('かやちゃんっておバカ？？')
# ex1.write('はいそうです。')

#プログレスバー
#空のイテレーションとバーを用意(画面には表示されない)
latest_iteration = st.empty()
bar = st.progress(0)

#値が入る
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'かやちゃんってFカップなんでしょ😎'
ex = st.beta_expander('かやちゃんってだれ？？',expanded=True)
ex.write('庚申塚の女です。')
ex1 = st.beta_expander('かやちゃんっておバカ？？',expanded=True)
ex1.write('はいそうです。')
