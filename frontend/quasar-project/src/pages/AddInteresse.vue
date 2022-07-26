<template>
  <div class="">
    <div class="">
        <q-select
          filled
          v-model="marca"
          option-label="name"
          use-input
          input-debounce="0"
          label="Marca"
          use-chips
          :options="MarcaOptions"
          @filter="filterFnMarca"
          @update:model-value="val => modelo = null"
          behavior="menu"
          class=""
          bg-color='white'
          label-color='black'
        >
          <template v-slot:option="{ itemProps, opt }">
            <q-item v-bind="itemProps">
              <q-item-section>
                <p>{{opt.name}}</p>
              </q-item-section>
            </q-item>
          </template>
        </q-select>

        <q-select
          filled
          v-model="modelo"
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
          v-if="marca!==null"
        >
          <template v-slot:no-option>
            <q-item>
              <q-item-section class="text-grey">
                No results
              </q-item-section>
            </q-item>
          </template>
        </q-select>

        <q-select
          filled
          v-model="modelo"
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
          disable
          v-else
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
          v-model.number="precoMin"
          type="number"
          label="Preço de"
          filled
          class=""
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="precoMax"
          type="number"
          label="Preço até"
          filled
          class=""
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="anoMin"
          type="number"
          label="Ano de"
          filled
          class=""
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="anoMax"
          type="number"
          label="Ano até"
          filled
          class=""
          bg-color='white'
          label-color='black'
        />

        <q-select
          filled
          v-model="combustivel"
          use-chips
          input-debounce="0"
          label="Combustível"
          :options="CombustivelOptions"
          behavior="menu"
          class=""
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
          v-model.number="quilometroMin"
          type="number"
          label="Quilómetros de"
          filled
          class=""
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="quilometroMax"
          type="number"
          label="Quilómetros até"
          filled
          class=""
          bg-color='white'
          label-color='black'
        />
    </div>

    <q-btn push color="primary" label="Adicionar" @click="addInteresse()"/>
  </div>
</template>

<script>

import { onMounted, ref } from 'vue'

import axios from 'axios'

import URL from '../url.js'

let stringMarcas = [
  'Google', 'Facebook', 'Twitter', 'Apple'
]

let stringModelo = [
  'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
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
    MarcaOptions.value = stringMarcas.filter(v => v.name.toLowerCase().indexOf(needle) > -1)
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

const MarcaOptions = ref(stringMarcas)
const ModeloOptions = ref(stringModelo)

const marca = ref(null)
const modelo = ref(null)
const combustivel = ref(null)
const precoMin = ref(null)
const precoMax = ref(null)
const anoMin = ref(null)
const anoMax = ref(null)
const quilometroMin = ref(null)
const quilometroMax = ref(null)

export default {
  name: 'AddInteressePage',

  setup () {
    const CombustivelOptions = [
      'Diesel', 'Eléctrico', 'Gasolina', 'GPL', 'Híbrido (Diesel)', 'Híbrido (Gasolina)', 'Hidrogénio'
    ]

    onMounted(async () => {
      const userJogos = await axios({
        method: 'get',
        url: 'https://parallelum.com.br/fipe/api/v2/cars/brands'
      })

      const userJogosData = await userJogos.data

      stringMarcas = []
      userJogosData.forEach((elem) => {
        if (elem.name === 'VW - VolksWagen') {
          elem.name = 'VW'
        }
        stringMarcas.push(elem)
      })
    })

    async function addInteresse () {
      const id = sessionStorage.getItem('IdentificadorCarvago')

      const ma = (marca.value === null) ? '' : marca.value.name
      const mo = (modelo.value === null) ? '' : modelo.value
      const c = (combustivel.value === null) ? '' : combustivel.value
      const pmin = (precoMin.value === null) ? '' : precoMin.value
      const pmax = (precoMax.value === null) ? '' : precoMax.value
      const amin = (anoMin.value === null) ? '' : anoMin.value
      const amax = (anoMax.value === null) ? '' : anoMax.value
      const qmin = (quilometroMin.value === null) ? '' : quilometroMin.value
      const qmax = (quilometroMax.value === null) ? '' : quilometroMax.value

      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/AddInteresse',
        params: { ID: id, Marca: ma, Modelo: mo, AnoMinimo: amin, AnoMaximo: amax, PrecoMinimo: pmin, PrecoMaximo: pmax, Combustivel: c, KMMinimo: qmin, KMMaximo: qmax }
      })

      let res = await userJogos.data
      res = res.resultado

      if (res) {
        marca.value = null
        modelo.value = null
        combustivel.value = null
        precoMin.value = null
        precoMax.value = null
        anoMin.value = null
        anoMax.value = null
        quilometroMin.value = null
        quilometroMax.value = null
      }
    }

    return {
      MarcaOptions,
      ModeloOptions,
      CombustivelOptions,

      marca,
      modelo,
      combustivel,
      precoMin,
      precoMax,
      anoMin,
      anoMax,
      quilometroMin,
      quilometroMax,

      filterFnMarca,
      filterFnModelo,

      addInteresse
    }
  },
  watch: {
    async marca (newValue, oldValue) {
      if (newValue !== null) {
        const userJogos = await axios({
          method: 'get',
          url: 'https://parallelum.com.br/fipe/api/v2/cars/brands/' + newValue.code + '/models'
        })

        const userJogosData = await userJogos.data

        var dict = {}
        userJogosData.forEach((elem) => {
          dict[elem.name.split(' ')[0]] = ''
        })

        stringModelo = []
        for (var key in dict) {
          stringModelo.push(key)
        }
      }
    }
  }
}

</script>

<style>

</style>
