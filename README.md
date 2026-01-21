
## Análise da evasão feminina em cursos STEM no IFSC (2019–2023)

### Descrição do projeto
Este repositório contém os scripts e procedimentos utilizados na análise da evasão escolar de estudantes do sexo feminino em cursos tecnológicos do Ensino Médio Técnico do Instituto Federal de Santa Catarina (IFSC), no período de 2019 a 2023, com base nos microdados de eficiência acadêmica disponibilizados pela Plataforma Nilo Peçanha (PNP).
O estudo está fundamentado no paradoxo da igualdade de gênero em STEM, conforme discutido por Stoet e Geary (2018), e adota a renda familiar como variável socioeconômica central para a análise das escolhas educacionais e da permanência escolar.
O código disponibilizado neste repositório visa garantir a transparência, reprodutibilidade e validação dos resultados apresentados no Trabalho de Conclusão de Curso (TCC).

### Objetivo
Analisar a evasão de mulheres e meninas em cursos tecnológicos do Ensino Médio Técnico do IFSC, considerando a renda familiar como variável explicativa, no período de 2019 a 2023, à luz do paradoxo da igualdade de gênero em STEM.

### Fonte dos dados
Plataforma Nilo Peçanha (PNP)
Microdados de Eficiência Acadêmica
Anos analisados: 2019, 2020, 2021, 2022 e 2023
Os dados são públicos e podem ser obtidos em:
https://www.gov.br/mec/pt-br/acesso-a-informacao/dados-abertos/plataforma-nilo-pecanha

### Metodologia (resumo)
Importação individual dos microdados anuais da PNP;
Construção de uma série histórica unificada (2019–2023);
Filtragem dos dados para:
Instituição: IFSC
Modalidade: Ensino Médio Técnico (Integrado, Concomitante e Subsequente)
Eixo tecnológico: Informação e Comunicação (STEM);
Separação dos dados por sexo;
Definição de evasão com base nas categorias:
Abandono e Desligada

Cálculo das taxas de evasão:
por ano,
por renda familiar,
por sexo;
Geração de gráficos para análise comparativa.

### Resultados esperados
Maior concentração de matrículas femininas em cursos STEM entre faixas de menor renda familiar;
Taxas de evasão feminina relativamente estáveis entre as diferentes faixas de renda;
Evidência empírica que complementa o paradoxo da igualdade de gênero em STEM, demonstrando que contextos socioeconômicos influenciam a escolha educacional sem necessariamente ampliar a evasão.

## Tecnologias utilizadas

**Linguagem:** Python 3.13

**Bibliotecas:** pandas 2.2.0, matplotlib

## Como reproduzir a análise

#### Clonar repositório:

``` bash
git clone https://github.com/festrati/tcc.git
```

#### Instalar dependências:

``` bash
pip install pandas matplotlib
```

#### Inserir os arquivos de microdados da PNP na pasta dados/

 ``` bash
https://www.gov.br/mec/pt-br/acesso-a-informacao/dados-abertos/plataforma-nilo-pecanha
 ```

#### Execute o script main.py

``` bash
   python src/main.py
```
    
## Referência

STOET, Gijsbert; GEARY, David C. The gender-equality paradox in science, technology, engineering, and mathematics education. Psychological Science, v. 29, n. 4, p. 581–593, 2018.

VOYER, Daniel; VOYER, Susan D.; SAINT-AUBIN, Jean. Sex differences in visual-spatial working memory: A meta-analysis. Psychonomic bulletin & review, v. 24, n. 2, p. 307-334, 2017. 

UNESCO. Decifrar o código: educação de meninas e mulheres em ciências, tecnologia, engenharia e matemática (STEM). 1. ed. Brasilia: UNESCO, 2018. ISBN 978-85-7652-231-7. 
BRASIL. Constituição Federal. Constituição da República Federativa do Brasil de 1988. Brasília: Presidência da República, 2019. Disponível em: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm Acesso em: 22 de dez. de 2025.

TEAM PYTHON DEVELOPMENT. Python: linguagem de programação. Versão 3.12. 2024. Programa de computador. Disponível em: www.python.org. Acesso em: 12 jan. 2026.

PANDAS DEVELOPMENT TEAM. pandas documentation (versão 2.2.0). Disponível em: https://pandas.pydata.org/docs/. Acesso em: 05 jan. 2026.

DA SILVA MONTEIRO, Daniela de Cássia; PITON SERRA SANCHES, Jane. EVASÃO NOS CURSOS TÉCNICOS DA REDE FEDERAL DE EDUCAÇÃO PROFISSIONAL E TECNOLÓGICA: UMA ANÁLISE À LUZ DOS DADOS DA PLATAFORMA NILO PEÇANHA. Educação Profissional e Tecnológica em Revista, [S. l.], v. 8, n. 2, p. 31–44, 2025. DOI: 10.36524/profept.v8i2.1523. Disponível em: https://ojs.ifes.edu.br/index.php/ept/article/view/1523.  Acesso em: 21 jan. 2026.

## Autor

- [@Festrati](https://www.github.com/festrati)

