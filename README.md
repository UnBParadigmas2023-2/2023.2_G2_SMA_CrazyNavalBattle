# Crazy Naval Battle

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo (de acordo com a Planilha de Divisão dos Grupos)**: 02<br>
**Paradigma**: SMA<br>

## Alunos

| Matrícula  | Aluno                           |
| ---------- | ------------------------------- |
| 20/0013181 | Adne Moretti Moreira            |
| 20/0057227 | Caio Vitor Carneiro de Oliveira |
| 19/0085819 | Cícero Barrozo Fernandes Filho  |
| 19/0045817 | Gabriel Costa de Oliveira       |
| 20/0018205 | Gabriel Moretti de Souza        |
| 20/0019015 | Guilherme Puida Moreira         |
| 20/0067923 | João Henrique Marques Calzavara |
| 20/2023903 | Lucas Lopes Rocha               |

## Sobre

O projeto **Crazy Naval Battle** é uma simulação envolvente de uma batalha naval maluca, desenvolvida utilizando a linguagem de programação **Python** e a biblioteca **Mesa** para criação da interface gráfica. A abordagem adotada para modelar o comportamento dinâmico dos elementos na simulação é baseada no paradigma de **Sistemas Multiagentes (SMA)**.

<!--TO DO DESCREVER A FUNCAO DE CADA AGENTE -->

#### Agentes Envolvidos na Batalha:

- **Barco Submarino:** Especializado em estratégias furtivas e ataques surpresa.
- **Porta-Avião:** Oferece suporte aéreo e serve como uma base móvel para aeronaves.
- **Cruzador:** Equilíbrio entre mobilidade e poder de fogo.
- **Torpedeiro:** Focado em ataques de longa distância com torpedos.
- **Morteiro:** Agente de longo alcance especializado em causar danos significativos.
- **Contra-Torpedeiro:** Destinado a neutralizar ameaças de torpedos.
- **Contra-Morteiro:** Especializado em defesa contra agentes de longo alcance.

#### Configuração Personalizada:

O jogo permite que os usuários personalizem a quantidade de cada agente antes de iniciar a simulação, oferecendo uma experiência única a cada execução. Essa flexibilidade proporciona a criação de cenários diversos, desafiando os jogadores a explorar estratégias diferentes em cada simulação.

#### Paradigma de Sistemas Multiagentes (SMA):

O desenvolvimento do "Crazy Naval Battle" adota o paradigma de Sistemas Multiagentes, proporcionando uma representação fiel das interações complexas entre os diferentes agentes. Cada agente é autônomo, respondendo dinamicamente às condições do ambiente e às ações dos outros agentes, resultando em uma simulação envolvente e estratégica.

## Screenshots

Adicione 2 ou mais screenshots do projeto em termos de interface e/ou funcionamento.

## Instalação

**Linguagens**: Python

**Tecnologias**: Mesa, Matplotlib

Para executar o projeto, é necessário uma instalação do Python 3.
Em sistemas Debian (ou derivados):

```
sudo apt install python3 python3-venv
```

Crie um `venv` usando:

```
python3 -m venv .venv
```

Ative o `venv` e instale as dependências:

```
source .venv/bin/activate
pip install -r requirements.txt
```

E rode o projeto:

```
python3 run.py
```

A interface estará disponível em `localhost:8521`.

## Uso

Explique como usar seu projeto.
Procure ilustrar em passos, com apoio de telas do software, seja com base na interface gráfica, seja com base no terminal.
Nessa seção, deve-se revelar de forma clara sobre o funcionamento do software.

## Vídeo

O vídeo de apresentação está disponível em:

- Youtube: [ACESSO]()
- GitHub: [ACESSO]()

## Participações

