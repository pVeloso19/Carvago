<template>
  <q-card class="my-card Card">
    <div class="q-pa-md Imagens">
      <q-carousel
        swipeable
        animated
        v-model="slide"
        infinite
        :autoplay="autoplay"
        arrows
        transition-prev="slide-right"
        transition-next="slide-left"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
        style="max-height: 100%;"
      >
        <q-carousel-slide
          :name="i-1"
          v-for="i in Links_foto.length"
          :key="i"
          :img-src="Links_foto[i-1]"
          @click="carousel = true; slide2=i-1"
        />
      </q-carousel>
    </div>

    <div class="Informacoes1">
      <p class="Titulo">{{Titulo}}</p>
      <div class="row DetalhesMinimos">
        <p class="MarcaDetalhe">{{Marca}}</p>
        <p class="IconSparate">♦</p>
        <p class="ModeloDestalhe">{{Modelo}}</p>
        <p class="IconSparate">♦</p>
        <p class="CombustivelDetalhe">{{Combustivel}}</p>
        <p class="IconSparate">♦</p>
        <p class="QuilometrosDetalhe">{{QuilometrosString()}} km</p>
        <p class="IconSparate">♦</p>
        <p class="AnoDetalhe">{{Ano}}</p>
        <p class="IconSparate AnuncianteSeparate">♦</p>
        <p class="Anunciante">{{Anunciante}}</p>
      </div>
    </div>

    <div class="Informacoes2">
      <p class="text-center Preco">{{PrecoString()}} EUR</p>
      <Avaliador class="btnOcultoAvaliarPreco" :Preco="PrecoString()" v-if="Avaliar">
      </Avaliador>
    </div>

    <div class="Botoes">
      <q-btn color="primary BtnFavorito" @click="addOrRemoveFav(ID)">
        <div class="row items-center no-wrap">
          <q-icon name="favorite" color='whait' v-if="(favorite === null) ? favoriteTemp : favorite"/>
          <q-icon name="favorite_border" color='whait' v-else/>
          <div class="text-center addFavorito" style="margin-left:5px;" v-if="!((favorite === null) ? favoriteTemp : favorite)">
            Adicionar aos Favoritos
          </div>
          <div class="text-center addFavorito" style="margin-left:5px;" v-else>
            Remover dos Favoritos
          </div>
        </div>
      </q-btn>

      <q-btn color="primary BtnDetalhes" @click="icon = true">
        <div class="row items-center no-wrap">
          <q-icon name="add" color='whait' />
          <div class="text-center detalhes" style="margin-left:5px;">
            Detalhes
          </div>
        </div>
      </q-btn>

      <q-btn color="primary BtnSite" @click="openNewTab(Link_anuncio)">
        <div class="row items-center no-wrap">
          <q-icon name="preview" color='whait' />
          <div class="text-center visitarSite" style="margin-left:5px;">
            Visitar Site
          </div>
        </div>
      </q-btn>
    </div>

  </q-card>

  <q-dialog
    v-model="carousel"
    full-width
    transition-show="slide-up"
    transition-hide="slide-down"
  >
    <q-carousel
      transition-prev="slide-right"
      transition-next="slide-left"
      swipeable
      animated
      v-model="slide2"
      control-color="primary"
      navigation
      arrows
      infinite
      padding
      height="100%"
      class="bg-white shadow-1 rounded-borders"
      style="overflow: hidden;"
    >
      <q-carousel-slide :name="i-1" v-for="i in Links_foto.length" :key="i" class="column no-wrap flex-center" >
        <q-img
          :src="Links_foto[i-1]"
          style="max-width: 100%; height: 100%;"
          fit="contain"
        />
        <q-btn round icon="close" class="absolute fixed-left fixed-top" style="width: 5px; height: 5px" @click="carousel = false;" />
      </q-carousel-slide>
    </q-carousel>
  </q-dialog>

   <div class="q-pa-md q-gutter-sm">
    <q-dialog v-model="icon" >
      <q-card>
        <q-card-section class="row items-center q-pb-none">
          <div class="text-h6 text-bold DetalhesTitulo">{{Titulo}}</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="TodosDetalhes">
          <div class="Titulo">
            <p class="text-bold tit">Anunciante:</p>
            <p class="text-bold tit">Marca:</p>
            <p class="text-bold tit">Modelo:</p>
            <p class="text-bold tit">Versão:</p>
            <p class="text-bold tit">Combustível:</p>
            <p class="text-bold tit">Mês de Registo:</p>
            <p class="text-bold tit">Ano:</p>
            <p class="text-bold tit">Quilómetros:</p>
            <p class="text-bold tit">Cilindrada:</p>
            <p class="text-bold tit">Potência:</p>
            <p class="text-bold tit">Cor:</p>
            <p class="text-bold tit">Tipo de Cor:</p>
            <p class="text-bold tit">Tipo de Caixa:</p>
            <p class="text-bold tit">Número de Portas:</p>
            <p class="text-bold tit">Origem:</p>
            <p class="text-bold tit">Condição:</p>
            <p class="text-bold tit">Preço:</p>
            <p class="text-bold tit">Site de origem:</p>
          </div>

          <div class="Valor">
            <p class="val">{{(Anunciante != '') ? Anunciante : '\n'}}</p>
            <p class="val">{{(Marca != '') ? Marca : '\n'}}</p>
            <p class="val">{{(Modelo != '') ? Modelo : '\n'}}</p>
            <p class="val">{{(Versao != '') ? Versao : '\n'}}</p>
            <p class="val">{{(Combustivel != '') ? Combustivel : '\n'}}</p>
            <p class="val">{{(Mes_Registo != '') ? Mes_Registo : '\n'}}</p>
            <p class="val">{{(Ano != '') ? Ano : '\n'}}</p>
            <p class="val">{{(QuilometrosString() != '') ? QuilometrosString() : '\n'}} km</p>
            <p class="val">{{(Cilindrada != '') ? Cilindrada : '\n'}} cm3</p>
            <p class="val">{{(Potencia != '') ? Potencia : '\n'}} cv</p>
            <p class="val">{{(Cor != '') ? Cor : '\n'}}</p>
            <p class="val">{{(Tipo_Cor != '') ? Tipo_Cor : '\n'}}</p>
            <p class="val">{{(Tipo_Caixa != '') ? Tipo_Caixa : '\n'}}</p>
            <p class="val">{{(Num_Portas != '') ? Num_Portas : '\n'}}</p>
            <p class="val">{{(Origem != '') ? Origem : '\n'}}</p>
            <p class="val">{{(Condicao != '') ? Condicao : '\n'}}</p>
            <p class="val">{{(PrecoString() != '') ? PrecoString() : '\n'}} €</p>
            <p class="val">{{(Fonte != '') ? Fonte : '\n'}}</p>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>

