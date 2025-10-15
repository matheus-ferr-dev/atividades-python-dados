# Guia de Contribuição

Obrigado por considerar contribuir para este projeto! Este documento fornece diretrizes para contribuir com os exercícios de Python.

## 🚀 Como Contribuir

### 1. Fork do Projeto
- Faça um fork do repositório
- Clone seu fork localmente
- Crie uma branch para sua contribuição

### 2. Estrutura do Projeto
```
atividades-python-dados/
├── atividade_um_p1/     # Estruturas de Dados
├── atividade_um_p2/     # Funções
└── docs/               # Documentação adicional (se necessário)
```

### 3. Padrões de Código

#### Python
- Use Python 3.6+
- Siga o PEP 8 para estilo de código
- Use type hints quando apropriado
- Documente funções com docstrings

#### Estrutura dos Exercícios
```python
# Exercício X - Descrição do exercício

def exercicio_x():
    """
    Descrição detalhada do que o exercício faz.
    """
    # Implementação aqui
    pass

if __name__ == "__main__":
    exercicio_x()
```

### 4. Tipos de Contribuição

#### ✅ Melhorias Aceitas
- Correção de bugs
- Melhoria na interface do usuário
- Otimização de código
- Adição de novos exercícios
- Melhoria na documentação
- Testes adicionais

#### ❌ Não Aceitas
- Mudanças que quebrem funcionalidade existente
- Código sem documentação adequada
- Exercícios que não sigam o padrão estabelecido

### 5. Processo de Submissão

1. **Teste seu código**
   ```bash
   python atividade_um_p1/exercicio_X.py
   ```

2. **Commit suas mudanças**
   ```bash
   git add .
   git commit -m "Descrição clara da mudança"
   ```

3. **Push para sua branch**
   ```bash
   git push origin sua-branch
   ```

4. **Abra um Pull Request**
   - Descreva claramente as mudanças
   - Referencie issues relacionadas
   - Inclua screenshots se aplicável

### 6. Padrões de Commit

Use mensagens de commit claras e descritivas:

```
feat: adiciona novo exercício de ordenação
fix: corrige erro na validação de entrada
docs: atualiza README com novas instruções
style: melhora formatação do código
refactor: otimiza algoritmo de busca
```

### 7. Diretrizes Específicas

#### Para Novos Exercícios
- Mantenha consistência com exercícios existentes
- Inclua tratamento de erros
- Use interface interativa amigável
- Adicione comentários explicativos

#### Para Correções
- Teste extensivamente antes de submeter
- Mantenha compatibilidade com código existente
- Documente mudanças significativas

### 8. Ambiente de Desenvolvimento

#### Configuração Recomendada
- Python 3.6+
- Editor com suporte a Python (VS Code, PyCharm, etc.)
- Git para controle de versão

#### Testes
- Execute todos os exercícios antes de submeter
- Verifique se não há erros de sintaxe
- Teste com diferentes entradas

### 9. Comunicação

- Use issues para reportar bugs ou sugerir melhorias
- Seja respeitoso e construtivo
- Ajude outros contribuidores quando possível

### 10. Reconhecimento

Contribuidores ativos serão listados no arquivo [CONTRIBUTORS.md](CONTRIBUTORS.md).

---

**Obrigado por contribuir!** 🎉
