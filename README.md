Este projeto em Python foi desenvolvido para automatizar o processo de extração, limpeza e organização de dados tabulares presentes em arquivos PDF, convertendo-os para um formato Excel (.xlsx) pronto para análise. Ele é ideal para cenários em que tabelas precisam ser extraídas de relatórios PDF de forma rápida e eficiente.

- Funcionamento detalhado
Leitura de tabelas no PDF

O código utiliza a biblioteca tabula, que permite a extração de tabelas de documentos PDF.
Todas as tabelas do arquivo PDF especificado são lidas em sequência (de todas as páginas do documento) e armazenadas como objetos DataFrame do Pandas.
Combinação de tabelas e limpeza dos dados

As tabelas extraídas são combinadas em um único DataFrame usando o método pd.concat().
Essa etapa organiza os dados em uma estrutura uniforme, ignorando índices anteriores e consolidando a informação.
Após a união dos dados, o código realiza a renomeação das colunas para descrever melhor o conteúdo das tabelas. Os nomes das colunas são ajustados manualmente para refletir os campos esperados, como "Número de Usuários", "Receita", "Despesa Total", etc.
Criação do diretório de saída

Antes de salvar os dados, o código garante que o diretório de saída (caminho onde o arquivo Excel será salvo) exista.
Caso o diretório especificado ainda não exista, ele é criado automaticamente utilizando a função os.makedirs().
Exportação dos dados para Excel

O DataFrame consolidado e processado é exportado para um arquivo Excel (.xlsx) usando a função to_excel() da biblioteca pandas.
A exportação mantém os dados organizados e prontos para análises posteriores no Excel ou em outras ferramentas.
Mensagens de status

O código exibe uma mensagem no console informando que o arquivo Excel foi criado com sucesso, além de mostrar o caminho onde ele foi salvo.
