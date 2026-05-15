import streamlit as st

st.set_page_config(
    page_title="streamlit的入门",
    layout="wide",
    # 控制侧边栏
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': 'https://www.streamlit.io/report-bug',
        'About': '测试信息',
    }
)

st.title("这是标题")
st.header("一级标题")
st.subheader("二级标题")

# 使用streamlit run .\第4章\streamlit入门\streamlit入门.py启动

st.write("""
```java
public static void main(String[] args) {
    System.out.println("Hello World!");
}
```
这是文件
""")

st.image(image="C:/Users/Administrator/Pictures/微信图片_20260320081030_33_4.jpg")

data = {
    "岗位": ["开发", "测试"],
    "部门": ["销售", "研发"]
}
st.table(data)
name = st.text_input(label="输入姓名：", type="password")
st.write(f"你的姓名:{name}")
radio = st.radio("请输入姓名", ["t1", "t2", "t3"])
st.write(f"单选：:{radio}")
multi = st.multiselect("多选", ["t1", "t2", "t3"])
st.write(f"多选：:{multi}")
