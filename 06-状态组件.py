import streamlit as st
import time
"""
# 状态组件用来向用户展示当前程序的运行状态，包括：

progress：进度条，如游戏加载进度

spinner：等待提示

balloons：页面底部飘气球，表示祝贺

error：显示错误信息

warning：显示报警信息

info：显示常规信息

success：显示成功信息

exception：显示异常信息（代码错误栈）
"""

"进度条"
st.progress(50)

"加载内容"
with st.spinner("稍等..."):
    time.sleep(3)
    # 加载完展示气球
    st.balloons()

"警告框"
st.warning("这是一个警告框")

"错误框"
st.error("这是一个报错的框")

"提示框"
st.info("这是一个提示框")

"成功框"
st.success("成功Success~")

"报错"
st.exception("这段代码报错了喵?")