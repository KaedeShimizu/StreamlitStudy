import streamlit as st

"""
# 主要的组件:

button：按钮

download_button：文件下载

file_uploader：文件上传

checkbox：复选框

radio：单选框

selectbox：下拉单选框

multiselect：下拉多选框

slider：滑动条

select_slider：选择条

text_input：文本输入框

text_area：文本展示框

number_input：数字输入框，支持加减按钮

date_input：日期选择框

time_input：时间选择框

color_picker：颜色选择器

# 有这些公共属性:

label：组件上展示的内容（如：按钮名称）

key：当前页面唯一标识一个组件

help：鼠标放在组件上展示说明信息

on_click / on_change：组件发生交互（如：输入、点击）后的回调函数

args：回调函数的参数

kwargs：回调函数的参数
"""

st.button("这是一个按钮")
st.file_uploader("这是上传按钮")
st.checkbox("这是一个复选框")
# 这里你只需要用一个数组即可
st.selectbox("这是下拉选择框", options=["Kaede", "Shimizu", "Good"])
st.slider("这是一个滑动条", 0, 100)
st.select_slider("这是一个选择条",["Kaede", "cute", "girl", "beauty"])
st.text_input("这是一个输入框", placeholder="这是默认的holder")
st.text_area("这是文本展示框", "这是文本框里面的东西")
st.number_input("数字输入框", 0, 100)
st.date_input("日期选择框")
st.time_input("时间选择器")
st.color_picker("颜色选择器")