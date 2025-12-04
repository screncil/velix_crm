<script lang="ts">
import { defineComponent } from 'vue';
import { login } from '../api/auth';

export default defineComponent({
  data() {
    return {
      email: "" as string,
      password: "" as string
    }
  },
  computed: {
    isValid(): boolean {
      return /\S+@\S+\.\S+/.test(this.email) && this.password.length >= 6
    }
  },
  methods: {
    authorizate() {
      login(this.email, this.password)
    }
  },
  mounted() {
    if (localStorage.getItem("access") !== null) {
      this.$router.back()
    }
  }
})
</script>

<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-20 w-auto" src="https://velix.com.ua/content/images/2/200x100l50nn0/19945050466328.webp" alt="Your Company" />
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <div class="space-y-6">
        <div>
          <label for="email" class="block text-sm/6 font-medium text-gray-900">Електронна пошта</label>
          <div class="mt-2">
            <input v-model="email" type="email" name="email" id="email" autocomplete="email" required class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-orange-400 sm:text-sm/6" />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-gray-900">Пароль</label>
            <div class="text-sm">
              <a href="#" class="font-semibold focus:outline-orange-400 hover:text-orange-500">Забули пароль?</a>
            </div>
          </div>
          <div class="mt-2">
            <input type="password" v-model="password" name="password" id="password" autocomplete="current-password" required class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-orange-400 sm:text-sm/6" />
          </div>
        </div>

        <div>
          <button @click="authorizate" :disabled="!isValid" class="flex w-full justify-center rounded-md bg-orange-400 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-orange-500 hover:cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Авторизуватись</button>
        </div>
      </div>
    </div>
  </div>
</template>
 
