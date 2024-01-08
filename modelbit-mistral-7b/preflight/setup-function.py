import modelbit as mb

def mistral_prompt(prompt):
    return {'output': 'Hello World!'}

mb.login()
mb.deploy(mistral_prompt, require_gpu=True)