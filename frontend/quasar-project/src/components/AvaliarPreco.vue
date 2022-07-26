<template>
  <div class="AvaliadorContainer" @click="bar = true">

    <div class="AvaliadorContent">
      <q-btn color="primary" icon="search" label="Analisar preço" class="PrecoAvaliadorContainer"/>
    </div>

    <q-dialog v-model="bar" persistent>
      <q-card>
        <q-bar>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>Close</q-tooltip>
          </q-btn>
        </q-bar>

        <q-card-section>
          <p>Modelo de inteligencia artificial que avalia o preço do carro ainda se encontra em desenvolvimento</p>
          <div class="q-pa-md" v-if="loading">
            <q-linear-progress query />
            <q-linear-progress query color="warning" class="q-mt-sm" />
            <q-linear-progress query color="secondary" class="q-mt-sm" />
            <q-linear-progress query color="accent" class="q-mt-sm" />
            <q-linear-progress query track-color="orange" color="purple" class="q-mt-sm" />
            <q-linear-progress query color="negative" class="q-mt-sm" />
            <p style="width=100%; text-align: center; padding-top: 15px;">A carregar...</p>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'AnalisarPreco',

  props: {
    Preco: {
      type: String,
      default: ''
    }
  },

  setup () {
    return {
      bar: ref(false),
      loading: ref(true)
    }
  }
})
</script>

<style>
.AvaliadorContainer{
  width: 100%;
  height: 100%;

  z-index: 10;
}

.AvaliadorContent .PrecoAvaliadorContainer{
  font-weight: bold;
  margin: 0px 0px 0px 0px;
  font-size: 200%;

  width: 100%;
  height: 100%;
}

@media (max-width: 780px) {

  .AvaliadorContent .PrecoAvaliadorContainer{
    --max-size: 45;
    --min-size: 25;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);

    margin-bottom: 10px;
  }
}

@media (max-width: 380px) {
  .AvaliadorContent .PrecoAvaliadorContainer{
    --max-size: 35;
    --min-size: 15;
    --diff: calc(var(--max-size) - var(--min-size));
    --responsive: calc((var(--min-size) * 1px) + var(--diff) * ((100vw - 420px) / (1200 - 420)));

    font-size: var(--responsive);
  }
}
</style>
