<template>
    <p>Adicionar Interesse</p>
    <Teste v-on:updateTeste="teste = $event" />
    <p>{{teste}}</p>
</template>

<script>

import { ref } from 'vue'
import Teste from 'components/teste.vue'

export default {
  name: 'AddInteressePage',

  components: {
    Teste
  },

  setup () {
    const teste = ref('')

    return {
      teste
    }
  }
}

</script>

<style>

</style>
