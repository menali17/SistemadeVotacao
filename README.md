# Sistema de Votação - Projeto Livre

Este é um sistema de votação eletrônico desenvolvido como Projeto Livre para a disciplina de **Orientação a Objetos** (semestre 01/2025), ministrada na Faculdade UnB Gama.

## 🎯 Objetivo do Projeto

Desenvolver um sistema completo de votação eletrônico com:
- Cadastro de eleitores
- Validação de dados
- Urna gráfica simulando uma urna real
- Registro de votos com persistência de dados em arquivos JSON

O sistema respeita o paradigma de **Programação Orientada a Objetos**, utilizando os principais conceitos vistos em sala, como **herança, polimorfismo, encapsulamento, composição forte, associação fraca** e **mixins**.

---

## 🧩 Casos de Uso

### 1. Cadastro de Eleitor
- O usuário preenche um formulário com:
  - Nome completo
  - CPF
  - RG
  - CEP
  - Data de nascimento
- O sistema valida:
  - CPF único e válido
  - Idade mínima (16 anos completos)
  - Formato dos campos
- Em caso de sucesso, o eleitor é armazenado em `eleitores.json`.

### 2. Validação de CPF
- Ao tentar cadastrar, o sistema verifica:
  - Se o CPF já está presente
  - Se o formato e dígitos do CPF são válidos
- Bloqueia duplicatas ou entradas inválidas.

### 3. Autenticação para Votação
- O eleitor informa seu CPF na urna.
- O sistema verifica:
  - Se o CPF está cadastrado
  - Se o eleitor ainda não votou

### 4. Votação por Cargo
- Para cada cargo (Presidente, Senador etc.):
  - O eleitor digita o número do candidato.
  - A urna exibe o nome e imagem (se implementado).
  - O eleitor confirma ou corrige o voto.

### 5. Registro de Voto
- Os votos são registrados no arquivo `todos_os_votos.json`.
- Cada CPF é uma chave, e os votos são armazenados como um dicionário dos cargos e respectivos candidatos.
  ```json
  {
    "12345678900": {
      "Presidente": "25",
      "Senador": "15"
    }
  }
  ```

### 6. Prevenção de Voto Duplicado
- Antes de permitir o voto, o sistema verifica se o CPF já consta no arquivo `todos_os_votos.json`.
- Caso já exista, o sistema impede novo acesso à votação.

---

## 🖼 Interface Gráfica

- Desenvolvida com `tkinter`, possui:
  - Interface de cadastro limpa e intuitiva
  - Simulação visual de urna eletrônica
  - Teclado virtual na tela
  - Exibição do candidato conforme número digitado

---

## 🧠 Recursos de Orientação a Objetos Aplicados

- ✅ **Herança:** Classe `Eleitor` herda de `Pessoa`
- ✅ **Polimorfismo:** Métodos sobrescritos em classes controladoras
- ✅ **Encapsulamento:** Atributos protegidos e validações internas
- ✅ **Composição Forte:** A urna contém e controla o fluxo de votação
- ✅ **Associação Fraca:** Associação entre objetos auxiliares e componentes de interface
- ✅ **Mixins:** (Pode ser implementado em futuras melhorias)

---

## 📁 Estrutura de Pastas

```
SistemaDeVotacao/
├── CadastroEleitores_Profissional/
│   ├── main.py
│   ├── dados/
│   │   └── eleitores.json
│   └── package/
│       ├── cadastro.py
│       ├── eleitor.py
│       ├── pessoa.py
│       ├── validacoes.py
│       └── interface.py
├── UrnaEletronica_Interface/
│   ├── main.py
│   ├── dados/
│   │   └── votos/
│   │       └── todos_os_votos.json
│   └── package/
│       ├── urna.py
│       ├── candidato.py
│       ├── interface_urna_exibir_candidato.py
│       └── eleitor.py
```

---

## 🗳️ Como Executar

### 1. Cadastro de Eleitores
```bash
cd CadastroEleitores_Profissional
python main.py
```

### 2. Urna Eletrônica
```bash
cd UrnaEletronica_Interface
python main.py
## 🗳️ Candidatos por Cargo

### Presidente
- **25** - José Mariano  
- **77** - Jéssica Fernandes  
- **12** - Rogério de Sá Silveira  

### Governador
- **45** - Lucas da Silva  
- **13** - Marina Costa  

### Senador
- **50** - Ana Paula Dias  
- **60** - Carlos Menezes  

### Deputado Federal
- **1010** - Fernanda Lima  
- **2020** - Ricardo Gomes  

### Deputado Estadual
- **3030** - Patrícia Souza  
- **4040** - Eduardo Ramos 
```

---

## 🧪 Testagem

- Eleitores cadastrados são salvos no arquivo `eleitores.json`.
- Apenas eleitores com idade mínima e CPF válido podem votar.
- O voto é gravado em `todos_os_votos.json` com rastreabilidade por CPF.
- O sistema previne votos duplicados.

---

## 📝 Autor

Projeto desenvolvido individualmente por **Enzo Menali Toledo**, estudante de Engenharia de Software na Universidade de Brasília (UnB Gama).

---

