# Vieira Fauna Shopping | Landing page

Página única, estática, em HTML, CSS e JavaScript puro. Não há etapa de build
nem dependências de execução: basta servir a pasta.

## Como visualizar

```bash
# na raiz do projeto
python3 -m http.server 4184
# abra http://localhost:4184
```

Qualquer servidor estático funciona (Nginx, Apache, Netlify, Vercel, Hostinger).
Publique `index.html` e a pasta `assets/`. A pasta `tools/` não precisa ir para
o servidor.

### Materiais de origem

Os arquivos enviados pelo cliente ficam reunidos na pasta
`materiais-de-origem/`, que não faz parte do repositório: ela existe só na
pasta local do projeto e é ignorada pelo git. As imagens que o site usa já
estão prontas em `assets/img`.

```
materiais-de-origem/
  fotos/         oito capturas de tela do Instagram da loja
  avaliacoes/    fotos de perfil de quem avaliou
```

Não foi recebido logo. A marca da página é provisória, desenhada por código
(veja "Marca provisória").

Só é preciso ter os originais para rodar `tools/optimize-images.py`, ou seja,
para trocar ou reprocessar uma foto.

## Dados do cliente

Recebidos em 30/09/2026.

| Dado | Valor |
| --- | --- |
| Nome | Vieira Fauna Shopping (no Google: Pet Shop Vieira Fauna Shopping) |
| Segmento | Pet shop |
| Produtos e serviços | Peixes, rações, produtos veterinários, banho e tosa, consultório veterinário, estética canina |
| Frases do Instagram | "Especialista em peixes e aquários sob medida", "Banho e tosa", "Atendimento veterinário há mais de 30 anos" |
| Público | Pessoas que têm animais de estimação |
| Objetivo | Landing page com qualidade premium, para divulgar a marca |
| WhatsApp | (44) 99923-9780 |
| Telefone | (44) 3222-7040 |
| Instagram | https://www.instagram.com/vieirafaunashopping/ |
| Endereço | Avenida Paraná, 652, Maringá, PR |

### Conferido no Google

Em 30/09/2026, o Google Maps mostrava o perfil "Pet Shop Vieira Fauna
Shopping" na Av. Paraná, 652, Zona 01, Maringá, com nota 4,5 e 297
avaliações. O briefing não informou nota, e a página não cita nota nem número
de avaliações. O mapa incorporado é carregado pelo endereço, e não pelo nome
da loja, para não exibir a nota dentro do quadro. O CEP não foi informado e
não aparece na página.

### Avaliações como foram recebidas

- **Larissa França:** Banho e tosa perfeitos! Deixei minha filhote lá  e ela
  voltou lindinha e alegre, com a tosa que pedi, cheirosa e com os pelos
  desembaraçados.
- **Rafael Santos:** Muito legal  variedades de peixes enorme recomendo! Preço
  ótimo.
- **Gabriel HR:** Muita variedades de peixes e bem organizado sempre chegando
  peixes novos.

Na página, foram corrigidos só a pontuação e a concordância: "variedades"
virou "variedade", vírgulas foram acrescentadas e o espaço duplo foi
removido. O sentido não mudou. As avaliações de Rafael e Gabriel aparecem
duas vezes: como notas na seção "Na água" e na seção "Avaliações".

## Estratégia

| Definição | Decisão |
| --- | --- |
| Proposta de valor | Loja, banho e tosa e consultório veterinário no mesmo endereço, com uma especialidade rara: peixes e aquários sob medida |
| Principal objeção | "Pet shop é tudo igual. Vão cuidar direito do meu bicho? E se eu tiver um peixe, uma ave, uma tartaruga?" |
| Conversão prioritária | Conversa no WhatsApp (agendar banho e tosa, perguntar sobre peixes, falar com o veterinário) |
| Ação secundária | Ligar ou visitar a loja |
| Ação de apoio | Seguir o Instagram @vieirafaunashopping |

