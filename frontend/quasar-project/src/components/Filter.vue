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
        />
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'

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

const MarcaOptions = ref(stringMarcas)
const ModeloOptions = ref(stringModelo)

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

export default defineComponent({
  name: 'FilterComponent',

  computed: {
    marca: {
      get () {
        return modelMarca.value
      },
      set (testeTemp) {
        modelMarca.value = testeTemp
        this.$emit('updateMarca', testeTemp)
      }
    },

    combustivel: {
      get () {
        return modelCombustivel.value
      },
      set (testeTemp) {
        modelCombustivel.value = testeTemp
        this.$emit('updateCombustivel', testeTemp)
      }
    },

    modelo: {
      get () {
        return modelModelo.value
      },
      set (testeTemp) {
        modelModelo.value = testeTemp
        this.$emit('updateModelo', testeTemp)
      }
    },

    precoMin: {
      get () {
        return ModelPrecoMin.value
      },
      set (testeTemp) {
        ModelPrecoMin.value = testeTemp
        this.$emit('updatePrecoMin', testeTemp)
      }
    },

    precoMax: {
      get () {
        return ModelPrecoMax.value
      },
      set (testeTemp) {
        ModelPrecoMax.value = testeTemp
        this.$emit('updatePrecoMax', testeTemp)
      }
    },

    anoMin: {
      get () {
        return ModelAnoMin.value
      },
      set (testeTemp) {
        ModelAnoMin.value = testeTemp
        this.$emit('updateAnoMin', testeTemp)
      }
    },

    anoMax: {
      get () {
        return ModelAnoMax.value
      },
      set (testeTemp) {
        ModelAnoMax.value = testeTemp
        this.$emit('updateAnoMax', testeTemp)
      }
    },

    quilometroMin: {
      get () {
        return ModelQuilometrosMin.value
      },
      set (testeTemp) {
        ModelQuilometrosMin.value = testeTemp
        this.$emit('updateQuilometroMin', testeTemp)
      }
    },

    quilometroMax: {
      get () {
        return ModelQuilometrosMax.value
      },
      set (testeTemp) {
        ModelQuilometrosMax.value = testeTemp
        this.$emit('updateQuilometroMax', testeTemp)
      }
    },

    ordem: {
      get () {
        return modelOrdem.value
      },
      set (testeTemp) {
        modelOrdem.value = testeTemp
        this.$emit('updateOrdem', testeTemp)
      }
    }
  },

  setup () {
    return {
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

      MarcaOptions,
      ModeloOptions,
      OrdemOptions,

      stringCombustiveis,

      filterFnMarca,
      filterFnModelo
    }
  }
})
</script>

<style>
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
