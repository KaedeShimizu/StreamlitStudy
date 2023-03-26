# 其实就是展示一些数据
# 最常见的就是表格 其他的数据可以直接展示在页面上
import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(
        np.random.randn(50, 5),
        columns=('col %d' % i for i in range(5))
)

"# 交互式表格"
st.dataframe(df)
"# 静态表格"
st.table(df)

"# 展示一个指标的变化"
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
# value 参数表示当前指标值
# delta 参数表示与前值的差值，向上的绿色箭头代表相比于前值，是涨的，反之向下的红箭头代表相比于前值是跌的。
# 当然涨跌颜色可以通过 delta_color 参数来控制。

"# JSON组件"
"可以展示JSON内容"
st.json({
    'foo': 'bar',
    'stuff': [
        'stuff 1',
        'stuff 2',
    ],
})