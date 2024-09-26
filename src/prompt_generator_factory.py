from prompt_generators import PromptGenerator, AdvancedPromptGenerator, ExpertPromptGenerator
from config import GENERATOR_CONFIG


class PromptGeneratorFactory:
    GENERATOR_CLASSES = {
        'PromptGenerator': PromptGenerator,
        'AdvancedPromptGenerator': AdvancedPromptGenerator,
        'ExpertPromptGenerator': ExpertPromptGenerator
    }

    @staticmethod
    def get_prompt_generator(generator_type):
        config = GENERATOR_CONFIG.get(generator_type, GENERATOR_CONFIG['default'])
        generator_class = PromptGeneratorFactory.GENERATOR_CLASSES[config['class']]
        return generator_class(config['scripts'])

    @staticmethod
    def get_available_generator_types():
        return list(GENERATOR_CONFIG.keys())
