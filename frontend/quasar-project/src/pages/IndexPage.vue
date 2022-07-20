<template>

  <Filtros
      v-if="maxPages > 0"

      :modelMarca="modelMarca"
      :modelCombustivel="modelCombustivel"
      :modelModelo="modelModelo"
      :ModelPrecoMin="ModelPrecoMin"
      :ModelPrecoMax="ModelPrecoMax"
      :ModelAnoMin="ModelAnoMin"
      :ModelAnoMax="ModelAnoMax"
      :ModelQuilometrosMin="ModelQuilometrosMin"
      :ModelQuilometrosMax="ModelQuilometrosMax"
      :modelOrdem="modelOrdem"

      v-on:updateMarca="modelMarca = $event"
      v-on:updateCombustivel="modelCombustivel = $event"
      v-on:updateModelo="modelModelo = $event"
      v-on:updatePrecoMin="ModelPrecoMin = $event"
      v-on:updatePrecoMax="ModelPrecoMax = $event"
      v-on:updateAnoMin="ModelAnoMin = $event"
      v-on:updateAnoMax="ModelAnoMax = $event"
      v-on:updateQuilometroMin="ModelQuilometrosMin = $event"
      v-on:updateQuilometroMax="ModelQuilometrosMax = $event"
      v-on:updateOrdem="modelOrdem = $event"

      v-on:Ordena="ordenaLista($event)"
    />

  <q-card class="bg-grey-3 relative-position Loding1">
    <q-card-section class="Loding2">
      <transition
        appear
        enter-active-class="animated fadeIn"
        leave-active-class="animated fadeOut"
      >
        <div class="Carros">
          <div class="Carro">
            <CarCard
              :ID="c.id"
              :Anunciante="c.anunciante"
              :Marca="c.marca"
              :Modelo="c.modelo"
              :Versao="c.versao"
              :Combustivel="c.combustivel"
              :Mes_Registo="c.mes_registo"
              :Ano="c.ano"
              :Quilometros="c.quilometros"
              :Cilindrada="c.cilindrada"
              :Potencia="c.potencia"
              :Cor="c.cor"
              :Tipo_Cor="c.tipo_cor"
              :Tipo_Caixa="c.tipo_caixa"
              :Num_Portas="c.num_portas"
              :Origem="c.origem"
              :Condicao="c.condicao"
              :Preco="c.preco"
              :Links_foto="c.link_foto"
              :Titulo="c.titulo"
              :Link_anuncio="c.link_anuncio"
              :Fonte="c.fonte"
              :Favorito="c.favorito"
              v-for="c in pages[current-1]"
              :key="c"
            />
          </div>

          <div class="q-pa-lg flex flex-center" v-if="maxPages>1">
            <q-pagination
              v-model="current"
              color="purple"
              :max="maxPages"
              max-pages="10"
              boundary-links
              direction-links
            />
          </div>

          <NoContent v-if="maxPages<1 && !visible" />
        </div>
      </transition>
    </q-card-section>

    <q-inner-loading
      :showing="visible"
      label="Carregar..."
      label-class="text-teal"
      label-style="font-size: 1.1em"
    />
  </q-card>
</template>

<script>

import { computed, onMounted, ref } from 'vue'
import CarCard from 'components/CarCard.vue'
import Filtros from 'components/Filter.vue'
import NoContent from 'components/EmptyPage.vue'

import axios from 'axios'

import URL from '../url.js'

const carros = ref([])

const modelMarca = ref([])
const modelCombustivel = ref([])
const modelModelo = ref(null)
const ModelPrecoMin = ref(null)
const ModelPrecoMax = ref(null)
const ModelAnoMin = ref(null)
const ModelAnoMax = ref(null)
const ModelQuilometrosMin = ref(null)
const ModelQuilometrosMax = ref(null)

