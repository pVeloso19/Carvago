<template>

  <Filtros
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

      v-on:updateMarca="modelMarca = $event; mudou=true"
      v-on:updateCombustivel="modelCombustivel = $event; mudou=true"
      v-on:updateModelo="modelModelo = $event; mudou=true"
      v-on:updatePrecoMin="ModelPrecoMin = $event; mudou=true"
      v-on:updatePrecoMax="ModelPrecoMax = $event; mudou=true"
      v-on:updateAnoMin="ModelAnoMin = $event; mudou=true"
      v-on:updateAnoMax="ModelAnoMax = $event; mudou=true"
      v-on:updateQuilometroMin="ModelQuilometrosMin = $event; mudou=true"
      v-on:updateQuilometroMax="ModelQuilometrosMax = $event; mudou=true"
      v-on:updateOrdem="modelOrdem = $event; mudou=true"

      :CarrosDestaques="carrosDestaques"

      v-on:Pesquisa="getCarros()"
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
              :Avaliar="false"
              v-for="c in carros"
              :key="c"
            />
          </div>

          <div class="q-pa-lg flex flex-center" v-if="maxPages>1">
            <q-pagination
              v-model="current"
              color="primary"
              :max="maxPages"
              max-pages="4"
              boundary-links
              direction-links
            />
          </div>
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

import { onMounted, ref } from 'vue'
import CarCard from 'components/CarCard.vue'
import Filtros from 'components/FilterHomePage.vue'

import axios from 'axios'

import URL from '../url.js'

const carros = ref([])

const mudou = ref(false)

const visible = ref(false)
const showSimulatedReturnData = ref(false)

const current = ref(1)
const maxPages = ref(0)

const modelMarca = ref([])
const modelCombustivel = ref([])
const modelModelo = ref(null)
const ModelPrecoMin = ref(null)
const ModelPrecoMax = ref(null)
const ModelAnoMin = ref(null)
const ModelAnoMax = ref(null)
const ModelQuilometrosMin = ref(null)
const ModelQuilometrosMax = ref(null)
const modelOrdem = ref('Mais Recentes')

const carrosDestaques = ref([])

const getCarros = async () => {
  maxPages.value = 0

  visible.value = true
  showSimulatedReturnData.value = false

  carros.value = []

  if (mudou.value) {
    current.value = 1
    mudou.value = false
  }

  const marcasTemp = []
  modelMarca.value.forEach((elem) => {
    marcasTemp.push(elem.name.toLowerCase())
  })

  const ma = (marcasTemp.length <= 0) ? '' : marcasTemp.toString()
  const c = (modelCombustivel.value.length <= 0) ? '' : modelCombustivel.value.toString()
  const mo = (modelModelo.value === null) ? '' : modelModelo.value
  const pmin = (ModelPrecoMin.value === null) ? '' : ModelPrecoMin.value
  const pmax = (ModelPrecoMax.value === null) ? '' : ModelPrecoMax.value
  const amin = (ModelAnoMin.value === null) ? '' : ModelAnoMin.value
  const amax = (ModelAnoMax.value === null) ? '' : ModelAnoMax.value
  const qmin = (ModelQuilometrosMin.value === null) ? '' : ModelQuilometrosMin.value
  const qmax = (ModelQuilometrosMax.value === null) ? '' : ModelQuilometrosMax.value
  const o = modelOrdem.value

  const id = -1 // sessionStorage.getItem('IdentificadorCarvago')

  const userJogos = await axios({
    method: 'get',
    url: URL.URL + '/AllCarsAvailable',
    params: { ID: id, Marca: ma, Modelo: mo, AnoMinimo: amin, AnoMaximo: amax, PrecoMinimo: pmin, PrecoMaximo: pmax, Combustivel: c, KMMinimo: qmin, KMMaximo: qmax, Pagina: current.value, Ordem: o }
  })

  let userJogosData = await userJogos.data
  maxPages.value = userJogosData.paginas
  userJogosData = userJogosData.carros

  carrosDestaques.value = []
  let i = 0
  userJogosData.forEach((elem) => {
    carros.value.push(elem)
    if (i < 4) {
      carrosDestaques.value.push(elem)
      i++
    }
  })

  visible.value = false
  showSimulatedReturnData.value = true
}

export default {
  name: 'IndexPage',

  components: {
    CarCard,
    Filtros
  },

  setup () {
    onMounted(async () => {
      getCarros()
    })

    return {
      carros,
      visible,
      showSimulatedReturnData,
      current,
      maxPages,

      modelMarca,
      modelCombustivel,
      modelModelo,
      ModelPrecoMin,
      ModelPrecoMax,
      ModelAnoMin,
      ModelAnoMax,
      ModelQuilometrosMin,
      ModelQuilometrosMax,
      modelOrdem,

      getCarros,
      carrosDestaques,

      mudou
    }
  },
  watch: {
    current (newValue, oldValue) {
      if (newValue !== oldValue) {
        getCarros()
      }
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
