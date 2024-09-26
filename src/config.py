# 配置文件，用于维护脚本列表、路径和生成器描述
GENERATOR_CONFIG = {
    'default': {
        'scripts': {
            'generate_random_num_from_1_100.py': '生成1到100之间的随机数',
            'sum_1_100.py': '计算1到100的和',
            'get_current_date.py': '获取当前日期和时间'
        },
        'description': '用于基本任务（随机数生成，当前时间，求和等任务）的生成器',
        'path': 'src/python_scripts',
        'class': 'PromptGenerator'
    },
    'permission_assign': {
        'scripts': {
            'assign_access_for_dataset.py': '为数据集分配访问权限',
            'assign_access_for_dashboard.py': '为Dashboard分配访问权限'
        },
        'description': '用于高级任务（权限分配等任务）的生成器',
        'path': 'src/advanced_scripts',
        'class': 'AdvancedPromptGenerator'
    }
}

GENERATOR_PROMPT_TEMPLATE = (
    "根据以下输入，选择一个生成器类型（{types}）：\n\n"
    "输入：{input_text}\n\n"
    "生成器类型说明：\n"
    "{descriptions}\n\n"
    "请只返回生成器类型。"
)

SCRIPT_PROMPT_TEMPLATE = (
    "根据以下输入，选择一个最合适的脚本（{scripts}）：\n\n"
    "输入：{input_text}\n\n"
    "脚本说明：\n"
    "{descriptions}\n\n"
    "请只返回脚本名称。"
)