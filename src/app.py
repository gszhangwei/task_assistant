import streamlit as st
from execute_script_with_ollama import analyze_and_execute

st.title("脚本分析与执行系统")

# 创建一个文本输入框
user_input = st.text_area("请输入一段话:", height=100)

# 创建一个按钮来触发分析和执行
if st.button("分析并执行"):
    if user_input:
        with st.spinner("正在分析和执行..."):
            # 调用analyze_and_execute函数并获取结果
            result = analyze_and_execute(user_input)
        st.success("分析和执行完成！")

        # 显示执行结果
        st.subheader("执行结果:")
        st.write(result)
    else:
        st.warning("请输入一些文本再进行分析。")

# 添加一些使用说明
st.sidebar.header("使用说明")
st.sidebar.write("""
1. 在文本框中输入您想要分析的内容。
2. 点击"分析并执行"按钮。
3. 系统将自动分析您的输入并执行相应的脚本。
4. 执行结果将显示在页面上。
""")