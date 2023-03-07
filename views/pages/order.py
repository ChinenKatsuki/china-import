import streamlit as st
import requests
import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
from dashboard.sidebar import sidebar_order
import json
# import views.dashboard

selected = sidebar_order()
if selected == '登録':
    with st.form(key='order_create'):
        order_name = st.text_input('注文書名')
        submit = st.form_submit_button(label='登録')
        if submit:
            st.write(order_name)
            data = {
                'order_name': order_name
            }
            order_create_url = 'http://127.0.0.1:8000/create/order'
            res = requests.post(
                order_create_url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('注文書の登録完了')