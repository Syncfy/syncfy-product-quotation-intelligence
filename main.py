from matching.coletores.produtos.gerador import gerarProdutos
from matching.normalizacao.limpeza import limparEPadronizarDados
from matching.normalizacao.desduplicacao import removerDuplicatas
from matching.enriquecimento.extracao import extrair_atributos

def main():
    dados = gerarProdutos(100)
    try:
        dadosLimpos = limparEPadronizarDados(dados)
        print("Dados após limpeza:")
        print(dadosLimpos)
        
        print("---------------------------------")
        
        dadosDesduplicados = removerDuplicatas(dadosLimpos)
        print("Dados finais após normalização:")
        print(dadosDesduplicados)
        
        print("---------------------------------")

        # # Extração de atributos
        # extrair_atributos(df)
    except Exception as e:
        print(f"Erro durante a execução do processo de normalização: {e}")

if __name__ == "__main__":
    main()
