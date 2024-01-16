import modelbit as mb

def svd():
    return {'output': 'Hello World!'}

mb.login()
mb.deploy(
        svd,
        require_gpu=True,
        system_packages=["python3-opencv"]
)
