from matching.coletores.produtos.gerador import gerarProdutos
from matching.normalizacao.limpeza import limpar_dados
from matching.normalizacao.padronizacao import padronizar_categorias
from matching.normalizacao.desduplicacao import remover_duplicatas
from matching.enriquecimento.categorizacao import categorizador
from matching.enriquecimento.extracao import extrair_atributos

def main():
    dados = gerarProdutos(100)
    try:
        dadosLimpos = limpar_dados(dados)
        print("Dados após limpeza:")
        print(dadosLimpos)
        
        print("---------------------------------")

        dadosPadronizados = padronizar_categorias(dadosLimpos)
        print("Dados após padronização:")
        print(dadosPadronizados)
        
        # df = remover_duplicatas(df)
        # print("Dados finais após normalização:")
        # print(df)
        # # Treinamento e avaliação do modelo de categorização
        # categorizador(df)
        # # Extração de atributos
        # extrair_atributos(df)
    except Exception as e:
        print(f"Erro durante a execução do processo de normalização: {e}")

if __name__ == "__main__":
    main()
