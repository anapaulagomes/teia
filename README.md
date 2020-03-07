# Teia

Descubra conexões entre diferentes entidades.

## Como executar

```
python teia.py sample.csv
```

## Fonte de dados

As duas primeiras colunas serão os nós que formarão uma aresta.
As demais colunas serão adicionadas como atributos das arestas.

O arquivo deve ser um `.csv` com o seguinte formato:

```
entidadeA,entidadeB,tipo,inicio,fim,fonte
```

Os nomes das colunas devem ser formatos por letras e números, sem símbolos ou espaços.