</template>

<script>
import { computed, defineComponent, ref } from 'vue'
import { useQuasar } from 'quasar'

import Avaliador from 'components/AvaliarPreco.vue'

import axios from 'axios'

import URL from '../url.js'

let self

export default defineComponent({
  name: 'CarCard',

  components: {
    Avaliador
  },

  props: {
    Anunciante: {
      type: String,
      default: ''
    },

    Marca: {
      type: String,
      default: ''
    },

    Modelo: {
      type: String,
      default: ''
    },

    Versao: {
      type: String,
      default: ''
    },

    Combustivel: {
      type: String,
      default: ''
    },

    Mes_Registo: {
      type: String,
      default: ''
    },

    Ano: {
      type: String,
      default: ''
    },

    Quilometros: {
      type: Number,
      default: 0
    },

    ID: {
      type: Number,
      default: -1
    },

    Cilindrada: {
      type: String,
      default: ''
    },

    Potencia: {
      type: String,
      default: ''
    },

    Cor: {
      type: String,
      default: ''
    },

    Tipo_Cor: {
      type: String,
      default: ''
    },

    Tipo_Caixa: {
      type: String,
      default: ''
    },

    Num_Portas: {
      type: String,
      default: ''
    },

    Origem: {
      type: String,
      default: ''
    },

    Condicao: {
      type: String,
      default: ''
    },

    Preco: {
      type: Number,
      default: 0
    },

    Links_foto: {
      type: Array,
      default: () => []
    },

    Titulo: {
      type: String,
      default: ''
    },

    Link_anuncio: {
      type: String,
      default: ''
    },

    Fonte: {
      type: String,
      default: ''
    },

    Favorito: {
      type: Boolean,
      required: true
    },

    Avaliar: {
      type: Boolean,
      default: true
    }
  },

  beforeCreate () {
    self = this
  },

  setup () {
    const $q = useQuasar()

    const favorite = ref(null)

    const openNewTab = (link) => {
      window.open(link, '_blank')
    }

    function PrecoString () {
      let teste = this.Preco.toString()
      teste = teste.replace(new RegExp('^(\\d{' + (teste.length % 3 ? teste.length % 3 : 0) + '})(\\d{3})', 'g'), '$1 $2').replace(/(\d{3})+?/gi, '$1 ').trim()
      return teste
    }

    function QuilometrosString () {
      let teste = this.Quilometros.toString()
      teste = teste.replace(new RegExp('^(\\d{' + (teste.length % 3 ? teste.length % 3 : 0) + '})(\\d{3})', 'g'), '$1 $2').replace(/(\d{3})+?/gi, '$1 ').trim()
      return teste
    }

    const favoriteTemp = computed(() => {
      return self.Favorito
    })

    async function addOrRemoveFav (idCarro) {
      const id = sessionStorage.getItem('IdentificadorCarvago')

      const favoritoTemp = (favorite.value === null) ? !favoriteTemp.value : !favorite.value

      let res = false

      if (id > 0) {
        if (favoritoTemp) {
          const userJogos = await axios({
            method: 'get',
            url: URL.URL + '/AddFavorito',
            params: { ID: id, IDCarro: idCarro }
          })
          res = await userJogos.data
        } else {
          const userJogos = await axios({
            method: 'get',
            url: URL.URL + '/RemoveFavorito',
            params: { ID: id, IDCarro: idCarro }
          })
          res = await userJogos.data
        }

        res = res.resultado

        if (res) {
          favorite.value = favoritoTemp

          if (!favoritoTemp) {
            this.$emit('RemoveFavorito', idCarro)
          }
        }
      } else {
        $q.notify({
          color: 'negative',
          message: 'Impossivel adicionar aos favoritos - Realize Login para efetuar esta operação!!'
        })
      }
    }

    return {
      openNewTab,
      icon: ref(false),
      slide: ref(1),
      autoplay: ref(true),
      carousel: ref(false),
      slide2: ref(1),

      QuilometrosString,
      PrecoString,

      favoriteTemp,
      favorite,

      addOrRemoveFav
    }
  }
})
</script>

