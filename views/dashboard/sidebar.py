import streamlit as st
import sys
sys.dont_write_bytecode = True

def sidebar_order():
    add_selectbox = st.sidebar.selectbox(
        "注文書",
        ("  ", "登録", "更新", "削除")
    )
    return add_selectbox