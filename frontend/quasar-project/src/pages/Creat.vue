<template>
  <div class="q-pa-md tabsLoginCreate">
    <div class="q-gutter-y-md" style="max-width: 400px">
      <q-tabs
        v-model="tab"
        dense
        align="justify"
      >
        <q-tab class="text-blue" name="login" label="Login" @click="goTo('login')"/>
        <q-tab class="text-blue" name="create" label="Criar conta" />
      </q-tabs>
    </div>
  </div>

  <div class="q-pa-md Teste">
    <form
      class="q-gutter-md Teste"
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
    >
      <p class="InputFormLoginText">Nome</p>
      <q-input
        filled
        v-model="nome"
        ref="nomeRef"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor preencha o campo']"
        class="InputFormLogin"
      />

      <p class="InputFormLoginText">E-mail</p>
      <q-input
        filled
        v-model="email"
        ref="emailRef"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor preencha o campo']"
        class="InputFormLogin"
      />

      <p class="InputFormLoginText">Password</p>
      <q-input
        v-model="pass"
        ref="passRef"
        filled :type="isPwd ? 'password' : 'text'"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor preencha o campo']"
        class="InputFormLogin"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>

      <p class="InputFormLoginTermosCondicoes" @click="goTo('')">Ao clicar no botão continuar aceito os Termos e Condições</p>

      <div>
        <q-btn class="InputFormLoginBtnLogin" label="Criar Conta" type="submit" color="primary"/>
      </div>
    </form>
  </div>
</template>

<script>

import { ref } from 'vue'
import { useQuasar } from 'quasar'

import axios from 'axios'

import URL from '../url.js'

export default {
  name: 'InicioCreatPage',

  setup () {
    const $q = useQuasar()

    const nome = ref(null)
    const email = ref(null)
    const pass = ref(null)
    const emailRef = ref(null)
    const passRef = ref(null)
    const nomeRef = ref(null)

    return {
      goTo (path) {
        window.location = '#/' + path
      },
      async onSubmit () {
        emailRef.value.validate()
        passRef.value.validate()
        nomeRef.value.validate()

        if (email.value.hasError || pass.value.hasError || nomeRef.value.hasError) {
          // erro
        } else {
          const userJogos = await axios({
            method: 'get',
            url: URL.URL + '/create',
            params: { nome: nome.value, email: email.value, password: pass.value }
          })

          const userJogosData = await userJogos.data

          if (userJogosData.resultado > 0) {
            email.value = ''
            pass.value = ''
            sessionStorage.setItem('IdentificadorCarvago', userJogosData.resultado)
            window.location = '#/home'
          } else {
            if (userJogosData.resultado === -1) {
              $q.notify({
                color: 'negative',
                message: 'Registo falhou! - Dados em falta.'
              })
            }

            if (userJogosData.resultado === -3) {
              $q.notify({
                color: 'negative',
                message: 'Impossivel criar conta - Email já está em uso'
              })
              email.value = null
              pass.value = null
            }
          }
        }
      },
      onReset () {
        email.value = null
        pass.value = null

        email.value.resetValidation()
        pass.value.resetValidation()
      },
      tab: ref('create'),
      nome,
      nomeRef,
      email,
      emailRef,
      pass,
      passRef,
      isPwd: ref(true)
    }
  }
}

</script>

<style>
.tabsLoginCreate{

}

.Teste{
  margin: 0px;
  padding: 0px;
  margin-top: 35px;
}

.InputFormLogin {
  width: 27vw;

  margin-top: 0px;
  margin-right: 20px;
  margin-left: 20px;
  margin-bottom: 35px;

  padding: 0px;
}

.InputFormLoginTermosCondicoes {
  margin: 0px;
  margin-left: 20px;
  margin-bottom: 20px;

  padding: 0px;

  width: 30vw;

  cursor: pointer;

  color: grey;
  font-size: 11px;
}

.InputFormLoginTermosCondicoes:hover {
  text-decoration: underline;
}

.InputFormLoginText {
  margin: 0px;
  margin-bottom: 5px;
  margin-left: 20px;

  padding: 0px;
}

.InputFormLoginBtnLogin {
  margin: 0px;
  margin-bottom: 20px;
  padding: 0px;

  width: 27vw;
}

@media (max-width: 1080px) {
  .InputFormLoginBtnLogin {
    width: 30vw;
  }

  .InputFormLogin {
    width: 30vw;
  }

  .InputFormLoginTermosCondicoes {
    width: 32vw;
  }
}

@media (max-width: 662px) {
  .InputFormLoginBtnLogin {
    width: calc(100vw - 130px);
  }

  .InputFormLogin {
    width: calc(100vw - 140px);
  }

  .InputFormLoginTermosCondicoes {
    width: calc(100vw - 110px);
  }
}
</style>
