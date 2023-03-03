from modules import shared

def on_ui_settings():
    section = "chatgptprompts", "ChatGPT Prompts"
    shared.opts.add_option(
        key="cp_openai_api_key",
        info=shared.OptionInfo(
            False,
            label="OpenAI API Key",
            section=section,
        ),
    )