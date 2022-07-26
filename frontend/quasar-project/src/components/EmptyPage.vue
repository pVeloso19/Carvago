<template>
  <div class="ConteudoNoContentPage">
    <q-icon name="warning" color="warning" size="10rem" />
    <p class="FraseSemConteudo">Sem resultados</p>
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

  display: flex;
  align-items: center;
  justify-content: center;

  margin: 0px;
  padding: 0px;
}

.FraseSemConteudo{
  font-size: 5rem;
  margin-left: 20px;
}

@media (max-width: 615px) {
  .FraseSemConteudo{
    display: none;
  }
}
</style>
