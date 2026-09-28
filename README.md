# Safedrive---Simulador-ADAS-Advanced-Driver-Assistance-Systems-
Simulador de assistente de direção em Python

Projeto acadêmico desenvolvido na disciplina de Algoritmos e Programação I, da Faculdade de Computação e Informática da Universidade Presbiteriana Mackenzie.

Sobre o projeto

O SafeDrive é um simulador simplificado de um sistema ADAS (Advanced Driver Assistance Systems).

O programa recebe dados de telemetria e sensores do veículo e utiliza regras matemáticas e condicionais para avaliar possíveis situações de risco, como aproximação de um veículo à frente e invasão das faixas laterais.

O projeto foi desenvolvido com foco na aplicação prática de conceitos fundamentais de programação, como funções, operadores relacionais, operadores lógicos, condicionais e modularização.

Funcionalidades

O sistema realiza cinco etapas principais:

Fusão de sensores: recebe três leituras de distância e determina a mediana como distância validada.
Cálculo da distância segura: considera a velocidade do veículo, o tempo de reação definido pelo modo de condução e o atrito da pista.
Análise de colisão frontal: calcula a velocidade relativa e classifica a situação como SEGURO, ATENÇÃO ou RISCO DE COLISÃO.
Assistente de faixa: calcula uma margem lateral de segurança que aumenta conforme a velocidade do veículo.
Decisão geral: combina as avaliações frontal e lateral e determina o status geral do sistema.
Modos de condução

O tempo de reação utilizado no cálculo depende do modo selecionado:

Modo	Tempo de reação
Esportivo	1.0 s
Normal	1.5 s
Seguro	2.0 s
Tecnologias
Python
Operadores matemáticos, relacionais e lógicos
Estruturas condicionais
Funções
Modularização
Restrições do projeto

Como parte dos requisitos da disciplina, a implementação foi realizada sem:

listas, tuplas, dicionários ou outras estruturas de dados;
for ou while;
sort(), min(), max() ou bibliotecas de estatística;
classes.

Essas restrições tiveram como objetivo praticar a construção da lógica utilizando principalmente funções e estruturas condicionais.

Estrutura da solução

O programa foi dividido em funções responsáveis por diferentes partes do sistema:

mediana() — determina a distância validada a partir dos três sensores;
modofun() — define o tempo de reação de acordo com o modo de condução;
distancia() — calcula a distância segura;
colisaofun() — analisa o risco de colisão frontal e o acionamento do AEB;
faixas() — avalia a distância das faixas laterais;
geralfun() — determina o status geral do sistema;
chama() — recebe as entradas, executa as funções e apresenta os resultados.
Objetivo acadêmico

O objetivo principal deste projeto foi transformar um conjunto de regras e fórmulas em uma solução funcional utilizando os conceitos fundamentais estudados em Algoritmos e Programação I.

Projeto acadêmico — 1º semestre de Computação.