| Nome do Membro                  | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| ------------------------------- | :----------: | :----------------------------------------------------------------------------: |
| Adne Moretti Moreira            |      -       |                                       -                                        |
| Caio Vitor Carneiro de Oliveira |      -       |                                       -                                        |
| Cícero Barrozo Fernandes Filho  |      -       |                                       -                                        |
| Gabriel Costa de Oliveira       |      -       |                                       -                                        |
| Gabriel Moretti de Souza        |      -       |                                       -                                        |
| Guilherme Puida Moreira         |      -       |                                       -                                        |
| João Henrique Marques Calzavara |      -       |                                       -                                        |
| Lucas Lopes Rocha               |      -       |                                       -                                        |

## Outros

### Lições Aprendidas

- **Sistema Multiagentes (SMA):** A principal lição aprendida foi a aplicação do paradigma de Sistemas Multiagentes (SMA) no desenvolvimento da simulação de batalha naval maluca. Utilizar SMA permitiu a modelagem de agentes autônomos interativos, representando diferentes unidades navais com comportamentos distintos. Isso facilitou a compreensão e simulação de estratégias e interações complexas entre os agentes.
- **Configuração Dinâmica:** Lidar com a configuração dinâmica do número de agentes de cada tipo foi desafiador. A flexibilidade do SMA permitiu a adaptação fácil do sistema às preferências do usuário, proporcionando uma experiência personalizada na simulação.
- **Interconexão de Agentes:** Compreendemos como estabelecer interconexões eficientes entre os agentes, facilitando a comunicação e coordenação durante a simulação. Isso desempenhou um papel crucial na dinâmica da batalha naval maluca.

### Contribuições

- **Modelagem Eficiente dos Agentes:** Conseguimos criar com sucesso um ambiente de simulação onde diversos agentes, como submarinos, porta-aviões e contra-morteiros, interagem de forma autônoma e estratégica.
- **Personalização da Experiência:** A flexibilidade do SMA permitiu que os usuários personalizassem a quantidade de cada tipo de agente na simulação, proporcionando diferentes cenários de batalha.

### Fragilidades

- **Concorrência de Projetos Acadêmicos:** Uma fragilidade significativa foi a concorrência de tempo devido aos projetos acadêmicos de outras disciplinas no fim do semestre. As demandas adicionais de outras disciplinas da faculdade impactaram a disponibilidade da equipe para se dedicar integralmente ao desenvolvimento.
- **Curva de Aprendizado do Paradigma SMA:** A adaptação ao paradigma de Sistemas Multiagentes exigiu esforço da equipe de desenvolvimento. A compreensão das interações e dinâmicas entre os agentes, bem como a implementação eficaz das estratégias, demandou tempo e ajustes.

### Possíveis Melhorias

- **Ampliação da Variedade de Agentes:** Buscar adicionar novos tipos de agentes para enriquecer a simulação, considerando diferentes habilidades e comportamentos na batalha.
- **Inteligência Artificial Avançada:** Incorporar técnicas avançadas de inteligência artificial para melhorar a tomada de decisões dos agentes, tornando a simulação mais realista e desafiadora.
- **Interface Gráfica Aprimorada:** Investir em uma interface gráfica mais intuitiva e visualmente atrativa para proporcionar uma experiência de simulação mais envolvente.
- **Avaliações de Estratégias:** Realizar avaliações contínuas das estratégias dos agentes, ajustando parâmetros conforme necessário para garantir uma simulação equilibrada e desafiadora.
- **Documentação Detalhada:** Fornecer uma documentação abrangente sobre a configuração de agentes, estratégias disponíveis e parâmetros de simulação para facilitar a compreensão e personalização por parte dos usuários.
- **Exploração de Ambientes 3D:** Explorar a possibilidade de representar a simulação em ambientes 3D para uma experiência mais imersiva e visualmente rica.

## Fontes

> Inspirado em: https://github.com/UnBParadigmas2023-1/2023.1_G5_SMA_Campo_De_Batalha;

> Linguagem de programação: https://www.python.org/;

> Interface gráfica (Mesa): https://mesa.readthedocs.io/en/stable/;

> Sistemas Multiagentes (SMA): https://pt.wikipedia.org/wiki/Sistema_multiagente;
