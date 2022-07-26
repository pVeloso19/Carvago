<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn color="primary" label="Página Inicial" icon='home' @click="goTo('home')" class="btnPaginaInicialBarra"/>

    <q-btn flat color="black" label="Todos os carros" icon='time_to_leave' @click="goTo('carros')" style="margin-bottom: 2vh;"/>

    <q-expansion-item
      expand-separator
      icon="remove_red_eye"
      label="Meus Interesses"
      caption="Nenhum Interesse"
      disable
      v-if="interesses.length==0"
      style="margin-bottom: 2vh;"
    />

    <q-expansion-item
      expand-separator
      icon="remove_red_eye"
      label="Meus Interesses"
      :caption="label"
      v-else
      @click="goTo('interesses')"
      style="margin-bottom: 2vh;"
    >
      <q-btn flat align="left" color="black" :label="i" v-for="i in interesses" :key="i" @click="goTo('interesses/'+i)" class="InteresseBtnEnterPage" />
    </q-expansion-item>

    <q-btn flat color="black" label="Favoritos" icon='star' @click="goTo('favoritos')" style="margin-bottom: 2vh;"/>
    <q-btn flat color="black" label="Novos Carros" icon='new_releases' @click="goTo('newCars')" style="margin-bottom: 2vh;"/>

    <q-separator style="margin-bottom: 2vh;"/>

    <q-btn flat color="black" label="Adicionar Interesses" icon='add' @click="goTo('add')"/>

    <q-btn color="primary" class="btnLogoutBarra" label="Logout" icon='logout' @click="logout()"/>
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
      const id = sessionStorage.getItem('IdentificadorCarvago')
      const userJogos = await axios({
        method: 'get',
        url: URL.URL + '/InteressesUser',
        params: { ID: id }
      })

      const userJogosData = await userJogos.data

      userJogosData.forEach((elem) => {
        interesses.value.push(elem.trim())
      })
    })

    return {
      goTo (path) {
        window.location = '#/' + path
      },
      logout () {
        sessionStorage.removeItem('IdentificadorCarvago')
        window.location = '#/'
      },
      interesses,
      label
    }
  }
}

</script>

<style>
.InteresseBtnEnterPage {
  width:100%;
  padding-left: 20px;
}

.btnLogoutBarra {
  position: absolute;
  left: 0;
  bottom: 20px;
  width:300px;
  max-width:85%;
  padding-left: 15px;
  margin-left: 20px;
}

.btnPaginaInicialBarra {
  width:270px;
  max-width:97%;

  margin-bottom: 2vh;
}
</style>
