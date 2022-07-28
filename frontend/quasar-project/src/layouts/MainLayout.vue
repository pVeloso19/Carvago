<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated style="height:50px;">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <div class="col text-left text-weight-bold">
          <q-img
            src="../../public/icons/logo.png"
            spinner-color="white"
            class="logoMain"
            fit="contain"
            @click="logout()"
          />
        </div>

        <div class="q-pa-md BtnDeficoes">
          <q-btn round flat size="md" icon="settings" color="white" >
            <q-menu>
              <div class="row no-wrap q-pa-md">
                <div class="column" v-if="mailValidado">
                  <div class="text-h6 q-mb-md">Definições</div>
                  <q-btn color="primary" label="Alterar nome" style="margin-bottom: 4px; font-size: 10px;"/>
                  <q-btn color="primary" label="Alterar e-mail" style="margin-bottom: 4px; font-size: 10px;"/>
                  <q-btn color="primary" label="Alterar password" style="font-size: 10px;"/>
                </div>
                <div class="column" v-else>
                  <div class="text-h6 q-mb-md" style="width: 130px;  text-align: center;">Validar E-mail</div>
                  <q-btn color="primary" size="40px" icon="touch_app" />
                </div>

                <q-separator vertical inset class="q-mx-lg" />

                <div class="column items-center">
                  <q-avatar size="80px">
                    <img :src="getLink()">
                  </q-avatar>

                  <div class="text-subtitle1 q-mt-md q-mb-xs" style="width: 150px;  text-align: center;">{{nome}}</div>

                  <q-btn
                    color="primary"
                    icon='logout'
                    label="Logout"
                    push
                    size="sm"
                    v-close-popup
                    style="width: 100px;"
                    @click="logout()"
                  />
                </div>
              </div>
            </q-menu>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Menu
        </q-item-label>

        <SideBarContent />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view :Notificacoes="notificacoes"/>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref, onMounted } from 'vue'
import SideBarContent from 'components/SideBarContent.vue'

import axios from 'axios'

import URL from '../url.js'

export default {
  name: 'MainLayout',

  components: {
    SideBarContent
  },

  setup () {
    const leftDrawerOpen = ref(false)

    const nome = ref('Miguel Veloso')

    const mailValidado = ref(true)

    const notificacoes = ref(true)

    function getLink () {
      return 'https://robohash.org/' + nome.value + '?set=set2'
    }

    onMounted(async () => {
      if (sessionStorage.getItem('IdentificadorCarvago') === null) {
        window.location = '#/'
      } else {
        const id = sessionStorage.getItem('IdentificadorCarvago')

        const userJogos = await axios({
          method: 'get',
          url: URL.URL + '/userData',
          params: { ID: id }
        })

        let userJogosData = await userJogos.data
        userJogosData = userJogosData.resultado
        nome.value = userJogosData.nome
        mailValidado.value = userJogosData.email_validado
        notificacoes.value = userJogosData.aceitou_notificacoes
      }
    })

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },

      logout () {
        sessionStorage.removeItem('IdentificadorCarvago')
        window.location = '#/'
      },

      nome,
      getLink,
      mailValidado,
      notificacoes
    }
  }
}
</script>

<style>
.BtnDeficoes {
  padding: 0%;
  margin: 5px;
}

.logoMain {
  height: 35px;
  max-width: 100px;
}

.logoMain:hover {
  cursor: pointer;
}

</style>
