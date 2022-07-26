<template>
  <div class="ContainerFiltrosIndexPage">

    <p class="MarcaTitIndex">Marca</p>
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
      bg-color='white'
      label-color='black'
      class="MarcaSelectIndex"
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

    <p class="ModeloTitIndex">Modelo</p>
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
      bg-color='white'
      label-color='black'
      v-if="marca.length==1"
      class="ModeloSelectIndex"
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
      bg-color='white'
      label-color='black'
      disable
      v-else
      class="ModeloSelectIndex"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
          No results
          </q-item-section>
        </q-item>
      </template>
    </q-select>

    <p class="PrecoTitIndex">Preço</p>
    <q-input
      v-model.number="precoMin"
      type="number"
      label="de"
      filled
      bg-color='white'
      label-color='black'
      class="PrecoMinSelectIndex"
    />

    <q-input
      v-model.number="precoMax"
      type="number"
      label="até"
      filled
      bg-color='white'
      label-color='black'
      class="PrecoMaxSelectIndex"
    />

    <p class="AnoTitIndex">Ano</p>
    <q-input
      v-model.number="anoMin"
      type="number"
      label="de"
      filled
      bg-color='white'
      label-color='black'
      class="AnoMinSelectIndex"
    />

    <q-input
      v-model.number="anoMax"
      type="number"
      label="até"
      filled
      bg-color='white'
      label-color='black'
      class="AnoMaxSelectIndex"
    />

    <p class="CombustivelTitIndex">Combustível</p>
    <q-select
      filled
      v-model="combustivel"
      :options="stringCombustiveis"
      label="Combustível"
      multiple
      emit-value
      map-options
      use-chips
      bg-color='white'
      label-color='black'
      class="CombustivelSelectIndex"
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

    <p class="KmTitIndex">Quilómetros</p>
    <q-input
      v-model.number="quilometroMin"
      type="number"
      label="de"
      filled
      bg-color='white'
      label-color='black'
      class="KmMinSelectIndex"
    />

    <q-input
      v-model.number="quilometroMax"
      type="number"
      label="até"
      filled
      bg-color='white'
      label-color='black'
      class="KmMaxSelectIndex"
    />

    <q-select
      filled
      v-model="ordem"
      :options="OrdemOptions"
      behavior="menu"
      bg-color='white'
      label-color='black'
      class="OrdemSelectIndex"
    />

    <q-btn
      color="primary"
      @click="$emit('Pesquisa')"
      class="PesquisarIndex"
    >
      <div class="row items-center no-wrap">
        <q-icon name="search" color="white" />
        <div class="text-center TextPesquisarIndex" style="margin-left:5px;">
          Pesquisar Agora
        </div>
      </div>
    </q-btn>

    <q-carousel
      animated
      v-model="slide"
      infinite
      :autoplay="true"
      transition-prev="slide-right"
      transition-next="slide-left"
      height="360px"
      class="ImagemIndex"
    >
      <q-carousel-slide
        :name="i-1"
        v-for="i in CarrosDestaques.length"
        :key="i"
        :img-src="CarrosDestaques[i-1].link_foto[0]"
      >
        <div class="absolute-bottom custom-caption">
          <div class="text-h2 TituloIndex">{{CarrosDestaques[i-1].titulo}}</div>
          <div class="text-subtitle1 SubtituloIndex">{{PrecoString(i-1)}} EUR</div>
        </div>
      </q-carousel-slide>
    </q-carousel>

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
    },

    CarrosDestaques: {
      type: Array,
      default: () => []
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

    function PrecoString (index) {
      let teste = this.CarrosDestaques[index].preco.toString()
      teste = teste.replace(new RegExp('^(\\d{' + (teste.length % 3 ? teste.length % 3 : 0) + '})(\\d{3})', 'g'), '$1 $2').replace(/(\d{3})+?/gi, '$1 ').trim()
      return teste
    }

    return {
      MarcaOptions,
      ModeloOptions,
      OrdemOptions,

      stringCombustiveis,

      filterFnMarca,
      filterFnModelo,
      slide: ref(1),
      PrecoString
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
.ContainerFiltrosIndexPage{
  background-color: rgba(197, 197, 197, 0.8);
  padding-top: 30px;
  padding-bottom: 20px;

  display: grid;
  grid-template-columns: 12% 10% 20px 10% 10% auto;
  grid-template-rows: 22px 70px 22px 70px 22px 90px 70px;
  grid-template-areas:
  "MarcaTit MarcaTit NADA ModeloTit ModeloTit Imagem"
  "MarcaSelect MarcaSelect NADA ModeloSelect ModeloSelect Imagem"
  "PrecoTit PrecoTit NADA AnoTit AnoTit Imagem"
  "PrecoMinSelect PrecoMaxSelect NADA AnoMinSelect AnoMaxSelect Imagem"
  "CombustivelTit CombustivelTit NADA KmTit KmTit Imagem"
  "CombustivelSelect CombustivelSelect NADA KmMinSelect KmMaxSelect Imagem"
  "OrdemSelect OrdemSelect NADA Pesquisar Pesquisar Imagem"
}

.MarcaTitIndex{
  grid-area: MarcaTit;
  margin: 0px;
  padding: 0px;

  font-weight: bold;
  margin-left: 50px;
}

.MarcaSelectIndex{
  grid-area: MarcaSelect;
  margin: 0px;
  padding: 0px;
  margin-left: 50px;
}

.ModeloTitIndex{
  grid-area: ModeloTit;
  margin: 0px;
  padding: 0px;

  font-weight: bold;
}

.ModeloSelectIndex{
  grid-area: ModeloSelect;
  margin: 0px;
  padding: 0px;
}

.PrecoTitIndex{
  grid-area: PrecoTit;
  margin: 0px;
  padding: 0px;

  font-weight: bold;
  margin-left: 50px;
}

.PrecoMinSelectIndex{
  grid-area: PrecoMinSelect;
  margin: 0px;
  padding: 0px;

  margin-left: 50px;
}

.PrecoMaxSelectIndex{
  grid-area: PrecoMaxSelect;
  margin: 0px;
  padding: 0px;

  margin-left: 10px;
}

.AnoTitIndex{
  grid-area: AnoTit;
  margin: 0px;
  padding: 0px;

  font-weight: bold;
}

.AnoMinSelectIndex{
  grid-area: AnoMinSelect;
  margin: 0px;
  padding: 0px;

  margin-right: 5px;
}

.AnoMaxSelectIndex{
  grid-area: AnoMaxSelect;
  margin: 0px;
  padding: 0px;

  margin-left: 5px;
}

.KmTitIndex{
  grid-area: KmTit;
  margin: 0px;
  padding: 0px;

  font-weight: bold;
}

.KmMinSelectIndex{
  grid-area: KmMinSelect;
  margin: 0px;
  padding: 0px;

  margin-right: 5px;
}

.KmMaxSelectIndex{
  grid-area: KmMaxSelect;
  margin: 0px;
  padding: 0px;

  margin-left: 5px;
}

.CombustivelTitIndex{
  grid-area: CombustivelTit;
  margin: 0px;
  padding: 0px;

  font-weight: bold;
  margin-left: 50px;
}

.CombustivelSelectIndex{
  grid-area: CombustivelSelect;
  margin: 0px;
  padding: 0px;
  margin-left: 50px;
}

.OrdemSelectIndex{
  grid-area: OrdemSelect;
  margin: 0px;
  padding: 0px;
  margin-left: 50px;
}

.PesquisarIndex{
  grid-area: Pesquisar;
  margin: 0px;
  padding: 0px;

  height: 55px;
}

.ImagemIndex{
  grid-area: Imagem;
  margin-left: 30px;
  max-width: calc(100% - 50px);
}

@media (max-width: 1100px) {
  .ContainerFiltrosIndexPage{
    grid-template-columns: 17% 15% 20px 15% 15% auto;
  }
}

@media (max-width: 800px) {
  .ContainerFiltrosIndexPage{
    grid-template-columns: 22% 20% 20px 20% 20% auto;
  }

  .ImagemIndex{
    display: none;
  }
}

@media (max-width: 720px) {
  .ContainerFiltrosIndexPage{
    grid-template-columns: 26% 22% 20px 22% 22% 0%;
  }
}

@media (max-width: 530px) {
  .MarcaTitIndex{
    margin-left: 10px;
  }

  .MarcaSelectIndex{
    margin-left: 10px;
  }

  .PrecoTitIndex{
    margin-left: 10px;
  }
  .PrecoMinSelectIndex{
    margin-left: 10px;
  }

  .CombustivelTitIndex{
    margin-left: 10px;
  }

  .CombustivelSelectIndex{
    margin-left: 10px;
  }

  .OrdemSelectIndex{
    margin-left: 10px;
  }

  .TextPesquisarIndex{
    display: none;
  }
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
</style>
