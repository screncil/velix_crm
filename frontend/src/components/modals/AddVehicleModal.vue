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
    <Dialog as="div" @close="closeModal()" class="relative z-10">
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
                <div v-if="error" class="p-4 mb-4 mt-4 text-sm text-red-500 rounded bg-red-400/15" role="alert">
                  <span class="font-medium">Помилка!</span>   Зверніться до адміністратора для вирішення проблеми
                </div>
                Добавити транспортний засіб
              </DialogTitle>
              <div class="text-gray-500">
                <div class="mt-3">
                  <label for="name" class="text-gray-500 text-sm">Найменування</label>
                  <input @change="handleButton" v-model="name" type="text" id="name" class="outline-none border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body focus:border-orange-500" placeholder="Trinx" required />
                  </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Модель</label>
                  <input @change="handleButton" v-model="model" type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body focus:border-orange-500 outline-none" placeholder="MF900" required />
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Серійний номер</label>
                  <input @change="handleButton" v-model="serial" type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body focus:border-orange-500 outline-none" placeholder="FX1UIJGDHS" required />
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Діаметр колес</label>
                  <input @change="handleButton" v-model="diameter" type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body focus:border-orange-500 outline-none" placeholder="27.5" required />
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Коментар</label>
                  <input @change="handleButton" v-model="comment" type="text" id="model" class="border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-xs placeholder:text-body focus:border-orange-500 outline-none" placeholder="..." required />
                </div> 
                <div class="flex flex-col mt-3">
                  <label for="model" class="text-gray-500 text-sm">Sinotrack</label>
                  <div class="top-16">
    <Listbox v-model="selectedSinotrack">
      <div class="relative mt-1">
        <ListboxButton
          class="relative w-full h-11 cursor-default rounded-md border border-1 border-gray-500 bg-white py-3 pl-3 pr-10 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white/75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm"
        >
          <span class="block truncate">{{ selectedSinotrack._id }}</span>
          <span
            class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2"
          >
            <ChevronUpDownIcon
              class="h-5 w-5 text-gray-400"
              aria-hidden="true"
            />
          </span>
        </ListboxButton>

        <transition
          leave-active-class="transition duration-100 ease-in"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <ListboxOptions
            class="mt-1 max-h-60 w-full overflow-y-auto bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm"
          >
            <ListboxOption
              v-slot="{ active, selected }"
              v-for="sinotrack in sinotracks"
              :key="sinotrack.id"
              :value="sinotrack"
              as="template"
            >
              <li
                :class="[
                  active ? 'bg-orange-500/40 text-orange-500' : 'text-gray-900',
                  'relative cursor-default select-none py-2 pl-10 pr-4',
                ]"
              >
                <span
                  :class="[
                    selected ? 'font-medium' : 'font-normal',
                    'block truncate',
                  ]"
                  >{{ sinotrack._id }} | {{ sinotrack.phone_number }}</span
                >
                <span
                  v-if="selected"
                  class="absolute inset-y-0 left-0 flex items-center pl-3 text-orange-500"
                >
                  <CheckIcon class="h-5 w-5" aria-hidden="true" />
                </span>
              </li>
            </ListboxOption>
          </ListboxOptions>
        </transition>
      </div>
    </Listbox>
  </div>
                </div>
              </div>

              <div class="mt-6">
                <button
                  type="button"
                  :class="[activeBtn ? 'w-full inline-flex justify-center rounded-md border border-orange-600 px-4 py-2 text-sm font-medium text-orange-600 hover:bg-orange-600/40 hover:cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2' : 'w-full inline-flex justify-center rounded-md border border-gray-400 px-4 py-2 text-sm font-medium text-gray-400 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2']"
                  @click="Test"
                  :disabled="!activeBtn"
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

import {
  Listbox,
  ListboxLabel,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'
import { getAvailableSinotracks } from '../../api/sinotrack'
import { AddBike } from '../../api/bike'


var sinotracks = [

]

const error = ref(false)
const selectedSinotrack = ref('')


const isOpen = ref(false)

function closeModal() {
  isOpen.value = false
  clearFields()
  error.value = false;
}
async function openModal() {
  isOpen.value = true
  const sinotrack = await getAvailableSinotracks();
  sinotracks = sinotrack
}

const activeBtn = ref(false);

function handleButton() {
  if (name.value === "" || model.value === "" || serial.value === "" || diameter.value === "" || comment.value === "") {
    activeBtn.value = false;
    return;
  }
  activeBtn.value = true;
}

async function Test() {
  console.log(selectedSinotrack.value._id)
  var add = await AddBike(name.value, model.value, serial.value, diameter.value.replace(',', '.'), comment.value, selectedSinotrack.value.id, {_id: selectedSinotrack.value._id})
  console.log(add)
  if (add.added == true) {
    closeModal()
    activeBtn.value = false;
    clearFields()
  } else {
    error.value = true;
  }
}

function clearFields() {
  name.value = ""
  model.value = ""
  serial.value = ""
  diameter.value = ""
  comment.value = ""
  selectedSinotrack.value = {}
}

const name = ref("");
const model = ref("")
const serial = ref("")
const diameter = ref(null)
const comment = ref("")
</script>
