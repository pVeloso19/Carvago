<template>
  <div class="PaginaInicial">
    <div class="PaginaInicialZonaImagens">
      <q-carousel
        animated
        v-model="slide"
        infinite
        :autoplay="true"
        transition-prev="slide-right"
        transition-next="slide-left"
        height="calc(100vh - 110px)"
        class="ImagemIndex"
      >
        <q-carousel-slide
          :name="i-1"
          v-for="i in CarrosDestaques.length"
          :key="i"
          :img-src="CarrosDestaques[i-1].link_foto"
        >
          <div class="absolute-bottom custom-caption">
            <div class="text-h2 TituloIndex">{{CarrosDestaques[i-1].titulo}}</div>
            <div class="text-subtitle1 SubtituloIndex">{{PrecoString(i-1)}} EUR</div>
          </div>
          <div>
            <p class="TitHP">Bem vindo</p>
            <q-btn color="primary" label="Procurar um veículo" class="ProcurarCarroHP" @click="goTo('carros')"/>
            <q-btn color="green" label="Adicionar Interesses" class="AddInteresseHP" @click="goTo('add')"/>
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>

<script>

import { onMounted, ref } from 'vue'

import axios from 'axios'

import URL from '../url.js'

export default {
  name: 'InicioPage',

  setup () {
    const CarrosDestaques = ref([])

    onMounted(async () => {
      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/ImagensCars'
      })

      const userJogosData = await userJogos.data
      CarrosDestaques.value = userJogosData.images
    })

    function PrecoString (index) {
      let teste = this.CarrosDestaques[index].preco.toString()
      teste = teste.replace(new RegExp('^(\\d{' + (teste.length % 3 ? teste.length % 3 : 0) + '})(\\d{3})', 'g'), '$1 $2').replace(/(\d{3})+?/gi, '$1 ').trim()
      return teste
    }

    return {
      goTo (path) {
        window.location = '#/' + path
      },
      slide: ref(1),
      CarrosDestaques,
      PrecoString
    }
  }
}

</script>

<style>
.PaginaInicial{
  display: grid;
  grid-template-columns: 30px auto 30px;
  grid-template-areas:
  "NADA Imagens";

  margin-top: 30px;
  margin-bottom: 30px;
}

.PaginaInicialZonaImagens{
  grid-area: Imagens;
}

.custom-caption {
  text-align: center;
  padding: 12px;
  color: white;
  background-color: rgba(0, 0, 0, .5);
}

.SubtituloIndex {
  color: #FFB7D0;
}

.TituloIndex {
  font-size: 30px;
}

.ProcurarCarroHP {
  margin-right: 30px;
}

.TitHP{
  font-size: 80px;
  background-color: rgba(0, 0, 0, .5);
  max-width: 410px;
  color: white;
  font-weight: bold;
  border-radius: 10px;
  padding-left: 5px;

  text-align: center
}

@media (max-width: 510px) {
  .TitHP{
    font-size: 70px;
  }

  .ProcurarCarroHP {
    margin-bottom: 15px;
  }
}

@media (max-width: 450px) {
  .TitHP{
    font-size: 60px;
  }
}

@media (max-width: 385px) {
  .TitHP{
    font-size: 40px;
  }
}

@media (max-width: 315px) {
  .TitHP{
    font-size: 30px;
  }

  .ProcurarCarroHP, .AddInteresseHP {
    font-size: 12px;
  }
}

@media (max-width: 296px) {
  .ProcurarCarroHP, .AddInteresseHP {
    font-size: 9px;
  }
}

@media (max-width: 250px) {
  .TitHP{
    font-size: 20px;
  }
}
</style>
