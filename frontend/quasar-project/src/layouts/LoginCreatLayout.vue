<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
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

      <div class="FormContainer" >
        <router-view />
      </div>

    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'LoginCreateLayout',

  setup () {
    return {
      goTo (path) {
        window.location = '#/' + path
      }
    }
  }
}
</script>

<style>
.FormContainer{
  width: 30vw;

  margin-top: 50px;
  margin-left: 50px;

  max-height: calc(100vh - 100px);
}

.BarraPaginaIndex {
  height: 70px;

  border-style: none none solid none;
  border-color: #F0F0F0;
  border-width: 2px;
}

.logoIndexPage {
  height: 55px;
  max-width: 150px;
  margin: 20px;
}

.logoIndexPage:hover {
  cursor: pointer;
}

@media (max-width: 1080px) {
  .FormContainer{
    width: 35vw;
  }
}

@media (max-width: 662px) {
  .FormContainer{
    width: calc(100vw - 100px);
    margin-right: 50px;
  }
}

@media (max-width: 600px) {
  .logoIndexPage {
    max-width: 100px;
    margin-left: 5px;
  }
}
</style>
