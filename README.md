# 🔄 Conversor Multiuso (Modularizado)

Projeto em Python desenvolvido com arquitetura modularizada no **VS Code**, dividido em múltiplos arquivos para separar as responsabilidades de negócio, chamadas de APIs externas e navegação do usuário.

---

## 📁 Estrutura de Arquivos e Módulos

O projeto foi dividido em módulos independentes para manter o código limpo, legível e fácil de manter:

meu_projeto/
│
├── main.py          # Arquivo principal: gerencia o menu e o fluxo de execução
├── moedas.py        # Módulo de Câmbio: consome a API de cotação em tempo real
├── unidades.py      # Módulo de Medidas: contém as regras de conversão matemática
└── README.md        # Documentação do repositório
