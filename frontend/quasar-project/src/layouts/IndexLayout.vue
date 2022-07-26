<template>
  <q-bar dark class="bg-primary text-white BarraPaginaIndex">
    <div class="col text-left text-weight-bold">
      <q-img
        src="../../public/icons/logo.png"
        spinner-color="white"
        class="logoIndexPage"
        fit="contain"
        @click="goTo('')"
      />
    </div>
    <q-btn-group>
      <q-btn flat color="white" label="Login" icon="person" @click="goTo('login')" />
      <q-separator color="white" vertical inset />
      <q-btn flat color="white" label="Criar Conta" @click="goTo('creat')" />
    </q-btn-group>
  </q-bar>

  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { onMounted } from 'vue'

export default {
  name: 'IndexLayout',

  setup () {
    onMounted(async () => {
      if (sessionStorage.getItem('IdentificadorCarvago') !== null) {
        window.location = '#/home'
      }
    })

    return {
      goTo (path) {
        window.location = '#/' + path
      }
    }
  }
}
</script>

<style>
.BarraPaginaIndex {
  height: 70px;

  border-style: none none solid none;
  border-color: #F0F0F0;
  border-width: 2px;

  margin-bottom: 7px;
}

.logoIndexPage {
  height: 55px;
  max-width: 150px;
  margin: 20px;
}

.logoIndexPage:hover {
  cursor: pointer;
}

@media (max-width: 600px) {
  .logoIndexPage {
    max-width: 100px;
    margin-left: 5px;
  }
}
</style>