## Direção visual: guia de campo

A loja se chama "Fauna Shopping" e as fotos mostram peixe, ave, tartaruga e
cães. A página foi montada como um guia de campo de naturalista: cada foto tem
uma legenda numerada ("Fig. 01", "Fig. 02"...), os serviços formam um índice
numerado com ícones de traço, e a página se divide em duas partes, "Na água"
(seção escura, cor de aquário, sobre peixes e aquários) e "Em terra" (seção
clara, sobre banho e tosa), separadas por uma onda. Sem gradientes, sem
efeitos de vidro, sem emojis como ícones.

## Seções da página

| Ordem | Seção | Âncora | Conteúdo |
| --- | --- | --- | --- |
| 1 | Cabeçalho | | Marca, navegação e CTA de WhatsApp. Fixo no topo |
| 2 | Hero | `#inicio` | "Do aquário ao quintal, tudo para quem você cuida", dois botões, prancha com duas fotos e três fatos (30+ anos, sob medida, 1 endereço) |
| 3 | Serviços | `#servicos` | Índice numerado com os seis itens do briefing e ícones desenhados por código |
| 4 | Na água | `#peixes` | Peixes e aquários sob medida, duas avaliações sobre peixes, três fotos |
| 5 | Em terra | `#banho-e-tosa` | Banho e tosa e estética canina, três passos para agendar, foto do golden |
| 6 | Veterinário | `#veterinario` | Consultório há mais de 30 anos, produtos veterinários e rações, foto da calopsita |
| 7 | Avaliações | `#avaliacoes` | Três depoimentos, o de Larissa em destaque |
| 8 | Onde fica | `#onde-fica` | Endereço, WhatsApp, telefone, Instagram e mapa |
| 9 | Chamada final | | "Para cada bicho, alguém que entende", WhatsApp e telefone |
| 10 | Rodapé | | Endereço, contato e redes sociais |

Componente de apoio: botão flutuante de WhatsApp, no canto inferior direito,
em todas as telas.

## Estrutura de arquivos

```
index.html                       conteúdo e SEO
assets/css/styles.css            estilos (tokens de cor e tipografia no topo)
assets/js/main.js                menu e revelação na rolagem
assets/img/                      imagens otimizadas (geradas pelos scripts)
assets/fonts/                    Fraunces e Manrope (arquivos locais)
tools/optimize-images.py         gera assets/img a partir dos originais
tools/marca/marca.svg            marca provisória, desenhada por código
tools/marca/render-marca.js      gera o PNG da marca e a imagem de compartilhamento
materiais-de-origem/             arquivos do cliente (só na pasta local, fora do git)
```

## Imagens recebidas e como foram usadas

As oito imagens são capturas de tela de publicações do Instagram. Sete foram
usadas. **Nenhuma imagem é ampliada**, e um teste automático confere que
nenhuma aparece na página acima do tamanho real.

| Arquivo | Conteúdo | Tamanho | Onde aparece |
| --- | --- | --- | --- |
| `Screenshot ... 101500.png` | Spitz branco tosado, no painel de fotos da loja | 886 x 885 | hero (foto principal) e imagem de compartilhamento |
| `Screenshot ... 101321.png` | Acará-bandeira em aquário | 496 x 846 | hero (foto menor) |
| `Screenshot ... 101400.png` | Aquário plantado | 498 x 843 | "Na água" |
| `Screenshot ... 101546.png` | Tigre-d'água sobre pedra | 882 x 886 | "Na água" |
| `Screenshot ... 101411.png` | Enfeites de aquário | 882 x 884 | "Na água" |
| `Screenshot ... 101519.png` | Golden retriever fantasiado de carnaval | 677 x 841 | "Em terra" (a seta do carrossel do Instagram, à direita, ficou fora do recorte) |
| `Screenshot ... 101228.png` | Calopsita branca | 887 x 887 | "Veterinário" |
| `Screenshot ... 101339.png` | Duas tartarugas pequenas sobre pedra, foto com filtro e desfocada | 499 x 813 | **não usada**, por causa da qualidade |

