# 脚本分析与执行系统

## 项目介绍

这是一个基于Streamlit和Ollama的脚本分析与执行系统。该系统能够分析用户输入的文本，确定适当的生成器类型，生成相应的脚本名称，并执行匹配的脚本。整个过程通过一个用户友好的Web界面呈现。

## 主要功能

- 文本输入：用户可以输入需要分析的文本。
- 自动分析：系统使用Ollama模型分析输入，确定合适的生成器类型。
- 脚本生成：基于分析结果，系统生成相应的脚本名称。
- 脚本执行：如果找到匹配的脚本，系统将执行该脚本并返回结果。
- 结果展示：执行结果直接显示在Web界面上。

## 环境要求

- Python 3.10+
- Streamlit
- Langchain
- Ollama

## 环境设置步骤

1. 克隆项目仓库：
   ```
   git clone git@github.com:gszhangwei/task_assistant.git
   cd task_assistant
   ```

2. 创建并激活虚拟环境（可选）：
   ```
   python3 -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip3 install -r requirements.txt
   ```

4. 安装并设置Ollama：
   - 访问 [Ollama官网](https://ollama.ai/) 下载并安装Ollama
   - ``ollama run llama3.1``确保Ollama服务正在运行

5. 配置项目：
   - 检查并更新 `config.py` 文件中的配置信息
   - 确保 `GENERATOR_CONFIG` 中的路径设置正确

## 运行应用

在项目根目录下执行以下命令：
```streamlit run src/app.py```

然后在浏览器中访问显示的URL（通常是 `http://localhost:8501`）。

## 使用说明

1. 在文本框中输入您想要分析的内容。
2. 点击"分析并执行"按钮。
3. 系统将自动分析您的输入并执行相应的脚本。
4. 执行结果将显示在页面上。

## 项目结构
````
project/
│
├── src/
│ ├── advanced_scripts
│ ├── expert_scripts
│ ├── python_scripts
│ ├── app.py # Streamlit应用主文件
│ ├── execute_script_with_ollama.py # 核心逻辑实现
│ ├── prompt_generator_factory.py # 提示生成器工厂
│ └── config.py # 配置文件
│
├── requirements.txt # 项目依赖
└── README.md # 项目说明文档
````
## 贡献
欢迎提交问题和拉取请求。这是一个基础版本，还有很多需要提升的地方，希望大家能多提意见，一起改进。

## 许可
[MIT](https://choosealicense.com/licenses/mit/)
