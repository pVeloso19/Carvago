<template>
    <p>Inicio</p>
</template>

<script>

import { ref } from 'vue'

export default {
  name: 'InicioPage',

  setup () {
    const carros = ref([])
    const visible = ref(false)
    const showSimulatedReturnData = ref(false)
    const maxPages = ref(0)

    return {
      carros,
      visible,
      showSimulatedReturnData,
      current: ref(1),
      maxPages
    }
  }
}

</script>

<style>

</style>
