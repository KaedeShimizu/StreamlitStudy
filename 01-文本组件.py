import streamlit as st
# 有很多种文本组件，都可以直接显示在页面上面

# Markdown文本
st.markdown("Kaede -> **Kaede加粗**")

# 设定大标题
st.title("这是一个大标题")

# 一级标题
st.header("这是一级标题")

# 二级标题
st.subheader("这是二级标题")

# 展示代码段落
code = '''
def sayHello():
    print("Hello World")
'''
# 你需要设定一下语言
st.code(code, language="python")

# 普通文本
st.text("这是一段普通的文本")

# LaTex公式
st.latex(r'''
  a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
  \sum_{k=0}^{n-1} ar^k =
  a \left(\frac{1-r^{n}}{1-r}\right)
''')