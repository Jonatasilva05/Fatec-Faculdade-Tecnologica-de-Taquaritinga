### OBS: Se não gosta de Linux, saiba que não poderá mexer com Docker pois o sistema operacional do windowns é relativamente fraco para os processos com Docker usando WSL


# O que é o Docker Hub?
Imagine que você está construindo algo com peças de LEGO. Em vez de fabricar cada pecinha do zero, você vai até uma loja gigante de LEGOs, onde encontra kits prontos e peças de todos os tipos, criadas tanto pela LEGO oficial quanto por outros fãs. 

O Docker Hub é exatamente essa loja gigante, mas para desenvolvedores, ele é um repositório na nuvem onde as pessoas e empresas podem guardar, gerenciar e compartilhar imagens de contêineres Docker.

## Uma analogia diferente

Para facilitar gravação é só pensar que o Docker Hub é como o GitHub de repositorios mas em vez de ser de ser um gerenciador de projetos ele é um "GitHub" das imagens Docker ou uma Play/App Store para servidores. Assim como você baixa um app no seu celular, um desenvolvedor "baixa" uma imagem do Docker Hub para rodar um programa (como um banco de dados, um site, etc.) em segundos.

### Vale ressaltar que:
Existem dois tipos principais de imagens lá:

- Imagens Oficiais: São Imagens mantidas e verificadas pela própria Docker ou pelos criadores do software (por exemplo, a imagem oficial do python ou do ubuntu). São as mais seguras e recomendadas! Essa tem um simbolo verde como uma "medalha de condecoração" geralmente tem a cor verde

- Imagens da Comunidade: São criadas por qualquer pessoa ou empresa. Há muita coisa útil, mas é como comprar de um vendedor desconhecido: é sempre bom dar uma olhada na popularidade e nas avaliações.

#### Em resumo: o Docker Hub resolve um grande problema

```
    Ele oferece um lugar central e confiável para encontrar os "blocos de construção" (as imagens) que você precisa para criar e rodar suas aplicações sem a necessidade de criar do zero.
```

### Para fixar com maior facilidade pense num enigma
 Eu sou uma biblioteca online, mas não tenho livros. Sou um mercado de aplicativos, mas meus apps rodam em servidores. Sou o ponto de encontro de desenvolvedores que não querem "reinventar a roda". Quem sou eu?

#### Resposta

```
    Docker Hub
```

---

Lembrando que  maquina virtual é totalmente diferente do container do docker



# Tópico 2

## Explorando Imagens no Hub
Agora que sabemos o que é o Docker Hub, vamos aprender a "passear" por ele e encontrar o que precisamos. É como aprender a usar o campo de busca de uma loja online.

Quando você acessa o site do Docker Hub e procura por algo, como "python", por exemplo, você verá uma lista de resultados. A primeira coisa a se procurar é o selo de Imagem Oficial (Docker Official Image), que indica confiança e segurança.

Ao clicar em uma imagem, você verá uma página cheia de informações úteis. As mais importantes são:

- Descrição: Um resumo do que a imagem contém e, geralmente, exemplos de como usá-la.

- Tags (Etiquetas): Essa é a parte mais importante! As "tags" são como as versões ou sabores de uma imagem.

Pense numa imagem de sorvete. A imagem seria "sorvete" e as tags seriam "chocolate", "morango", "flocos". Para as imagens Docker, é a mesma coisa.

#### - > imagem = sorvete
#### - > sorvete = sabores

Por exemplo, para a imagem node (que executa JavaScript), você pode encontrar tags como:

node:latest: A versão mais recente e estável.

node:18: Especificamente a versão 18 do Node.js.

node:18-alpine: A versão 18, mas construída sobre uma base de sistema operacional super leve chamada Alpine Linux (uma versão "light" da imagem).

Saber escolher a tag certa é fundamental para garantir que sua aplicação funcione como esperado!