Observações:

- Os nomes dos animais nas legendas (acará-bandeira, tigre-d'água, calopsita,
  spitz, golden retriever) identificam o que aparece em cada foto. A página
  não afirma que a loja vende essas espécies; ela diz que "cães, peixes,
  tartarugas e aves aparecem nas publicações da loja".
- O painel de fundo da foto do spitz traz o nome da loja e o telefone fixo.
  É material da própria loja e ficou na foto.
- A foto de perfil de Larissa não mostra uma pessoa (é uma flor). Ficou como
  veio.

### Marca provisória

Não foi recebido logo. A página usa uma marca desenhada por código: uma pata
cujo coxim é um peixe, em verde-água e âmbar, com o nome "Vieira" em Fraunces
e "Fauna Shopping" em Manrope. O símbolo está em `tools/marca/marca.svg` e
também inline no `index.html` (cabeçalho e rodapé); o nome é texto.

O painel de fotos da loja, visível na foto do spitz, mostra a identidade que a
loja usa hoje: nome em letra cursiva branca sobre quadros azul-claro e rosa,
com patinhas. A marca provisória não copia esse painel.

**Quando o logo oficial chegar:**

1. Salve o arquivo em `materiais-de-origem/logo/`.
2. Em `tools/optimize-images.py`, acrescente uma função que gere as versões do
   logo em `assets/img` (o script dos outros projetos desta série serve de
   modelo) e troque `MARK_PNG` pelo logo para os ícones.
3. No `index.html`, substitua os dois blocos `<a class="brand">` por uma tag
   `<img>` com o logo, ou mantenha o texto e troque só o `<svg
   class="brand__mark">`.
4. Reveja as cores em `assets/css/styles.css`, bloco `:root`, para combinar
   com o logo.
5. Rode `node tools/marca/render-marca.js` de novo, ou ajuste o cartão de
   compartilhamento nesse script para usar o logo.

## Como atualizar o conteúdo

| O que mudar | Onde |
| --- | --- |
| Textos e endereço | `index.html` (seções comentadas) |
| Número e mensagem do WhatsApp | `index.html`: procure por `wa.me/` (9 ocorrências). O texto vem depois de `?text=`, com espaços escritos como `%20` e acentos codificados |
| Telefone | `index.html`: procure por `tel:` (3 ocorrências) e o bloco JSON-LD no `<head>` |
| Mapa | `index.html`: procure por `google.com/maps` (4 ocorrências, uma delas no `<iframe>`) |
| Cores e fontes | `assets/css/styles.css`, bloco `:root` |
| Serviços | `index.html`, lista `index` na seção "SERVIÇOS" (a numeração é automática) |
| Ícones dos serviços | `index.html`, símbolos `s-*` no início do `<body>` |
| Passos do agendamento | `index.html`, lista `steps` na seção "EM TERRA" |
| Fotos | substitua o original, ajuste a lista `PHOTOS` de `tools/optimize-images.py` e rode o script |
| Avaliações | `index.html`, seções "NA ÁGUA" (notas) e "AVALIAÇÕES". Fotos de perfil: lista `AVATARS` do script |

Mensagens de WhatsApp, conforme o ponto da página:

| Onde | Mensagem |
| --- | --- |
| Cabeçalho, hero, "Onde fica", chamada final, rodapé e botão flutuante | Olá! Vi o site da Vieira Fauna Shopping e quero mais informações. |
| Seção "Na água" | ... quero saber sobre peixes e aquários. |
| Seção "Em terra" | ... quero agendar banho e tosa. |
| Seção "Veterinário" | ... quero saber sobre o atendimento veterinário. |

Para gerar as imagens (requer Pillow e a pasta `materiais-de-origem/`):

