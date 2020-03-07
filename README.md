# Teia

Descubra conexões entre diferentes entidades.

## Como executar

```
python teia.py sample.csv
```

Ao executar esse comando, esse simples script criará um arquivo `.gml`,
com um grafo contendo as informações preenchidas no `.csv` informado.
O arquivo `.gml` pode ser importado em programas como Gephi e Cytoscape.

## Fonte de dados

As duas primeiras colunas serão os nós que formarão uma aresta.
As demais colunas serão adicionadas como atributos das arestas.

O arquivo deve ser um `.csv` com o seguinte formato:

```
entidadeA,entidadeB,tipo,inicio,fim,fonte
```

Os nomes das colunas devem ser formatos por letras e números, sem símbolos ou espaços.
