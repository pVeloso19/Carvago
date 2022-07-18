<template>
  <div class="SectionFilterOrder">
    <div class="Filtros grid-container">
        <q-select
          filled
          v-model="modelMarca"
          use-input
          :options="MarcaOptions"
          @filter="filterFnMarca"
          label="Marca"
          multiple
          emit-value
          map-options
          use-chips
          class="Filtro prim"
          bg-color='white'
          label-color='black'
        >
          <template v-slot:option="{ itemProps, opt, selected, toggleOption }">
            <q-item v-bind="itemProps">
              <q-item-section>
                <p>{{opt}}</p>
              </q-item-section>
              <q-item-section side>
                <q-toggle :model-value="selected" @update:model-value="toggleOption(opt)" />
              </q-item-section>
            </q-item>
          </template>
        </q-select>

        <q-select
          filled
          v-model="modelModelo"
          use-input
          input-debounce="0"
          label="Modelo"
          :options="ModeloOptions"
          @filter="filterFnModelo"
          behavior="menu"
          use-chips
          class="Filtro"
          bg-color='white'
          label-color='black'
        >
          <template v-slot:no-option>
            <q-item>
              <q-item-section class="text-grey">
                No results
              </q-item-section>
            </q-item>
          </template>
        </q-select>

        <q-input
          v-model.number="ModelPrecoMin"
          type="number"
          label="Preço de"
          filled
          class="Filtro"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="ModelPrecoMax"
          type="number"
          label="Preço até"
          filled
          class="Filtro"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="ModelAnoMin"
          type="number"
          label="Ano de"
          filled
          class="Filtro last"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="ModelAnoMax"
          type="number"
          label="Ano até"
          filled
          class="Filtro prim"
          bg-color='white'
          label-color='black'
        />

        <q-select
          filled
          v-model="modelCombustivel"
          :options="stringCombustiveis"
          label="Combustível"
          multiple
          emit-value
          map-options
          use-chips
          class="Filtro"
          bg-color='white'
          label-color='black'
        >
          <template v-slot:option="{ itemProps, opt, selected, toggleOption }">
            <q-item v-bind="itemProps">
              <q-item-section>
                <p>{{opt}}</p>
              </q-item-section>
              <q-item-section side>
                <q-toggle :model-value="selected" @update:model-value="toggleOption(opt)" />
              </q-item-section>
            </q-item>
          </template>
        </q-select>

        <q-input
          v-model.number="ModelQuilometrosMin"
          type="number"
          label="Quilómetros de"
          filled
          class="Filtro"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="ModelQuilometrosMax"
          type="number"
          label="Quilómetros até"
          filled
          class="Filtro last"
          bg-color='white'
          label-color='black'
        />
    </div>

    <div class="OrderSection">
      <q-separator color="blue-grey-4" inset />
      <p class="OrderTitle">Ordenar por</p>
      <q-select
          filled
          v-model="modelOrdem"
          :options="OrdemOptions"
          behavior="menu"
          class="Order"
          bg-color='white'
          label-color='black'
          @update:model-value="val => ordenaLista(val)"
        />
    </div>
  </div>

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

const stringMarcas = [
  'Google', 'Facebook', 'Twitter', 'Apple'
]

const stringCombustiveis = [
  'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
]

const stringModelo = [
  'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
]

const OrdemOptions = [
  'Mais Recentes', 'Preço: Mais Baixo', 'Preço: Mais Alto', 'KM: Mais Baixo', 'KM: Mais Alto', 'Ano: Mais Baixo', 'Ano: Mais Alto'
]

function filterFnMarca (val, update) {
  if (val === '') {
    update(() => {
      MarcaOptions.value = stringMarcas
    })
    return
  }

  update(() => {
    const needle = val.toLowerCase()
    MarcaOptions.value = stringMarcas.filter(v => v.toLowerCase().indexOf(needle) > -1)
  })
}

function filterFnModelo (val, update) {
  if (val === '') {
    update(() => {
      ModeloOptions.value = stringModelo
    })
    return
  }

  update(() => {
    const needle = val.toLowerCase()
    ModeloOptions.value = stringModelo.filter(v => v.toLowerCase().indexOf(needle) > -1)
  })
}

