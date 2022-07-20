<template>
  <div class="ConteudoNoContentPage">
    <p>Sem resultados</p>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'NoContentComponent',

  setup () {
    return {
    }
  }
})
</script>

<style>
.ConteudoNoContentPage{
  height: calc(100vh - 90px);
  background-color: red;

  display: flex;
  align-items: center;
  justify-content: center;

  margin: 0px;
  padding: 0px;
}
</style>
