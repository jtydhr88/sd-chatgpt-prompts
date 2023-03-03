# Automatic1111 entry point.

from sd_chatgpt_prompts.chatgpt_prompting import Script
from modules import script_callbacks
from modules import shared

__all__ = ["Script"]

def on_ui_settings():
    section = ('chatgpt', "ChatGPT")
    shared.opts.add_option("openai_api_key", shared.OptionInfo(
        "", "OpenAI API key", section=section))
    shared.opts.add_option("chatgpt_prefix", shared.OptionInfo(
        "If you are an AI artist, please describe a painting, must includes the following elements:", "ChatGPT Prefix", section=section))
    shared.opts.add_option("chatgpt_temperature", shared.OptionInfo(
        "0.6", "Temperature",
        section=section))
    shared.opts.add_option("max_tokens", shared.OptionInfo(
        "512", "Max Tokens",
        section=section))

script_callbacks.on_ui_settings(on_ui_settings)

