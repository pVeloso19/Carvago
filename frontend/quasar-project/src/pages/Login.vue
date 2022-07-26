<template>
  <div class="q-pa-md tabsLoginCreate">
    <div class="q-gutter-y-md">
      <q-tabs
        v-model="tab"
        dense
        align="justify"
      >
        <q-tab class="text-blue" name="login" label="Login" />
        <q-tab class="text-blue" name="create" label="Criar conta" @click="goTo('creat')"/>
      </q-tabs>
    </div>
  </div>

  <div class="q-pa-md Teste">
    <form
      class="q-gutter-md Teste"
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
    >
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

      <p class="InputFormLoginEsquecerPass" @click="goTo('')">Não se lembra da password?</p>

      <div>
        <q-btn class="InputFormLoginBtnLogin" label="Login" type="submit" color="primary"/>
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
  name: 'InicioLoginPage',

  setup () {
    const $q = useQuasar()

    const email = ref(null)
    const pass = ref(null)
    const emailRef = ref(null)
    const passRef = ref(null)

    return {
      goTo (path) {
        window.location = '#/' + path
      },
      async onSubmit () {
        emailRef.value.validate()
        passRef.value.validate()

        if (email.value.hasError || pass.value.hasError) {
          // erro
        } else {
          const userJogos = await axios({
            method: 'get',
            url: URL.URL + '/login',
            params: { email: email.value, password: pass.value }
          })

          const userJogosData = await userJogos.data

          if (userJogosData.resultado > 0) {
            sessionStorage.setItem('IdentificadorCarvago', userJogosData.resultado)
            window.location = '#/home'
          } else {
            if (userJogosData.resultado === -1) {
              $q.notify({
                color: 'negative',
                message: 'Login falhou! - Dados em falta.'
              })
            }

            if (userJogosData.resultado === -2) {
              $q.notify({
                color: 'negative',
                message: 'Login falhou - Password inválida'
              })
              pass.value = null
            }

            if (userJogosData.resultado === -3) {
              $q.notify({
                color: 'negative',
                message: 'Login falhou - Email inválido'
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
      tab: ref('login'),
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

.InputFormLoginEsquecerPass {
  margin: 0px;
  padding: 0px;

  width: 30vw;

  text-align: center;

  cursor: pointer;

  color: #1976D2;
  font-weight: bold;
}

.InputFormLoginEsquecerPass:hover {
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

  .InputFormLoginEsquecerPass {
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

  .InputFormLoginEsquecerPass {
    width: calc(100vw - 110px);
  }
}
</style>
