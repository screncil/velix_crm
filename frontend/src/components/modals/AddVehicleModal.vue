<template>
  <div class="">
    <button
      type="button"
      @click="openModal"
      class=""
    >
      <slot></slot>
    </button>
  </div>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
      <TransitionChild
        as="template"
        enter="duration-300 ease-out"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="duration-200 ease-in"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black/25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div
          class="flex mt-8 min-h-full items-center justify-center p-4 text-center"
        >
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <DialogPanel
              class="w-full max-w-md transition overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
            >
              <DialogTitle
                as="h3"
                class="text-lg font-medium leading-6 text-gray-900"
              >
                Добавити транспортний засіб
              </DialogTitle>
              <div class="text-gray-500">
                <div class="mt-3">
                  <label for="name" class="text-gray-500 text-sm">Найменування</label>
                  <input type="text" id="name" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body" placeholder="Trinx" required />
                  </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Модель</label>
                  <input type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body" placeholder="MF900" required />
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Серійний номер</label>
                  <input type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body" placeholder="FX1UIJGDHS" required />
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Діаметр колес</label>
                  <input type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body" placeholder="27.5" required />
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Коментар</label>
                  <input type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body" placeholder="..." required />
                </div>
                <div class="flex flex-col mt-3">
                  <label for="model" class="text-gray-500 text-sm">Sinotrack</label>
                  <ListboxLayout />
                </div>
              </div>

              <div class="mt-4">
                <button
                  type="button"
                  class="w-full inline-flex justify-center rounded-md border border-orange-600 px-4 py-2 text-sm font-medium text-orange-600 hover:bg-orange-600/40 hover:cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  @click="closeModal"
                >
                  Зберегти
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import {
  TransitionRoot,
  TransitionChild,
  Dialog,
  DialogPanel,
  DialogTitle,
} from '@headlessui/vue'

import ListboxLayout from '../layout/ListboxLayout.vue'

const isOpen = ref(false)

function closeModal() {
  isOpen.value = false
}
function openModal() {
  isOpen.value = true
}
</script>