```bash
node tools/marca/render-marca.js   # marca em PNG e imagem de compartilhamento (requer Node e Playwright)
python3 tools/optimize-images.py   # fotos, avatares e ícones
```

Se o Playwright não estiver instalado no projeto, informe os caminhos pelas
variáveis `PLAYWRIGHT_MODULE` e `CHROMIUM_PATH`. Sem o PNG da marca, o
`optimize-images.py` mantém os ícones que já estão em `assets/img`.

Se a proporção de uma foto mudar, atualize `width` e `height` da tag `<img>`
correspondente no `index.html`, para não haver salto de layout.

### Título do hero

O título tem quatro linhas ("Do aquário / ao quintal, / tudo para quem / você
cuida."), e o tamanho da letra é calculado para que "tudo para quem" caiba em
uma linha em qualquer tela. Se o texto mudar, confira a quebra em 320 px e em
900 px de largura. A regra está em `.hero__title`, no `styles.css`.

### Cache do navegador

Os arquivos de estilo e script são chamados com versão: `styles.css?v=1` e
`main.js?v=1`. Ao alterar um deles, aumente o número no `index.html` para que
os visitantes recebam a versão nova.

## Identidade visual

Sem logo, a paleta veio das fotos: a água dos aquários e o pelo dos cães.

| Token | Cor | Origem |
| --- | --- | --- |
| `--deep` | `#0B3B3A` | fundo dos aquários: seção "Na água", chamada final e rodapé |
| `--teal` | `#12615C` | cor da marca provisória: botões, destaques dos títulos, rótulos |
| `--teal-700` | `#0D4C48` | hover dos botões |
| `--aqua`, `--aqua-100` | `#A9E0DA`, `#DCEFEC` | água clara: destaques sobre o escuro e fundo dos ícones |
| `--amber` | `#E2A34A` | pelo do golden e do acará: botões da seção escura, números dos passos, traço dos rótulos |
| `--amber-800` | `#8A5A10` | âmbar escurecido: numeração "Fig." e do índice sobre fundo claro |
| `--sand`, `--white` | `#F5EFE4`, `#FFFDF9` | papel do guia: fundos claros, alternados |
| `--ink`, `--ink-soft` | `#172321`, `#4F5D5A` | textos sobre fundo claro |
| `--mist` | `#B7D3CF` | texto secundário sobre o escuro |
| `--whatsapp` | `#25D366` | verde oficial do WhatsApp, usado só no botão flutuante |

Tipografia: Fraunces (títulos, com o destaque em itálico) e Manrope (textos).

## Decisões de conteúdo

- Só foram usados dados fornecidos: nome, serviços, frases do Instagram,
  endereço, telefones, Instagram, fotos e avaliações. Não há preços, marcas,
  raças atendidas, horários, prazos ou promessas inventadas.
- "Há mais de 30 anos" refere-se ao atendimento veterinário, como no
  Instagram da loja. A página não aplica o número à loja inteira.
- "Aquários sob medida" vem do Instagram. A explicação ("você escolhe o
  tamanho, a decoração e os acessórios, e a equipe orienta a montagem")
  descreve o que "sob medida" significa; se o processo for diferente, ajuste
  o texto da seção "Na água".
- Os três passos de agendamento do banho e tosa descrevem o caminho pelo
  WhatsApp; não citam prazo, preço nem horário.
- "Banho e tosa do jeito que você pediu" e "pelos desembaraçados" vêm da
  avaliação de Larissa.
- "Quem passa por aqui" diz que cães, peixes, tartarugas e aves aparecem nas
  publicações da loja e pede para confirmar pelo WhatsApp se o animal é
  atendido. A página não afirma quais espécies o veterinário atende.
- "Confirme o horário de atendimento pelo WhatsApp antes de vir" está na
  página porque o horário não foi informado.
- Avaliações sem estrelas desenhadas e sem nota, porque nenhuma nota foi
  informada.
- O mapa é um mapa do Google incorporado, carregado pelo endereço. Ele só
  carrega quando o visitante chega perto da seção.
- Não há formulário, porque não existe destino de envio definido.
- A foto do hero não tem legenda por cima; a legenda "Fig. 01" fica abaixo.
- O ícone do botão flutuante é escuro sobre o verde, e não branco, para manter
  contraste suficiente.

## Testes realizados

Executados em 30/09/2026, em Chromium automatizado (Playwright).

- Revisão visual das capturas de tela: página inteira em 390 e 1440 px e
  primeira tela em 320, 768 e 1024 px.
- Sem rolagem horizontal e com o título do hero em quatro linhas nos tamanhos
  320, 360, 390, 480, 600, 768, 900, 1024, 1200, 1440 e 1920 px.
- Sem erros de console e sem imagens quebradas.
- 41 verificações automáticas aprovadas: menu no celular (toque, Esc, toque
  fora, foco), âncoras, botão flutuante de WhatsApp (posição, nome acessível,
  sem cobrir o texto do rodapé), fotos sem ampliação acima do tamanho real,
  mapa com título e carregamento adiado, revelação na rolagem, link de pular
  para o conteúdo, foco visível, destino e atributos de todos os links, quatro
  mensagens de WhatsApp, hierarquia de títulos e atributos das imagens, sem
  travessões, emojis ou textos de exemplo.
- O mapa foi aberto no teste e mostrou o marcador na Av. Paraná, 652.
- Página utilizável sem JavaScript.
- Animações desligadas quando o sistema pede movimento reduzido.
- Contraste AA em todos os textos.
- Carga inicial no celular abaixo de 700 KB, medida em tela de densidade 3x,
  sem saltos de layout (CLS 0). Página inteira: 554 KB, sem contar o mapa.
- O mapa do Google é baixado só quando o visitante chega à seção "Onde fica".

Não testado: Safari, Firefox e aparelhos físicos. Dos links externos, foi
conferido apenas o endereço, não o conteúdo de destino. Também não foi
verificado se o número responde no WhatsApp.

## Histórico de ajustes

| Ajuste | Arquivos |
| --- | --- |
| Versão inicial da página, com marca provisória | todos |

## Créditos e licenças

- Fotos, avaliações e fotos de perfil: fornecidos pelo cliente.
- Marca provisória, ícones dos serviços e demais ícones: criados para este
  projeto. Ícone do WhatsApp: Simple Icons (CC0).
- Fraunces e Manrope: SIL Open Font License 1.1, obtidas do Google Fonts e
  hospedadas localmente.
- Mapa: Google Maps, incorporado.

## Pendências que dependem do cliente

- **Logo oficial.** A marca da página é provisória. Com o logo, as cores e o
  cabeçalho devem ser revistos (veja "Marca provisória").
- **Fotos da loja, do setor de peixes e do banho e tosa, em alta resolução.**
  As recebidas são capturas de tela de posts. Uma foto de um aquário montado
  sob medida, na casa de um cliente, seria a melhor prova da especialidade.
- **Espécies atendidas pelo veterinário** (só cães e gatos? aves? peixes?
  répteis?), para a página poder afirmar em vez de pedir confirmação.
- **Como funciona o "sob medida"** dos aquários: quem monta, se há entrega e
  instalação, prazos.
- Horário de funcionamento e formas de pagamento.
- Raças e portes atendidos no banho e tosa, e se há busca e entrega.
- Marcas de ração vendidas, se quiserem citar.
- Mais avaliações, com autorização de uso do nome e da foto.
- Domínio de publicação, para completar `og:image` com URL absoluta e adicionar
  `link rel="canonical"`.
- Fotos de perfil das avaliações têm 72 x 72 px. Ficam nítidas no tamanho usado
  (48 px), mas não podem ser ampliadas.
