import modelbit as mb

def zephyr_prompt(prompt):
    return {'output': 'Hello World!'}

mb.login()
mb.deploy(zephyr_prompt, require_gpu=True)