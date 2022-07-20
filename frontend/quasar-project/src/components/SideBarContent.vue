<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn flat color="primary" label="Página Inicial" icon='home' @click="goTo('home')"/>
    <q-btn flat color="primary" label="Todos os carros" icon='time_to_leave' @click="goTo('carros')"/>

    <q-expansion-item
        expand-separator
        icon="remove_red_eye"
        label="Meus Interesses"
        caption="Nenhum Interesse"
        disable
        v-if="interesses.length==0"
      />

      <q-expansion-item
        expand-separator
        icon="remove_red_eye"
        label="Meus Interesses"
        :caption="label"
        v-else
        @click="goTo('interesses')"
      >
        <q-btn flat color="primary" :label="i" v-for="i in interesses" :key="i" @click="goTo('interesses/'+i)"/>
      </q-expansion-item>

    <q-btn flat color="primary" label="Favoritos" icon='star' @click="goTo('favoritos')"/>
    <q-btn flat color="primary" label="Novos Carros" icon='new_releases' @click="goTo('newCars')"/>

    <q-btn flat color="primary" label="Adicionar Interesses" icon='add' @click="goTo('add')"/>
    <q-btn flat color="primary" label="Logout" icon='logout' @click="logout()"/>
  </div>
</template>

<script>

import { computed, onMounted, ref } from 'vue'

import axios from 'axios'

import URL from '../url.js'

export default {
  setup () {
    const interesses = ref([])

    const label = computed(() => {
      const plural = (interesses.value.length > 1) ? 's' : ''
      return interesses.value.length + ' Interesse' + plural
    })

    onMounted(async () => {
      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/InteressesUser',
        params: { ID: 1 }
      })

      const userJogosData = await userJogos.data
      const entries = Object.entries(userJogosData)

      entries.forEach((elem) => {
        let interesse = ''
        elem[1].forEach((elem2) => {
          elem2.forEach((elem3) => {
            interesse += elem3 + ' '
          })
        })

        interesses.value.push(interesse.trim())
      })
    })

    return {
      goTo (path) {
        window.location = '#/' + path
      },
      logout () {
        window.location = '#/'
      },
      interesses,
      label
    }
  }
}

</script>
