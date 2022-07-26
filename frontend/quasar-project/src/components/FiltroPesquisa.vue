<template>
  <div class="SectionFilterOrder">
    <div class="Filtros grid-container">
        <q-select
          filled
          v-model="marca"
          use-input
          :options="MarcaOptions"
          option-label="name"
          @filter="filterFnMarca"
          label="Marca"
          multiple
          emit-value
          map-options
          use-chips
          @update:model-value="val => modelo = null"
          class="Filtro prim"
          bg-color='white'
          label-color='black'
        >
          <template v-slot:option="{ itemProps, opt, selected, toggleOption }">
            <q-item v-bind="itemProps">
              <q-item-section>
                <p>{{opt.name}}</p>
              </q-item-section>
              <q-item-section side>
                <q-toggle :model-value="selected" @update:model-value="toggleOption(opt)" />
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
          v-if="marca.length==1"
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
          class="Filtro"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="precoMax"
          type="number"
          label="Preço até"
          filled
          class="Filtro"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="anoMin"
          type="number"
          label="Ano de"
          filled
          class="Filtro last"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="anoMax"
          type="number"
          label="Ano até"
          filled
          class="Filtro prim"
          bg-color='white'
          label-color='black'
        />

        <q-select
          filled
          v-model="combustivel"
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
          v-model.number="quilometroMin"
          type="number"
          label="Quilómetros de"
          filled
          class="Filtro"
          bg-color='white'
          label-color='black'
        />

        <q-input
          v-model.number="quilometroMax"
          type="number"
          label="Quilómetros até"
          filled
          class="Filtro last"
          bg-color='white'
          label-color='black'
        />
    </div>

    <div class="OrderSectionPesquisa">
      <q-separator color="blue-grey-4" inset />
      <p class="OrderTitlePesquisa">Ordenar por</p>
      <div class='row'>
        <q-select
            filled
            v-model="ordem"
            :options="OrdemOptions"
            behavior="menu"
            class="OrderPesquisa"
            bg-color='white'
            label-color='black'
          />
        <q-btn color="primary" @click="$emit('Pesquisa')" class="ButtonPesquisa">
          <div class="row items-center no-wrap">
            <q-icon name="search" color="white" />
            <div class="text-center Pesquisar" style="margin-left:5px;">
              Pesquisar
            </div>
          </div>
        </q-btn>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, defineComponent, ref } from 'vue'

import axios from 'axios'

let stringMarcas = [
  'Google', 'Facebook', 'Twitter', 'Apple'
]

const stringCombustiveis = [
  'Diesel', 'Eléctrico', 'Gasolina', 'GPL', 'Híbrido (Diesel)', 'Híbrido (Gasolina)', 'Hidrogénio'
]

let stringModelo = [
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

export default defineComponent({
  name: 'FilterComponent',

  props: {
    modelMarca: {
      type: Array,
      default: () => []
    },

    modelCombustivel: {
      type: Array,
      default: () => []
    },

    modelModelo: {
      type: String,
      default: null
    },

    ModelPrecoMin: {
      type: Number,
      default: null
    },

    ModelPrecoMax: {
      type: Number,
      default: null
    },

    ModelAnoMin: {
      type: Number,
      default: null
    },
    ModelAnoMax: {
      type: Number,
      default: null
    },

    ModelQuilometrosMin: {
      type: Number,
      default: null
    },

    ModelQuilometrosMax: {
      type: Number,
      default: null
    },

    modelOrdem: {
      type: String,
      default: 'Mais Recentes'
    }
  },

  computed: {
    marca: {
      get () {
        return this.modelMarca
      },
      set (testeTemp) {
        this.$emit('updateMarca', testeTemp)
      }
    },

    combustivel: {
      get () {
        return this.modelCombustivel
      },
      set (testeTemp) {
        this.$emit('updateCombustivel', testeTemp)
      }
    },

    modelo: {
      get () {
        return this.modelModelo
      },
      set (testeTemp) {
        this.$emit('updateModelo', testeTemp)
      }
    },

    precoMin: {
      get () {
        return this.ModelPrecoMin
      },
      set (testeTemp) {
        this.$emit('updatePrecoMin', testeTemp)
      }
    },

    precoMax: {
      get () {
        return this.ModelPrecoMax
      },
      set (testeTemp) {
        this.$emit('updatePrecoMax', testeTemp)
      }
    },

    anoMin: {
      get () {
        return this.ModelAnoMin
      },
      set (testeTemp) {
        this.$emit('updateAnoMin', testeTemp)
      }
    },

    anoMax: {
      get () {
        return this.ModelAnoMax
      },
      set (testeTemp) {
        this.$emit('updateAnoMax', testeTemp)
      }
    },

    quilometroMin: {
      get () {
        return this.ModelQuilometrosMin
      },
      set (testeTemp) {
        this.$emit('updateQuilometroMin', testeTemp)
      }
    },

    quilometroMax: {
      get () {
        return this.ModelQuilometrosMax
      },
      set (testeTemp) {
        this.$emit('updateQuilometroMax', testeTemp)
      }
    },

    ordem: {
      get () {
        return this.modelOrdem
      },
      set (testeTemp) {
        this.$emit('updateOrdem', testeTemp)
      }
    }
  },

  setup () {
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

    return {
      MarcaOptions,
      ModeloOptions,
      OrdemOptions,

      stringCombustiveis,

      filterFnMarca,
      filterFnModelo
    }
  },
  watch: {
    async marca (newValue, oldValue) {
      if (newValue.length === 1) {
        const userJogos = await axios({
          method: 'get',
          url: 'https://parallelum.com.br/fipe/api/v2/cars/brands/' + newValue[0].code + '/models'
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
})
</script>

<style>
.Filtros{
  margin: 0px 0px 0px 0px;
  padding: 0px 0px 0px 0px;
  width: 100%;

  padding-right: 50px;
  padding-left: 40px;

  display: inline-block;
}

.Filtro{
  margin: 0px 0px 0px 0px;
  padding: 0px 0px 0px 0px;

  margin-top: 10px;
  margin-left: 10px;
}

.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto auto;
}

.OrderSectionPesquisa{
  margin-top: 20px;
}

.OrderPesquisa{
  margin-top: 10px;
  margin-left: 45px;

  width: 500px;
}

.ButtonPesquisa{
  margin-top: 10px;
  max-width: 200px;
  margin-left: 45px;
  margin-right: 45px;
}

.OrderTitlePesquisa{
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

@media (max-width: 1071px) {
  .OrderPesquisa{
    width: 1000px;
    margin-right: 45px;
  }

  .ButtonPesquisa{
    width: 1000px;
    max-width: 1000px;
  }
}

@media (max-width: 780px) {
  .grid-container {
    grid-template-columns: 26% 24% 24% 26%;
  }

  .Filtros{
    padding-right: 20px;
    padding-left: 10px;
  }
}

@media (max-width: 500px) {
  .grid-container {
    grid-template-columns: 34% 32% 34%;
  }

  .Filtros{
    padding-right: 10px;
    padding-left: 0px;
  }
}

@media (max-width: 235px) {
  .Pesquisar{
    display: none
  }
}
</style>
