<template>
  <div class="ZonaAdicionarInteresses">
    <div class="ZonaAdicionarInteresse">
      <div class="ZonaSemNotificacoes" v-if="!Notificacoes">
        <div v-if="!temPermissao" class="row AlertaSemNotificacoes">
          <q-icon name="warning" color='red' size="30px"/>
          <p class="TextWarningZonaSemNotificacoes">Ative as permissões para poder adicionar adicionar interesses</p>
        </div>
        <div v-else>
          <q-btn class="BtnAtivarNotificationZonaInteresse" color="primary" icon="mail" label="Ativar Notificações" @click="initPushSubscription()"/>
        </div>
      </div>

      <div class="ZonaAdicionarParamAddInteresse">
        <p class="ZonaAdicionarParamAddInteresseTit">Adicionar Interesse</p>
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

      <q-btn
        push
        class="BtnAddInteresseZonaInteresse"
        color="primary"
        label="Adicionar"
        @click="addInteresse()"
        v-if="Notificacoes && modelo!=null && marca!=null"
      />
      <q-btn
        push
        class="BtnAddInteresseZonaInteresse"
        color="primary"
        label="Adicionar"
        disable
        v-else
      />
    </div>

    <div class="ZonaMeusInteressesAtuais">
      <q-markup-table flat bordered class="TabelaMeusInteresses">
        <thead>
          <tr>
            <th class="bg-indigo-2" colspan="5">
              <div class="row no-wrap items-center">
                <q-icon name="visibility" size="20px"/>
                <p class="ZonaAdicionarParamAddInteresseTit ZonaAdicionarParamRemInteresseTit">Meus Interesses</p>
              </div>
            </th>
          </tr>
          <tr class="bg-indigo-3" v-if="interesses.length > 0">
            <th class="text-left"></th>
            <th class="text-right">Marca</th>
            <th class="text-right">Modelo</th>
          </tr>
        </thead>
        <tbody class="bg-grey-3" v-if="interesses.length > 0">
          <tr v-for="i in interesses" :key="i">
            <q-btn class="BtnEliminarInteresse" color="red" icon="delete" @click="eliminarInteresse(i.marca, i.modelo)"/>
            <td class="text-right">{{i.marca}}</td>
            <td class="text-right">{{i.modelo}}</td>
          </tr>
        </tbody>
        <tbody class="bg-grey-3" v-else>
          <tr>
            <p class="SemInteressesLabelTabelaVerInteresses">Sem interesses</p>
          </tr>
        </tbody>
      </q-markup-table>
    </div>
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

const temPermissao = ref(false)

function urlB64ToUint8Array (base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4)
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/')

  const rawData = window.atob(base64)
  const outputArray = new Uint8Array(rawData.length)

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i)
  }
  return outputArray
}

async function handlePermission () {
  const promisse = navigator.permissions.query({ name: 'notifications' }).then(permissionQuery)
  temPermissao.value = await promisse
}

function permissionQuery (result) {
  if (result.state === 'granted') {
    return true
  } else {
    if (result.state === 'prompt') {
      return true
    } else {
      if (result.state === 'denied') {
        return false
      }
    }
  }
  return false
}

