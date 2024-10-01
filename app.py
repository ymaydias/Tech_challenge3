import streamlit as st
import pandas as pd  # Importação do pandas para evitar NameError
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
import base64
import os

# Função para carregar e codificar a imagem em base64
def get_image_as_base64(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return encoded

# Configuração da página
st.set_page_config(
    page_title="Análise de Dados COVID-19 - PNAD IBGE",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS personalizado para Dark Mode com a paleta Dracula e Sidebar estilizado como balão
dracula_css = """
<style>
/* Backgrounds */
body {
    background-color: #282a36;
    color: #f8f8f2;
}

/* Sidebar */
.sidebar .sidebar-content {
    background-color: #21222c !important;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    padding: 20px;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #ff79c6;
}

/* Links */
a {
    color: #8be9fd;
    text-decoration: none;
    font-weight: bold;
}
a:hover {
    color: #ff79c6;
    text-decoration: underline;
}

/* Containers */
.main-content {
    max-width: 800px;
    margin: auto;
    padding: 20px;
}

/* Buttons */
.css-1emrehy.edgvbvh3 {
    background-color: #6272a4;
    color: #f8f8f2;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #21222c;
}

::-webkit-scrollbar-thumb {
    background: #6272a4;
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: #ff79c6;
}

/* Suavizar a rolagem */
html {
    scroll-behavior: smooth;
}

/* Estilização da imagem de capa */
.cover-image {
    position: relative;
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

img {
    max-width: 100%;
}
</style>
"""

st.markdown(dracula_css, unsafe_allow_html=True)

# Menu Lateral de Navegação com Links de Âncoras
st.sidebar.title("Navegação")
st.sidebar.markdown("""
<ul style="list-style-type: none; padding: 0;">
    <li><a href="#introducao">Introdução</a></li>
    <li><a href="#sintomas-clinicos">Sintomas Clínicos</a></li>
    <li style="margin-left: 10px;"><a href="#sintomas-faixa-etaria">Por Faixa Etária</a></li>
    <li style="margin-left: 10px;"><a href="#Distribuição Percentual de Pessoas que Buscaram Ajuda Médica por Sexo">Por Sexo</a></li>
    <li style="margin-left: 10px;"><a href="#Caracterização dos sintomas clínicos da população">Caracterização</a></li>
    <li style="margin-left: 10px;"><a href="#Distribuição de Sintomas por Gênero">Por Gênero</a></li>
    <li><a href="#Nível de Restrição de Contato Social Durante a Pandemia">Restrição de Contato Social</a></li>
    <li><a href="#Adoção de Home Office Durante a Pandemia">Home Office</a></li>
    <li><a href="#Distribuição de Renda por Nível de Escolaridade">Renda por Escolaridade</a></li>
    <li><a href="#Média de Renda por Estado">Renda por Estado</a></li>
    <li><a href="#Conclusao">Conclusão</a></li>
</ul>
""", unsafe_allow_html=True)

# Inserir a imagem de capa
image_path = "images/unsplash.jpg"  # Caminho relativo para a imagem
encoded_image = get_image_as_base64(image_path)

if encoded_image:
    cover_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image}" alt="Cover Image" class="cover-image">
    </div>
    """
    st.markdown(cover_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path}")

# Espaço para centralizar o conteúdo
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

# Introdução
st.markdown("<a id='introducao'></a>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Análise de Dados COVID-19 - PNAD IBGE</h1>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: justify;">
A pandemia de COVID-19, iniciada em 2019, representou um dos maiores desafios de saúde pública da era moderna. Desde os primeiros meses, governos e instituições ao redor do mundo se mobilizaram para monitorar o impacto da doença, tanto em termos clínicos quanto em relação ao comportamento social e econômico da população. No Brasil, o Instituto Brasileiro de Geografia e Estatística (IBGE) desempenhou um papel fundamental ao coletar dados por meio da Pesquisa Nacional por Amostra de Domicílios (PNAD) COVID-19, um levantamento minucioso realizado por telefone. Essa pesquisa visou traçar um panorama abrangente das características de saúde, sociais e econômicas da população brasileira ao longo da pandemia.</div>
""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""
<div style="text-align: justify;">
Os dados coletados fornecem um vasto acervo para análise, especialmente no que tange à identificação de sintomas clínicos prevalentes, às atitudes adotadas pela população para lidar com a crise, e às repercussões econômicas decorrentes das medidas de isolamento social e distanciamento físico. Esse material é essencial para entender os efeitos multidimensionais da pandemia e, mais importante, para guiar a formulação de estratégias eficazes em caso de futuros surtos de doenças infecciosas.</div>
""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""
<div style="text-align: justify;">
Esta análise exploratória, foca em três aspectos principais: a caracterização dos sintomas clínicos reportados pela população, o comportamento adotado frente à pandemia, e as características econômicas resultantes do período de crise. A partir dessa análise, serão sugeridas medidas e recomendações que instituições de saúde, como hospitais, podem implementar para otimizar suas respostas a potenciais novas ondas da COVID-19 ou futuras pandemias. A correta compreensão desses fatores permitirá que o sistema de saúde e governo se prepare de forma mais eficiente, adotando ações preventivas e corretivas com base em evidências.
</div>
""", unsafe_allow_html=True)