function ordenaLista (ordem) {
  if (ordem === 'Mais Recentes') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.ano - carro2.ano === 0) ? 1 : carro2.ano - carro1.ano
    })
  }

  if (ordem === 'Preço: Mais Baixo') {
    carros.value.sort(function (carro1, carro2) {
      return (parseFloat(carro1.preco) - parseFloat(carro2.preco) === 0) ? 1 : parseFloat(carro1.preco) - parseFloat(carro2.preco)
    })
  }

  if (ordem === 'Preço: Mais Alto') {
    carros.value.sort(function (carro1, carro2) {
      return (parseFloat(carro1.preco) - parseFloat(carro2.preco) === 0) ? 1 : parseFloat(carro2.preco) - parseFloat(carro1.preco)
    })
  }

  if (ordem === 'KM: Mais Baixo') {
    carros.value.sort(function (carro1, carro2) {
      return (parseFloat(carro1.quilometros) - parseFloat(carro2.quilometros) === 0) ? 1 : parseFloat(carro1.quilometros) - parseFloat(carro2.quilometros)
    })
  }

  if (ordem === 'KM: Mais Alto') {
    carros.value.sort(function (carro1, carro2) {
      return (parseFloat(carro1.quilometros) - parseFloat(carro2.quilometros) === 0) ? 1 : parseFloat(carro2.quilometros) - parseFloat(carro1.quilometros)
    })
  }

  if (ordem === 'Ano: Mais Baixo') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.ano - carro2.ano === 0) ? 1 : carro1.ano - carro2.ano
    })
  }

  if (ordem === 'Ano: Mais Alto') {
    carros.value.sort(function (carro1, carro2) {
      return (carro1.ano - carro2.ano === 0) ? 1 : carro2.ano - carro1.ano
    })
  }
}

const MarcaOptions = ref(stringMarcas)
const ModeloOptions = ref(stringModelo)

export default {
  name: 'IndexPage',

  components: {
    CarCard
  },

  setup () {
    const visible = ref(false)
    const showSimulatedReturnData = ref(false)
    const elemByPages = ref(10)

    onMounted(async () => {
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
        elem.preco = elem.preco.toString()
        elem.preco = elem.preco.replace(new RegExp('^(\\d{' + (elem.preco.length % 3 ? elem.preco.length % 3 : 0) + '})(\\d{3})', 'g'), '$1 $2').replace(/(\d{3})+?/gi, '$1 ').trim()

        elem.quilometros = elem.quilometros.toString()
        elem.quilometros = elem.quilometros.replace(new RegExp('^(\\d{' + (elem.quilometros.length % 3 ? elem.quilometros.length % 3 : 0) + '})(\\d{3})', 'g'), '$1 $2').replace(/(\d{3})+?/gi, '$1 ').trim()

        carros.value.push(elem)
      })

      visible.value = false
      showSimulatedReturnData.value = true
    })

    function filtrosOK (carro) {
      var preco = parseFloat(carro.preco.replace(' ', ''))
      var km = parseFloat(carro.quilometros.replace(' ', ''))

      if (modelMarca.value.length !== 0 && !modelMarca.value.includes(carro.marca)) {
        return false
      }

      if (modelCombustivel.value.length !== 0 && !modelCombustivel.value.includes(carro.combustivel)) {
        return false
      }

      if (modelModelo.value !== null && modelModelo.value !== carro.modelo) {
        return false
      }

      if (ModelPrecoMin.value !== null && parseFloat(ModelPrecoMin.value) > preco) {
        return false
      }

      if (ModelPrecoMax.value !== null && parseFloat(ModelPrecoMax.value) < preco) {
        return false
      }

      if (ModelAnoMin.value !== null && parseInt(ModelAnoMin.value) > parseInt(carro.ano)) {
        return false
      }

      if (ModelAnoMax.value !== null && parseInt(ModelAnoMax.value) < parseInt(carro.ano)) {
        return false
      }

      if (ModelQuilometrosMin.value !== null && parseFloat(ModelQuilometrosMin.value) > km) {
        return false
      }

      if (ModelQuilometrosMin.value !== null && parseFloat(ModelQuilometrosMin.value) < km) {
        return false
      }

      return true
    }

    const pages = computed(() => {
      var list = []
      var i = 0

      list.push([])

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
      modelOrdem: ref('Mais Recentes'),

      MarcaOptions,
      ModeloOptions,
      OrdemOptions,

      stringCombustiveis,

      filterFnMarca,
      filterFnModelo
    }
  }
}

</script>

<style>
.Loding1{
  height: 55vh;
}

.Loding2{
  background-color: white;
}

.Filtros{
  margin: 0px 0px 0px 0px;
  padding: 0px 0px 0px 0px;
  width: 100%;

  display: inline-block;
}

.Filtro{
  margin: 0px 0px 0px 0px;
  padding: 0px 0px 0px 0px;

  margin-top: 10px;
  margin-right: 10px;
}

.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto auto;
}

.prim{
  margin-left: 50px;
}

.last{
  margin-right: 50px;
}

.OrderSection{
  margin-top: 20px;
}

.Order{
  margin-top: 10px;
  margin-left: 45px;
  margin-right: 45px;
}

.OrderTitle{
  margin-top: 10px;
  margin-bottom: 0px;
  margin-left: 45px;
  color: rgba(100, 100, 100, 0.8);
}

.SectionFilterOrder{
  background-color: rgba(197, 197, 197, 0.8);
  padding-bottom: 20px;
  padding-top: 10px;
}
</style>