<style>

.Card {
  display: grid;
  grid-template-columns: 20% 57% 23%;
  grid-template-rows: 160px 40px;
  grid-template-areas:
  "Imagens Informacoes1 Informacoes2"
  "Imagens Botoes Botoes";

  padding: 10px 10px 10px 10px;
  margin-left: 50px;
  margin-right: 50px;
}

.Imagens{
  grid-area: Imagens;
  margin: 0px 0px 0px 0px;
  padding: 0px 0px 0px 0px;

  background-color: blue;

  max-height:200px;
}

.Informacoes1{
  grid-area: Informacoes1;
}

.Informacoes2{
  grid-area: Informacoes2;
  display: grid;
  grid-template-areas:
  "preco";
}

.Informacoes1 .Titulo {
  --max-size: 23;
  --min-size: 10;
  --diff: calc(var(--max-size) - var(--min-size));
  --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

  font-size: var(--responsive);
  font-weight: bold;

  margin: 0px 0px 0px 0px;
  margin-left: 20px;
  padding-top: 10px;

  height: auto;
}

.Informacoes1 .DetalhesMinimos{
  display: flex;
  align-items: center;
  justify-content: center;

  height: auto;

  font-size: 20px;

  margin: 0px 0px 0px 0px;
}

.Informacoes1 .DetalhesMinimos p{
  margin: 10px;
}

.Informacoes1 .DetalhesMinimos .IconSparate{
  margin: 0px 0px 0px 0px;
}

.Informacoes2 .Preco{
  grid-area: preco;
  font-weight: bold;

  font-size: 300%;
  color:red;

  display: flex;
  align-items: center;
  margin: 0px 0px 0px 0px;

  z-index: 1;

  -webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
     -khtml-user-select: none; /* Konqueror HTML */
       -moz-user-select: none; /* Old versions of Firefox */
        -ms-user-select: none; /* Internet Explorer/Edge */
            user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}