# Separador
st.markdown("---")

# Análise dos Sintomas Clínicos Relacionados à COVID-19
st.markdown("<a id='sintomas-clinicos'></a>", unsafe_allow_html=True)
st.markdown("<h2>Análise dos Sintomas Clínicos Relacionados à COVID-19</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: justify;">
De acordo com a análise exploratória dos dados clínicos selecionados, foram registrados 66.564 casos clínicos relacionados à COVID-19 com respostas afirmativas “SIM” na pesquisa da PNAD COVID-19. Esses números nos permitem entender como os sintomas se distribuíram entre a população durante o período estudado.</div>
""", unsafe_allow_html=True)

st.markdown("<h3>Distribuição dos Sintomas Clínicos</h3>", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf1.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Sintomas Clínicos" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("""
<div style="text-align: justify;">
O sintoma mais frequente foi a <strong>tosse</strong>, presente em 29.554 casos, o que corresponde a <strong>44,4%</strong> de todos os quadros clínicos analisados. Este resultado está alinhado com a característica de infecções respiratórias, nas quais a tosse é um dos sinais mais comuns e facilmente perceptíveis, o que a torna um dos primeiros sintomas a ser monitorado em futuras triagens.

Outro sintoma amplamente relatado foi a <strong>perda de olfato ou paladar</strong>, com 13.946 casos, representando <strong>20,9%</strong> do total. Este sintoma se consolidou como um dos marcadores mais distintivos da COVID-19, especialmente nos primeiros estágios da doença, sendo frequentemente usado para identificar possíveis infectados.

A <strong>dificuldade respiratória</strong>, por sua vez, foi observada em 11.858 casos, correspondendo a <strong>17,8%</strong> dos quadros clínicos. Embora esteja diretamente associada a quadros mais graves da doença, sua incidência foi inferior à de sintomas mais leves como tosse ou perda de olfato. Mesmo assim, este sintoma merece atenção especial devido à sua gravidade e à possível necessidade de cuidados intensivos.

Por fim, a <strong>dor nos olhos</strong>, um sintoma menos discutido, foi relatada em 11.206 casos, ou <strong>16,8%</strong> do total. Apesar de não ser um dos sintomas mais amplamente associados à COVID-19, sua presença significativa nos dados sugere que ele não deve ser descartado como um possível indicador de infecção.
</div>
""", unsafe_allow_html=True)

# Sintomas Clínicos por Faixa Etária
st.markdown("<a id='sintomas-faixa-etaria'></a>", unsafe_allow_html=True)
st.markdown("<h2>Sintomas Clínicos por Faixa Etária</h2>", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf2.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Sintomas Clínicos" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("""
<div style="text-align: justify;">
O gráfico apresenta a prevalência de sintomas clínicos relacionados à COVID-19, distribuídos em quatro faixas etárias: crianças, adolescentes, adultos e idosos. A tosse é o sintoma mais reportado em todas as faixas etárias, com maior incidência entre os adultos, onde representa aproximadamente 60% dos casos totais observados. Em relação à perda de olfato/paladar, esse sintoma também aparece com destaque entre os adultos, correspondendo a cerca de 20% dos casos registrados nesta faixa etária. Nos idosos, tanto a tosse quanto a perda de olfato/paladar também são significativos, representando juntos cerca de 20% dos casos totais exibidos no gráfico.

Já entre crianças e adolescentes, os números são consideravelmente menores. Nas crianças, a tosse corresponde a menos de 2% dos casos no gráfico, enquanto outros sintomas, como perda de olfato/paladar e dificuldade respiratória, são quase insignificantes, ficando abaixo de 1%. Entre os adolescentes, a tosse tem uma leve maior incidência, representando aproximadamente 5% dos casos totais, mas outros sintomas como dificuldade respiratória e dor nos olhos continuam com baixa prevalência, somando menos de 2% cada.

No geral, mais de 70% dos casos no gráfico estão associados à tosse, tornando-a o sintoma mais prevalente em todas as faixas etárias. A perda de olfato/paladar aparece em segundo lugar, com cerca de 20% de prevalência, especialmente entre adultos e idosos. Já os sintomas de dificuldade respiratória e dor nos olhos são os menos frequentes, somando menos de 10% do total de casos observados. Esses dados indicam que a maioria dos quadros clínicos reportados com resposta "Sim" estão concentrados na faixa etária dos adultos, enquanto crianças e adolescentes reportam muito menos sintomas relacionados à COVID-19.
</div>
""", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf3.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

st.markdown("<a id='Distribuição Percentual de Pessoas que Buscaram Ajuda Médica por Sexo'></a>", unsafe_allow_html=True)
st.markdown("<h2>Distribuição Percentual de Pessoas que Buscaram Ajuda Médica por Sexo</h2>", unsafe_allow_html=True)

st.markdown("""
<p>O gráfico horizontal de barras ilustra a <b>distribuição percentual</b> de pessoas que buscaram ajuda médica, diferenciando entre <b>homens</b> e <b>mulheres</b> durante a pandemia da COVID-19. Ele exibe três categorias principais:</p>
<ul>
    <li><b>Sim</b> (indivíduos que buscaram ajuda médica),</li>
    <li><b>Não</b> (indivíduos que não buscaram ajuda médica),</li>
    <li><b>Ignorado</b> (respostas não informadas).</li>
</ul>

<h3>Principais Observações:</h3>

<p><b>1. Alta Proporção de Pessoas que Não Buscaram Ajuda Médica:</b><br>
A maioria significativa tanto de homens quanto de mulheres não buscou ajuda médica durante o período analisado. <b>90,8% das mulheres</b> e <b>92,8% dos homens</b> indicaram que não buscaram assistência médica. Isso pode refletir a gravidade dos sintomas ou a percepção da necessidade de buscar tratamento, onde apenas casos mais graves levariam a essa procura.
</p>

<p><b>2. Diferença Leve entre Homens e Mulheres:</b><br>
A diferença entre os sexos em termos de busca por ajuda médica é pequena, mas notável. <b>7,5% das mulheres</b> buscaram assistência, em comparação com <b>5,8% dos homens</b>. Essa diferença, embora sutil, pode indicar uma maior tendência entre as mulheres de procurar cuidados médicos, o que pode ser relacionado à conscientização sobre saúde ou à gravidade percebida dos sintomas.
</p>

<p><b>3. Respostas Ignoradas:</b><br>
Uma pequena porcentagem de respostas foi ignorada para ambos os sexos: <b>1,8% para mulheres</b> e <b>1,4% para homens</b>. Isso pode indicar uma possível falta de clareza nas respostas ou um desinteresse em informar sobre essa questão.
</p>

<p>Este gráfico destaca um ponto importante: <b>a maioria da população não buscou ajuda médica</b> durante a pandemia, o que pode levantar questões sobre o acesso ao sistema de saúde, a gravidade dos sintomas ou a percepção da necessidade de tratamento. A diferença de comportamento entre homens e mulheres é pequena, mas pode refletir diferenças de percepção ou comportamento em relação à saúde.</p>

<p>Essa informação pode ser relevante para estratégias futuras de saúde pública, incentivando campanhas de conscientização para que mais pessoas busquem atendimento médico antes que os sintomas se agravem, especialmente em situações de crise sanitária como a pandemia da COVID-19.</p>
""", unsafe_allow_html=True)


if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Sintomas Clínicos" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("<a id='Caracterização dos sintomas clínicos da população'></a>", unsafe_allow_html=True)
st.markdown("<h2>Caracterização dos sintomas clínicos da população</h2>", unsafe_allow_html=True)

st.markdown("""
O trecho apresenta uma análise sobre a caracterização dos sintomas clínicos mais comuns reportados pela população durante a pandemia da COVID-19. O gráfico destaca quatro sintomas principais: tosse, perda de olfato/paladar, dor nos olhos e dificuldade respiratória.

Entre os sintomas, a tosse é o mais prevalente, com mais de 30.000 casos relatados, sendo significativamente mais comum do que os outros sintomas. Esse dado é importante, pois a tosse foi um dos primeiros e mais amplamente associados à COVID-19, especialmente em casos moderados a graves.

A perda de olfato e paladar também se destacou durante a pandemia, com mais de 15.000 casos relatados. Embora menos prevalente do que a tosse, esse sintoma tornou-se uma característica marcante da infecção pelo vírus.

Além disso, a dificuldade respiratória e a dor nos olhos foram relatadas com frequência semelhante, ambas em mais de 10.000 casos. A dificuldade respiratória, em particular, é um sinal crítico que pode indicar a necessidade de cuidados médicos urgentes, especialmente em casos mais graves da doença.

Em termos de interpretação, a tosse e a perda de olfato/paladar aparecem como os principais sintomas relacionados à COVID-19. A dificuldade respiratória e a dor nos olhos ocorrem com menos frequência, mas ainda em números consideráveis, ressaltando a importância de se considerar esses sintomas na triagem e no tratamento dos pacientes.
""", unsafe_allow_html=True)


image_path_sintomas = "graficos/graf4.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Sintomas Clínicos" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("<a id='Distribuição de Sintomas por Gênero'></a>", unsafe_allow_html=True)
st.markdown("<h2>Distribuição de Sintomas por Gênero</h2>", unsafe_allow_html=True)

st.markdown("""
<p>O gráfico exibe a <b>frequência de sintomas</b> relatados por homens e mulheres durante a pandemia. A <b>tosse</b> é o sintoma mais frequente entre ambos os gêneros, com uma prevalência maior entre as mulheres. Outros sintomas, como <b>perda de olfato/paladar</b> e <b>dor nos olhos</b>, também aparecem mais frequentemente nas mulheres, enquanto a <b>dificuldade respiratória</b> foi reportada com menor frequência em ambos os grupos, embora mais comum entre as mulheres.</p>

<p>Esses dados sugerem uma maior prevalência de sintomas entre as mulheres, indicando que elas podem ter sido mais afetadas ou estavam mais propensas a relatar esses sintomas em comparação aos homens.</p>
""", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf5.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Distribuição de Sintomas por Gênero" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")


st.markdown("<a id='Nível de Restrição de Contato Social Durante a Pandemia'></a>", unsafe_allow_html=True)
st.markdown("<h2>Nível de Restrição de Contato Social Durante a Pandemia</h2>", unsafe_allow_html=True)

st.markdown("""
<p>Este gráfico apresenta os diferentes níveis de <b>restrição de contato social</b> adotados pela população durante a pandemia. Uma grande parte dos respondentes (<b>mais de 700.000</b>) não especificou seu nível de restrição. Entre os que responderam, a maioria afirmou que <b>ficou em casa e só saiu em casos de necessidade</b>, seguida por aqueles que <b>reduziram o contato social</b>, mas continuaram saindo para atividades essenciais.</p>

<p>Apenas uma pequena parte da população <b>não fez restrição</b> e levou uma vida normal, enquanto um número ainda menor ficou <b>rigorosamente em casa</b> sem sair.</p>
""", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf6.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Nível de Restrição de Contato Social" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("<a id='Adoção de Home Office Durante a Pandemia'></a>", unsafe_allow_html=True)
st.markdown("<h2>Adoção de Home Office Durante a Pandemia</h2>", unsafe_allow_html=True)

st.markdown("""
<p>O gráfico a seguir mostra a <b>adoção do home office</b> durante a pandemia. A maioria das pessoas classificadas como "Não aplicável" sugere que suas ocupações não permitiam a modalidade de trabalho remoto. Apenas uma pequena parcela da população conseguiu adotar o home office, com um número ligeiramente maior indicando que o trabalho remoto não foi uma opção viável para elas.</p>

<p>Esses dados refletem a limitação do home office a setores específicos, enquanto grande parte da população, que atua em setores onde o trabalho remoto não era aplicável, continuou operando de forma presencial ou em atividades que não permitiam essa flexibilidade.</p>
""", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf7.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Adoção de Home Office" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("<a id='Média de Renda por Estado'></a>", unsafe_allow_html=True)
st.markdown("<h2>Média de Renda por Estado</h2>", unsafe_allow_html=True)

st.markdown("""
<p>O gráfico a seguir apresenta a <b>média de renda</b> por estado no Brasil, destacando as diferenças econômicas entre as diversas regiões do país. Essa análise fornece uma visão clara das disparidades de renda entre os estados, com alguns estados tendo uma média significativamente maior que outros.</p>

<h3>Principais Observações:</h3>

<p><b>1. Distrito Federal com a Maior Média de Renda:</b><br>
O <b>Distrito Federal (DF)</b> se destaca com a maior média de renda do país, ultrapassando os R$ 4.000. Isso pode ser explicado pela alta concentração de funcionários públicos, especialmente de cargos de alto escalão, e de empregos no setor de serviços altamente qualificados, que tendem a ter salários mais elevados.</p>

<p><b>2. Estados do Sudeste e Sul:</b><br>
Os estados das regiões <b>Sudeste</b> e <b>Sul</b>, como <b>São Paulo (SP)</b>, <b>Rio de Janeiro (RJ)</b>, <b>Santa Catarina (SC)</b> e <b>Rio Grande do Sul (RS)</b>, também apresentam médias de renda relativamente altas, acima de R$ 2.000. Essas regiões concentram a maior parte da indústria, do comércio e dos serviços do país, o que justifica a média salarial mais elevada.</p>

<p><b>3. Disparidades Regionais:</b><br>
Os estados do <b>Norte</b> e <b>Nordeste</b>, como <b>Alagoas (AL)</b>, <b>Maranhão (MA)</b>, <b>Piauí (PI)</b> e <b>Ceará (CE)</b>, possuem as menores médias de renda, geralmente abaixo de R$ 1.500. Essa disparidade reflete os desafios econômicos e a menor industrialização nessas regiões, que são historicamente mais dependentes do setor primário, como a agricultura, pesca e extrativismo.</p>

<p><b>4. Centro-Oeste e Norte:</b><br>
Os estados do <b>Centro-Oeste</b>, como <b>Mato Grosso (MT)</b> e <b>Goiás (GO)</b>, além de alguns estados do <b>Norte</b>, como <b>Rondônia (RO)</b> e <b>Roraima (RR)</b>, têm médias de renda um pouco mais elevadas que os estados do Nordeste. Essas regiões, em especial o Centro-Oeste, têm um forte setor agropecuário, o que contribui para a economia e eleva a média de renda em comparação com outras regiões.</p>

<h3>Interpretação:</h3>

<p>O gráfico destaca as <b>disparidades econômicas regionais</b> no Brasil, com o <b>Distrito Federal</b> e os estados do <b>Sudeste</b> e <b>Sul</b> liderando com as maiores médias de renda. Essas regiões concentram a maior parte das oportunidades de emprego em setores que pagam melhor, como o setor público, tecnologia, serviços e indústrias. Por outro lado, os estados do <b>Norte</b> e <b>Nordeste</b> continuam apresentando médias de renda mais baixas, reflexo de uma economia baseada em setores menos valorizados no mercado de trabalho.</p>
""", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf9.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Média de Renda por Estado" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("<a id='Distribuição de Renda por Nível de Escolaridade'></a>", unsafe_allow_html=True)
st.markdown("<h2>Distribuição de Renda por Nível de Escolaridade</h2>", unsafe_allow_html=True)

st.markdown("""O trecho de código apresenta a seguinte análise sobre a distribuição de renda por nível de escolaridade no Brasil. Ele evidencia como a renda é predominantemente concentrada em valores mais baixos, especialmente entre aqueles com menor escolaridade, enquanto há uma variação significativa entre os indivíduos com educação superior.

No gráfico, observamos que a maior parte da população, independentemente do nível de escolaridade, possui renda abaixo de Reais 5.000. Esse fenômeno é mais evidente nos grupos com Sem Instrução e Fundamental Incompleto, onde praticamente não há dispersão para faixas de renda mais altas. Já os grupos com Pós-graduação e Superior Completo apresentam uma maior dispersão de renda, com uma parte significativa atingindo valores superiores a R$ 10.000, refletindo melhores oportunidades de trabalho e remunerações para indivíduos com maior qualificação.

Além disso, é interessante notar que as distribuições de renda entre os grupos de Médio Completo e Médio Incompleto são bastante próximas, o que sugere que a conclusão do ensino médio, por si só, não leva a diferenças significativas nos ganhos.

Em conclusão, a distribuição da renda no Brasil está fortemente ligada ao nível de escolaridade, e indivíduos com mais educação têm maior probabilidade de alcançar faixas de renda mais altas. No entanto, mesmo entre os mais escolarizados, a maioria da população ainda tem renda concentrada nas faixas mais baixas, o que evidencia a desigualdade de oportunidades econômicas no país.

O gráfico ilustrativo da distribuição de renda acompanha essa análise, mas, caso o arquivo da imagem não seja encontrado, será exibida uma mensagem de erro.""", unsafe_allow_html=True)

image_path_sintomas = "graficos/graf10.png"
encoded_image_sintomas = get_image_as_base64(image_path_sintomas)

if encoded_image_sintomas:
    sintomas_image_html = f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{encoded_image_sintomas}" alt="Distribuição de Renda por Nível de Escolaridade" class="graf">
    </div>
    """
    st.markdown(sintomas_image_html, unsafe_allow_html=True)
else:
    st.error(f"Imagem não encontrada no caminho: {image_path_sintomas}")

st.markdown("<a id='Conclusao Geral'></a>", unsafe_allow_html=True)
st.markdown("<h2>Conclusão Geral</h2>", unsafe_allow_html=True)

st.markdown("""
Com base na análise dos dados da PNAD COVID-19, é evidente que a prevalência de sintomas como tosse, dificuldade respiratória, dor nos olhos e perda de olfato/paladar variou significativamente entre as diferentes faixas etárias e regiões do Brasil. Essa variação demonstra a importância de uma preparação diferenciada e direcionada por parte do governo e dos hospitais para lidar com futuras crises de saúde pública.

Uma das principais lições aprendidas é que a resposta a uma pandemia não pode ser padronizada para todo o país, uma vez que algumas regiões foram significativamente mais afetadas por sintomas graves, como dificuldade respiratória, enquanto outras apresentaram sintomas mais leves. No futuro, o governo deve priorizar o desenvolvimento de planos de contingência regionais, levando em consideração as diferenças demográficas e de infraestrutura entre os estados. Um sistema de vigilância epidemiológica mais robusto, com monitoramento contínuo dos dados regionais em tempo real, permitirá respostas mais rápidas e adequadas.

Os hospitais também devem investir em infraestrutura e treinamento contínuo das equipes, para que possam lidar com surtos de doenças infecciosas com maior eficácia. A implementação de centros de saúde com maior capacidade de tratamento intensivo em estados mais vulneráveis pode ser uma estratégia eficaz para reduzir a sobrecarga hospitalar e melhorar os índices de recuperação. Além disso, o governo deve investir em campanhas educacionais voltadas para a prevenção e conscientização da população, incentivando o uso de medidas de proteção individual, como máscaras e higiene das mãos, especialmente em regiões onde o sistema de saúde já enfrenta dificuldades.

Outro ponto essencial é o uso de tecnologia para aprimorar a gestão de dados e prever padrões de comportamento durante novas crises. Ferramentas de análise preditiva podem ser utilizadas para detectar focos emergentes de doenças e alocar recursos com mais eficiência. A comunicação rápida e eficaz entre as autoridades de saúde, hospitais e a população deve ser uma prioridade, garantindo que as informações sobre novos surtos e protocolos de atendimento sejam disseminadas de forma clara e precisa.

Por fim, a pandemia evidenciou a importância de se manter uma reserva estratégica de equipamentos médicos e medicamentos essenciais, como ventiladores e EPI’s, principalmente em locais onde a demanda por atendimento pode crescer rapidamente. Com essas medidas, o Brasil estará mais preparado para enfrentar futuras emergências de saúde, minimizando os impactos sociais e econômicos, e salvando mais vidas.
""", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)
