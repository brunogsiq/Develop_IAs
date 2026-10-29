"""Servidor MCP de laboratório: consulta a PTAX do dólar no Banco Central."""
import json
import urllib.request
from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("cambio-lab")

URL_PTAX = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarDia(dataCotacao=@dataCotacao)"
    "?@dataCotacao='{data}'&$format=json"
)


@mcp.tool()
def consultar_ptax_dolar(data: str) -> str:
    """Retorna a cotação PTAX (compra e venda) do dólar americano em reais
    para uma data específica, segundo o Banco Central do Brasil.
    Use quando o usuário perguntar o valor do dólar ou a PTAX.

    Args:
        data: data no formato DD/MM/AAAA. Para hoje, informe a data de hoje.
    """
    try:
        dia = datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return "Erro: data inválida. Use o formato DD/MM/AAAA."

    url = URL_PTAX.format(data=dia.strftime("%m-%d-%Y"))
    try:
        with urllib.request.urlopen(url, timeout=15) as resposta:
            corpo = json.load(resposta)
    except Exception as erro:
        return f"Erro ao consultar o Banco Central: {erro}"

    cotacoes = corpo.get("value", [])
    if not cotacoes:
        return (
            f"Não há cotação PTAX para {data}. "
            "Pode ser fim de semana, feriado ou a cotação do dia ainda não foi publicada."
        )

    c = cotacoes[-1]
    return (
        f"PTAX do dólar em {data}: compra R$ {c['cotacaoCompra']:.4f}, "
        f"venda R$ {c['cotacaoVenda']:.4f} (publicada em {c['dataHoraCotacao']})."
    )


if __name__ == "__main__":
    mcp.run()
