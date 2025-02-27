
2. **Adicionar testes automatizados**:
   Crie um arquivo `test_main.py` para adicionar testes automatizados usando `unittest` ou `pytest`.

3. **Configurar CI/CD**:
   Adicione um workflow GitHub Actions para automatizar a execução dos testes. Crie um arquivo `.github/workflows/python-app.yml` com o seguinte conteúdo:

```yaml
name: Python application

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest