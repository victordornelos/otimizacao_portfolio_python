# Otimização de portfólio utilizando Python
![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Wall street](https://revistaazul.voeazul.com.br/wp-content/uploads/2023/03/os-centros-financeiros-mais-poderosos-de-todo-o-mundo-1536x1031.jpeg.webp)

 **Autor:** Victor Flávio P. Dornelos\
**E-mail:** victor.dornelos@hotmail.com\
**Linkedin**: [Victor Flávio Pereira Dornelos](https://www.linkedin.com/in/victor-flavio-pereira-dornelos/)

## Sumário
1. [Descrição](https://github.com/victordornelos/otimizacao_portfolio_python/tree/main?tab=readme-ov-file#1-descrição)
2. [Objetivo](https://github.com/victordornelos/otimizacao_portfolio_python/tree/main?tab=readme-ov-file#2-objetivo)
3. [Metodologia](https://github.com/victordornelos/otimizacao_portfolio_python/tree/main?tab=readme-ov-file#3-metodologia)
4. [Resultados](https://github.com/victordornelos/otimizacao_portfolio_python/tree/main?tab=readme-ov-file#4-resultados)
5. [Referências](https://github.com/victordornelos/otimizacao_portfolio_python/tree/main?tab=readme-ov-file#5-referências)

## 1. Descrição
O mercado financeiro é um ambiente dinâmico onde ocorrem negociações de diversos tipos de ativos, como câmbio, títulos, commodities e ações. Diariamente, as bolsas de valores ao redor do mundo movimentam volumes monetários gigantescos durante suas transações.

Um dos principais benefícios do mercado de capitais é conectar tomadores de recursos financeiros com poupadores, permitindo trocas em troca de remuneração e/ou participação. No caso das ações, isso possibilita que empresas, por meio de ofertas públicas iniciais (IPOs) no mercado primário, se financiem emitindo papéis que representam parte de sua posse para os investidores, que podem obter ganhos. Já no mercado secundário, é criada liquidez para os investidores que desejam desfazer suas posições, vendendo-as para outros que desejam comprá-las.

Todavia, é importante lembrar que ações são investimentos de risco, altamente voláteis e sujeitos a diversos fatores. Uma maneira eficiente de proteção contra esse risco é a criação de um portfólio, ou seja, uma carteira que contenha um conjunto de ativos (ou até mesmo um único ativo, dependendo do caso) que equilibre risco e retorno.

Com os avanços tecnológicos atuais, as linguagens de programação e algoritmos se tornaram ferramentas essenciais para auxiliar na tomada de decisões no mercado financeiro. Utilizando métodos como Markowitz, Hill Climb e Simulated Annealing, é possível otimizar portfólios de forma eficiente e eficaz.

## 2. Objetivo
O objetivo deste repositório é explorar o uso dos métodos de Markowitz, Hill Climb e Simulated Annealing por meio de uma carteira de ações fictícias. Assim, verificamos e comparamos os resultados obtidos por cada método, criando conclusões sobre sua eficiência e hipóteses sobre os fatores que podem ter influenciado seus resultados em cada caso.

## 3. Metodologia
Neste repositório, foram utilizados Python e Jupyter Notebook. Dois arquivos de código foram criados: um principal, contendo a exploração das ações e dos métodos, e um auxiliar, com algumas funções separadas por questões de organização.

Para a escolha das ações durante os testes, foram utilizados diversos portfólios visando explorar uma variedade de resultados possíveis. No projeto final, o portfólio selecionado inclui 7 ações (incluindo BDRs): Taesa, Banco do Brasil, Ambev, WEG, Irani, Google e Berkshire Hathaway, com o objetivo de obter diversificação de setores e países. Os dados foram obtidos utilizando a biblioteca Yahoo Finance, cobrindo o período de janeiro de 2021 a junho de 2024, e armazenados em um DataFrame do Pandas (disponível como carteira.csv).

Primeiramente, foi realizada uma análise exploratória inicial dos dados das cotações, verificando as volatilidades e os retornos de cada empresa. Posteriormente, foi criada uma função para montar uma carteira fictícia das ações escolhidas, com capital inicial de 1 milhão de reais distribuído com os pesos encontrados pelos métodos de otimização de Markowitz, Hill Climb e Simulated Annealing. Esses métodos foram avaliados usando o índice de Sharpe, que mensura a relação entre retorno e risco (utilizando a média do CDI nesse intervalo de tempo como ativo de menor risco). Quanto maior o índice de Sharpe, melhor o ativo.

Abaixo, segue uma descrição do funcionamento de cada um dos métodos:

•  **Otimização de Markowitz**: A ideia desse método é criar uma carteira de ativos que maximize a relação entre retorno e risco. Para isso, foram realizados diversos testes com diferentes pesos para os ativos de forma randômica, calculando o risco e retorno para cada caso com o objetivo de obter o melhor índice de Sharpe. Foram feitas 100 mil simulações para alcançar o melhor índice de Sharpe possível. Como se trata de um método randômico, apesar da grande quantidade de simulações proporcionar uma convergência dos valores pela lei dos grandes números, é difícil replicar exatamente os resultados, além de envolver um grande esforço computacional (no computador utilizado, o processo levou aproximadamente 3 horas). Os resultados obtidos foram disponibilizados nos arquivos df_M.csv e Pickle.

•  **Hill Climb**: O método Hill Climb, ou "subida da encosta", é um algoritmo de otimização que inicia de um ponto aleatório e busca melhores resultados ao se mover lentamente para soluções vizinhas. No entanto, este algoritmo não retorna para resultados piores, de modo que o melhor resultado é alcançado quando não há soluções vizinhas melhores, encontrando assim as melhores soluções locais, mas não necessariamente a global. Neste repositório, foi utilizada a biblioteca mlrose e realizados diversos testes para obter o melhor resultado possível com este algoritmo. Diversos pontos iniciais aleatórios foram escolhidos durante os testes para obter os pesos dos ativos que resultassem no maior índice de Sharpe possível. Assim como o método de Markowitz, este também possui um componente randômico e exige grande esforço computacional. Os resultados estão disponíveis nos formatos CSV e Pickle.

•  **Simulated Annealing**: O algoritmo Simulated Annealing (ou recozimento simulado) funciona de forma semelhante ao Hill Climb, partindo de um ponto inicial aleatório e buscando soluções vizinhas com melhores resultados. A diferença é que este modelo não descarta vizinhos com valores menores, considerando essa probabilidade, o que o torna mais eficiente em encontrar soluções globais do que o Hill Climb. Neste contexto, assim como no Hill Climb, foi utilizada a biblioteca mlrose e realizados diversos testes com diferentes pontos iniciais, visando obter a composição da carteira que proporcionasse o melhor índice de Sharpe. Os dados resultantes também estão disponíveis nos formatos CSV e Pickle.

## 4. Resultados
Após realizar diversos testes com os três métodos, foi possível chegar a algumas conclusões. A primeira é que tanto o Hill Climb quanto o Simulated Annealing, apesar das mudanças nas ações do portfólio, dos pontos iniciais e da adição de loops para gerar vários pontos de partida aleatórios (o que não foi muito eficaz), ainda concentravam a maior parte do capital em uma única ação com o melhor Sharpe Ratio ou, em alguns casos, em apenas duas ações. Ou seja, os algoritmos tiveram grande dificuldade em escapar das soluções locais para encontrar a solução global.

Outro desafio foi o esforço computacional. Devido à natureza randômica desses métodos, foi necessário realizar diversos testes, resultando em um longo tempo de execução do código. Isso foi particularmente evidente ao tentar inserir loops no Hill Climb e no Simulated Annealing.

Enfim, os resultados obtidos demonstraram que a melhor relação entre risco e retorno foi alcançada pelo método de Markowitz. Outro ponto positivo é que todos os três métodos apresentaram um Sharpe Ratio melhor do que o Ibovespa e o S&P 500. No entanto, o Hill Climb e o Simulated Annealing tiveram os mesmos resultados, concentrando todo o capital na Irani. Apesar dos métodos terem superado os índices das bolsas, ainda assim, apresentaram um Sharpe Ratio relativamente baixo, sendo o maior de 0,58 obtido pelo método de Markowitz.

## 5. Referências

Udemy. Python para Finanças: Análise de Dados e Machine Learning. Udemy, 2024. Disponível em: https://www.udemy.com/course/python-para-financas-analise-de-dados-e-machine-learning/?couponCode=LETSLEARNNOWPP. Acesso em: 9 jun. 2024.

Carneiro, A. L. C. Algoritmos de Otimização: Hill Climbing e Simulated Annealing. Medium, 2024. Disponível em: https://medium.com/data-hackers/algoritmos-de-otimização-hill-climbing-e-simulated-annealing-3803061f66f0. Acesso em: 9 jun. 2024.