export default {
  name: 'AddInteressePage',

  props: {
    Notificacoes: {
      type: Boolean,
      required: true
    }
  },

  setup () {
    const CombustivelOptions = [
      'Diesel', 'Eléctrico', 'Gasolina', 'GPL', 'Híbrido (Diesel)', 'Híbrido (Gasolina)', 'Hidrogénio'
    ]

    const interesses = ref([])

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

    async function initPushSubscription () {
      let res = true
      try {
        const userJogos = await axios({
          method: 'get',
          url: URL.URL + '/subscription'
        })

        const response = await userJogos.data
        localStorage.setItem('applicationServerPublicKey', response.public_key)

        if ('serviceWorker' in navigator && 'PushManager' in window) {
          console.log('Service Worker and Push is supported')
          const url = URL.URL + '/sw.js'
          navigator.serviceWorker.register(url)
            .then(function (swReg) {
              console.log('Service Worker is registered', swReg)

              const applicationServerPublicKey = localStorage.getItem('applicationServerPublicKey')
              const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey)
              swReg.pushManager.subscribe({
                userVisibleOnly: true,
                applicationServerKey: applicationServerKey
              }).then(async function (subscription) {
                console.log('User is subscribed.')
                localStorage.setItem('sub_token', JSON.stringify(subscription))
                const userJogos = await axios({
                  method: 'post',
                  url: URL.URL + '/subscription',
                  data: { subscription_token: subscription }
                })
                await userJogos.data
                location.reload()
              }).catch(function (error) {
                res = false
                console.error('Service Worker Error', error)
              })
            })
            .catch(function (error) {
              res = false
              console.error('Service Worker Error', error)
            })
        } else {
          res = false
        }
      } catch (e) {
        alert(e)
        res = false
      }

      return res
    }

    onMounted(async () => {
      await handlePermission()
    })

    onMounted(async () => {
      const id = sessionStorage.getItem('IdentificadorCarvago')
      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/InteressesUser',
        params: { ID: id }
      })

      const userJogosData = await userJogos.data

      userJogosData.forEach((elem) => {
        const marcaModelo = elem.split(' ')
        const temp = {
          marca: marcaModelo[0].trim().toUpperCase(),
          modelo: marcaModelo[1].trim().toUpperCase()
        }
        interesses.value.push(temp)
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
        location.reload()
      }
    }

    async function eliminarInteresse (ma, mo) {
      const id = sessionStorage.getItem('IdentificadorCarvago')

      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/RemoveInteresse',
        params: { ID: id, Marca: ma, Modelo: mo }
      })

      let res = await userJogos.data
      res = res.resultado

      if (res) {
        location.reload()
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

      addInteresse,
      interesses,

      initPushSubscription,
      temPermissao,

      eliminarInteresse
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
.ZonaAdicionarInteresses{
  display: grid;
  grid-template-columns: 55% 30px auto;
  grid-template-areas:
  "Add NADA Remove"
}

.ZonaAdicionarParamAddInteresse{
  margin: 0px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 30px;
}

.ZonaSemNotificacoes{
  margin: 0px;
  margin-top: 10px;
  margin-left: 30px;
}

.BtnAddInteresseZonaInteresse{
  margin: 0px;
  margin-left: 30px;
  width: calc(100% - 30px);
}

.BtnAtivarNotificationZonaInteresse{
  width: 100%;
  font-size: 10px;
}

.ZonaAdicionarParamAddInteresseTit{
  font-weight: bold;
  font-size: 20px;
}

.TextWarningZonaSemNotificacoes{
  margin-left: 10px;
  height: 30px;
  line-height : 30px;
}

.ZonaMeusInteressesAtuais{
  grid-area: Remove;
}

.ZonaAdicionarInteresse{
  grid-area: Add;
}

.TabelaMeusInteresses{
  margin-top: 20px;
  margin-right: 30px;
}

.SemInteressesLabelTabelaVerInteresses{
  margin-top: 20px;
  text-align: center;
}

.ZonaAdicionarParamRemInteresseTit{
  height: 60px;
  line-height : 75px;
  margin-left: 10px;
}

.BtnEliminarInteresse{
  margin-top: 5px;
  margin-left: 5px;
}

@media (max-width: 1200px) {
  .TextWarningZonaSemNotificacoes{
    font-size: 10px;
  }
}

@media (max-width: 630px) {
  .ZonaAdicionarInteresses{
    display: grid;
    grid-template-columns: auto;
    grid-template-areas:
    "Add"
    "Remove"
  }

  .ZonaAdicionarInteresse{
    margin-right: 30px;
  }

  .TabelaMeusInteresses{
    margin-left: 30px;
  }

  .TextWarningZonaSemNotificacoes{
    font-size: 8px;
  }
}

@media (max-width: 340px) {
  .TextWarningZonaSemNotificacoes{
    font-size: 6px;
  }
}
</style>
