def removerDuplicatas(df):
    linhas_antes = len(df)
    print(f"Total de linhas antes da remoção de duplicatas: {linhas_antes}")

    df_deduplicado = df.drop_duplicates(subset=['nome', 'categoria'])

    linhas_depois = len(df_deduplicado)
    print(f"Total de linhas após a remoção de duplicatas: {linhas_depois}")

    duplicatas_removidas = linhas_antes - linhas_depois
    print(f"Duplicatas removidas: {duplicatas_removidas}")

    return df_deduplicado