function ordenaLista (ordem) {
  if (ordem === 'Mais Recentes') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.ano - carro2.ano === 0) ? 1 : carro2.ano - carro1.ano
    })
    return
  }

  if (ordem === 'Preço: Mais Baixo') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.preco - carro2.preco === 0) ? 1 : carro1.preco - carro2.preco
    })
    return
  }

  if (ordem === 'Preço: Mais Alto') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.preco - carro2.preco === 0) ? 1 : carro2.preco - carro1.preco
    })
    return
  }

  if (ordem === 'KM: Mais Baixo') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.quilometros - carro2.quilometros === 0) ? 1 : carro1.quilometros - carro2.quilometros
    })
    return
  }

  if (ordem === 'KM: Mais Alto') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.quilometros - carro2.quilometros === 0) ? 1 : carro2.quilometros - carro1.quilometros
    })
    return
  }

  if (ordem === 'Ano: Mais Baixo') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.ano - carro2.ano === 0) ? 1 : carro1.ano - carro2.ano
    })
    return
  }

  if (ordem === 'Ano: Mais Alto') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.ano - carro2.ano === 0) ? 1 : carro2.ano - carro1.ano
    })
  }
}

export default {
  name: 'IndexPage',

  components: {
    CarCard,
    Filtros,
    NoContent
  },

  setup () {
    const visible = ref(false)
    const showSimulatedReturnData = ref(false)
    const elemByPages = ref(10)

    onMounted(async () => {
      carros.value = []

      visible.value = true
      showSimulatedReturnData.value = false

      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/AllCars',
        params: { ID: 1, marca: 'ford', modelo: 'focus' }
      })

      let userJogosData = await userJogos.data
      userJogosData = userJogosData.carros

      userJogosData.forEach((elem) => {
        carros.value.push(elem)
      })

      visible.value = false
      showSimulatedReturnData.value = true
    })

    function filtrosOK (carro) {
      if (modelMarca.value.length !== 0 && !modelMarca.value.includes(carro.marca)) {
        return false
      }

      if (modelCombustivel.value.length !== 0 && !modelCombustivel.value.includes(carro.combustivel)) {
        return false
      }

      if (modelModelo.value !== null && modelModelo.value !== '' && modelModelo.value !== carro.modelo) {
        return false
      }

      if (ModelPrecoMin.value !== null && ModelPrecoMin.value !== '' && ModelPrecoMin.value > carro.preco) {
        return false
      }

      if (ModelPrecoMax.value !== null && ModelPrecoMax.value !== '' && ModelPrecoMax.value < carro.preco) {
        return false
      }

      if (ModelAnoMin.value !== null && ModelAnoMin.value !== '' && ModelAnoMin.value > carro.ano) {
        return false
      }

      if (ModelAnoMax.value !== null && ModelAnoMax.value !== '' && ModelAnoMax.value < carro.ano) {
        return false
      }

      if (ModelQuilometrosMin.value !== null && ModelQuilometrosMin.value !== '' && ModelQuilometrosMin.value > carro.quilometros) {
        return false
      }

      if (ModelQuilometrosMin.value !== null && ModelQuilometrosMin.value !== '' && ModelQuilometrosMin.value < carro.quilometros) {
        return false
      }

      return true
    }

    const pages = computed(() => {
      var list = []
      var i = 0

      if (carros.value.length > 0) {
        list.push([])
      }

      var pag = 0
      carros.value.forEach(function (g) {
        if (filtrosOK(g)) {
          list[pag].push(g)

          i += 1
          i = i % elemByPages.value

          if (i === 0) {
            pag++
            list.push([])
          }
        }
      })

      return list
    })

    const maxPages = computed(() => {
      return pages.value.length
    })

    return {
      carros,
      visible,
      showSimulatedReturnData,
      current: ref(1),
      maxPages,
      pages,

      ordenaLista,

      modelMarca,
      modelCombustivel,
      modelModelo,
      ModelPrecoMin,
      ModelPrecoMax,
      ModelAnoMin,
      ModelAnoMax,
      ModelQuilometrosMin,
      ModelQuilometrosMax,
      modelOrdem: ref('Mais Recentes')
    }
  }
}

</script>

<style>
.Loding1{
  height: calc(100vh - 50px);
}

.Loding2{
  background-color: white;
}
</style>
