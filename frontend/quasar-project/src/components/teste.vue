<template>
  <q-input standout v-model="show" />
</template>

<script>
import { ref } from 'vue'

const teste = ref(null)

export default {
  name: 'TestePage',

  computed: {
    show: {
      get () {
        return teste.value
      },
      set (testeTemp) {
        teste.value = testeTemp
        this.$emit('updateTeste', testeTemp)
      }
    }
  },

  setup () {
    return {
      text: ref(''),
      ph: ref(''),
      dense: ref(false)
    }
  }
}
</script>

<style>

</style>