.Informacoes2 .btnOcultoAvaliarPreco {
  grid-area: preco;

  width: 100%;
  height: 95%;

  display: none;

  -webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
     -khtml-user-select: none; /* Konqueror HTML */
       -moz-user-select: none; /* Old versions of Firefox */
        -ms-user-select: none; /* Internet Explorer/Edge */
            user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}

.Preco:hover + .btnOcultoAvaliarPreco {
  display: block;
}

.btnOcultoAvaliarPreco:hover {
  display: block;
}

.Botoes{
  grid-area: Botoes;
  display: grid;
  grid-template-areas:
  "btn1 btn2 btn3";
  max-height:40px;
}

.Botoes .BtnFavorito{
  grid-area: btn1;
  margin-left: 10px;

  --max-size: 10;
  --min-size: 7;
  --diff: calc(var(--max-size) - var(--min-size));
  --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

  font-size: var(--responsive);
}

.Botoes .BtnDetalhes{
  grid-area: btn2;
  margin-left: 10px;

  --max-size: 10;
  --min-size: 7;
  --diff: calc(var(--max-size) - var(--min-size));
  --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

  font-size: var(--responsive);
}

.Botoes .BtnSite{
  grid-area: btn3;
  margin-left: 10px;

  --max-size: 10;
  --min-size: 7;
  --diff: calc(var(--max-size) - var(--min-size));
  --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

  font-size: var(--responsive);
}

.TodosDetalhes {
  display: grid;
  grid-template-columns: auto auto auto;
  grid-template-areas:
  "Titulo NADA Valor";
}

.TodosDetalhes .Titulo{
  grid-area: Titulo;
  margin-right: 20px;
}

.TodosDetalhes .Valor{
  grid-area: Valor;
  white-space: pre;
}

.DetalhesTitulo{
  margin-right: 20px;
}

@media (max-width: 1370px) {
  .Anunciante{
    display: none
  }

  .AnuncianteSeparate{
    display: none
  }

  .Informacoes1 .DetalhesMinimos{
    font-size: 18px;
  }
}

@media (max-width: 780px) {
  .Card {
    display: grid;
    grid-template-columns: 100%;
    grid-template-rows: auto auto auto auto;
    grid-template-areas:
    "Imagens"
    "Informacoes1"
    "Informacoes2"
    "Botoes";

    padding: 10px 10px 10px 10px;
    margin-left: 40px;
    margin-right: 40px;
  }

  .Informacoes1 .Titulo {
    --max-size: 35;
    --min-size: 20;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);
  }

  .Informacoes1 .DetalhesMinimos{
    margin-bottom: 10px;
    margin-top: 10px;
  }

  .Informacoes2 .Preco{
    justify-content: center;
    margin-bottom: 10px;
  }
}

@media (max-width: 600px) {
  .Card {
    margin-left: 25px;
    margin-right: 25px;
  }

  .addFavorito{
    display: none
  }

  .detalhes{
    display: none
  }

  .Botoes .BtnFavorito{
    font-size: 12px;
  }

  .Botoes .BtnDetalhes{
    font-size: 12px;
  }
}

@media (max-width: 380px) {
  .Card {
    margin-left: 5px;
    margin-right: 5px;
  }

  .visitarSite{
    display: none
  }

  .Botoes .BtnFavorito{
    font-size: 10px;
  }

  .Botoes .BtnDetalhes{
    font-size: 10px;
  }

  .Botoes .BtnSite{
    font-size: 10px;
  }

  .Informacoes1 .DetalhesMinimos {
    display: none;
  }

  .Informacoes2 .Preco{
    --max-size: 45;
    --min-size: 25;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);
  }
}

@media (max-width: 310px) {
  .Botoes .BtnFavorito{
    --max-size: 25;
    --min-size: 12;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);
    width: var(--responsive);
    min-width: var(--responsive);
  }

  .Botoes .BtnDetalhes{
    --max-size: 25;
    --min-size: 12;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);
    width: var(--responsive);
    min-width: var(--responsive);
  }

  .Botoes .BtnSite{
    --max-size: 25;
    --min-size: 12;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);
    width: var(--responsive);
    min-width: var(--responsive);
  }
}
</style>
