import re


class ExtratorURL:
    def __init__(self, url:str):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url: str) -> str:
        if (type(url) == str):
            return url.strip()
        else:
            return ""

    def valida_url(self) -> bool:
        if (not self.url):
            raise ValueError('A URL está vazia.')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A url não é válida.')

    def get_url_base(self) -> str:
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self) -> str:
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[(indice_interrogacao + 1):]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(f"O tamanho da URL é {len(extrator_url)}")
# print(extrator_url)
# print(valor_quantidade)
print(extrator_url == extrator_url2)
print(id(extrator_url))
print(id(extrator_url2))