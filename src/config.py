# 配置文件，用于维护脚本列表、路径和生成器描述
GENERATOR_CONFIG = {
    'default': {
        'scripts': [
            'assign_access_for_dataset.py',
            'generate_random_num_from_1_100.py',
            'sum_1_100.py',
            'get_current_date.py'
        ],
        'description': '用于基本任务（任务分配，随机数生成，当前时间，求和等任务）的生成器',
        'path': 'src/python_scripts',
        'class': 'PromptGenerator'
    },
    'advanced': {
        'scripts': [
            'advanced_script_1.py',
            'advanced_script_2.py'
        ],
        'description': '用于高级任务的生成器',
        'path': 'src/advanced_scripts',
        'class': 'AdvancedPromptGenerator'
    },
    'expert': {
        'scripts': [
            'expert_script_1.py',
            'expert_script_2.py'
        ],
        'description': '用于专家任务的生成器',
        'path': 'src/expert_scripts',
        'class': 'ExpertPromptGenerator'
    }
}

GENERATOR_PROMPT_TEMPLATE = (
    "根据以下输入，选择一个生成器类型（{types}）：\n\n"
    "输入：{input_text}\n\n"
    "生成器类型说明：\n"
    "{descriptions}\n\n"
    "请只返回生成器类型。"
)
